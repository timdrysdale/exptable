#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 08:46:46 2020
Timothy D Drysdale <timothy.d.drysdale@gmail.com>
"""
import numpy as np
import matplotlib.pyplot as plt

from pytablewriter import MarkdownTableWriter


# udr returns the rate at position x when the up/down rates are different
def udr(x, down, up):
    if (np.sign(x) == 0):
        return 0
    if (np.sign(x) > 0):
        return up
    if (np.sign(x) < 0):
        return down
    
# rc_exp returns the exponential value provided by an RC transmitter for a given stick input    
# it mixes a third-order polynomial with a line    
def rc_exp(x, rate):
    x_abs = np.abs(x)/100.
    rate_unit = rate/100
    y_abs = (rate_unit * x_abs**3) + (1 - rate_unit)* x_abs
    return np.sign(x) * y_abs * 100

def split_exp(x, down, up):
     return  rc_exp(x,udr(x, down, up))
 
    
def rc_exp5(x, rate):
    x_abs = np.abs(x)/100.
    rate_unit = rate/100
    y_abs = (rate_unit * x_abs**5) + (1 - rate_unit)* x_abs
    return np.sign(x) * y_abs * 100   
      
# exptable prints markdown table of X-Y coords for given up/down exponential rates
def exptable(points, down, up):
    headers = ["X","Y"]
    table_name = "down %d%% + up%d%%"%(down, up)
    
    value_list = []
    
    x_values = np.linspace(-100,100,points)
    
    for x in x_values:
        y = split_exp(x,down,up)
        value_list.append([x,y])
     
    writer = MarkdownTableWriter(
        table_name=table_name,
        headers=headers,
        value_matrix=value_list,
        margin=1 
        
    )
    return writer.dumps()

if __name__ == "__main__":

    # save intro figure(s)
   
    rate_count = 5
    up_rates = np.linspace(0,100,rate_count)
    x_list = np.linspace(-100,100,100)
    
    fig = plt.figure()
       
    for rate in up_rates:
        y_list = []
        for x in x_list:
            y_list.append(rc_exp(x,rate))
        plt.plot(x_list,y_list,label="%d%%"%(rate))
       
    ax = plt.gca()
    ax.set_aspect('equal')   
    plt.ylim([-110,110])
    plt.xlim([-110,110])
    plt.xlabel("Stick position (%)")
    plt.ylabel("Output position (%)")
    plt.legend()
    plt.savefig("./img/expo.png",dpi=150)
    
    #split exponential
    fig = plt.figure()
    down = 15
    up = 25
    y_list = []
    for x in x_list:
       y_list.append(split_exp(x,down,up))
    plt.plot(x_list,y_list,label="-%d+%d"%(down,up))
    
    down = 50
    up = 75
    y_list = []
    for x in x_list:
       y_list.append(split_exp(x,down,up))
    plt.plot(x_list,y_list,label="-%d+%d"%(down,up))    
    
    ax = plt.gca()
    ax.set_aspect('equal')   
    plt.ylim([-110,110])
    plt.xlim([-110,110])
    plt.xlabel("Stick position (%)")
    plt.ylabel("Output position (%)")
    plt.legend()
    
    plt.savefig("./img/split.png",dpi=150)
   
    rate_count = 5
    up_rates = np.linspace(0,100,rate_count)
    x_list = np.linspace(-100,100,100)
    
    fig = plt.figure()
       
    for rate in up_rates:
        y_list = []
        for x in x_list:
            y_list.append(rc_exp5(x,rate))
        plt.plot(x_list,y_list,label="%d%%"%(rate))
       
    ax = plt.gca()
    ax.set_aspect('equal')   
    plt.ylim([-110,110])
    plt.xlim([-110,110])
    plt.xlabel("Stick position (%)")
    plt.ylabel("Output position (%)")
    plt.legend()
    plt.savefig("./img/expo5.png",dpi=150)
    
    # add tables to readme
    rate_count = 5
    up_rates = np.linspace(0,100,rate_count)
    down_rates = np.linspace(0,100,rate_count)  
    with open("README.md",'w') as file:
        
        f = open("intro.md", "r")
        for line in f:
            file.write(line)
        f.close()
        
        
        