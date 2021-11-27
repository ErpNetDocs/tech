# FormattedString

FormattedString is a parameter type of the user business rules **[actions](https://docs.erp.net/tech/advanced/user-business-rules/action-types/index.html)**, introduced in version 2020.1. <br> It represents a text which supports multi-line, variable interpolation, and variable formatting.

This parameter type is typically used with **[NOTIFYUSER](https://docs.erp.net/tech/advanced/user-business-rules/action-types/notifyuser.html)**.
 
Functionalities which can be used in the value of the formatted string parameter are: 
 
- **escape charts** 

The following are handled:<br>

`\n - newline - supported in the Body.`

`\r\n - also new line - supported in the Body.` 

`\{ - insert opening curly bracket '{' in output.`

`\} - insert closing curly bracket '}' in output.`
 
- **variable interpolation**

This allows specifying variables into a string using placeholders. When these placeholders are executed, they're replaced with their corresponding values. 

In @@name, those variables are **domain attributes** - both system domain and calculated attributes. 

When called, the domain attribute value is calculated for the particular entity record for which the rule is executed. In order to specify a placeholder, a.k.a call a domain attribute in text, you must specify the domain attribute name in curly brackets '{...}'.

Currently, the following options are supported:<br>

a. Attributes: {DocumentDate}, {#CalsulatedAttribute1}, {@CustomProperty1}. <br>
b. References: {Customer}.<br>
c. Reference path: {Customer.Party.PartyName}. Note that child collections are **not** supported.<br>
 
- **variable formatting** 
  
The value of the domain attributes which will be loaded in the text can be formatted. <br> This is achieved using **[format specifiers](https://docs.erp.net/tech/advanced/string-interpolation/format-specifiers.html)**: {DocumentDate:dd-MM-yyyy}.
 
**Example:**

Using formatted string, this text<br>

     Your web store has a new order!\r\n\n\{SUMMARY\} \nNumber: {DocumentNo}\nOrder date: {DocumentDate:dd-MM-yyyy}\nShipping address:
     {ShipToPartyContactMechanism.ContactMechanism.Name}\nOrder total: {#CalculatedAttributeTotalSalesOrderAmount:C}
 
will be returned as:

     Your web store has a new order!
 
     {SUMMARY}
     
     order number: 00329
     
     order date: 10-05-2019
     
     shipping address: 21 Lombard St
     
     delivery date: 12-05-2019
     
     order total: $14.82
