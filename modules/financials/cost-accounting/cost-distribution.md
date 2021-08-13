# Cost Distribution

Cost Distribution document is used to distribute costs. The user may enter one or more cost types and their amounts. The cost distribution may be performed manually or automatically by using the integrated functions.

## How to use the document?

At first, the user has to enter the dates and (if necessary) store, where they are distributing costs. The period of the cost distribution is specified in the Cost Distribution table by the following fields:

- Start Date - starting date of the period for which the current document distributes costs. The field cannot be empty and it is entered manually by the user. 
- End Date - end date of the period for which the current document distributes costs. The field cannot be empty and it is entered manually by the user.
- Store - specifies the store in which the cost is distributed.

In the Distribution cost types table the user enters the cost types and their amounts.

> [!NOTE]  
> The cost type amounts are entered in enterprise company base currency!

The Distributed Cost Amount field accepts decimal values.

Then the user has to enter/load the outputs on which they are distributing the specified amounts and cost types. This is performed in the Outputs table. The fields are:

- Line No - this is the consecutive line number in the document, unique within the document.
- Cost Object - the ID of the cost object, for which costs will be distributed. The domain of the cost object is determined by the distribution document type.
- Weight Coefficient - the field is mandatory. This is a weight coefficient for the cost distribution on the current row.

Manual data entering in the Outputs table is not available. The document has a function which automatically loads the outputs for the specified period (and store, if entered). For more information see **[Add Production Function](https://github.com/ErpNetDocs/tech/blob/master/modules/financials/cost-accounting/add-production-function.md)**.

After the production is filled in the document, the cost distribution calculation may be performed manually or automatically. The table Cost Distribution Results contains the amounts calculated for distribution on the Outputs data. In the Results table, there are the following fields:

- Output Id - the distribution output over which we are distributing the cost (the amount in the current row);
- Cost Type - the cost type for which the distribution in the current row is calculated;
- Distributed Amount Base - the amount (in base currency) of the distributed cost. The amount is calculated for the combination of output and cost type. 

The data in the Results table has a function that calculates distributed amounts on each output. The amount is the total amount (distributed to the current output) of all cost types, which are set for distribution. For more information see **[Calculate Distribution Function](https://github.com/ErpNetDocs/tech/blob/master/modules/financials/cost-accounting/calculate-distribution-function.md)**.


