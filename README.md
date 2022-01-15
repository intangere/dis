# dis
dis interpreter in python.  
It is identical to the original interpreter (as far as I have observed).  

However I added a dirt simple "macro" operator to make changes to code easier:
```
/<num><op>/
```
For example:
```
/42_/
```
will fill everything from the current memory location to 42 with a no-op.
which is the same as filling from the current position in code up to column 43.
```
To see what this expands to just append *--expand* when running the interpreter.
```  

python3 dis.py example.dis --expand
Output: __________________________________________
```

Usage:
```
python3 dis.py <filename> [--expand]
```
