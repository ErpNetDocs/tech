
# Referenced Documents

There are cases when we enter an additional amount in a document and calculate, distributing it not only to the rows in the current document, but in others as well. For example, if there is a Purchase Invoice for goods transported to our location and this transport has to be paid. Then it is possible for the Purchase Invoice that the transport will be delivered later than the original Purchase Invoice (which is already Released and possibly Completed) and we have to enter the transport (as additional amount) in a separate document. Even if the Purchase Invoice for the transport is not late, it can also be necessary to enter it in a separate document - for example, if the transport is performed by another company , not the one of the goods supplier. So, there is an additional amount ‘Transport’ in one Purchase Invoice and it will be distributed to the rows of other documents (already Released or Completed), so its value can be added to the goods cost in the Logistics module.

For such cases the user is able to record that an additional amount is calculated through and distributed by documents, different from the one in which we enter it. This is performed in the ‘Document Amount Referenced Documents’ panel where for each additional amount from the current document  0 or more documents can be entered. These documents are usually from the same system type as the current one (i.e. in Invoices we enter Invoices as referenced documents, in Sales Orders - Sales Orders and etc.) or at least these documents support additional amounts. The meaning of this information is that we indicate that this amount is calculated and distributed by these exact documents (i.e. if the amount was originally entered in the listed documents). Thus, for every additional amount it may be defined for which documents it is related:

- if in ’Document Amount Referenced Documents’ panel there is no information for the additional amount - the amount is distributed only in the current document and no other documents;

- if in ’Document Amount Referenced Documents’ panel there are listed documents - the amount is distributed in the listed documents and no other documents.

This makes it possible for the user to enter additional amount in the current document, which is not distributed in the current document, and is distributed only in other documents (i.e. in ’Document Amount Referenced Documents" panel other documents are listed, but not the current one).

> Respectively, this requires listing the current document as a referenced one if such distribution is necessary. 

*Example 1*  describes the standard case for referenced documents usage - transport for purchased goods. For more information about the calculation and distribution formulas see **[Amounts Calculation](https://github.com/ErpNetDocs/tech/blob/master/advanced/documents/additional-amounts/amounts-calculation/index.md)** and **[Amounts Distribution](https://github.com/ErpNetDocs/tech/blob/master/advanced/documents/additional-amounts/amounts-distribution/index.md)**.


*Example 1:*

There is Purchase Invoice #1. It has three rows - row #10 with amount of **50 EUR**, row #20 with amount of **80 EUR** and row #30 with amount of **140 EUR**. Second Purchase Invoice #2 is entered with no rows - only additional amount with Input Amount of **38 EUR**. The Purchase Invoice #2, in ’Document Amount Referenced Documents’ panel the user enters Purchase Invoice #1 (Purchase Invoice #2 is not listed here!). In this case the amount is distributed on the three rows from Purchase Invoice #1, but the distribution is only entered in Purchase Invoice #1. This is the resulting distribution (assume that the transport is distributed by amount and is rounded up to the second digit):

- row #10, Purchase Invoice #1: **7.04 EUR**;

- row #20, Purchase Invoice #1: **11.26 EUR**;

- row #30, Purchase Invoice #1: **19.70 EUR**;

*Example 2:*

There is Sales Order at the end of the previous year (Sales order #1). It has two rows - row #10 with amount of **100 EUR** and row #20 with amount of **80 EUR**. In this Sales Order the user has missed to enter holidays discounts - additional amount ‘Christmas Discount’ ; (Default Percent: **-3%**; Base On Lines: **True**; Distributed By: **Amount**; Round Scale: **2**). It is not appropriate to edit this Sales Order as it was in the previous fiscal year. So now - in the Easter Holidays - a Sales Order for the same customer is entered separately. The user enters the missed from the first Sales Order discount in it (i.e. ‘Christmas Discount’ in Sales Order #2 is distributed only in Sales Order #1 - this is indicated in ’Document Amount Referenced Documents’ panel). Also in Sales Order #2 the user enters a new discount for the Easter Holidays (Default Percent: **-2%**; Base On Lines: **True**; Distributed By: **Amount**; Round Scale: **2**). This additional amount is applied only on the current document and it is not entered in the ’Document Amount Referenced Documents’ panel. Also in Sales Order #2 a special bonus for the customer is agreed, which decrease **10%** of the amounts of both Sales Order #1 and #2. This is also an additional amount ‘Reorder Bonus’ and has the following properties - Default Percent: **-10%**, Base On Lines: **True**, the amount is based on ‘Christmas Discount’ and ‘Easter Discount’ also, Distributed By: **Amount**, Round Scale: **2**. So for the last additional amount in ’Document Amount Referenced Documents’ panel both Sales Orders are listed.

If the rows in Sales Order #2 are: row #10 with amount of **35 EUR**, row #20 with amount of **75 EUR** and row #30 with amount **40 EUR**, so the three additional amounts in Sales Order #2 are calculated and distributed as follows (the distributions are only entered in Sales Order #2):

- the amount of [Christmas Discount] is **-5.40 EUR** and it is distributed as follows:<br>
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
