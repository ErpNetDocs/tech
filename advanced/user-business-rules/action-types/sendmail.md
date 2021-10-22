---
uid: brat-SENDMAIL
items: ActionTypes
---

# SENDMAIL

| Name                  | SENDMAIL                                                     |
| --------------------- | ------------------------------------------------------------ |
| Description           | Used for sending notification emails using [Business rules](https://docs.erp.net/tech/advanced/user-business-rules/business-rules/index.html). The email can be sent to more than one recipients and the email's  subject and body can be customized according to the particular business  reason needs (for more info see the *'Subject and body customization'* section below). <br/><br/>The  address from which the emails are sent is the e-mail address that is set in the *From E-mail Address For System Notifications* field in  the @@name application server settings. <br/><br/>Note that  the SENDMAIL action is performed asynchronously. I.e. it is performed  every time when the Event happens (and the conditions are met) and it  does not matter whether the event has finished successfully or not. This means that if we have a [SENDMAIL] (https://docs.erp.net/tech/advanced/user-business-rules/action-types/sendmail.html) business rule that is triggered when we are saving a product, for example - an email will  be sent every time when a product saving is initiated and even if during the saving is thrown an error, the email is going to be sent regardless that action has failed. <br/><br/> **IMPORTANT:** The Sendmail action is not compatible with all [events](https://docs.erp.net/tech/advanced/user-business-rules/events/index.html). For more info, see the *Compatible Events Chart* below. |
| Parameter 1           | **[TO]** - the email address/es to which the mail is going to be sent. If there are more than one  recipients they can be entered in a comma-separated list  (email1,email2...,emailN). |
| Parameter 1 Type      | Constant, Attribute (the attribute's type must be String)    |
| Parameter 2           | **[SUBJECT]** - The line with the subject of the email.      |
| Parameter 2 Type      | Constant, Attribute (the attribute's type must be String)    |
| Parameter 3           | **[BODY]** - The content of the body of the email. Supports multi-line, for more  info see the 'Subject and Body Customization' section below. |
| Parameter 3 Type      | Constant, Attribute (the attribute's type must be String)    |
| Example               | see the end of the article                                   |
| Introduced In Version | 2019.1                                                       |



 

**Note:** Currently, the parameters of the business rules can include up to 256 symbols. 

## Compatible Events Chart

The SENDMAIL action is not compatible with all [events](https://docs.erp.net/tech/advanced/user-business-rules/events/index.html). For more info look into the following chart.

| Event Type                                                   | Compatibility with SENDMAIL                                |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| Client Commit (e.g. CLIENTCOMMIT, AGGREGATECLIENTCOMMIT)     | compatible                                                   |
| Document Events - (e.g. STATECHANGING, STATECHANGED, VOIDING) | compatible                                                   |
| Commit (e.g. COMMIT)                                         | compatible but not recommended - if possible, use CLIENTCOMMIT instead|
| Front-End (e.g ATTRIBUTECHANGING, ATTRIBUTECHANGED)          | not compatible, the server will not send an email|



## Subject and body customization 

The text in the parameters for Subject and Body can be customized according to the specific needs. For added convenience, we've made a couple of implementations in order to provide more formatting capabilities and to  facilitate the action as a whole.

- escape charts 

The following escape chars are handled:

\n - newline - supported in the Body

\r\n - also new line - supported in the Body

\{ - insert opening curly bracket '{' in output. - supported in both the Subject and the Body

\} - insert closing curly bracket '}' in output. - supported in both the Subject and the Body



- HTML tags - supported in the Body

The body could be also formatted using HTML. In order for the text to be  recognized as HTML, the body has to contain the tag </html>. The  place of the tag is irrelevant, if the tag </html> is placed somewhere in the body's text it is considered that the whole text is written in HTML.



- use of domain attributes in text - supported in both the Subject and the Body

In the text of both parameters for Subject and Body, we can now reach and  use the domain attributes' values (system domain attributes and calculated attributes). They are calculated for the particular entity  record for which the rule is executed. In order for the domain attribute to be property recognized by the system, it needs to be surrounded with curly brackets '{...}'.

Currently are supported the following options:
\1. Attributes: {DocumentDate}. 
\2. References: {Customer}.
\3. Reference path: {Customer.Party.PartyName}. Note that Child Collections are not supported.



- Domain attributes formatting - supported in both the Subject and the Body

The domain attribute values can be formatted with the standard .Net format  specifiers and the system-specific attributes. For more information, see [Format specifiers](https://docs.erp.net/tech/advanced/string-interpolation/format-specifiers.html).



## Example

А [business rule](https://docs.erp.net/tech/advanced/user-business-rules/business-rules/index.html) that sends an email with an order confirmation to the customer and the sales manager when a sales order has been released.



| Repository            |                 |                    |                                                              |                 |                                         |                 |                                                              |
| --------------------- | --------------- | ------------------ | ------------------------------------------------------------ | --------------- | --------------------------------------- | --------------- | ------------------------------------------------------------ |
| Crm.Sales.SalesOrders |                 |                    |                                                              |                 |                                         |                 |                                                              |
| **Events**            |                 |                    |                                                              |                 |                                         |                 |                                                              |
| Event Type            | Event Parameter | Execution Priority |                                                              |                 |                                         |                 |                                                              |
| Change of State       | RELEASED        | Normal             |                                                              |                 |                                         |                 |                                                              |
| **Actions**           |                 |                    |                                                              |                 |                                         |                 |                                                              |
| Action No             | Action Type     | Parameter1 Type    | Parameter1 Value                                             | Parameter2 Type | Parameter2 Value                        | Parameter3 Type | Parameter3 Value                                             |
| 1                     | SENDMAIL        | Constant           | salesmanager@mail.com,customer@gmail.com | Constant        | Order No{DocumentNo} has been confirmed | Constant        | \<p>Dear Customer,\</p>\<p>\<b> Your order has been confirmed!  \</b>\</p>\<br/>\<p>\<h3>SUMMARY\</h3>\</p>\<p>Order Number: \<i>{DocumentNo}\</i>\</p>\<p>Order Date:  \<i>{DocumentDate:dd-MM-yyyy}\</i>\</p>\<p>Shipping  Address: \<i>{ShipToPartyContactMechanism.  ContactMechanism.Name}\</i>\</p>\<p>Delivery Date:  \<i>{RequiredDeliveryDate:dd-MM-yyyy}\</i>\</p>\<p>Order Total:  \<i>{#CalculatedAttributeTotalSalesOrderAmount:C}\</i>\</p>\<p>Payment Method:  \<i>{PaymentType.Name}\</i>\</p>\<br/>\<p>Please expect your parcel to arrive on the delivery date stated above at the  address or at the office of the courier  company.\</p>\<br/>\<p>Kind  Regards,\</p>\<strong>{SalesPerson.Person.FirstName}  {SalesPerson.Person.LastName}\<strong/>\</html> |



### A representation of the email which is going to be received by the recipients:



**Subject:** 'Order No00329 has been confirmed'



**Body:**
'Dear Customer,

**Your order has been confirmed!**

### SUMMARY

Order Number: *00329*

Order Date: *10-05-2019*

Shipping Address: *21 Lombard St*

Delivery Date: *12-05-2019*

Order Total: *$14.82*

Payment Method: *Cash on Delivery*



Please expect your parcel on the delivery date stated above at the address or at the office of the courier company.



Kind Regards,

**John Smith**'
