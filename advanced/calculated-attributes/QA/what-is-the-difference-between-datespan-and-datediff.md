---
items: CalculatedAttributesQA
---

# What is the difference between DATESPAN and DATEDIFF operators?

## DATESPAN

[**DATESPAN**](../operators/datespan.md) calculates the time duration between two dates based on specified intervals, such as days, weeks, or months. It provides the duration within these intervals and is ideal for scenarios where you need to measure time in meaningful units.

For instance, if you want to know the time gap between two events in days or months, [**DATESPAN**](../operators/datespan.md) is the go-to operator.

Example: Consider two dates - `2023-01-01 23:59`, and `2023-01-03 00:00`. Using [**DATESPAN**](../operators/datespan.md) with a day interval, you'd get a result of 1 day, emphasizing the specific interval.

Another example: If you choose a month as the interval, the same two dates will yield a result of 0 months, focusing on the month-level duration.

## DATEDIFF

[**DATEDIFF**](../operators/datediff.md), on the other hand, computes the absolute difference between two dates in terms of the specified interval type, like days, months, or years. It's useful when you need a precise count of these units between two dates, disregarding the specific intervals.

For instance, to determine the exact number of days between two dates, [**DATEDIFF**](../operators/datediff.md) provides this precise difference.

Example: If you choose months as the interval, and the dates are `2023-01-01` and `2023-03-01`, [**DATEDIFF**](../operators/datediff.md) would yield 2 months, reflecting the month-level difference.

In summary, [**DATESPAN**](../operators/datespan.md) is ideal for measuring time in specified intervals, providing the duration within those intervals (e.g., days, months). [**DATEDIFF**](../operators/datediff.md), however, offers the absolute difference between dates in terms of the specified interval type (e.g., days, months), disregarding specific intervals.

--

- [DATESPAN operator](../operators/datespan.md)
- [DATEDIFF operator](../operators/datediff.md)
