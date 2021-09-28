# Warehouse order execution

Warehouse order execution can be done through the WMS mobile application. 

The warehouse order lines are loaded one by one and are executed by the worker using the execution Wizzard. 
The Wizard loads information about the Task Type, Warehouse Location, Product and Quantity of the executed line.
The proposed Warehouse Location, Product and Quantity can be either confirmed or changed.

When the line is completed, the execution is recorded as both Warehouse Transaction and Warehouse Order Execution. 
The count of the records information in them depends on the Task Type.

If Task Type is MOVE are created:
- two Warehouse Transactions - one with OUT direction and the the Warehouse Location specified during the line execution and one with IN direction and the To Warehouse Location specified in the warehouse order line
- one Document Fulfillment with Completed fulfillment type and the Quantity speficied during the line execution

If Task Type is RECEIVE are created:
- one Warehouse Transaction with IN direction and the the Warehouse Location specified during the line execution 
- one Document Fulfillment with Completed fulfillment type and the Quantity speficied during the line execution
 
If Task Type is RECEIVE are created:
- one Warehouse Transaction with OUT direction and the the Warehouse Location specified during the line execution 
- one Document Fulfillment with Completed fulfillment type and the Quantity speficied during the line execution
 
