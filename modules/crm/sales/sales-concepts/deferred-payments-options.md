# Deferred Payments Options
 
Some companies may apply the sales policy of selling with deferred payment. And sometimes there are additional requirements needed to be met, so the deferred payment is allowed.
 
In @@name, there is an option to set a minimal total amount on a Sales Order in order to use deferred payments.
 
The minimal amount may be set for each @@name separately in the specified currency.
 
If a sales order is set with a minimal deferred payment amount, there are certain system validations that @@name requires. 
The first option for the user is to have a sales order with **[Amount to pay](https://github.com/ErpNetDocs/tech/blob/master/modules/crm/sales/sales-concepts/amount-to-pay.md)** greater than the sales order minimal deferred payment 
amount. If this is not true, the current sales order may be processed if:

- there are no payment plans;
- the Payment Due Date is not greater than the Document Date;
- the payment type system type is In Cash or Card.
