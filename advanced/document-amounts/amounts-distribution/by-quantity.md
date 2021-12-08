# Amount distribution by quantity

When using this distribution method, the coefficients for calculating the proportions [**ki**]/[**S**] are defined by the quantities in the lines on which the additional amount is distributed. It's necessary to convert the quantities to the **same** measurement unit. 

Therefore, the additional amounts using this property (_Distribute By_ = Quantity), are **required** to have a selected value in the *Distribute By Measurement Category* field. The base measurement unit in the selected category is the unit to which quantities from all lines will be converted. If a line with a product has no such dimension, the calculation stops and an error message is displayed.

As long as [distribution measurement unit] is the measurement unit from the selected category in the additional amount definition, then for each line, the coefficients are as follows:

[**k<sub>i</sub>**] = [quantity on line **i**] converted to [distribution measurement unit].

The additional amount distribution is performed by a standard formula <br> (in proportions [**k<sub>i</sub>**]/[**S**], if [**S**] is not **0**, or otherwise - equally throughout the lines).

**Example 1:**

There's a transport additional amount with input of **42 EUR**, which is paid by goods 'box'. 

In the definition, transport is distributed by quantity and the measurement category is 'Boxes' (base measurement unit = boxes). 

The document where the additional amount is selected has three lines:

line #10 with quantity of **2 boxes**, <br> 
line #20 with quantity of **25 pieces** <br> 
line #30 with quantity of **18 kg**. 

The product ofline #20 has the following dimension: **1 boxes = 10 pieces**. <br> The product of line #30 has the following dimension: **1 boxes = 3 kg**. 

After converting all line quantities to 'boxes', the following coefficients are calculated:

- line #10: [**k<sub>1</sub>**] = **2**; <br>
- line #20: [**k<sub>2</sub>**] = **2.5**; <br>
- line #30: [**k<sub>3</sub>**] = **6**. <br>

The amount of **42 EUR** is distributed in 2:2.5:6 ratio. The results are:

- line #10: **42 EUR** * 2 / 10.5 = **8 EUR**; <br>
- line #20: **42 EUR** * 2.5 / 10.5 = **10 EUR**; <br>
- line #30: **42 EUR** * 6 / 10.5 = **24 EUR**. <br>

**Example 2:**

There is an amount of **42 EUR** of transport as in Example 1. The document lines are: 

line #10 with quantity of **2 boxes** <br> line #20 with quantity of **30 pieces** <br> line #30 with quantity of **-15 kg** 

The coefficients are [**k<sub>1</sub>**] = **2**, [**k<sub>2</sub>**] = **3** and [**k<sub>3</sub>**] =**-5** and total amount of **[S] = 0**.

In this case, the additional amount is distributed equally among the lines and the result is:

- line #10: **42 EUR** / 3 = **14 EUR**; <br>
- line #20: **42 EUR** / 3 = **14 EUR**; <br>
- line #30: **42 EUR** / 3 = **14 EUR**. <br>
