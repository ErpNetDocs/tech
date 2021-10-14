---
uid: cao-INCNUM
items: Operators
---

# INCNUM 

| Specification         | Value                                                        |
| --------------------- | ------------------------------------------------------------ |
| Description           | The INCNUM operator increases the value of its parameter by 1. The operator can be used only for string values whose last character is a number. The INCNUM operator can be used for consecutive numbering of documents and nomenclatures. |
| Parameter 1 Name      | Value                                                         |
| Parameter 1 Type      | string                                    |
| Parameter 2 Name      | -                                                            |
| Parameter 2 Type      | -                                                            |
| Parameter 3 Name      | -                                                            |
| Parameter 3 Type      | -                                                            |
| Return value          | ++Value                                                    |


> [!NOTE]
> 
>- If you try to increment the string value whose last character is a number 'AA01', the incrementation will be successful and result will be 'AA02'; 
>- If you try to increment a value whоse type is decimal, int or date, the incrementation won't be successful and the calculated attribute won't be compilated;
>- If the value is a string whose last character is not a number ('AA', for example), the incrementation won't be successful.

## Examples

 The following example shows how to increase the LotNumber of the lot by 1 with the INCNUM operator:

```
10: INCNUM ATTRIB:Number 
```
OUTPUT: 
<br/>If 'Number = 0001'', the output will be '0002'.
<br/>If 'Number = AA01'', the output will be 'AA02'.

> [!NOTE]
> 
> The repository of the attribute is *Logistics.Inventory.Lots*
