---
uid: cao-IFERROR
items: Operators
---
# IFERROR 

| Specification | Value |
| ---- | ----- |
| Name | IFERROR |
| Description | Evaluates an expression and returns a specified value if the expression returns an error. <br> Otherwise returns the value of the expression itself. |
| Parameter 1 Name | Value |
| Parameter 1 Type | any type |
| Parameter 2 Name | ValueIfError |
| Parameter 2 Type | any type |
| Parameter 3 Name |
| Parameter 3 Type |
| Return value | When the expression returns a value other than error, then the value of the Parameter 1 is returned. <br> When the expression evaluates to an error, then the value of the Parameter 2 is returned. |

**Example:**

```      
10: IFERROR EXP:20 CONST:'Error in calculation'  
20: DIVIDE CONST:2.00 ATTRIB:QuantityValue 
```
OUTPUT: 
<br/>If 'QuantityValue = 1.00', the output will be 2.
<br/>If 'QuantityValue = 0.00', the output will be 'Error in calculation'.


> [!NOTE]
> 
> The repository of the attribute is *Crm.Sales.SalesOrderLines*
