---
items: StringInterpolationExamples
---

# Constant expression examples

### Plain string

#### Input
```cs
'This is a simple string.'
```
Will result to the same output because string interpolation is **not** applicable. 

The input **doesn't** meet the syntax requirements.

#### Output
```cs
'This is a simple string.'
```

### Expression with escaped curly braces

#### Input
```cs
'{{This is a simple string.}}'
'\{This is a simple string.\}'
```
Will create a **constant** expression, which results to an output that's the **same** as the input.

#### Output
```cs
'{This is a simple string.}'
```
