# Additional amounts determination and recording

These amounts are recorded in the **Аdditional Amounts** panel, which can be found in the following documents: 

- Sales orders
- Invoice orders
- Invoices purchase orders
- Purchase invoices
- Transfer orders
- Transactions 

The input/primary data is entered in the **Additional Amounts** panel, where it's used for calculating the amount and determining its impact on the document. This calculation is executed every time the document is saved and consists of 2 stages:

1. Amounts determination.

2. Stage 1 amounts distribution through the affected documents. <br> That distribution is saved in the document in which it's entered, no matter if the amount affects the current document or more.
  
The amount is determined by entering an exact value or by indicating that the amount is calculated as a **percent** of the base document amount or other additional amounts. 

This data is entered by adding the amount to a document in its **Additional Amounts** panel. Then, it's used to **[calculate](https://docs.erp.net/tech/advanced/document-amounts/amounts-calculation/index.html)** the real value. 
  
After the amount value is calculated, it's **[distributed](https://docs.erp.net/tech/advanced/document-amounts/amounts-distribution/index.html)** among the affected documents. 

This is necessary because you often need to determine what part of the additional amount is distributed to a **specific row** - <br> for example, the value of the additional amount VAT for a specific sales order row.

There may be cases when an additional amount is entered in one document, but it affects others as well. 

**Take the thansport of deliveries from outside the country as an example.** 

In this case, the original purchase invoice for the delivery of goods has arrived and is entered in @@name. 

The purchase invoice is released **before** the purchase invoice for the transport arrives. Transport is entered as an **additional amount** so it can be included in the product's costs. 

Transport can't be entered in the original purchase invoice because the document state, of which it **isn't** a part, is 'Released'. <br> Instead, transport is entered in another document and it should be distributed into the original purchase invoice, so its amount can be **included** in the invoice's good costs.

Therefore, you're able to indicate additional - **[referenced documents](https://docs.erp.net/tech/advanced/document-amounts/referenced-documents.html)**, where you distribute the current amount. 

An amount may be entered in a document or referenced in others - once calculated and distributed, you need to see its **real value**. 

It's meant to show how the amount affects the business activities of the documents. 

Thus, amount distribution should be **summed** from all documents it's distributed in.
