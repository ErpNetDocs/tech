# Amount distribution by quantity

When using this distributional method the coefficients for calculation of the proportions [**ki**]/[**S**] are defined by the quantities in the rows on which the additional amount is distributed. So at first it is necessary to bring the quantities to the same measurement unit. Therefore, the additional amounts that use this  property (Distribute By = Quantity), are required to have a selected  option in the *Distribute By Measurement Category* field. Thus, the base measurement unit in the selected category is the measurement unit which the quantities from all rows will be converted to (if there is a row  with product with no dimension for the base measurement unit of the  selected measurement category, than the calculation is ceased and an  error message is displayed), So, if the [distribution measurement unit]  is the measurement unit from the selected category in the additional  amount definition, than for each row the coefficients are as follows:

[**ki**] = [quantity on row **i**] converted to [distribution measurement unit].

Than the additional amount distribution is performed by the standart formula (in proportions [**ki**]/[**S**], if [**S**] is not **0**, or otherwise - equally throught the rows).

#### Example 1:

There is a Transport additional amount with input amount of **42 EUR**, which is payed by goods **box**. In the transport definition is marked that it is distributed by quantity and that the measurement category is **Boxes** (where the base measurement unit is **boxes**). The document where the additional amount is selected has three rows = row #10 with quantity of **2 boxes**, row #20 with quantity of **25 pieces** and row #30 with quantity of **18 kg**. The product of row #20 has the following dimension: **1 boxes = 10 pieces**. The product of row #30 has the following dimension: **1 boxes = 3 kg**. Than after converting all row quantities to **boxes**, the following coefficients are calculated:

- row #10: [**k1**] = **2**;
- row #20: [**k2**] = **2.5**;
- row #30: [**k3**] = **6**.

Than the amount of **42 EUR** is distributed in the 2:2.5:6 ratio and the results are:

- row #10: **42 EUR** * 2 / 10.5 = **8 EUR**;
- row #20: **42 EUR** * 2.5 / 10.5 = **10 EUR**;
- row #30: **42 EUR** * 6 / 10.5 = **24 EUR**.

#### Example 2:

There is amount of **42 EUR** of transport as in *Example 1*. Only in the current example the document rows are: row #10 with quantity of **2 boxes**, row #20 with quantity of **30 pieces** and row #30 with quantity of **-15 kg**. Than the coefficients are [**k1**] = **2**, [**k2**] = **3** and [**k3**] =**-5** and total amount of **[S] = 0**.

In this case the additional amount is distributed equally through the rows and the result is:

- row #10: 42 EUR/ 3 = **14 EUR**;
- row #20: **42 EUR** / 3 = **14 EUR**;
- row #30: **42 EUR** / 3 = **14 EUR**.
