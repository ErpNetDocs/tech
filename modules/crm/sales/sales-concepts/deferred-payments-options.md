---
uid: deferred-payments-options
---

# Deferred payments options
 
Some companies may apply the sales policy of selling with deferred payment. And sometimes there are additional requirements needed to be met, so the deferred payment is allowed.
 
In @@name, there is an option to set a minimal total amount on a sales order in order to use deferred payments.
 
The minimal amount may be set for each Enterprise company separately in the specified currency.
 
If a sales order is set with a minimal deferred payment amount, there are certain system validations that @@name requires. 
The first option for the user is to have a sales order with @amount-to-pay greater than the sales order minimal deferred payment 
amount. If this is not true, the current sales order may be processed if:

- there are no payment plans;
- the Payment Due Date is not greater than the document date;
- the payment type system type is in cash or card.
