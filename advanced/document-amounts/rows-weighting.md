# Rows weighting

Line amounts from document rows often play a major role in the **[additional amounts](https://docs.erp.net/tech/advanced/document-amounts/index.html)** calculation. Either the value of the amount is defined by the row amounts (VAT or customs), or the distribution of the amount through the row depends on the line amounts. 

However, there are cases when **not all** rows participate equally in the distribution.

For example, it's possible for some products in an invoice to be **exempt** from income tax (VAT). This leads to some document rows unable to participate in the VAT calculation. The calculated amount will be distributed only among the ones that **have** participated. 

Similarly, for the 'Customs' additional amount in purchase invoices, a customs fee is due for particular products.

There's a mechanism that allows for the indication of particular rows as being more important than others. You can set weights, coefficients, or in some cases percentages for each document row. 

The feature is found in the **Document Line Amounts** panel, also known as **Amounts Distribution By Rows**. 

Here, the coefficient of the specific row is entered in the *Line Percent* field. These specific parameters may only be entered for additional amounts marked as **[distributed](https://docs.erp.net/tech/advanced/document-amounts/amounts-distribution/index.html)** by product definition.

In this panel, weights are entered in two ways:

- manually, when the document is created
- setting them as default values in the product definition

> [!NOTE] 
> 
> If there are no weights for an additional amount in the panel, it's considered that all weights are equal to **100%**.

Below, brief descriptions and examples for the different input methods are given. For more information on the role of weights/coefficients in the calculation and distribution processes, see **[Amounts calculation](https://docs.erp.net/tech/advanced/document-amounts/amounts-calculation/index.html)** and **[Amounts distribution](https://docs.erp.net/tech/advanced/document-amounts/amounts-distribution/index.html)**.

## Weights & coefficients in product definitions

Sometimes, weights of specific services are known **before** documents are created. 

When customs taxes are paid for goods on import, some of the products have taxes and others don't. For many, taxes are defined by law and they're a constant percentage of the product value. You have to enter their weight for the additional amount 'Customs'. 

Then, once the documents are entered in @@name, and a product is selected in a document row, its weight is copied from the product definition into the **Document Line Amount** panel. You can change the default weights of the products.

**Example 1:**

There's an additional amount 'Customs' with the following properties:

- Distributed By: **Product Definition**;
- Default Percent: **100%**.

You enter a purchase invoice with four rows: 

#10 with amount of **44 EUR**, #20 with amount of **56 EUR**, #30 with amount of **24 EUR** and #40 with amount of **71 EUR**. 

In row #10, there's a product with default weight for additional amount ‘Customs’ of **5%** <br> and in row #30, there's a product with default weight of **25%**. 

These are the coefficients/weights for each row:

- row #10: weight = **0.05**;
- row #20: weight = **0.00**;
- row #30: weight = **0.25**;
- row #40: weight = **0.00**;

The 'Customs' amount is **8.20 EUR** and it's distributed through the rows as **2.20 EUR : 0 EUR : 6 EUR : 0 EUR** 

## Weights & coefficients in the document

In certain cases, products weights for specific additional amounts are **not** known in advance. They may depend on a document parameter and rely on the deal type of the sales order. 

Regardless of whether VAT is applicable or not and whether the document row has different deal types, you will have to enter the weights/coefficients in the specific document, along with deal type. 

Products don't have percentages in their definitions in advance.

**Example 2:**

There's an additional amount 'Specific VAT', distributed by product definition and having a default percentage of **20%**. 

You enter a sales order with four rows:

#10 with amount of **44 EUR**, #20 with amount of **56 EUR**, #30 with amount of **24 EUR** and #40 with amount of **71 EUR**. 

Rows #10 and #20 are exempt from VAT, while the others have 20% VAT. 

You manually set the following percentages (**100%** on rows #30 and #40):

- row #10: weight = **0.00**;
- row #20: weight = **0.00**;
- row #30: weight = **1.00**;
- row #40: weight = **1.00**.

The Specific VAT is **19 EUR** and it's distributed through the rows as **0 EUR : 0 EUR : 4.80 EUR : 14.20 EUR**.

**Example 3:**

The following example describes a case where data is absent from the **Document Line Amount** panel:

There's an additional amount VAT with a default percentage of **20%**. It doesn't reveal any data.

In this case, no weights/coefficients are used for calculating and distributing the VAT amount. <br> It's considered that all document rows have **100%** VAT, so you can take advantage of easier calculation formulas.
