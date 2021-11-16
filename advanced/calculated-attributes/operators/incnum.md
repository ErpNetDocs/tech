---
uid: cao-INCNUM
items: Operators
---

# INCNUM 

| Specification         | Value                                                        |
| --------------------- | ------------------------------------------------------------ |
| Description           | Increases the value of its parameter by 1. <br> Can be used only with string values whose last character is a number. <br> Allows for consecutive numbering of documents and nomenclatures. |
| Parameter 1 Name      | Value                                                         |
| Parameter 1 Type      | string                                    |
| Parameter 2 Name      | -                                                            |
| Parameter 2 Type      | -                                                            |
| Parameter 3 Name      | -                                                            |
| Parameter 3 Type      | -                                                            |
| Return value          | ++Value                                                    |


> [!NOTE]
> 
> If you try incrementing a string whose last character is 'AA01', the incrementation will be successful and result will be 'AA02'. 
> If you increment a value of type decimal, int or date, the incrementation will be unsuccessful and the attribute won't compilate.
> If the value is a string whose last character isn't a number ('AA', for example), the incrementation won't be successful.

**Example:**

Let's see how to increase the **LotNumber** of a lot by 1:

```
10: INCNUM ATTRIB:Number 
```
OUTPUT: 
<br/>If 'Number = 0001'', the output will be '0002'.
<br/>If 'Number = AA01'', the output will be 'AA02'.

> [!NOTE]
> 
> The repository of the attribute is *Logistics.Inventory.Lots*
