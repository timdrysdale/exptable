# exptable
Custom exponential curve tables for use in RC transmitters

RC transmitters create a softer middle range in the control by applying a curve to the stick

https://forum.alofthobbies.com/index.php?threads/exponential-primer.1479/

A [number of formulas have been proposed](https://www.rcgroups.com/forums/showthread.php?1675540-who-know-the-algorithm-for-exponential-curve-in-RC) for the exponential in RC transmitters.
It is nota 'true' exponential in that ```exp(0)=1``` while RC transmitters require
```exp(x)=0``` for the case  ```x=0```.

[]