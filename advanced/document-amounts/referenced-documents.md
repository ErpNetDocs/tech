# Referenced documents

There are cases when you enter an **[additional amount](index.md)** in a document and calculate it, distributing it not only to the lines of the current document, but to others as well. 

For example, if there's a purchase invoice for goods transported to your location, and this transport must be paid, then it can be delivered later than the original purchase invoice. That original invoice may already be 'Released and possibly 'Completed'. 

As a result, you'll have to enter the transport as an additional amount in a **separate** document.

Even if the purchase invoice isn't late, it could still be necessary to enter the transport in a separate document. This might help when the transport is performed by a different company from the supplier of the goods. 

Therefore, the additional amount 'transport' in one purchase invoice will be distributed to the lines of other 'Released' or 'Completed' documents, so its value can be added to the goods cost in **[Logistics module](~/modules/logistics/index.md)**.

The additional amount is calculated and distributed by documents different from the ones in which you enter it. 

This is performed using the **Document Amount Referenced Documents** panel, where can be specified referenced documents for each additional amount of the current document. These documents are usually from the same system type as the current one (invoices, sales orders), or at least support additional amounts. 

If it's entered in the listed documents, the amount is calculated and distributed by these exact documents (as if the amount was originally entered in the listed documents).  

The documents which will be used in the calculations are determnined as follows:

- If there's no information for the additional amount in the **Document Amount Referenced Documents** panel, the amount is distributed only in the current document and no other documents;

- If there are listed documents in the **Document Amount Referenced Documents** panel - the amount is distributed in the listed documents and no other documents.

This makes it possible to enter additional amounts in the document which is distributed only in other documents.

> [!NOTE] 
> 
> Respectively, if you want the same amount to be distrbuten in both the current document and other documents, this requires listing the current document as 'Referenced' as well. 

For more information, see **[Amounts calculation](amounts-calculation/index.md)** and **[Amounts distribution](amounts-distribution/index.md)**.

Let's see the standard case for referenced document usage: transport of purchased goods. 

**Example 1:**

Purchase invoice #1 has three lines: 

- #10 with amount of **50 EUR**; <br>
- #20 with amount of **80 EUR**; <br>
- #30 with amount of **140 EUR**; <br>

Second purchase invoice #2 is entered with no lines - only an additional amount with _Input Amount_ of **38 EUR**. 

Then, purchase invoice #1 is entered as a referenced document for the additional amount in the **Document Amount Referenced Documents** panel of purchase invoice #2, without adding a record for #2 itself .

The amount is distributed among the lines from #1, and distribution is entered in purchase invoice #1. This is the resulting distribution, assuming transport is distributed by amount and is rounded up to the second digit:

- line #10, purchase invoice #1: **7.04 EUR**; <br>
- line #20, purchase invoice #1: **11.26 EUR**; <br>
- line #30, purchase invoice #1: **19.70 EUR**; <br>

**Example 2:**

There's sales order #1 from the end of last year. It has two lines: 

- line #10 with amount of **100 EUR**; <br> 
- line#20 with amount of **80 EUR**; <br> 

You have missed to enter holidays discounts: additional amount 'Christmas discount’

Default Percent: **-3%** <br> Base On Lines: **True** <br>  Distributed By: **Amount** <br>  Round Scale: **2** 

You don't edit the sales order since it comes from the previous fiscal year. 

During the Easter holidays, a sales order for the same customer is added separately.

You enter the discount missed from the first sales order: ‘Christmas discount’ in sales order #2 is distributed only in sales order #1. This is indicated in the **Document Amount Referenced Documents** panel. 

In sales order #2, you enter a new discount for the Easter holidays:

Default Percent: **-2%** <br> Base On Lines: **True** <br>  Distributed By: **Amount** <br> Round Scale: **2** 

This additional amount is applied only to the current document and it's NOT entered in **Document Amount Referenced Documents**. 

Sales order #2 gets a special bonus, which decreases **10%** of the amounts from sales order #1 and #2. 

This becomes an additional amount ‘Reorder bonus’ and has the following properties: 

Default Percent: **-10%** <br>
Base On Lines: **True** (the amount is also based on ‘Christmas discount’ and ‘Easter discount’) <br> 
Distributed By: **Amount**, Round Scale: **2**

For the last additional amount in **Document Amount Referenced Documents**, both orders are listed.

If the lines in sales order #2 are: 

- line #10 with amount of **35 EUR**; <br>
- line #20 with amount of **75 EUR**; <br> 
- line #30 with amount **40 EUR**; <br> 

the three additional amounts in sales order #2 are calculated and distributed as follows:

- The amount of [Christmas discount] is **-5.40 EUR** and it is distributed as follows: <br>

    - line #10, Sales Order #1: **-3 EUR**;<br>
    - line #20, Sales Order #1: **-2.40 EUR**.<br><br>

- The amount of [Easter discount] is **-3 EUR** and it is distributed as follows:

    - line #10, Sales Order #2: **-0.70 EUR**;
    - line #20, Sales Order #2: **-1.50 EUR**;
    - line #30, Sales Order #2: **-0.80 EUR**.<br><br>

- The amount of [Reorder bonus] is **-32.16 EUR** and it is distributed as follows:

    - line #10, Sales Order #1: **-9.70 EUR**;
    - line #20, Sales Order #1: **-7.76 EUR**;
    - line #10, Sales Order #2: **-3.43 EUR**;
    - line #20, Sales Order #2: **-7.35 EUR**;
    - line #30, Sales Order #2: **-3.92 EUR**.
