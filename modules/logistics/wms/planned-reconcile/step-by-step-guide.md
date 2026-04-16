## Step-by-Step Guide

### Step 1: Create a new Warehouse Reconciliation document

Click **New** and create a document of type Warehouse Reconciliation.<br>
Select the warehouse and save the document in status Planned.<br>
At this stage, you only define where the process will run – no counting data is created yet.<br><br>

### Step 2: Define what will be counted

Select the scope of the reconciliation – full warehouse, zones, locations, or a combination of them.<br>
If the whole warehouse is selected, the system will include all available stock.<br>
If zones or locations are selected, only the stock in those locations will be included.<br><br>

### Step 3: Generate Snapshot

Click the **Generate Snapshot** UI function.<br>
The system captures the current warehouse availability and creates records in the Details panel.<br>
Each line contains the expected (snapshot) quantity and an empty counted quantity.<br>
All lines are initialized with Session = 0 and Review Status = Created.<br><br>

### Step 4: Start Initial Count

Click the **Initial Count** UI function.<br>
The system generates Warehouse Orders for counting, containing only locations.<br>
The goal is to count all selected locations in the warehouse.<br>
Depending on configuration, orders can be created as a single order or split by zones.<br>
All lines move to Session = 1 and Review Status = Started, indicating that counting has begun.<br><br>

### Step 5: Perform counting and monitor results

Open WMS Worker and execute the generated counting tasks.<br>
Workers scan locations and then scan products or enter quantities.<br>
If no quantity is entered, scanning a product counts it as 1.<br><br>

All counted data is recorded in the Counts panel:<br>
- Each worker sees only their own counts<br>
- Supervisors can see all counts with details such as time, product, and quantity<br><br>

When a Warehouse Order is completed by the worker:<br>
- The counted quantities are calculated<br>
- They are filled in the Counted Quantity field in the Details panel<br>
- The corresponding lines move to Review Status = Finished<br><br>

The Details panel shows both expected (snapshot) and counted quantities.<br>
While counting is in progress, lines remain in Session = 1 and Review Status = Started.<br><br>

### Step 6: Review results and decide next actions

Review the results in the Details panel by comparing expected and counted quantities.<br>
Select one or multiple lines and use the available buttons to change their Review Status:<br>
- Approved – based on user decision, even if differences exist<br>
- Cancelled – if the line should be excluded<br>
- Recount – if the line needs to be counted again<br><br>

The buttons work in multi-select mode, allowing you to update multiple lines at once.<br><br>

### Step 7: Generate Recount

Use one of the available functions:<br>
- Recount (Single Order) – creates one warehouse order for all selected lines<br>
- Recount (Split by Zones) – creates separate orders by zones<br><br>

The system generates new Warehouse Orders only for the lines marked for recount.<br>
A new session is created by taking the highest existing session and incrementing it by one.<br>
Only the selected lines move to the new session and change their Review Status to Started.<br><br>

### Step 8: Perform recount

Execute the recount tasks in WMS Worker.<br>
This time, counting is done with full product details for more precise verification.<br>
The new counted results are recorded for the new session.<br><br>

### Step 9: Review final results

Return to the document and review the updated values in the Details panel.<br>
The system uses the latest session to determine the final counted quantities.<br>
You can approve lines here as well using the available buttons.<br><br>

### Step 10: Final approval

Ensure all lines are finalized with Approved or Cancelled status.<br>
This confirms that the reconciliation results are complete.<br><br>

### Step 11: Release the document

Change the document status to Released.<br>
The system generates Warehouse Transactions based on the final results.<br>
Warehouse availability is updated according to the approved quantities.
