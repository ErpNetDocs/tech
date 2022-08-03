# Lines weighting

Amounts from document lines often play a major role in the **[additional amounts](../document-amounts/index.md)** calculation. Either the value of the additional amount is defined by the line amounts (VAT or customs), or the distribution of the additional amount through the lines depends on their lines amounts. 

However, there are cases when **not all** lines participate equally in the distribution.

For example, it's possible for some products in an invoice to be **exempt** from income tax (VAT). This leads to some document lines unable to participate in the VAT calculation. The calculated amount will be distributed only among the ones that **have** participated. 

Similarly, for the 'Customs' additional amount in purchase invoices, a customs fee is due for particular products.

There's a mechanism that allows for the indication of particular lines as being more important than others. You can set weights, coefficients, or in some cases percentages for each document line. The feature is found in the **Document: Input line percentages** panel, also known as **amounts distribution by lines**. 

Here, the coefficient of the specific row is entered in the *Line Percent* field. These specific parameters may only be entered for additional amounts marked as **[distributed](amounts-distribution/index.md)** by product definition.

In this panel, weights are entered in two ways:

- **manually**, when the document is created
- **automaticall** using pre-entered **default values** in the product'с definition

> [!NOTE] 
> 
> If there are no weights for an additional amount in the panel, all weights are considered equal to **100%**.

Below you'll find brief descriptions and examples for different input methods. <br> For more information, see **[Amounts calculation](amounts-calculation/index.md)** and **[Amounts distribution](amounts-distribution/index.md)**.

## Default weights/coefficients in product definitions

Sometimes, weights of specific services are known **before** documents are created. 

When customs taxes are paid for goods on import, some of the products have taxes and others don't. For many, taxes are defined by law and they're a constant percentage of the product value. You have to enter their weight for the additional amount 'Customs'. 

Once the documents are entered in @@name and a product is selected in a document line, its weight is copied from the product definition into the **Document: Input line percentages** panel. Of course, these are just default values that can be changed if necessary.

**Example 1:**

There's an additional amount 'Customs' with the following properties:

- Distributed By: **Product definition**;
- Default Percent: **100%**.

You enter a purchase invoice with four lines: 

- line #10 for **44 EUR**;
- line #20 for **56 EUR**;
- line #30 for **24 EUR**; 
- line #40 for **71 EUR**. 

In line #10, there's a product with default weight for additional amount ‘Customs’ of **5%** <br> and in line #30, there's a product with default weight of **25%**. 

These are the coefficients/weights for each row:

- row #10: weight = **0.05**;
- row #20: weight = **0.00**;
- row #30: weight = **0.25**;
- row #40: weight = **0.00**;

The 'Customs' amount is **8.20 EUR** and it's distributed as **2.20 EUR : 0 EUR : 6 EUR : 0 EUR** 

## Manual weights/coefficients in the document

In certain cases, products weights for specific additional amounts are **not** known in advance. They may depend on a document parameter and rely on the deal type of the sales order. 

Regardless of whether VAT is applicable or not and whether the document lines have different deal types, you will have to enter the weights/coefficients in the specific document, along with deal type. 

Products don't have default weights/coefficients in their definitions in advance.

**Example 2:**

There's an additional amount 'Specific VAT', distributed by product definition with a default percentage of **20%**. 

You enter a sales order with four lines:

- line #10 for **44 EUR**;
- line #20 for **56 EUR**; 
- line #30 for **24 EUR**;
- line #40 for **71 EUR**. 

Rows #10 and #20 are exempt from VAT, while the others have 20% VAT. 

You manually set the following percentages (**100%** on lines #30 and #40):

- line #10: weight = **0.00**;
- line #20: weight = **0.00**;
- line #30: weight = **1.00**;
- line #40: weight = **1.00**.

The Specific VAT is **19 EUR** and it's distributed through the rows as **0 EUR : 0 EUR : 4.80 EUR : 14.20 EUR**.

**Example 3:**

This is a case where data is absent from the **Document: Input line percentages** panel:

There's an additional amount VAT, distributed by **amount** with a default percentage of **20%**. The amount is not distributed by the product definitions, therefore there will be no data in the **Document: Input line percentages** panel.

In this case, no weights/coefficients are used for calculating and distributing the VAT amounr, so it is considered that all document lines have **100%** VAT.
