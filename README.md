# pycharty
pycharty creates minimal, beautiful and fully responsive Python bar charts for your presentations.
## Why use pycharty?
Just use your dataframe and, based on your data, pycharty will figure out the perfect configuration, size, alignments and all that boring stuff.
## Examples
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

![Preview 2](https://i.imgur.com/NJfB1sX.png)

## Dataframe structure
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
