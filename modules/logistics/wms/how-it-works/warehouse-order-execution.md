# Warehouse order execution

Warehouse order execution can be done through the WMS mobile application. 

The warehouse order lines are loaded one by one and are executed by the worker using the execution Wizzard. 
The Wizard loads information about the task type, warehouse location, product and quantity of the executed line.
The proposed warehouse location, product and quantity can be either confirmed or changed.

When the line is completed, the execution is recorded as both warehouse transaction and warehouse order execution. 
The count of the records information in them depends on the task type.

If task type is MOVE, then :
- two warehouse transactions - one with OUT direction and the the warehouse location specified during the line execution and one with IN direction and the To Warehouse Location specified in the warehouse order line
- one document fulfillment with completed fulfillment type and the quantity speficied during the line execution
  are created.

If task type is RECEIVE, then :
- one warehouse transaction with IN direction and the the warehouse location specified during the line execution 
- one document fulfillment with completed fulfillment type and the quantity speficied during the line execution
 are created.
 
If task type is RECEIVE, then:  
- one warehouse Transaction with OUT direction and the the warehouse location specified during the line execution 
- one document Fulfillment with completed fulfillment type and the quantity speficied during the line execution
 are created.
