# FormattedString

Formatted String is a Parameter Type of the User Business Rules Actions which is introduced in version 2020.1. This parameter represents a text which supports multi-line, variable interpolation, and variable formatting. Usually used with **NOTIFYUSER** user businesses rule action.
 
In more, details the functionalities which can be used in the value of the Formatted String parameter are: 
 
  - escape charts 

The following escape chars are handled:<br>
\n - newline - supported in the Body<br>
\r\n - also new line - supported in the Body<br>
\{ - insert opening curly bracket '{' in output.<br> 
\} - insert closing curly bracket '}' in output. <br>
 
  - variable interpolation

Variable interpolation allows specifying variables into a string using placeholders which when executed are replaced with their corresponding values. In the perspective of EnterpriseOne those variables are the domain attributes - both system domain attributes and calculated attributes. When called the domain attribute value is calculated for the particular entity record for which the rule is executed. In order to specify a placeholder, aka call a domain attribute in text, we must specify the domain attribute name in curly brackets '{...}'.

Currently are supported the following options:<br>
1. Attributes: {DocumentDate}, {#CalsulatedAttribute1}, {@CustomProperty1}. <br>
2. References: {Customer}.<br>
3. Reference path: {Customer.Party.PartyName}. Note that Child Collections are not supported.<br>
 
-  variable formatting - the value of the domain attributes which is going to be loaded in the text can be formatted using **Format Specifiers** - {DocumentDate:dd-MM-yyyy}.
 
#### Example
Using Formatted String, this text:<br>

     Your web store has e new order!\r\n\n\{SUMMARY\} \nNumber: {DocumentNo}\nOrder Date: {DocumentDate:dd-MM-yyyy}\nShipping Address:
     {ShipToPartyContactMechanism.ContactMechanism.Name}\nOrder Total: {#CalculatedAttributeTotalSalesOrderAmount:C}
 
will, for example, be returned as:

     Your web store has e new order!
 
{SUMMARY}<br>
Order Number: 00329<br>
Order Date: 10-05-2019<br>
Shipping Address: 21 Lombard St<br>
Delivery Date: 12-05-2019<br>
Order Total: $14.82<br>


