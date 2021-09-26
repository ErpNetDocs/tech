# Additional Amounts Determination And Recording

These amounts are recorded in the ‘Additional Amounts’ panel, which can be found in the following documents: 

- Sales Orders
- Invoice Orders
- Invoices Purchase Orders
- Purchase Invoices
- Transfer Orders
- Transactions 

The input/primary data is entered in the _‘Additional Amounts’_ panel, where it is used for calculating the amount and determining its impact on the document. This calculation is executed every time the document is saved and consists of 2 stages:

1. Amounts determination.

2. Stage 1 amounts distribution through the affected documents. That distribution is saved in the document in which it is entered, no matter if the amount affects only the current document or more.
  
The amount is determined by entering an exact value or by indicating that the amount is calculated as a percent of the base document amount or other additional amounts. This data is entered by adding the amount to a document in its _‘Additional Amounts’_ panel. Then, it is used to calculate the real value. 

For further information see **[Amounts Calculation](https://github.com/ErpNetDocs/tech/blob/master/advanced/documents/additional-amounts/amounts-calculation/index.md)**.
  
After the amount value is calculated, it is not saved in the document. First, it is distributed through the affected documents. This is necessary because we often need to determine what part of the additional amount is distributed to a specific row (for example, the value of the additional amount VAT for a specific Sales Order row).

The algorithm is explained in details in **[Amounts Distribution](https://github.com/ErpNetDocs/tech/blob/master/advanced/documents/additional-amounts/amounts-distribution/index.md)**.

There may be cases when an additional amount is entered in one document, but it affects others as well. 

Take the thansport of deliveries from outside the country as an example. In this case, the original Purchase Invoice for the delivery of goods has arrived and it is entered in @@name . The Purchase Invoice is released before the Purchase Invoice for the transport arrives. The transport is entered as an **additional amount** so it can be included in the product's costs. As it cannot be entered in the original Purchase Invoice (because the document state is Released and the transport is not actually part of it), the transport is entered in another document and it should be distributed into the original Purchase Invoice (so its amount is included in the original Purchase Invoice goods costs). Therefore, we are able to indicate additional - referenced documents, where we distribute the current amount. 

This mechanism is described in **[Referenced Documents](https://github.com/ErpNetDocs/tech/blob/836ab6ef73ea2f82dc153d67a5032e35e69b7f44/advanced/documents/additional-amounts/amounts-distribution/referenced-documents.md)**.

No matter if an amount is entered in a document or referenced in others, once it is calculated and distributed, we will need to see its **real value**. It is meant to show how the amount affects the business activities of the documents. Thus, the amount distributions should be summed from all documents it is distributed in.
