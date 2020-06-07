# Pythagorean Tree Fractal 2
**Category:** Algorithms

**Points:** 100

**Description:**
> Because every good thing must have a sequel ;)
>
> Please see the attached file for more details (and ignore the red dots on the images).
>
> Note: Don't worry about overlapping squares!
>
> Author: Plate_of_Sunshine
>
> **Given:** pdf named "PTF2.pdf"

## Writeup
From the pdf given, we are given an area of the square in Stage 1
(**70368744177664**). We are also given an objective to find the total area
at stage 25, which includes all of the branches squares as well.

I assumed that the triangle made between the squares was an isosceles triangle.
This tells us the two sides of the branched squares are the same in each step.
The isosceles triangle shown in the PDF tells us the angles are 90, 45, and 45.
Here's the math:
```
side_stage_1 = sqrt(70368744177664)
θ = 45 deg
cos(θ) = adj/hyp
cos(45) = side_stage_1 / (2 * side_next)
side_next = side_stage_1 / (2 * cos(45))
```

Doing this repetitively and adding up all of the areas of each stage will bring
us to the answer. My script brought it to me in scientific notation, but I was
too lazy to change my script.

```
Total Area at 25 = 1.29902254294e+15
1.29902254294e+15
```

## Flag
flag{1299022542940000}
