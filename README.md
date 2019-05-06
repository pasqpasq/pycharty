# pycharty
pycharty creates minimal, beautiful and fully responsive bar charts for your presentations with Python.
## Why use pychart?
Just use your dataframe and pychart will figure the optimal bar widths and configuration based on your data. 
## Examples
Group | Type | Value 
----- | ---- | ------
A | Type 1 | 1
A | Type 2 | 2
A | Type 3 | 3
B | Type 1 | 4
B | Type 2 | 5
B | Type 3 | 6
C | Type 1 | 7
C | Type 2 | 8
C | Type 3 | 9

```
pycharty(df,
         size     = .5,
         stacked  = False, # or 'True'
         theme    = 'blue', # or 'pink' or 'yellow'
         title    = 'This is the title',
         legend   = True,
         )
```
![Preview 1](https://i.imgur.com/Xs0fxAV.png)

![Preview 2](https://i.imgur.com/NMUFWd1.png)
