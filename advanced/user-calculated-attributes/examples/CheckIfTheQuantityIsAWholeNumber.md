---
items: CalculatedAttributeExamples
---

# Check If The Quantity Is A Whole Number

The current calculated attribute returns true if the  quantity in the Sales Order line is whole number, and False - if it is  decimal number. The repository of the attribute is  Crm.Sales.SalesOrders.

It expressions are as follows:

```
10: IIF EXP:20 CONST:True CONST:False
20: EQUAL ATTRIB:QuantityValue EXP:30 
30: CEILING ATTRIB:QuantityValue
```



Explanation:

- 10: check if expression 20 is true. If so - return True, else - return False
- 20: check if attribute QuantityValue is equal to expression 30
- 30: get the smallest integral value greater than or equal to the value in attribute QuantityValue

