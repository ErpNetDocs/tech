---
uid: cao-CAST
items: Operators
---

# CAST 

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
| Return value | Returns the param converted to the type. |

> [!NOTE]
> 
> The CAST operator is a secondary operator, used by the other operators to convert their parameters to the same type. The type is usually entered as a constant (CONST).



***Example***




The following example converts the value of the state of a sales order, whose type is enum, to an integer number. Conveting to integer allows comparison between the states (lower -> higher):
```
10: CONVERT ATTRIB:State CONST:System.Int32      
```
OUTPUT: If 'State = Released', the output will be '30'.

> [!NOTE] 
> 
> The repository of the attribute is Crm.Sales.SalesOrders

#### More examples:


- **[Check whether the releasing of the document is first or not](https://docs.erp.net/tech/advanced/calculated-attributes/examples/check-for-first-releasing.html)**
- **[Check if the system type of payment type in the sales order is 'In Cash'](https://docs.erp.net/tech/advanced/calculated-attributes/examples/check-if-system-type-is-in-cash.html)**

