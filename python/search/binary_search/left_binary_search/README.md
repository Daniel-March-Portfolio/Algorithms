# Left binary search

This type of "binary search" returns the index of the FIRST 
element that is greater than or equal to the target.

```
target = 2:
[1, 2, 2, 4, 4, 6]
    ^
```
```
target = 3:
[1, 2, 2, 4, 4, 6]
          ^
```
```
target = 7:
[1, 2, 2, 4, 4, 6]
None
```
```
target = 0:
[1, 2, 2, 4, 4, 6]
 ^
```