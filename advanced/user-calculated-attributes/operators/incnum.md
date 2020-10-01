---
uid: cao-INCNUM
---

# INCNUM - Calculated Attribute Operator

| Specification         | Value                                                        |
| --------------------- | ------------------------------------------------------------ |
| Description           | The INCNUM operator increases the value of its parameter by 1. The operator can be used only for String values whоose last character is a number.           |
| Parameter 1 Name      | Value                                                         |
| Parameter 1 Type      | string                                    |
| Parameter 2 Name      | -                                                            |
| Parameter 2 Type      | -                                                            |
| Parameter 3 Name      | -                                                            |
| Parameter 3 Type      | -                                                            |
| Return Value          | ++Value                                                    |


## Example

```
If the user tries to increment the string value 'AA01', the incrementation will be successful and result will be 'AA02'; 

If the user tries to increment a value whoоse type is Decimal, Int or Date, the incrementation won't be successful and the Calculated Attribute won't be compilated;

Also if the value is a string whose last character is not a number ('AA', for example), the incrementation won't be successful.

The INCNUM operator can be used for consecutive numbering of documents and nomenclatures.
```

This simple example returns 'AA02':

```
10: INCNUM CONST:AA01
```
The example below shows how to increase the LotNumber of the Lot by 1 with the INCNUM operator:
```
Logistics.Inventory.Lots =>

10: INCNUM ATTRIB:Number 
```
