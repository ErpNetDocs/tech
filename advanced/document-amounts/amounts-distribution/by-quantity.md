# Amount distribution by quantity

When using this distribution method, the coefficients for calculating the proportions [**ki**]/[**S**] are defined by the quantities in the rows on which the additional amount is distributed. It's necessary to bring the quantities to the **same** measurement unit. 

Therefore, the additional amounts using this property (_Distribute By_ = Quantity), are **required** to have a selected option in the *Distribute By Measurement Category* field. The base measurement unit in the selected category is the unit to which quantities from all rows will be converted. If a row with a product has no such dimension, the calculation stops and an error message is displayed.

As long as [distribution measurement unit] is the measurement unit from the selected category in the additional amount definition, then for each row, the coefficients are as follows:

[**ki**] = [quantity on row **i**] converted to [distribution measurement unit].

The additional amount distribution is performed by a standard formula <br> (in proportions [**ki**]/[**S**], if [**S**] is not **0**, or otherwise - equally throughout the rows).

**Example 1:**

There's a transport additional amount with input of **42 EUR**, which is paid by goods 'box'. 

In the definition, transport is distributed by quantity and the measurement category is 'Boxes' (base measurement unit = boxes). 

The document where the additional amount is selected has three rows:

row #10 with quantity of **2 boxes**, <br> row #20 with quantity of **25 pieces** <br> row #30 with quantity of **18 kg**. 

The product of row #20 has the following dimension: **1 boxes = 10 pieces**. <br> The product of row #30 has the following dimension: **1 boxes = 3 kg**. 

After converting all row quantities to 'boxes', the following coefficients are calculated:

- row #10: [**k1**] = **2**; <br>
- row #20: [**k2**] = **2.5**; <br>
- row #30: [**k3**] = **6**. <br>

The amount of **42 EUR** is distributed in 2:2.5:6 ratio. The results are:

- row #10: **42 EUR** * 2 / 10.5 = **8 EUR**; <br>
- row #20: **42 EUR** * 2.5 / 10.5 = **10 EUR**; <br>
- row #30: **42 EUR** * 6 / 10.5 = **24 EUR**. <br>

**Example 2:**

There is an amount of **42 EUR** of transport as in Example 1. The document rows are: 

row #10 with quantity of **2 boxes** <br> row #20 with quantity of **30 pieces** <br> row #30 with quantity of **-15 kg** 

The coefficients are [**k1**] = **2**, [**k2**] = **3** and [**k3**] =**-5** and total amount of **[S] = 0**.

In this case, the additional amount is distributed equally among the rows and the result is:

- row #10: **42 EUR** / 3 = **14 EUR**; <br>
- row #20: **42 EUR** / 3 = **14 EUR**; <br>
- row #30: **42 EUR** / 3 = **14 EUR**. <br>
