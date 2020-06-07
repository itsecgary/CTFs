# Pythagorean Tree Fractal 1
**Category:** Algorithms

**Points:** 100

**Description:**
> Please see the attached file for more details (and ignore the red dots on the images).
>
> **Author:** Plate_of_Sunshine
>
> **Given:** pdf named "Pythagorean_Tree_Fractal"

## Writeup
This algorithm was pretty simple to make. After looking at the PDF given to us,
we can see that our goal is to see how many rectangles there are at stage 50!

Here is the math:
```
Stage 1 = 1 square
Stage 2 = 3 square
Stage 3 = 7 square

Number of rectangles at stage "x" = ((the number of rectangles from last stage)*2) + 1
```

I build a simple script to iterate through and give me the number I should put
in the flag since that is the format they want us to put it in.

## Flag
flag{2251799813685245}
