# Additional amounts determination and recording

These amounts are recorded in the **Аdditional Amounts** panel, found in the following documents: 

- Sales orders
- Invoice orders
- Invoices purchase orders
- Purchase invoices
- Transfer orders
- Transactions 

The input/primary data is entered in the **Additional Amounts** panel, where it's used for calculating the amount and determining its impact on the document.

This calculation is executed every time the document is saved and consists of 2 stages:

1. **Amounts determination**

2. **Distribution of the detrmined amounts through the affected documents** <br> The distribution is saved in the document in which it's entered, no matter if the amount affects the current or another document.
  
The amount is determined by entering an exact value, or by indicating that the amount is calculated as a **percent** of the base document amount or other **[additional amounts](index.md)**. 

This data is entered by adding the amount to a document in its **Additional Amounts** panel. Then, it's used to **[calculate](amounts-calculation/index.md)** the real value. 
  
After the amount value is calculated, it's **[distributed](amounts-distribution/index.md)** among the affected documents. 

This is necessary because you often need to determine what part of the additional amount is distributed to a **specific line** - for example, the value of the additional amount VAT for a specific sales order lines.

There may be cases when an additional amount is entered in one document, but it affects others as well. 

**Take the transport of deliveries from outside the country as an example.** 

In this case, the original purchase invoice for the delivery of goods has arrived and is entered in @@name. 

The purchase invoice is released **before** the purchase invoice for the transport arrives. Transport is entered as an **additional amount** so it can be included in the product's costs. 

Transport can't be entered in the original purchase invoice (because the document state is Released and also the transport is not actually part of it and it should not be included there). Instead, transport is entered in another document and it should be distributed into the original purchase invoice, so its amount can be **included** in the invoice's products costs.

As a result, you're able to indicate additional - **[referenced documents](referenced-documents.md)**, to which you have to distribute the current amount. 

No matter if it's distrubuted only in the document it's entered or in other/referenced documents, once an amount is calculated and distributed, to see its real value, which shows how the amount affects business activities from the documents, its distributions should be **summed** from all documents it's distributed in.



