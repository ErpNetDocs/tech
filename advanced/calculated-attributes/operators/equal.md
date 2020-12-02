---
uid: cao-EQUAL
items: Operators
---
# EQUAL - Calculated Attribute Operator

| Specification | Value |
| ---- | ----- |
| Name | EQUAL |
| Description | Checks if two values are equal. If they are equal, the return value is True, else - the return value is False. |
| Parameter 1 Name | Value1 |
| Parameter 1 Type | numeric type - int, double or decimal; string; |
| Parameter 2 Name | Value2 |
| Parameter 2 Type | numeric type - int, double or decimal; string; |
| Parameter 3 Name |
| Parameter 3 Type |
| Return Value | boolean (True or False) |

> [!NOTE]
> Ensure that the values which are compared up have the same type. For example, Parameter 1 and Parameter 2 must be both integers, or doubles, or decimals, or strings.

## Example

```      
10: EQUAL ATTRIB:LineNo CONST:30   
```
OUTPUT: 
<br/>If 'LineNo = 30', the output will be 'True'.
<br/>If 'LineNo = 10', the output will be 'False'.


> [!NOTE]
> The repository of the attribute is *Crm.Sales.SalesOrderLines*

#### More Examples
[Check If The Quantity Is A Whole Number](../examples/CheckIfTheQuantityIsAWholeNumber.md)
<br/>[Check Whether the Releasing of the Document Is First or Not](../examples/CheckWhetherTheReleasingOfTheDocumentIsFirstOrNot.md)
<br/>[Get Current Availabilities of a Product](../examples/GetCurrentAvailabilitiesOfAProduct.md)
