---
uid: cao-LEN
items: Operators
---

# LEN 

| Specification         | Value                                                        |
| --------------------- | ------------------------------------------------------------ |
| Description           | Returns the length of a string.                              |
| Parameter 1 Name      | String                                                       |
| Parameter 1 Type      | string                                                       |
| Parameter 2 Name      | -                                                            |
| Parameter 2 Type      | -                                                            |
| Parameter 3 Name      | -                                                            |
| Parameter 3 Type      | -                                                            |
| Return value          | The string's length.                                         |

> [!NOTE] 
> 
> Spaces are included when calculating the length.


**Example:**

Let's return the length of the notes set in a sales order:
```
10: LEN ATTRIB:Notes
```
OUTPUT: 
<br/> If 'Notes = Apple', the output will be '5'.
<br/> If 'Notes = I am', the output will be '4'. 

> [!NOTE] 
> 
> The repository of the attribute is *Crm.Sales.SalesOrders*.

[!NOTE]
> It is important to note that if the string being passed to the LEN function is null, it will return an error. Therefore, it is recommended to add an IF > > > operator to check whether the string is null before passing it to the LEN function. This will prevent any errors from occurring and ensure that the function > > 
works as intended.

**Example:**
10	IIF	EXP	7	CONST	0	EXP	10
20	EQUAL	ATTRIB	DocumentNotes	CONST	Null
30	LEN	ATTRIB	DocumentNotes
