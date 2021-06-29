---
uid: sales-order-payment-plan
---

# Sales Order Payment Plan

This topic describes the essence of the Sales Order Payment Plans, the method of calculating the Installments, and the algorithm for creating payment requests under a plan.

## Sales Order Payment Plans

The sales order payment plan determines how the amount of the given sales order is paid (with how many instalments and their individual amounts).

For each instalment, there are two main attributes - **a method for determining the amount and a method for determining the due dates (the payment term).**

**Methods for determining the amount (specified by the "Amount Percent", "Amount" and "Remainder" fields):**

- an indication of a fixed amount that does not depend on other factors;

- the amount of the instalment is a percentage of the total amount of the transaction;

- the amount is the remainder that is not covered by the other instalments.

It is mandatory that in every plan there must be exactly one instalment marked as a "Remainder" (usually this is the last instalment in the plan). 
It is necessary to have such an instalment because it "picks up" all of the small inaccuracies and differences of rounding (if there are other instalments whose amounts are determined by a percentage). 
It can also "picks up" and the changes in the total amount that happen due to changes in the terms of trade in the Invoices (see Example 3 below).

There are two main fields whose values need to be determined in order to define the payment term - Payment Due Start Date (aka Execution Date) and Payment Due Date. 
Payment Due Start Date (aka Execution Date) is the date when the payment becomes due/executable and Payment Due Date is the last day of the payment term.

**Due Date Form Methods according to which the payment term is calculated:**

- Specify the date explicitly: the payment due start date is determined by adding "Payment Term Days" to the "Explicit Payment Due Date" and the due date is "Explicit execution date" added with "Execution term, days";
- Use Sales Order Due Date: “Due Start Date”/”Execution date” and “Payment Due Date” are copied directly from the Sales Order header fields “Payment Due Start Date “ and “Payment Due Date”;
- Use Sales Order Date: the dates are calculated using the Sales Order “Document date” added with the number of days entered in "Execution term, days” (for the calculation of the payment start due date) or "Payment Term Days" (for the calculation of the due date);
- Use Invoice Due date: “Due Start Date”/”Execution date” and “Payment Due Date” are copied directly from the Invoice header fields “Payment Due Start Date “ and “Payment Due Date”;
- Use Invoice Date: the dates are calculated using the Invoice “Document date” added with the number of days entered in "Execution term, days” (for the calculation of the payment start due date) or "Payment Term Days" (for the calculation of the due date);

The last two methods use the delivery invoice dates. If they are not yet issued, then the dates are calculated according to the values inserted in the Sales Order header.

If for the particular sales order there is no indicated payment plan at all, then it is considered that there is a plan that consists of only one instalment.
This instalment is not numbered (see the Create Payment Orders section below) and is for total Amount to Pay of the Sales Order. 
In a "service" instalment the method of determining the payment term depends on whether the Payment Orders for the invoiced amounts will be created from the Sales Order or not (this depends on the setting of the Payment Order generation procedure). 
If the Payment Orders for invoiced amounts will be generated from the Sales Order, then for the Due Date Form Method is used the “Use Invoice Due date” method, otherwise is used the “Use Sales Order Due date” method.

## Determining the total payment amount

In order to determine the amount of each instalment, it is first necessary to determine what is the total / final amount that has to be paid for this transaction. 
This is done using the data from several documents - the Sales Order with which the transaction is reflected and all Invoices for this sale (both for the advance and for delivery).

For this purpose, two types of Amounts are calculated separately – Sales Order Amounts and Invoice Amounts, which are then summed to obtain the final amount.
Invoice Amounts are the Amounts to Pay (see topic [Amount To Pay](amount-to-pay.md)) of the delivery Invoices.
And the Sales Orders Amounts are the paid advances and the remaining part of the Amount to Pay (see topic [Amount To Pay](amount-to-pay.md)) of the Sales Order, which is not covered by an advance or delivery.

To determine the last amount (the remaining part of the Amount to Pay of the Sales Order), the following formula is used:

**[remaining part] = [Amount to Pay of the Sales Order] - [advances paid] - [invoiced part of the Sales Order]**

 The invoiced part is calculated by determining how much of the Amount to Pay of the Sales Order is covered by the delivery Invoices. This is done for each line of Invoices in two alternative methods:
- through the "Covered amount" field of the Invoice lines;
- or through the Quantities in the Invoice lines (this is used for the lines in which the "Covered Amount" is not filled in).
Finally, the results of all lines of delivery Invoices for current Sales Order are summed into **[invoiced part of the Sales Order]**. 
It does not matter what the final Amount to Pay for the Invoice is.
The reason why the final Amount to Pay of the Invoice is not to be considered is that there may be a change in the trading conditions (prices, discounts, etc.). 
This should not change the ratio - what part of the Sales Order is covered by this Invoice.

The first method is based on this how much of the basе of the Sales Order (the "Line Amount" field of the sales order line) is covered by the value of "Sales Order Amount" field in the line of the Invoice.
This relationship determines what part of the Sales Order line has been invoiced. For example, if the Sales Order lines is for **100.00 BGN** and we have **20.00 BGN** VAT (ie the Amount to Pay of the Sales Order is 120.00 BGN) and there is one Invoice line in which the covered "Sales Order Amount" is 70.00 BGN, then the invoiced part of the Sales Order line is **120.00 * 70.00 / 100.00 = 84.00 BGN.**

The second method works on the same principle, but the relationship is made between the quantities of the Sales Order line and the Invoice line.
For example, if in the Sales Order line there is a Quantity = **10 pcs** with a total Amount to Pay = **90.00 BGN** and there is only one Invoice line for Quantity = **7 pcs** then the invoiced part of the Sales Order line is **90.00 BGN * 7 pc / 10 pc = 63.00 BGN**.

If in the Invoice there also is an advance deduction, this deduction is also subtracted from the invoiced part (because advances are aggregated in **[advances paid]**). If in the example described above there is an advance deduction of **15.00 BGN** in the Invoice, then the invoiced part of the Sales Order is **(90.00 BGN * 7 pcs / 10pcs) – 15.00 BGN = 48.00 BGN**.

### Example 1:

There is a Sales Order with Quantity = **10 pcs** for a total Amount to Pay of **90.00 BGN**, there already is a paid advance of **15.00 BGN** and two delivery Invoices (in which the field "Sales Order Amount" is not filled in):

- one for Quantity =  **3 pcs** in which we deduct the advance and therefore we have an Amount to Pay of the Invoice **12.00 BGN = (27.00 BGN – 15.00 BGN)**;

- one for Quantity =  **4 pcs**, in which trade conditions are changed and so we have an Amount to Pay of the Invoice **41.00 BGN** (instead of the expected **36.00 BGN**).

The result is:

**[invoiced part of Sales Order] = (90.00 BGN * 3 pss / 10 pcs) + (90.00 BGN * 4 pcs / 10 pcs) – 15.00 BGN = 48.00 BGN;**

**[remaining part] = 90.00 BGN – 15.00 BGN – 48.00 BGN = 27.00 BGN;**

Thus, we receive two Invoice Amounts – **12.00 BGN** and **41.00 BGN** - and two Sales Order Amounts – **15.00 BGN** (advance) and **27.00 BGN**. The final payment amount is:

**[total Amount to Pay] = 12.00 BGN + 41.00 BGN + 15.00 BGN + 27.00 BGN = 95.00 BGN**

In principle, (and from **Example 1**) we see that the total Amount to Pay practically is the Amount to Pay of the Sales Order summed with the increases/decreases that occurred due to a change in the terms of trade in the Invoices. 
The reason behind the using of such a breakdown of individual (smaller) amounts in the calculation is to avoid a (technical) complex analysis of how exactly the trade terms of the Invoices have changed and how this changes and affects the total amount. 
Also, these individual amounts help with the creation of Payment Orders.

## Determination of the instalments amounts

The instalments are calculated by computing of the total Amount to Pay and applying the method of determining the instalment amount. Here are two examples:

### Example 2:

There is a Sales Order with a total Amount to Pay **95.00 BGN**. For this Sales Order, there is a payment plan with three instalments: the first for **33.30 %**, the second for **33.70 %** and the third is marked as a "**Remainder**". Thus, we get the following instalments:

- **[Instalment 1]** **= 95.00 BGN * 33.30 %** = 31.635 ~ **31.64 BGN;**

- **[Instalment 2]** **= 95.00 BGN * 33.70 %** = 32.015 ~ **32.02 BGN;**

- **[Instalment 3] = 95.00 BGN - 31.64 BGN - 32.02 BGN = 31.34 BGN;**

**Example 2** shows that when using a percent-based instalment and we have a change (increase/decrease) in the Amount to Pay because of changing the terms of trade in the invoices, this change is evenly distributed among the instalments.

It also illustrates the usefulness of the "Remainder" instalment. If it was, instead, **33.00 %**, then the total amount of the three instalments (after determining the percentages after the rounding) would be **95.05 BGN** and not **95.00 BGN!**

### Example 3:

There is a Sales Order with a total Amount to Pay **95.00 BGN**. For this Sales Order, there is a payment plan with three instalments - the first for an exact amount of **30.00 BGN**, the second for an exact amount of **40.00 BGN** and the third is marked as a "remainder". 
Thus, we get the following instalments:

- **[Instalment 1]** = **30.00 BGN** (fixed amounts do not change);

- **[Instalment 2]** = **40.00 BGN** (fixed amounts do not change);

- **[Instalment 3] = 95.00 BGN – 30.00 BGN – 40.00 BGN = 25.00 BGN;**

This example illustrates the other benefits of the "Remainder" instalment.
When there are only fixed amounts in the previous instalments and there is s change of the trade terms in the Invoices, then this change is reflected in the last instalment.

## Create Payment Orders

When we create Payment Orders by a Sales Order Payment Plan, first we have to determine the Amount (as described above) and the Due Dates for any of the plan instalments.
Thereafter, are determined individual Sales Order and Invoices Amounts (those from which the total amount is formed). 
We make an additional breakdown of the instalments and the instalments are exhausted in the order of creation of the individual amounts.

### Example 4:

Let's use the situation of Example 1 and the payment plan of **Example 3**. We get the following breakdown:

- **15.00 BGN** - from **[instalment 1]** and because of the advance amount of the Sales Order;

- **12.00 BGN** - from **[instalment 1]** and because of the amount of the first Invoice;

- **3.00 BGN** - from **[instalment 1]** and because of the amount of the second Invoice;

- **38.00 BGN** - from **[instalment 2]** and because of the amount of the second Invoice;

- **2.00 BGN** - from **[instalment 2]** and because of the remaining part amount of the Sales Order;

- **25.00 BGN** - from **[instalment 3]** and because of the remaining part amount of the Sales Order.

More examples of Payment Orders generated by Sales Order Payment Plans there are in topic [Transitional Documents](~/advanced/documents/transitional-documents.md).

> [!NOTE:]
>  In the usual case, the Sales and Invoice Amounts will match the instalments Amounts, in fact, the resulting breakdown will match the payment plan (none of the instalments will be "broken down").

Then, for each **Amount** of the resulting breakdown can be created a separate Payment Order.
Whether it will be created or not depends on the settings of the generation procedure.
If in settings is indicated that the Payment Orders have to be created for the invoiced the amounts, then for the relevant Invoice Amounts (these are amounts of 12.00 BGN, 3.00 BGN and 38.00 BGN from the example above) are going to be created separate Payment Orders.
Otherwise, no Payment Orders are going to be created for those amounts. 
The same is valid and for the non-invoiced amounts (amounts 15.00 BGN, 2.00 BGN and 25.00 BGN from above) with the only difference that the setting of the generation procedure has another name.

The Due Start Date **(Amount.DueStartDate)** and the Due Date **(Amount.DueDate)** are the determined dates for the current instalment (from which the amount has been broken down) according to its method. 
The fields for reference invoice data (**"Invoice Amount", "Referent invoice document type", " Referent invoice number", etc. ...)** are filled in depending on whether the amount of the breakdown has been calculated according to the Sales Order or Invoice Amount.

The Party **(Amount.Party)** in the Payment Order is inherited from the Customer and the Location Party is inherited from the "Ship to Customer" field in the Sales Order.

The instalment number **(Amount.InstallmentNumber)** in the Payment Order is filled in according to the corresponding field in the instalment from which the amount has been broken down. 
If the instalment is "service" (ie no payment plan has been entered in the Sales Order), then the field for the instalment number in the Payment Order remains blank.

The payment account **(Amount.PaymentAccount)** and the payment type **(Amount.PaymentType)** in the Payment Order are inherited from the corresponding instalment from the plan. If they are not filled in in the instalment or the instalment is "service" then they are inherited from the Sales Order header.
Additionally, if the payment type is not filled in both places but the amount is an Invoice Amount and payment type is filled in in the Invoice, then it is inherited from the Invoice.

The document notes **(Amount.DocumentNotes)** in the Payment Order are a combination of the document notes of the Parent document and the notes of the corresponding in the plan.
If both are filled in – then they are concatenated, separated by a space (or a new line). And if only one of them is filled in – it is the only one that is inherited.

