# Amounts Calculation


There are two common ways to determine the value of the additional amounts:
- setting an explicit amount;
- setting the amount as a percent from other amounts (additional or base amounts from the document rows).

Which method is used is a property of the document form – ‘Additional Document Amounts’ panel, by using ‘Input Percent’, ‘Input Amount’ and ‘Input Amount Currency’ fields. Usually, the user either sets a value in the ‘Input Percent’ field and the ‘Input Amount’ and ‘Input Amount Currency’ fields stay empty (this is the setting that the amount is percent of other amounts), or the user sets value to ‘Input Amount’ and ‘Input Amount Currency’ fields (this is the way we set an explicit amount), and the ‘Input Percent’ field stays empty.

Additionally, in the additional amount definition the user can control which method for determining the additional amount value is allowed - by using ‘Amount Input Allowed’ and ‘Percent Input Allowed’ fields. Also, if the ‘Percent Input Allowed’ field is True, then the user can set a default percent value, which will appear automatically in the documents.

In the additional amount definition, there is also property to control the values entered by the user in ‘Input Percent’ and ‘Input Amount’ fields. This is applied by the ‘Allowed Directions’ field:
- when ‘Allow only positive’ is selected, the user can enter only numbers bigger or equal to 0;
- when ‘Allow only negative’ is selected, the user can enter only numbers less or equal to 0;
- when ‘Allow all’ is selected, there is no limitations on the value entered in ‘Input Percent’ and ‘Input Amount’ fields.

> [!NOTE] In both methods the program is calculating an end amount, rounded to a specific >number of digits after the decimal point - this is an option of the additional amount >definition – ‘Round Scale’ field. The round scale is not used in the end amount. This >intermediate amount is used for the amount distribution. These amounts, rounded to a >specific digit after the decimal point, are always limited to the second digit after the decimal >point before saving them in the database.
 
For further information on calculating the additional amount depending on the selected method, see the following articles:
- **Explicit Value Calculation**
- **Percent Value Calculation**

