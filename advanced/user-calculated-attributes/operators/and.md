---
uid: cao-AND
---

# AND - Calculated Attribute Operator

| Specification | Value |
| ---- | ----- |
| Name | AND |
| Description | Checks if the two conditions are True. If so - the operator returns True. If any of the specified conditions are not True, the operator returns False. |
| Parameter 1 Name | Condition1 |
| Parameter 1 Type | boolean |
| Parameter 2 Name | Condition2 (optional) |
| Parameter 2 Type | boolean |
| Parameter 3 Name | Condition3 (optional) |
| Parameter 3 Type |  boolean |
| Return Value | Condition1 AND Condition2|

> [!NOTE]
> Parameter 1 and Parameter 2 are optional.
> If only Parameter 1 has value, the result is its value (Parameter 1).

 
## Example

```
10: AND EXP:20 EXP:30       
20: EQUAL ATTRIB:LineNo CONST:10 
30: EQUAL ATTRIB:Notes CONST:Apple   
```
OUTPUT: 
If 'LineNo = 10' and 'Notes = Apple', the output will be 'True'.
If 'LineNo = 50' and 'Notes = Apple', the output will be 'False'.
If 'LineNo = 10' and 'Notes = Pear', the output will be 'False'.

> [!NOTE]
> The repository of the attribute is *Crm.Sales.SalesOrderLines*
