---
items: CalculatedAttributeExamples
---

# Check if the quantity is a whole number

This attribute returns 'Тrue' if the quantity in the sales order line is а whole number, and False - if it's decimal number. The repository of the attribute is **Crm.Sales.SalesOrderLines**.

Its expressions are as follows:

```
10: IIF EXP:20 CONST:True CONST:False
20: EQUAL ATTRIB:QuantityValue EXP:30 
30: CEILING ATTRIB:QuantityValue
```

**Explanation:**

- 10: check if expression 20 is true. If so - return 'True', else - return 'False'
- 20: check if attribute **QuantityValue** is equal to expression 30
- 30: get the smallest integral value greater than or equal to the value in attribute **QuantityValue**
