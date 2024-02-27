# Determine payment account in sales order

The algorithm for the determination of the payment account in the sales order is the following:

SalesOrder.PaymentAccount is set to one of the following (in order of their precedence):

1. If the ShipToCustomer.DefaultPaymentType = SalesOrder.PaymentType AND the ShipToCustomer.PaymentAccount is not null => it is taken.
2. If the Customer.DefaultPaymentType = SalesOrder.PaymentType AND the Customer.PaymentAccount is not null => it is taken.
3. If the PaymentType.DefaultPaymentAccount is not null => it is taken.
4. No changes are applied.

## The rationale, expected setup and usage

1. Initially, the user chooses a customer. The payment type and the payment account of the customer would be copied to the sales order.

> [!NOTE] 
> It is important, that the customers' payment type IS set to some non-null value!

The following events happen:
- The user selects a customer.
- The payment type of the customer is loaded in the sales order.
- Since the payment type of the sales order is the same as the customers, the customer’s payment account is copied to the sales order.

2. If however, the user chooses a different payment type, the default account of this new payment type is selected.
 
For example, the customer usually pays cash and has a cash payment account specified. But now he chose to pay by credit card. In this case, the system loads the payment account of the 'Credit Card' payment type. 
 
The event order is the following:
 
- The user selects a customer
- The payment type of the customer is loaded in the sales order.
- The user selects different payment types.
- Since the payment type of the sales order is no longer the same as the customers', the payment account of the sales order is now copied from the definition of the payment type.
