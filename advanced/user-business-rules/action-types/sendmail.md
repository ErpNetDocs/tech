---
uid: brat-SENDMAIL
items: ActionTypes
---

# SENDMAIL

| Name                  | SENDMAIL                                                     |
| --------------------- | ------------------------------------------------------------ |
| Description           | Used for sending notification emails using **[business rules](https://docs.erp.net/tech/advanced/user-business-rules/business-rules/index.html)**. Emails can be sent to multiple recipients and the subject and body can be customized according to the business's needs. <br><br> For more information, check out the **Subject and body customization** section below. <br/><br/> The address from which emails are sent is the one set in the *From E-mail Address For System Notifications* field in the @@name application server settings. <br/><br/> **IMPORTANT:** SENDMAIL is not compatible with all **[events](https://docs.erp.net/tech/advanced/user-business-rules/events/index.html)**. <br> For more info, see the *Compatible Events Chart* section below. |
| Parameter 1           | **[TO]** - the email address/es to which the mail is going to be sent. If there's more than one recipient, they can be entered in a comma-separated list (email1,email2...,emailN). |
| Parameter 1 type      | Constant, Attribute (type must be 'String')    |
| Parameter 2           | **[SUBJECT]** - the line with the subject of the email.      |
| Parameter 2 type      | Constant, Attribute (type must be 'String')    |
| Parameter 3           | **[BODY]** - the content of the body of the email. Supports multi-line. |
| Parameter 3 type      | Constant, Attribute (type must be 'String')    |
| Example               | see the end of the article                                   |
| Introduced in version | 2019.1                                                       |

> [!NOTE]
> 
> Currently, parameters of business rules can include up to 256 symbols. 

## Compatible events chart

SENDMAIL is **not** compatible with all events. Take a look at the following chart:

| Event type                                                   | Compatibility with SENDMAIL                                |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| Client commit (e.g. [CLIENTCOMMIT](https://docs.erp.net/tech/advanced/user-business-rules/events/client-commit.html), [AGGREGATECLIENTCOMMIT](https://docs.erp.net/tech/advanced/user-business-rules/events/aggregate-client-commit.html))     | compatible                                                   |
| Document events - (e.g. [STATECHANGING](https://docs.erp.net/tech/advanced/user-business-rules/events/statechanging.html), [STATECHANGED](https://docs.erp.net/tech/advanced/user-business-rules/events/statechanged.html), [VOIDING](https://docs.erp.net/tech/advanced/user-business-rules/events/voiding.html))| compatible                                                   |
| Commit (e.g. [COMMIT](https://docs.erp.net/tech/advanced/user-business-rules/events/commit.html))                                         | compatible but not recommended - if possible, use CLIENTCOMMIT instead |
| Front-end (e.g ATTRIBUTECHANGING, ATTRIBUTECHANGED)          | incompatible, the server won't send an email |

## Subject and body customization 

Text in the parameters for _Subject_ and _Body_ can be **customized**. For added convenience, there are a couple of implementations providing more formatting capabilities and facilitating the action as a whole.

- **escape charts** 

The following escape chars are handled:

`\n - newline - supported in the Body`

`\r\n - new line - supported in the Body`

`\{ - insert opening curly bracket '{' in output. - supported in both the Subject and the Body`

`\} - insert closing curly bracket '}' in output. - supported in both the Subject and the Body`

- **HTML tags** - supported in the Body

For text to be recognized as HTML, the Body has to contain the `</html>` tag. The position of the tag is irrelevant. If it's placed somewhere, the whole text is considered written in HTML.

- **Use of domain attributes in text** - supported in both the Subject and the Body

In the text of both parameters for Subject and Body, you can reach and use the domain attributes' values (system domain attributes and **[calculated attributes](https://docs.erp.net/tech/advanced/calculated-attributes/index.html)**). They're calculated for the entity record for which the rule is executed. In order for a domain attribute to be property recognized by the system, it needs to be surrounded with curly brackets '{...}'.

The following options are supported:

1. Attributes: {DocumentDate}. <br>
2. References: {Customer}. <br>
3. Reference path: {Customer.Party.PartyName}. Note that child collections are not supported.

- **Domain attributes formatting** - supported in both the Subject and the Body

Domain attribute values can be formatted with standard .Net **[format specifiers](https://docs.erp.net/tech/advanced/string-interpolation/format-specifiers.html)** and system-specific attributes.

### Example:

А business rule that sends an email with an order confirmation to the customer and the sales manager when a sales order has been released.

| Repository            |                 |                    |                                                              |                 |                                         |                 |                                                              |
| --------------------- | --------------- | ------------------ | ------------------------------------------------------------ | --------------- | --------------------------------------- | --------------- | ------------------------------------------------------------ |
| Crm.Sales.SalesOrders |                 |                    |                                                              |                 |                                         |                 |                                                              |
| **Events**            |                 |                    |                                                              |                 |                                         |                 |                                                              |
| Event type            | Event parameter | Execution priority |                                                              |                 |                                         |                 |                                                              |
| Change of state       | RELEASED        | Normal             |                                                              |                 |                                         |                 |                                                              |
| **Actions**           |                 |                    |                                                              |                 |                                         |                 |                                                              |
| Action No             | Action type     | Parameter1 type    | Parameter1 value                                             | Parameter2 type | Parameter2 value                        | Parameter3 type | Parameter3 value                                             |
| 1                     | SENDMAIL        | Constant           | salesmanager@mail.com, customer@gmail.com | Constant        | Order No{DocumentNo} has been confirmed | Constant        | \<p>Dear Customer,\</p>\<p>\<b> Your order has been confirmed!  \</b>\</p>\<br/>\<p>\<h3>SUMMARY\</h3>\</p>\<p>Order Number: \<i>{DocumentNo}\</i>\</p>\<p>Order Date:  \<i>{DocumentDate:dd-MM-yyyy}\</i>\</p>\<p>Shipping  Address: \<i>{ShipToPartyContactMechanism.  ContactMechanism.Name}\</i>\</p>\<p>Delivery Date:  \<i>{RequiredDeliveryDate:dd-MM-yyyy}\</i>\</p>\<p>Order Total:  \<i>{#CalculatedAttributeTotalSalesOrderAmount:C}\</i>\</p>\<p>Payment Method:  \<i>{PaymentType.Name}\</i>\</p>\<br/>\<p>Please expect your parcel to arrive on the delivery date stated above at the  address or at the office of the courier  company.\</p>\<br/>\<p>Kind  Regards,\</p>\<strong>{SalesPerson.Person.FirstName}  {SalesPerson.Person.LastName}\<strong/>\</html> |

### Sample email received by the recipients:

**Subject:** 'Order No00329 has been confirmed'

**Body:**

Dear Customer,

Your order has been confirmed!

#### SUMMARY

Order number: *00329*

Order date: *10-05-2019*

Shipping address: *21 Lombard St*

Delivery date: *12-05-2019*

Order total: *$14.82*

Payment method: *Cash on delivery*

Expect your parcel at the address or the office of the courier company on the delivery date stated above.

Kind Regards,

John Smith
