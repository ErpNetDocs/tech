---
uid: cao-EQUAL
items: Operators
---
# EQUAL 

| Specification | Value |
| ---- | ----- |
| Name | EQUAL |
| Description | Checks if two values are equal. If that's the case, the return value is 'True', else - the return value is 'False'. |
| Parameter 1 Name | Value1 |
| Parameter 1 Type | numeric type - int, double or decimal; string; |
| Parameter 2 Name | Value2 |
| Parameter 2 Type | numeric type - int, double or decimal; string; |
| Parameter 3 Name |
| Parameter 3 Type |
| Return value | boolean (True or False) |


Make sure the compared values are from the same type. 

For example, Parameter 1 and Parameter 2 must be both integers, or doubles, or decimals, or strings.

**Example:**

```      
10: EQUAL ATTRIB:LineNo CONST:30   
```
OUTPUT: 
<br/>If 'LineNo = 30', the output will be 'True'.
<br/>If 'LineNo = 10', the output will be 'False'.


> [!NOTE]
> 
> The repository of the attribute is *Crm.Sales.SalesOrderLines*

#### More examples:

- **[Check if the quantity is a whole number](https://docs.erp.net/tech/advanced/calculated-attributes/examples/check-if-quantity-is-whole-number.html)**
- **[Check whether the releasing of the document is first or not](https://docs.erp.net/tech/advanced/calculated-attributes/examples/check-for-first-releasing.html)**
- **[Get current availability of a product](https://docs.erp.net/tech/advanced/calculated-attributes/examples/get-current-availability-of-product.html)**
