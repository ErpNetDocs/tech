# Parameter type CONST

When used, indicates that the Value for this parameter type would be a constant for every calculation of the calculated attribute. 

The formats of the different types of values which are entered are as follows:



| Value   | Description                                                  | Example                              |
| ------- | ------------------------------------------------------------ | ------------------------------------ |
| NULL    | null or empty value                                          | NULL                                 |
| Boolean | true or false value                                          | True                                 |
| Integer | a whole number (not a fractional number) that can be positive, negative, or zero | 93                                   |
| Decimal | number, containing decimal symbol - '.'                      | 93.012                               |
| Date    | date values used in the 'yyyy-MM-dd' format                  | 2020-12-25                           |
| GUID    | Global Unique Identifier - used for objects identification   | 6B29FC40-CA47-1067-B31D-00DD010662DA |
| String  | explicitly denoted string, entered in single quotation marks | 'Example text.'                      |
| Type    | used with [CAST](../operators/cast.md). Used for type conversions and the constant is the type to which we want to convert. | System.Int32                         |

Everything else is treated as string!
