
# Rows Weighting

In many cases the line amounts from the document rows play major role in the additional amounts calculation. Either the value of the amount is defined by the row amounts (for example VAT or customs), or the distribution of the amount through the row depends on the line amounts. But there are cases when not all rows participate equally in the distribution.

For example, it is possible for some of the products in an Invoice to be exempt from income tax (VAT). I.e. not all document rows will participate in the VAT calculation and afterwards the calculated amount has to be distributed only on the rows having participated in the calculation. Similar case is the ‘Customs additional amount’ in Purchase Invoices - Customs fee is due for particular products.

So there is a mechanism which allows the user to indicate that some rows are more important than others - i.e. the user sets weights/coefficients (percentages in some cases) for each document row. This is available in the documents (where the user enters the additional amount) in the 'Document Line Amounts' panel (also known as 'Amounts distribution by rows'). In this panel the coefficient of the specific row is entered in the 'Line Percent' field. These specific percentages/coefficients may be entered only for additional amounts marked as distributed by product definition (see [**Amounts Distribution**](https://github.com/ErpNetDocs/tech/blob/master/advanced/documents/additional-amounts/amounts-distribution/index.md)).

In this panel the weights are entered in two ways - manually when the document is created or the weights can be set as default values in the product definition.

> If there are no weights for additional amount in the panel then it is considered that all weights are equal to **100%**.

Below, some brief descriptions and examples for the different input methods are explained. For more information how entered weights/coefficients are used in the calculation and the distribution, see [**Amounts Calculation**](https://github.com/ErpNetDocs/tech/blob/master/advanced/documents/additional-amounts/amounts-calculation/index.md) and  [**Amounts Distribution**](https://github.com/ErpNetDocs/tech/blob/master/advanced/documents/additional-amounts/amounts-distribution/index.md).

## Weights/ coefficients in the product definitions

In some cases the weights of specific services are known in advance (before the documents are created). For example when Customs taxes are paid for goods import, some of the products have Customs taxes and others - do not. Also for many products the Customs taxes are defined by law and they are a constant percent of the product value. For such products the user enters their weight for the additional amount Customs. Then when the documents are entered in @@name, when such product is selected in a document row, its weight is copied from the product definition to the 'Document Line Amount' panel. The user can change the default weights of the products.

*Example 1*

There is an additional amount ‘Customs’ with the following properties:

- Distributed by: **Product Definition**;
- Default percent: **100%**.

The user enters Purchase invoice with four rows: row #10 with amount of 44 EUR, row #20 with amount of **56 EUR**, row #30 with amount of **24 EUR** and row #40 with amount of **71 EUR**. In row #10 there is a product with default weight for additional amount ‘Customs’ of **5%** and in row #30 there is a product with default weight **25%**. So these are the coefficients/weights for each row:

- row #10: weight = **0.05**;
- row #20: weight = **0.00**;
- row #30: weight = **0.25**;
- row #40: weight = **0.00**;

So the Customs amount is **8.20 EUR** (see [**Amounts Calculation**](https://github.com/ErpNetDocs/tech/blob/master/advanced/documents/additional-amounts/amounts-calculation/index.md)) and it is distributed through the rows as **2.20 EUR : 0 EUR : 6 EUR : 0 EUR** (see [**Amounts Distribution**](https://github.com/ErpNetDocs/tech/blob/master/advanced/documents/additional-amounts/amounts-distribution/index.md)).

## Weights/coefficients in the document

In some cases the weights for the products for specific additional amounts are not known in advance, because for example they depend on a document parameter. For example, if the weights depend on the Deal Type of the Sales Order - whether VAT is applicable or not. And as the document row may have different Deal Types, then the user will have to enter the weights/coefficients in the specific document along with Deal Type (the products do not have percentages in their definitions in advance).

*Example 2:*

There is additional amount ‘Specific VAT’ which is distributed by product definition and has a default percent of **20%**. The user enters Sales Order with four rows = row #10 with amount of **44 EUR**, row #20 with amount of **56 EUR**, row #30 with amount of **24 EUR** and row #40 with amount of **71 EUR**. Rows #10 and #20 are exempt from VAT, only rows #30 and #40 have 20% VAT. So the user sets manually the following percents (**100%** on rows #30 and #40):

- row #10: weight = **0.00**;
- row #20: weight = **0.00**;
- row #30: weight = **1.00**;
- row #40: weight = **1.00**.

So the amount of Specific VAt is **19 EUR** (see[**Amounts Calculation**](https://github.com/ErpNetDocs/tech/blob/master/advanced/documents/additional-amounts/amounts-calculation/index.md)) and it is distributed through the rows as **0 EUR : 0 EUR : 4.80 EUR : 14.20 EUR**.

*Example 3:*

The following example describes the case when there is no data in the ’Document Line Amount’ panel:

There is an additional amount VAT (distributed by amount and having default percent of **20%**). So as the amount is not distributed by the product definitions in ’Document Line Amount’ panel, there is no data. I.e. in this case it is considered that no weights/coefficients are used for calculating and distributing the VAT amount, or more precisely (so we have more common and easy calculation formulas) it is considered that all document rows have **100%** VAT.
