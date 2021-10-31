# FormattedString

Formatted string is a parameter type of the User Business Rules actions which is introduced in version 2020.1. This parameter represents a text which supports multi-line, variable interpolation, and variable formatting.</br>
It's typically used with the [NOTIFYUSER](https://docs.erp.net/tech/advanced/user-business-rules/action-types/notifyuser.html) businesses rule action.
 
The functionalities which can be used in the value of the formatted string parameter are: 
 
  - escape charts 

The following are handled:<br>

           \n - newline - supported in the Body<br>
           \r\n - also new line - supported in the Body<br>
           \{ - insert opening curly bracket '{' in output.<br> 
           \} - insert closing curly bracket '}' in output. <br>
 
  - variable interpolation

This allows specifying variables into a string using placeholders which when executed are replaced with their corresponding values. In the perspective of @@name those variables are the domain attributes - both system domain attributes and calculated attributes. When called the domain attribute value is calculated for the particular entity record for which the rule is executed. In order to specify a placeholder, a.k.a call a domain attribute in text, we must specify the domain attribute name in curly brackets '{...}'.

Currently, the following options are supported:<br>

a. Attributes: {DocumentDate}, {#CalsulatedAttribute1}, {@CustomProperty1}. <br>
b. References: {Customer}.<br>
c. Reference path: {Customer.Party.PartyName}. Note that Child Collections are **not** supported.<br>
 
-  variable formatting 
  
The value of the domain attributes which is going to be loaded in the text can be formatted using **format specifiers**: {DocumentDate:dd-MM-yyyy}.

 
***Example:***


Using formatted string, this text<br>

     Your web store has e new order!\r\n\n\{SUMMARY\} \nNumber: {DocumentNo}\nOrder date: {DocumentDate:dd-MM-yyyy}\nShipping address:
     {ShipToPartyContactMechanism.ContactMechanism.Name}\nOrder total: {#CalculatedAttributeTotalSalesOrderAmount:C}
 
will be returned as:

     Your web store has e new order!
 
     {SUMMARY}<br>
     order number: 00329<br>
     order date: 10-05-2019<br>
     shipping address: 21 Lombard St<br>
     delivery date: 12-05-2019<br>
     order total: $14.82<br>
