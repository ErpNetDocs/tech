---
uid: document-amounts
---

# Additional amounts 

**Additional amounts** are a mechanism for reporting financial amounts in documents that **aren't** contained in document lines and/or **don't** represent measurement of the main purpose of the document. 

This main purpose is written in document lines or in the document header. An example of amounts reletaed to the main purpose are:
- product price or product cost of a product (goods or services), which is sold or bought;
- enterprise company asset price or cost (fixed, financial or rental);
- value/amount of monetary transaction (transfer, payment or obligation).

The amounts listed above are base amounts in documents and they are **NOT** additional.

<br/>Additional amounts, on the other hand, are amounts that should not be indicated together with the main activity or are **secondary** effect of the main document purpose. 
Here are some examples:

- **VAT (and other taxes)** - taxes are not products an enterprise company is selling, producing or supplying; that's why they're usually reported as additional amounts in the documents;

- **VAT deviation** - this special amount is used for equalization of the VAT in store sales (because of specific roundings); this amount is additional because it's used to obtain the legal rate of the VAT.

- **Taxes (as customs)** - the same principles as in taxes are applied;

- **Discounts** - some types of customer discounts are represented as additional amounts when the discount can't be entered in a specific document row or there are no active promotions or bonus programs which control the discount;

- **Increases and decreases** -  the same principle as in discounts: if the increases and/or decreases can't be defined in the rows or as part of a sale instrument, such as promotional programs or bonus packages, they're entered as additional amounts;

- **Commissions (and other internal mechanisms for payments or money accounting)** - if used as additional amounts, they can represent a percentage of the document amount and the result can be used for recording internal company performance or personal employee indicators.


## Usage

Additional amounts are used for different reasons, such as adding amounts to the main business activity in a document or reporting secondary measurements for a business or outside activities.

#### Calculating the amount to pay

Some additional amounts serve to calculate the [amount-to-pay](~/modules/crm/sales/sales-concepts/amount-to-pay.md) for a document. This is marked in the definition by adding a check to the *Add To Customer* field. Usually, these are amounts like VAT, VAT deviation, discounts, increases, decreases. 

#### Calculating goods cost

Additional amounts may be used to add value to the cost of the goods in the [Logistics](~/modules/logistics/index.md)

For example, if the transport is entered as an additional amount when goods are purchased, the transport value will be **added** to the purchase price. When a stock transfer from one store to another is executed and it includes transport cost added to the issued products, the value of this transport should be **added** to the products cost **before** they are received in the second store. 

Adding transport to the purchase price or the store cost is done in the receiving store orders or store transactions. When a row in the sub-document is created, the value of this row is **increased** by the distribution in the current row amount of the transport.

The same procedure is applied to **all** additional amounts marked as part of the store cost calculation. 

This is the *Add To Line* field in the definition of the additional amount.

#### Calculating outside activities

Additional amounts may also be used to report the external activities of an enterprise company.

For example, if a salesman in a company receives commission or other additions to their salaries equal to a percentage of the turnover they achieve, the commision may be entered as an additional amount in the sales order, which is a **percentage** of the amount to pay.


-------
### See more

[!list folder="." depth=0 style="bullet" limit=100]
