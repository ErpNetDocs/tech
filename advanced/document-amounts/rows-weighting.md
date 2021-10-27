# Rows weighting

In many cases, the line amounts from the document rows play a major role in the [additional amounts](https://docs.erp.net/tech/advanced/documents/additional-amounts.html) calculation. Either the value of the amount is defined by the row amounts (VAT or customs), or the distribution of the amount through the row depends on the line amounts. However, there are cases when **not all rows participate equally in the distribution**.

For example, it is possible for some products in an invoice to be **exempt** from income tax (VAT). This leads to not all document rows participating in the VAT calculation. The calculated amount will be distributed only among the ones that **have** participated. Similar is the case with the 'Customs additional amount’ in purchase invoices, where a customs fee is due for particular products.

There is a mechanism allowing the indication of some rows as more important than others - users can set weights, coefficients, or in some cases percentages for each document row. It is available in the *Document Line Amounts* panel, also known as *Amounts Distribution By Rows'. Here, the coefficient of the specific row is entered in the *Line Percent* field. These specific parameters may only be entered for additional amounts marked as distributed by product definition (see [**Amounts Distribution**](https://docs.erp.net/tech/advanced/document-amounts/amounts-distribution/index.html).

In this panel, weights are entered in two ways:

- manually, when the document is created
- setting them as default values in the product definition

> [!NOTE] 
> If there are no weights for additional amount in the panel, then it is considered that all weights are equal to **100%**.

Below, brief descriptions and examples for the different input methods are explained. For more information on the role of weights/coefficients in the calculation and distribution, see [Amounts Calculation](https://docs.erp.net/tech/advanced/document-amounts/amounts-calculation/index.html) and [Amounts Distribution](https://docs.erp.net/tech/advanced/document-amounts/amounts-distribution/index.html).

## Weights & coefficients in the product definitions

Sometimes, weights of specific services are known before documents are created. 

For example, when customs taxes are paid for goods on import, some of the products have taxes and others do not. For many, taxes are defined by law and they are a constant percent of the product value. Users have to enter their weight for the additional amount 'Customs'. Then, once the documents are entered in @@name, when a product is selected in a document row, its weight is copied from the product definition into the *Document Line Amount* panel. Users can change the default weights of the products.

#### Example 1:

There is an additional amount ‘Customs’ with the following properties:

- Distributed by: **Product Definition**;
- Default percent: **100%**.

A user enters a purchase invoice with four rows: #10 with amount of **44 EUR**, #20 with amount of **56 EUR**, #30 with amount of **24 EUR** and #40 with amount of **71 EUR**. In row #10, there is a product with default weight for additional amount ‘Customs’ of **5%** and in row #30, there is a product with default weight of **25%**. 

These are the coefficients/weights for each row:

- row #10: weight = **0.05**;
- row #20: weight = **0.00**;
- row #30: weight = **0.25**;
- row #40: weight = **0.00**;

The 'Customs' amount is **8.20 EUR** and it is distributed through the rows as **2.20 EUR : 0 EUR : 6 EUR : 0 EUR** 

Check out [Amounts Calculation](https://docs.erp.net/tech/advanced/document-amounts/amounts-calculation/index.html) and [Amounts Distribution](https://docs.erp.net/tech/advanced/document-amounts/amounts-distribution/index.html) for more information.

## Weights & coefficients in the document

In certain cases, weights of the products for specific additional amounts are not known in advance. 

For example, they may depend on a document parameter and rely on the deal type of the sales order. Regardless of whether VAT is applicable or not and whether the document row has different deal types, users will have to enter the weights/coefficients in the specific document along with deal type. Products do not have percentages in their definitions in advance.

####Example 2:

There is an additional amount ‘Specific VAT’, which is distributed by product definition and has a default percentage of **20%**. 

A user enters a sales order with four rows = #10 with amount of **44 EUR**, #20 with amount of **56 EUR**, #30 with amount of **24 EUR** and #40 with amount of **71 EUR**. Rows #10 and #20 are exempt from VAT, while the others have 20% VAT. 

The user manually sets the following percentages (**100%** on rows #30 and #40):

- row #10: weight = **0.00**;
- row #20: weight = **0.00**;
- row #30: weight = **1.00**;
- row #40: weight = **1.00**.

The Specific VAT is **19 EUR** [Amounts Calculation](https://docs.erp.net/tech/advanced/document-amounts/amounts-calculation/index.html) and it is distributed through the rows as **0 EUR : 0 EUR : 4.80 EUR : 14.20 EUR**.

####Example 3:

The following example describes a case where data is absent from the *Document Line Amount* panel:

There is an additional amount VAT with a default percentage of **20%**. Since it is not distributed by the product definitions in the *Document Line Amount* panel, there is no data. In this case, no weights/coefficients are used for calculating and distributing the VAT amount. It is considered that all document rows have **100%** VAT so we can have easier calculation formulas.
