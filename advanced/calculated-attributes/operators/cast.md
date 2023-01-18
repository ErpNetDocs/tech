---
uid: cao-CAST
items: Operators
---

# CAST 

| Specification | Value |
| ---- | ----- |
| Name | CAST |
| Description | Casts a parameter to a specified type. |
| Parameter 1 Name | 	param |
| Parameter 1 Type | 	any type |
| Parameter 2 Name | 	type |
| Parameter 2 Type | string - 'System.Int32', 'System.String', 'System.Decimal', 'System.Double' and all standard .net types. |
| Parameter 3 Name |
| Parameter 3 Type |
| Return value | Returns the param converted to the type. |

> [!NOTE]
> 
> CAST is used by other operators to convert their parameters to the same type. <br> The type is usually entered as a constant (CONST).

**Example:**

Let's convert the value of the state of a sales order with type 'enum' to an integer number. 

Conveting to integer allows for comparison between the states (lower -> higher):
```
10: CONVERT ATTRIB:State CONST:System.Int32      
```
OUTPUT: <br> If 'State = Released', the output will be '30'.

> [!NOTE] 
> 
> The repository of the attribute is Crm.Sales.SalesOrders

#### More examples:

- **[Check whether the releasing of the document is first or not](https://docs.erp.net/tech/advanced/calculated-attributes/examples/check-for-first-releasing.html)**
- **[Check if the system type of payment type in the sales order is 'In Cash'](https://docs.erp.net/tech/advanced/calculated-attributes/examples/check-if-system-type-is-in-cash.html)**

