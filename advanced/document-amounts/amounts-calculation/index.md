# Amounts calculation

There are two common ways to determine the value of [additional amounts](https://docs.erp.net/tech/advanced/document-amounts/index.html?q=document%20amounts):

- setting an **[explicit amount]()**;
- setting an amount as a **[percent](https://docs.erp.net/tech/advanced/document-amounts/amounts-calculation/percent-calculation.html)** of other amounts (additional or base amounts from the document rows)

Whichever method is used becomes a **property** of the document form inside the *Additional Document Amounts* panel and the corresponding  
*Input Percent*, *Input Amount* and *Input Amount Currency* fields. 

Typically, the user sets a value in the *Input Percent* field and leaves the other two empty, or in the *Input Amount* and *Input Amount Currency* fields, leaving the remaining one empty.

In the additional amount definition, the user can control which method for determining the additional amount value is allowed. This is achieved by the *Amount Input Allowed* and *Percent Input Allowed* fields. If the second one is True, then the user can set a default percent value which will appear automatically in the documents.

The values entered by the user in the *Input Percent* and *Input Amount* fields can be managed by the *Allowed Directions* field:

- when ‘Allow only positive’ is selected, the user can enter only numbers bigger than or equal to 0;
- when ‘Allow only negative’ is selected, the user can enter only numbers less than or equal to 0;
- when ‘Allow all’ is selected, there are no limitations to the value entered in the fields.

> [!NOTE]
> In both methods, the program calculates an end amount rounded to a specific number of digits after the decimal point. This is an option of the additional amount definition – the *Round Scale* field. The round scale itself is not used in the end amount. As an intermediate amount, it is used for the amount distribution. The rounded amounts are always limited to the second digit after the decimal point before being saved in the database.
 
For further information, refer to:

- **[Explicit Value Calculation](https://github.com/ErpNetDocs/tech/blob/master/advanced/documents/additional-amounts/amounts-calculation/explicit-calculation.md)**
- **[Percent Value Calculation](https://docs.erp.net/tech/advanced/document-amounts/amounts-calculation/percent-calculation.html)**
