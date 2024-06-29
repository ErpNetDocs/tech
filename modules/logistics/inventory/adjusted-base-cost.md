# Adjusted Base Cost

The **Adjusted Base Cost** feature is responsible for automatically adding each **Base Cost Adjustment** to its respective **Line Base Cost**. 

It achieves this by simultaneously deducting the respective adjustment from itself and adding it to the base cost.

This speeds up the process of issuing transactions as it limits the often-frequent need to make cost corrections resulting from accummulated discrepancies between original and base cost calculations.

## Using Adjusted Base Cost

Here, you'll find detailed steps on how to effectively perform base cost adjustment.

### 1. Create a Cost Correction document

You first need to create a monthly cost correction responsible for adjusting your stores' costs over a specified period.

![picture](pictures/Adjustment_Base_cost_New_correction_27_06.png)

Fill in the **from** and **thru date** of the period and click **Save**.

Then, navigate to the **Functions** tab and select **Recalculate corrections for the period**.

![picture](pictures/Adjustment_Base_cost_Functions_recalculate_27_06.png)

Once prepared, **Release** the document.

### 2. Create a new document type

The next step is creating a special document of type **Cost Correction**.

Its purpose is to generate a cost correction for the actual costs of the current transaction.

### 3. Create a Cost correction transaction

Start creating a cost correction transaction using the new document type you've created.

Required fields are:

- **Store** - the store for which the transaction will be issued
- **Movement Type** - set as Receipt
- **Document Currency** - main currency of the enterprise company.

![picture](pictures/Adjustment_Base_cost_Fill_and_save_27_06.png)

### 4. Apply the function

**Save** the document, navigate to **Functions** and select **Adjust base costs**.

![picture](pictures/Adjustment_Base_cost_Functions_adjust_27_06.png) 

The function will load all products (with 0 quantities) from the selected store whose base costs are different from their original line costs.

It is only after **releasing** this transaction that it will match their current base costs with their adjusted costs.

Values added to the **Line Base Cost** will be simultaneously subtracted from the **Base Cost Adjustment**.

![picture](pictures/Adjustment_Base_cost_Released_27_06.png) 

The **Cost Source** of the document will change to **Adjustment**.

During subsequent adjustments, any recorded discrepancies in **Base Cost** are offset against **Adjusted Cost**, maintaining equilibrium as quantities normalize to zero.
