# pycharty
PyCharty creates minimal and beautiful fully responsive charts with Python, for your presentations. You just have to give the data frame as input and size, everything else is done automatically by the module (font size, bar widths, spaces, etc).
## Why use pychart?

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
         stacked  = False,
         theme    = 'blue',
         title    = 'This is the title',
         legend   = True,
         )
```
![Image of Yaktocat](https://i.imgur.com/Xs0fxAV.png)
