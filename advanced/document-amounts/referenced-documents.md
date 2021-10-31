# Referenced documents

There are cases when we enter an additional amount in a document and calculate it, distributing it not only to the rows of the current document, but in others as well. 

For example, if there is a purchase invoice for goods transported to our location and this transport has to be paid, then it can be delivered later than the original purchase invoice (which is already Released and possibly Completed) and we have to enter the transport (as additional amount) in a separate document.
Even if the purchase invoice is not late, it can also be necessary to enter it in a separate document - for example, if the transport is performed by a company, different from the one of the goods supplier. 

So, there is an additional amount transport in one purchase invoice and it will be distributed to the rows of other documents (already Released or Completed), so its value can be added to the goods cost in [Logistics](https://docs.erp.net/tech/modules/logistics/index.html).

For such cases, the additional amount is calculated through and distributed by documents different from the ones in which we enter it. This is performed in the *Document Amount Referenced Documents* panel where for each additional amount of the current document 0 or more documents can be entered.
These documents are usually from the same system type as the current one (i.e. in invoices, we enter invoices, in sales orders - sales orders) or at least support additional amounts. The amount is calculated and distributed by these exact documents (if it was originally entered in the listed documents). 

Thus, for every additional amount, it can be defined to which documents it is related:

- if there is no information for the additional amount in the *Document Amount Referenced Documents* panel - the amount is distributed only in the current document and no other documents;
- if there are listed documents in the *Document Amount Referenced Documents* panel - the amount is distributed in the listed documents and no other documents.

This makes it possible to enter additional amounts in the current document, which is distributed only in other documents.

> [!NOTE] 
> Respectively, this requires listing the current document as 'Referenced' if such distribution is necessary. 

*Example 1*  describes the standard case for referenced document usage - transport for purchased goods. 

For more information about the calculation and distribution formulas, see [Amounts calculation](https://docs.erp.net/tech/advanced/document-amounts/amounts-calculation/index.html) and [Amounts distribution](https://docs.erp.net/tech/advanced/document-amounts/amounts-distribution/index.html).


***Example 1:***

Purchase invoice #1 has three rows: #10 with amount of **50 EUR**, #20 with amount of **80 EUR** and #30 with amount of **140 EUR**. 

Second purchase invoice #2 is entered with no rows - only additional amount with Input Amount of **38 EUR**. 

The user enters purchase invoice #1 in the *Document Amount Referenced Documents* panel purchase invoice #2 is not listed there). 
The amount is distributed among the three rows from #1, but the distribution is only entered in purchase invoice #1. 

This is the resulting distribution, assuming that the transport is distributed by amount and is rounded up to the second digit:

- row #10, purchase invoice #1: **7.04 EUR**;
- row #20, purchase invoice #1: **11.26 EUR**;
- row #30, purchase invoice #1: **19.70 EUR**;

***Example 2:***

There is sales order #1 at the end of last year. It has two rows: #10 with amount of **100 EUR** and #20 with amount of **80 EUR**. 

In this sales order,  the user has missed to enter holidays discounts - additional amount 'Christmas discount’ ; (Default Percent: **-3%**; Base On Lines: **True**; Distributed By: **Amount**; Round Scale: **2**). 

It is not appropriate to edit the sales order since it comes from the previous fiscal year. 
Now, in the Easter Holidays, a sales order for the same customer is entered separately.
The user enters the discount missed from the first sales order (‘Christmas Discount’ in sales order #2 is distributed only in sales order #1 - this is indicated in the *Document Amount Referenced Documents* panel). 

In sales order #2, the user enters a new discount for the Easter Holidays (Default Percent: **-2%**; Base On Lines: **True**; Distributed By: **Amount**; Round Scale: **2**). This additional amount is applied only to the current document and it is not entered in the *Document Amount Referenced Documents* panel. 

Also in sales order #2, a special bonus for the customer is agreed, which decreases **10%** of the amounts from both sales order #1 and #2. This becomes an additional amount ‘Reorder Bonus’ and has the following properties - Default Percent: **-10%**, Base On Lines: **True**, the amount is based on ‘Christmas Discount’ and ‘Easter Discount’ also, Distributed By: **Amount**, Round Scale: **2**. 

So for the last additional amount from the *Document Amount Referenced Documents* panel, both sales orders are listed.

If the rows in sales order #2 are: row #10 with amount of **35 EUR**, row #20 with amount of **75 EUR** and row #30 with amount **40 EUR**, the three additional amounts in sales order #2 are calculated and distributed (the distributions are only entered in sales order #2):

- the amount of [Christmas Discount] is **-5.40 EUR** and it is distributed as follows:

    - row #10, Sales Order #1: **-3 EUR**;<br>
    - row #20, Sales Order #1: **-2.40 EUR**.

- the amount of [Easter Discount] is **-3 EUR** and it is distributed as follows:

    - row #10, Sales Order #2: **-0.70 EUR**;
    - row #20, Sales Order #2: **-1.50 EUR**;
    - row #30, Sales Order #2: **-0.80 EUR**.

- the amount of [Reorder Bonus] is **-32.16 EUR** and it is distributed as follows:

    - row #10, Sales Order #1: **-9.70 EUR**;
    - row #20, Sales Order #1: **-7.76 EUR**;
    - row #10, Sales Order #2: **-3.43 EUR**;
    - row #20, Sales Order #2: **-7.35 EUR**;
    - row #30, Sales Order #2: **-3.92 EUR**.
