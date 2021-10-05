# Standard quantity base

In Version 2018.2, we added a new dimension to measure the quantity in Logistics Documents - Standard Quantity Base (SQB). 

SQB represents the theoretical quantity in the base measurement unit according to the current dimensions of the product. 

The main objective is to improve algorithms for exhaustion and clear traceability of the execution of the ordered quantity.
 
## More details

Quantity (Q) and Quantity Base (QB) were used for the exhaustion of the quantities between parent and generated (child) documents. 

Variable measurement ratios allowed the **editing** of QB. It no longer tracks the exhaustion between a parent and a child document.
 
*Example*:

PRODUCT (2 pcs = 1 kg standard)

SALES ORDER (Q = 100 pcs, QB = 50 kg)

STORE TRANSACTION (Q = 100 pcs, QB = 49 kg)

- The QB in the STORE TRANSACTION is 49 because that quantity has been measured in the store. </br>QB in the SALES ORDER is 50 kg because this is the theoretical (standard) quantity in the base measurement unit.

- Although QB in the STORE TRANSACTION  is 49 kg, the ordered quantity is fully exhausted.

The example above shows that QB can no longer be used to monitor exhaustion, at least in the case of products with a variable ratio of units of measurement. This led to the need of adding a new measure - **SQB** (quantity in a standard unit of measure). 

**SQB** is the theoretical quantity in Base Measurement Unit which will be calculated if QB remains read-only, unchangeable by the user.
 
*Example*:

PRODUCT (2 pcs = 1 kg)

SALES ORDER (Q = 100 pcs, QB = 50 kg, SQB = 50 kg)

STORE TRANSACTION (Q = 100, QB = 49 kg (measured), SQB = 50 kg)

Here, it is clear that if we use SQB, we can easily and accurately determine whether the document is exhausted or not.
 
This made the SQB Metric the **main generation procedure indicator** as to deciding whether the quantity of the parent document is fully exhausted or not. It does not mean that Q and QB will no longer be taken into account. An exhaustion of Q and QB will continue to be performed - otherwise, the algorithms won’t be able to solve problems with rounding when we are partially executing the ordered quantity. The difference is that they **will not** determine whether a new child record must be created.

For more information, see **Metrics**.

SQB also allows for exhaustion monitoring and the unification not only of all generation procedures but also of all functional navigators.</br> A record/line in functional navigators will be available for execution only if there is а remaining SQB that hasn’t been thoroughly fulfilled by the child documents.

When using exhaustion by SQB, all functionalities will also work for non-VMR products while preserving resilience in terms of manual change in the measurement ratios.
 
## General SQB purposes 

In Conclusion, the new SQB dimension allows:

- QB exhaustion even when we are using VMR;

- QB and SQB exhaustion for non-VMR products;

- solving problems with rounding when we are partially executing the ordered quantity;

- clear traceability of how much of the ordered quantity is exhausted;

- implementation of the same algorithm for executing and exhausting quantities for all functional navigators. 

