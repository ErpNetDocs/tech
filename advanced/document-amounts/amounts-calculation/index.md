# Amounts calculation

There are two common ways to determine the value of **[additional amounts](/advanced/document-amounts/index.md)**:

- setting an **[explicit amount](explicit-calculation.md)**;
- setting an amount as a **[percent](percent-calculation.md)** of other amounts (additional or base amounts from the document rows)

Whichever method is used, it becomes a **property** of the document form inside the *Additional Document Amounts* panel and the corresponding *Input Percent*, *Input Amount* and *Input Amount Currency* fields. 

You either set a value in the *Input Percent* field and leave the other two empty, <br> or set a value for *Input Amount* and *Input Amount Currency* and leave the remaining one empty. 

In the additional amount definition, you can control which method for determining the additional amount value is allowed. This is achieved by the *Amount Input Allowed* and *Percent Input Allowed* fields. 

If the second one is True, you can set a default percent value which will appear in the documents.

The values entered in *Input Percent* and *Input Amount* can be managed by the *Allowed Directions* field:

- when ‘Allow only positive’ is selected, you can only enter numbers bigger than or equal to 0;
- when ‘Allow only negative’ is selected, you can only enter numbers less than or equal to 0;
- when ‘Allow all’ is selected, there are no limitations to the value entered in the fields.

> [!NOTE]
> 
> In both methods, the program calculates an end amount rounded to a specific number of digits after the decimal point. This is an option of the additional amount definition – the *Round Scale* field. <br> The round scale itself isn't used in the end amount. As an intermediate amount, it's used for amount distribution. The rounded amounts are always limited to the second digit after the decimal point before being saved in the database.
 
------------
### See more

- **[Explicit value calculation](explicit-calculation.md)**
- **[Percent value calculation](percent-calculation.md)**
