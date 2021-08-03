# Sales Order Payment plan

This topic describes the essence of the Sales order Payment plans, the method of calculating the Instalments, and the algorithm for creating payment requests under a plan.


## Sales Order Payment plans


The Sales order payment plan determines how the amount of the given Sales order is paid (with how many instalments and their individual amounts).

For each instalment, there are two main attributes - a *method for determining the amount* and a *method for determining the due dates (the payment term*).

**Methods for determining the amount (specified by the 'Amount Percent', 'Amount' and 'Remainder' fields):**


- an indication of a fixed amount that does not depend on other factors;
- the amount of the instalment is a percentage of the total amount of the transaction;
- the amount is the remainder that is not covered by the other instalments.


It is mandatory that in every plan there must be exactly one instalment marked as a 'Remainder' (usually this is the last instalment in the plan). It is necessary to have such an instalment because it 'picks up' all of the small inaccuracies and differences of rounding (if there are other instalments whose amounts are determined by a percentage). It can also 'pick up' the changes in the total amount happening due to changes in the terms of trade in the Invoices (see Example 3 below).

There are two main fields with values that need to be determined in order to define the payment term - Payment due Start date (aka Execution date) and Payment due date. Payment due Start date (aka Execution date) is the date when the payment becomes due/executable and Payment due date is the last day of the payment term.


**Due date form Methods according to which the payment term is calculated:**


- Specify the date explicitly: the Payment due start date is determined by adding 'Payment term days' to the 'Explicit Payment due date' and the due date is 'Explicit execution date' added with 'Execution term, days';
- Use Sales order due date: 'Due Start date'/'Execution date' and 'Payment due date' are copied directly from the Sales order header fields 'Payment due Start date ' and 'Payment due date';
- Use Sales order date: the dates are calculated using the Sales order 'Document date' added with the number of days entered in 'Execution term, days' (for the calculation of the payment start due date) or 'Payment Term days' (for the calculation of the due date);
- Use Invoice Due date: 'Due Start date'/'Execution date' and 'Payment due date'  are copied directly from the Invoice header fields 'Payment Due Start date ' and 'Payment due date';
- Use Invoice date: the dates are calculated using the Invoice 'Document date' added with the number of days entered in 'Execution term, days' (for the calculation of the payment start due date) or 'Payment term days' (for the calculation of the due date);


The last two methods use the delivery invoice dates. If they are not yet issued, then the dates are calculated according to the values inserted in the Sales order header.


If  there is no indicated payment plan for the particular Sales order at all, then it is considered that there is a plan that consists of only one instalment. This instalment is not numbered (see the Create Payment orders section below) and is for total Amount to pay of the Sales order. In a 'service' instalment the method of determining the payment term depends on whether the Payment orders for the invoiced amounts will be created from the Sales order or not (this depends on the setting of the Payment order generation procedure). If the Payment orders for invoiced amounts will be generated from the Sales order, then for the 'Due date form Method' the 'Use Invoice due date' method is used, otherwise the 'Use Sales order Due date' method  is used.


## Determining the total payment amount


In order to determine the amount of each instalment, it is first necessary to determine what is the total / final amount that has to be paid for this transaction. This is done using the data from several documents - the Sales order with which the transaction is reflected and all Invoices for this sale (both for the advance and for delivery).
For this purpose, two types of Amounts are calculated separately – Sales order amounts and Invoice amounts, which are then summed to obtain the final amount. Invoice amounts are the Amounts to pay (see topic **[Amount To pay](https://github.com/ErpNetDocs/tech/blob/master/modules/crm/sales/sales-concepts/amount-to-pay.md)**) of the delivery Invoices. And the Sales orders amounts are the paid advances and the remaining part of the Amount to pay (see topic **[Amount To pay](https://github.com/ErpNetDocs/tech/blob/master/modules/crm/sales/sales-concepts/amount-to-pay.md)**) of the Sales order, which is not covered by an advance or delivery.
To determine the last amount (the remaining part of the Amount to pay of the Sales order), the following formula is used:

**[remaining part] = [Amount to Pay of the Sales order] - [advances paid] - [invoiced part of the Sales order]**

 The invoiced part is calculated by determining how much of the Amount to pay of the Sales order is covered by the delivery Invoices. This is done for each line of Invoices in two alternative methods:
- through the 'Covered amount' field of the Invoice lines;
- or through the Quantities in the Invoice lines (this is used for the lines in which the 'Covered Amount' is not filled in).

Finally, the results of all lines of Delivery Invoices for current Sales order are summed into **[invoiced part of the Sales order]**. It does not matter what the final Amount to pay for the Invoice is. The reason why the final Amount to pay of the Invoice is not to be considered is that there may be a change in the trading conditions (prices, discounts, etc.). This should not change the ratio - what part of the Sales order is covered by this Invoice.

The first method is based on how much of the basе of the Sales order (the 'Line amount' field of the Sales order line) is covered by the value of the 'Sales order amount' field in the line of the Invoice. This relationship determines what part of the Sales order line has been invoiced. For example, if the Sales order lines is for **100.00 BGN** and we have **20.00 BGN** VAT (ie the Amount to pay of the Sales order is 120.00 BGN) and there is one Invoice line in which the covered 'Sales order amount' is 70.00 BGN, then the invoiced part of the Sales order line is **120.00 * 70.00 / 100.00 = 84.00 BGN**.


The second method works on the same principle, but the relationship is made between the quantities of the Sales order line and the Invoice line. For example, if in the Sales order line there is a Quantity = **10 pcs** with a total Amount to pay = **90.00 BGN** and there is only one Invoice line for Quantity = **7 pcs** then the invoiced part of the Sales order line is **90.00 BGN * 7 pc / 10 pc = 63.00 BGN**.


If in the Invoice there also is an advance deduction, this deduction is also subtracted from the invoiced part (because advances are aggregated in **[advances paid]**). If in the example described above there is an advance deduction of **15.00 BGN** in the Invoice, then the invoiced part of the Sales order is **(90.00 BGN * 7 pcs / 10pcs) – 15.00 BGN = 48.00 BGN**.


**Example 1:**


There is a Sales order with Quantity = **10 pcs** for a total Amount to pay of **90.00 BGN**, there already is a paid advance of **15.00 BGN** and two delivery Invoices (in which the field 'Sales order Amount' is not filled in):
- one for Quantity =  **3 pcs** in which we deduct the advance and therefore we have an Amount to pay of the Invoice **12.00 BGN = (27.00 BGN – 15.00 BGN)**;
- one for Quantity =  **4 pcs**, in which trade conditions are changed and so we have an Amount to pay of the Invoice **41.00 BGN** (instead of the expected **36.00 BGN**).
The result is:

**[invoiced part of Sales order] = (90.00 BGN * 3 pss / 10 pcs) + (90.00 BGN * 4 pcs / 10 pcs) – 15.00 BGN = 48.00 BGN**;

**[remaining part] = 90.00 BGN – 15.00 BGN – 48.00 BGN = 27.00 BGN**;
Thus, we receive two Invoice Amounts – **12.00 BGN** and **41.00 BGN** - and two Sales order amounts – **15.00 BGN** (advance) and **27.00 BGN**. The final payment amount is:

**[total Amount to pay] = 12.00 BGN + 41.00 BGN + 15.00 BGN + 27.00 BGN = 95.00 BGN**

In principle, (and from **Example 1**) we see that the total Amount to pay practically is the Amount to pay of the Sales order summed with the increases/decreases that occurred due to a change in the terms of trade in the Invoices. The reason behind the using of such a breakdown of individual (smaller) amounts in the calculation is to avoid a (technical) complex analysis of how exactly the trade terms of the Invoices have changed and how this changes and affects the total amount. Also, these individual amounts help with the creation of Payment orders.


## Determination of the instalments amounts


The instalments are calculated by computing the total Amount to pay and applying the method of determining the instalment amount. Here are two examples:


**Example 2:**


There is a Sales order with a total Amount to pay **95.00 BGN**. For this Sales order, there is a payment plan with three instalments: the first for **33.30 %**, the second for **33.70 %** and the third is marked as a '**Remainder**'. Thus, we get the following instalments:

- **[Instalment 1] = 95.00 BGN * 33.30 % = 31.635 ~ 31.64 BGN**;
- **[Instalment 2] = 95.00 BGN * 33.70 % = 32.015 ~ 32.02 BGN;**
- **[Instalment 3] = 95.00 BGN - 31.64 BGN - 32.02 BGN = 31.34 BGN**;

**Example 2** shows that when using a percent-based instalment and we have a change (increase/decrease) in the Amount to pay because of changing the terms of trade in the invoices, this change is evenly distributed among the instalments.
It also illustrates the usefulness of the 'Remainder' instalment. If it was, instead, 33.00 %, then the total amount of the three instalments (after determining the percentages after the rounding) would be **95.05 BGN** and not **95.00 BGN!**


**Example 3:**


There is a Sales order with a total Amount to pay **95.00 BGN**. For this Sales order, there is a payment plan with three instalments: the first for an exact amount of **30.00 BGN**, the second for an exact amount of **40.00 BGN** and the third is marked as a 'remainder'. Thus, we get the following instalments:

- **[Instalment 1] = 30.00 BGN** (fixed amounts do not change);
- **[Instalment 2] = 40.00 BGN** (fixed amounts do not change);
- **[Instalment 3] = 95.00 BGN – 30.00 BGN – 40.00 BGN= 25.00 BGN**;


This example illustrates the other benefits of the 'Remainder' instalment. When there are only fixed amounts in the previous instalments and there is change of the trade terms in the Invoices, then this change is reflected in the last instalment.


## Create Payment orders


When we create Payment orders by a Sales order Payment plan, first we have to determine the Amount (as described above) and the Due dates for any of the plan instalments. Thereafter,  individual Sales order and Invoices Amounts (those from which the total amount is formed) are determined. We make an additional breakdown of the instalments and the instalments are exhausted in the order of creation of the individual amounts.


**Example 4:**


Let's use the situation of Example 1 and the payment plan of **Example 3**. We get the following breakdown:
- **15.00 BGN** - from **[instalment 1]** and because of the advance amount of the Sales order;
- **12.00 BGN** - from **[instalment 1]** and because of the amount of the first Invoice;
- **3.00 BGN** - from **[instalment 1]** and because of the amount of the second Invoice;
- **38.00 BGN** - from **[instalment 2]** and because of the amount of the second Invoice;
- **2.00 BGN** - from **[instalment 2]** and because of the remaining part amount of the Sales order;
- **25.00 BGN** - from **[instalment 3]** and because of the remaining part amount of the Sales order.


More examples of Payment orders generated by Sales order Payment plans there are in topic [Transitional Documents](https://github.com/ErpNetDocs/tech/blob/4271ce55e062e4994ff7ccfa4ee8ab2ff350ced9/advanced/documents/transitional-documents.md).


> NOTE: In the usual case, the Sales and Invoice amounts will match the Instalments amounts, in fact, the resulting breakdown will match the payment plan (none of the instalments will be 'broken down').

Then, for each **Amount** the resulting breakdown can create a separate Payment order. Whether it will be created or not depends on the settings of the generation procedure. If in the **Settings** it is indicated that the Payment orders have to be created for the invoiced amounts, then for the relevant Invoice amounts (these are amounts of 12.00 BGN, 3.00 BGN and 38.00 BGN from the example above)  separate Payment orders will be created. Otherwise, no Payment orders are going to be created for those amounts. The same is valid for the non-invoiced amounts (amounts 15.00 BGN, 2.00 BGN and 25.00 BGN from above) with the only difference that the setting of the generation procedure has another name.

The Due start date (**Amount.DueStartdate**) and the Due date (**Amount.Duedate**)are the determined dates for the current instalment (from which the amount has been broken down) according to its method. The fields for reference invoice data (**'Invoice amount', 'Referent invoice document type', ' Referent invoice number', etc. ...**) are filled in depending on whether the amount of the breakdown has been calculated according to the Sales order or Invoice amount.

The Party (**Amount.Party**) in the Payment order is inherited from the Customer and the Location party is inherited from the 'Ship to customer' field in the Sales order.

The instalment number (**Amount.InstallmentNumber**) in the Payment order is filled in according to the corresponding field in the instalment from which the amount has been broken down. If the instalment is 'service' (i.e. no payment plan has been entered in the Sales order), then the field for the instalment number in the Payment order remains blank.

The payment account (**Amount.PaymentAccount**) and the payment type (**Amount.PaymentType**) in the Payment order are inherited from the corresponding instalment from the plan. If they are not filled in in the instalment or the instalment is 'service' then they are inherited from the Sales order header. Additionally, if the payment type is not filled in both places but the amount is an Invoice amount and payment type is filled in in the Invoice, then it is inherited from the Invoice.

The document notes (**Amount.DocumentNotes**) in the Payment order are a combination of the document notes of the Parent document and the notes of the corresponding in the plan. If both are filled in – then they are concatenated, separated by a space (or a new line). And if only one of them is filled in – it is the only one that is inherited.
