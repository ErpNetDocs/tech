# VAT Deviation


VAT Deviation is a term used in sales orders and invoices. It is used in POS/store sales and their sales invoices. VAT deviation is the difference between the amount of the document that is obtained, when value added tax is calculated on the total amount of the document (which is the standard method of calculation in @@name) and the amount that is obtained when value added tax is charged on each Unit price in the document separately (which is the case for Store sales).


## Usage 


VAT Deviation is used in store sales and their sales invoices when in those documents the VAT and/or discounts are not applied directly to the line amounts. Then the total amount of payment that @@name will calculate (value **[Standard Amount]**) may differ, usually by a few cents, from the amount the client actually pays (value **[POS Amount]**). In these cases, VAT deviation is calculated as an additional amount in the Sales order / Invoice that is paid by the customer and serves as an adjustment to the standard @@name way of calculating a payment amount. The additional VAT deviation can be used for accounting purposes as well, in order to make a transition between the standard amounts and the POS amounts.


## Calculation


If we denote the value of the two amounts of the document by **[POS Amount]** and **[Standard Amount]** then the formula would be:

**[VAT Deviation] = [POS Amount] - [Standard Amount]**.

The difference between **[POS Amount]** and the **[Standard amount]** is that when calculating the **[POS Amount]** VAT is applied to the line amount for each line separately (taking into consideration the standard and specific discounts and then rounding off the result to a second decimal sign before calculating the amount of the line). Whereas while calculating **[Standard Amount]** the value added tax is applied to the entire amount of all lines (the rounding is performed on the total amount).

**[POS Amount]** and **[Standard Amount]** are calculated as follows:

**[Standard Amount]** = Round (**[Line Amount_Line1]** + **[Line Amount_Line2]** + ... + **[Line Amount_LineN]**) * (1 + **[VAT Rate]**))

**[POS Amount] = [POS Line Amount_Line1] + [POS Line Amount_Line2] + ... + [POS Line Amount_LineN]**, 

where **Line1, Line2, ... LineN** are all lines in the Sales / Invoice (the formula of the Line Amount is described it the topic **Determine Line Amount in Sales Orders**), and the POS Amount for each line is calculated as follows:

**[POS Line Amount]** = Round (**[Quantity] * [POS Unit Price],**

**[POS Unit Price]** = Round (**[Unit Price]** * [1 - **[Standard Discount]**) * (1 - **[Custom Discount]**) * (1 + **[VAT Rate]**)).

The rounding made to a second decimal place. It is also considered that all percentages - [VAT rate], [Standard Discount] and [Custom Discount] - are fractional numbers between 0 and 1.


#### Example:


Let's have a sales order with two lines: in the first one we have 7 pcs with a Unit Price - 7.37 (without VAT) and in the second one we have 0.354 kg with a Unit Price of 3.58 (VAT excluded). The VAT rate is 20% (i.e. [VAT rate] = 0.2).
So we can calculate that:

**[LineAmount_Line1]** = Round (**7 * 7.37**) = **51.59**;

**[LineAmount_Line2]** = Round (**0.354 * 3.58**) = Round (**1.26732**) = **1.27**;

**[Standard Amount]** = Round ((**51.59 + 1.27**) * (**1 + 0.2**)) = Round (**63.432**) = **63.43**;

**[POS Unit Price_Line1]** = Round (**7.37 * (1 + 0.2**)) = Round (**8.844**) = **8.84**;

**[POS Unit Price_Line2]** = Round (**3.58 * (1 + 0.2**)) = Round (**4.296**) = **4.30**;

**[POS Line Amount_Line1]** = Round (**7 * 8.84**) = **61.88**;

**[POS Line Amount_Line2]** = Round (**0.354 * 4.30**) = Round (**1.5222**) = **1.52**;

**[POS Amount]** = **61.88** + **1.52** = **63.40**;

**[VAT Deviation]** = **63.40** - **63.43** = **-0.03**.
