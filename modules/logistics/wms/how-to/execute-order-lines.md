# How to execute order lines

А **warehouse order (WO)** is the document that contains the actual plan that needs to be executed by the WMS module. 

The WO **lines** can be executed through the **Orders** menu of the **[WMS Worker](https://docs.erp.net/tech/modules/logistics/wms/wms-worker/index.html)** or through the **Execute lines** UI function.

How these lines are executed depends on their **[task type](https://docs.erp.net/tech/modules/logistics/wms/how-it-works/task-types/index.html)**.

**NOTE!** 

Not all task types are currently available for order lines execution. 

Some, such as **[count](https://docs.erp.net/tech/modules/logistics/wms/how-it-works/task-types/count.html)**, are available only as ad hoch operation (e.g. the Reconciliation menu of the WMS Worker).

If you're not familiar with how

### Orders menu

The **[WMS Worker](https://docs.erp.net/tech/modules/logistics/wms/wms-worker/index.html)** is our WMS mobile application available on all compatible Android devices, including handheld devices.

The **Orders** menu is used by the warehouse worker to execute the lines of the warehouse orders that have been assigned to them. 

### Execute lines UI function 

This function is available in the definition of each warehouse order.

When initiated, it executes warehouse order lines based on the specified information, such as product, quantity, lot, warehouse location, and other details.

As a result, it creates warehouse transactions, document fulfillments, or both, depending on the particular line's **[task type](https://docs.erp.net/tech/modules/logistics/wms/how-it-works/task-types/index.html)**. 

The function is especially useful when **[entering initial availability](https://docs.erp.net/tech/modules/logistics/wms/how-to/initial-availability.html)** in the warehouse or as a backup way to execute lines without using the WMS Worker, in case there is a problem with mobile devices, for example.

#### Step-by-step 

1. To begin, go to the definition of the warehouse wrder you want to execute.

Make sure that its state is **released**. If it's not, **release** the document before starting the function.

![Picture](pictures/release-document.png)

2. Then, click the **UI Functions** and select **Execute lines**.

![Picture](pictures/executelines.png)

3. You'll get a confirmation message preceding the operation. Confirm that you want to perform it by clicking **OK**.

![Picture](pictures/warning-message.png)

The line execution functionality processes every line separately.

If the execution of all lines is successful, the function will finish with a **success message**. 

![Picture](pictures/success.png)

If there's problem during the execution of the lines, the function will stop running and it will display a message giving more details about the problem and its cause.

Once the error is identified and resolved, you can continue the execution process from where it was stopped. The system will automatically detect the unexecuted lines left from the previous attempt (based on the document fulfillments that have been created) and proceed with their execution.
