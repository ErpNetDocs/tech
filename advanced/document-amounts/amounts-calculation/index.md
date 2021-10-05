# Amounts calculation

There are two common ways to determine the value of **[additional amounts](https://github.com/ErpNetDocs/tech/blob/master/advanced/documents/additional-amounts/index.md)**:

- setting an **[explicit amount](https://github.com/ErpNetDocs/tech/blob/master/advanced/documents/additional-amounts/amounts-calculation/explicit-calculation.md)**;
- setting an amount as a **[percent](https://github.com/ErpNetDocs/tech/blob/master/advanced/documents/additional-amounts/amounts-calculation/percent-calculation.md)** of other amounts (additional or base amounts from the document rows)

Whichever method is used becomes a **property** of the document form inside the ‘Additional Document Amounts’ panel and the corresponding _‘Input Percent’_, _‘Input Amount’_ and _‘Input Amount Currency’_ fields. 

Typically, the user sets a value in the _‘Input Percent’_ field and leaves the other two empty, or in the _‘Input Amount’_ and _‘Input Amount Currency’_ fields, leaving the remaining one empty.

In the additional amount definition, the user can control which method for determining the additional amount value is allowed. This is achieved by the ‘_Amount Input Allowed’_ and _‘Percent Input Allowed’_ fields. If the second one is True, then the user can set a default percent value which will appear automatically in the documents.

The values entered by the user in the _‘Input Percent’_ and _‘Input Amount’_ fields can be managed by the _‘Allowed Directions’_ field:

- when ‘Allow only positive’ is selected, the user can enter only numbers bigger than or equal to 0;
- when ‘Allow only negative’ is selected, the user can enter only numbers less than or equal to 0;
- when ‘Allow all’ is selected, there are no limitations to the value entered in the fields.

> [!NOTE]
> In both methods, the program calculates an end amount rounded to a specific number of digits after the decimal point. This is an option of the additional amount definition – the _‘Round Scale’_ field. The round scale itself is not used in the end amount. As an intermediate amount, it is used for the amount distribution. The rounded amounts are always limited to the second digit after the decimal point before being saved in the database.
 
For further information, refer to:

- **[Explicit Value Calculation](https://github.com/ErpNetDocs/tech/blob/master/advanced/documents/additional-amounts/amounts-calculation/explicit-calculation.md)**
- **[Percent Value Calculation](https://github.com/ErpNetDocs/tech/blob/master/advanced/documents/additional-amounts/amounts-calculation/percent-calculation.md)**
