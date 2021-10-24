
# Non agreed services and materials

When a service activity creates store order, in order to invoice the used materials and the services which are performed, the sales orders have to include the non-agreed quantities of the materials and the services. The rest of the materials and services are covered by the guarantee, which is agreed in the service agreements. 
The current topic describes the calculation of the non agreed services and materials based on the data in a service activity.

The agreed services and materials are listed in the service agreements, in the ServiceAgreementService and ServiceAgreementMaterial tables.
After that the quantities which are listed in there are distributed through the service activities. 
When a service activity is released, what part of the agreed quantities has not been used by the previous service activities is calculated and the result (the remaining quantities) is distributed in the current document (only if the remaining quantities are not greater than the used quantities recorded in the current document). 
The distributed quantities are recorded in the Distributed Service Agreement Materials and Distributed Service Agreement Services tables.
After all, the non-agreed materials and services are calculated by subtracting the quantities from those tables from the quantities in the current service activity. 

## Non agreed materials

For each Material line in the current service activity all records from Distributed Service Agreement Materials table which correspond the current line are derived.
The amounts from the Agreed Quantity column are summed up (converted to the measurement unit of the material in the service activity line; the values in Agreed Quantity column are in measurement unit of the service agreement) and the sum is subtracted from the quantity in the current line (only if the sum is not greater than the quantity in the current line).
This is the calculation:
```
[**non-agreed material quantity**] =
  if [**Service Activity Material Quantity**] >= [**sum of distributed service agreement materials**]
    then [**Service Activity Material Quantity**] - [**sum of distributed service agreement materials**]
    else **0**
```
### Example 1:
There is a service activity with three lines with materials:
- line #10, Material #1, **10PCS**;
- line #20, Material #2, **13PCS**;
- line #30, Material #3, **40PCS**.

Distributed Service Agreement Materials table has the following data:
- line #20 from the Service Activity, line #70 from Service Agreement #00007, **4PCS**;
- line #20 from the Service Activity, line #30 from Service Agreement #00019, **11PCS**;
- line #30 from the Service Activity, line #10 from Service Agreement #00007, **48KG**.

Thus, for line #10 from the Service Activity the distributed quantity is **0PCS**, for line #20 from the Service Activity the distributed quantity is **15PCS**, and if Material #3 has the following dimension: 3KG = 1PCS, than for line #30 the sum is 16 PCS. Thus, the non agreed quantities are calculated s follows:

- for line #10: [non agreed quantity of the material] = 10PCS - 0PCS = **10PCS;**
- for line #20: [non agreed quantity of the material] = **0PCS** (because 13PCS < 15PCS);
- for line #30: [non agreed quantity of the material] = 40PCS - 16PCS = **24PCS;**

## Non agreed services

The services are not invoices directly as they are not products, so to invoice them the information in service invoicing from the service definition is used.
So, for each service activity line with service and for each record in service invoicing the following quantity of the product from the service invoicing records, is calculated:
```
[**quantity to invoice**] =
  [**Service Activity Service Quantity**] * [**ServiceInvoicing.QuantityOfProduct**] /
    [**ServiceInvoicing.QuantityOfService**]
```
The distributed quantities from the service agreements which correspond the current service line are subtracted from the described above **quantity to invoice**. 
But this is performed in two stages as in the service agreements there are two methods to describe agreements for services - one is to agree on a certain number of the **service**, and the second is to agree on certain number from the product from the **service invoicing**. 

Thus the non-agreed quantity of a specific product which invoices a specific service (i.e. a product listed in the Service Invoicing table of the service definition), happens by the following two formulas:

At first, what quantity is not agreed by service agreements is calculated. 
This happens as all distributed quantities for the specified line listed in the Distributed Service Agreement Services table (but only records which are on specific service agreements where the service attribute is selected and service product attribute is null) are subtracted from the quantity from the Service Activity line.
The following temporary value is calculated:
```
[**preliminary quantity 1**] =
  if [**Service Activity Service Quantity**] >= [**sum of distributed service agreement services**]
    then [**Service Activity Service Quantity**] - [**sum of distributed service agreement services**]
    else **0**
```
Using this **preliminary quantity 1** for each product in service invoicing in the service definition a preliminary quantity for invoice is calculated:
```
[**preliminary quantity** **2**] =
  [**preliminary quantity** **1**] * [**ServiceInvoicing.QuantityOfProduct**] /
    [**ServiceInvoicing.QuantityOfService**]
```
And at the end, from the **sum of distributed service agreement services** which are for the same product and for which we have calculated the preliminary quantity, the calculated **preliminary quantity 2** is subtracted. 
But only for quantities which are based on Service Agreements lines and which have empty service attribute and not null product attribute. 
Also, the distributed quantities are always converted to the measurement unit which is selected in the Service Invoicing record (as the measurement unit in the service agreement may be different).
So:
```
[**non agreed quantity of a product for invoicing**] =
  if [**preliminary quantity** **2**] >= [**sum of the distributed quantities of the product from Service Agreements**]
    then [**preliminary quantity** **2**] - [**sum of the distributed quantities of the product from Service Agreements**]
    else **0**
```
### Example 2:
Lets have Service #1 with the following Service Invoicing data:
- 1 PCS of Service = 2 PCS of Product #1;
- 2 PCS of Service = 3 PCS of Product #2.

And for Service #2, the invoicing products are:
- 1 PCS of Service= 4 PCS of Product #1;
- 1 PCS of Service= 10 PCS of Product #3.

There is Service Activity with the following services:
- line #10, Service #1, **6PCS**;
- line #20, Service #2, **8PCS**.

Distributed Service Agreement Services table contains the following:
- line #10 of the Service Activity, line #40 (with Service #1) from Service Agreement #00023, **2PCS**;
- line #20 of the Service Activity, line #50 with Service #2) from Service Agreement #00023, **3PCS**;
- line #20 of the Service Activity, line #30 (with Service Product #3) from Service Agreement #00037, **78KG**.

So the first preliminary quantity is calculated as follows:
- for line #10: [preliminary quantity 1] = 6PCS - 2PCS = **4PCS**;
- for line #20: [preliminary quantity 1] = 8PCS - 3PCS = **5PCS**.

Then the preliminary quantity for invoicing is:
- for line #10 and Product #1: [preliminary quantity 2] = 4PCS * 2PCS / 1PCS = **8PCS**;
- for line #10 and Product #2: [preliminary quantity 2] = 4PCS * 3PCS / 2PCS = **6PCS**;
- for line #20 and Product #1: [preliminary quantity 2] = 5PCS * 4PCS / 1PCS = **20PCS**;
- for line #20 and Product #3: [preliminary quantity 2] = 5PCS * 10PCS / 1PCS = **50PCS**.

And at the end, if the dimensions of Product #3 are 3KG = 1PCS, the final calculations are:
- for line #10 and Product #1: [non agreed quantity] = 8PCS - 0PCS = **8PCS**;
- for line #10 and Product #2: [non agreed quantity] = 6PCS - 0PCS = **6PCS**;
- for line #20 and Product #1: [non agreed quantity] = 20PCS - 0PCS = **20PCS**;
- for line #20 and Product #3: [non agreed quantity] = 50PCS - 26PCS = **34PCS**.
