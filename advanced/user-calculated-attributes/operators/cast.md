---
uid: cao-CAST
items: Operators
---

# CAST - Calculated Attribute Operator

| Specification | Value |
| ---- | ----- |
| Name | CAST |
| Description | Casts the parameter to the specified type. |
| Parameter 1 Name | 	param |
| Parameter 1 Type | 	any type |
| Parameter 2 Name | 	type |
| Parameter 2 Type | string - 'System.Int32', 'System.String', 'System.Decimal', 'System.Double' and all standart .net types. |
| Parameter 3 Name |
| Parameter 3 Type |
| Return Value | Returns the param converted to the type. |

> [!NOTE]
> The CAST operator is a secondary operator, used by the other operators to convert their parameters to the same type. The type is usually entered as a constant (CONST).

## Example
The following example converts the value of the 'State' of a Sales Order, whoose type is Enum, to an integer number. Conveting to integer allows comparison between the states (lower -> higher):
```
10: CONVERT ATTRIB:State CONST:System.Int32      
```
OUTPUT: If 'State = Released', the output will be '30'.

> [!NOTE] 
> The repository of the attribute is Crm.Sales.SalesOrders

#### More Examples
[Check Whether the Releasing of the Document Is First or Not](../examples/CheckWhetherTheReleasingOfTheDocumentIsFirstOrNot.md)
<br/>[Check If the System type of Payment type in the Sales Order Is 'In Cash'](../examples/CheckIfTheSystemTypeOfPaymentTypeInTheSalesOrderIsInCash.md)

