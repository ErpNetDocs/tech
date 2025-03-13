# Costing methods

The costing methods are used to determine the exact cost price of products, which is essential for:

- Pricing: Knowing the cost price helps companies set competitive and profitable prices for their products.

- Cost control: By analyzing the cost price, companies can identify and reduce unnecessary expenses.

- Planning and budgeting: Accurate cost price is the basis for effective financial planning and budgeting.

and others.

<br/>In @@name, costing methods can be configured both globally at the Enterprise Company level and individually for each Product. 
The application priorities are as follows:
-	If a method is specified in both the Product definition and the Enterprise Company definition, the one from the Product is with higher priority;
-	If no method is specified in the Product definition, the one from the Enterprise Company is used. Since the costing method is a mandatory field for the Enterprise Company, it will always have a defined value.

> **_NOTE:_** Regardless of where the method is specified, the cost price is calculated in the same way.


@@name supports multiple costing methods to accommodate diverse business needs. The available costing methods include:

## 1. **Average cost for the whole product:**
The most commonly used method, given that not all products have lots. It is used when lots are not assigned to the product or when tracking cost price by lots is unnecessary.

  The cost is calculated by taking the value of all available products, regardless of whether they have lots or not, and averaging it.

<details>
  <summary>Click here so see the <b>Example:</b></summary>
 
  - **Product X** has 100 units in stock.
  - 50 units were bought at 8 BGN each, and 50 units were bought at 10 BGN each.
  
  To calculate the average cost:
 
  - Total cost = (50 * 8) + (50 * 10) = 400 BGN + 500 BGN = **900 BGN.**
  - Average cost per unit = 900 BGN / 100 units = **9 BGN** per unit.
  
  In this case, the cost is averaged across all units, regardless of whether they have lots assigned to them.
</details>

## 2. **Separate cost for each lot:** 
Used when products have unique lots and it is important to calculate the cost price of each separately (due to different acquisition prices, regulatory requirements, or other reasons). 

 The cost is calculated by taking the value of all available products by lots and averaging it for each lot. If for the same product, there are availabilities without a lot, then the cost for them is calculated by assuming that all are a part of a single, unified lot.

<details>
  <summary>Click here so see the <b>Example:</b></summary>
 
- **Product Y** has two lots: 
     - **Lot 1:** 100 units in stock - 50 units were bought at 8 BGN each, and 50 units were bought at 10 BGN each.
     - **Lot 2:** 100 units in stock - 50 units were bought at 4 BGN each, and 50 units were bought at 6 BGN each.
   
To calculate the cost for each lot separately:

**Lot 1 cost:** 
  - Total cost = (50 * 8) + (50 * 10) = 400 BGN + 500 BGN = **900 BGN.**
  - Average cost per unit = 900 BGN / 100 units = **9 BGN** per unit.

**Lot 2 cost:** 
  - Total cost = (50 * 4) + (50 * 6) = 200 BGN + 300 BGN = **500 BGN.** 
  - Average cost per unit = 500 BGN / 100 units = **5 BGN** per unit.
  
<br/>If there are another 100 units of Product Y available **without a lot**, they are considered part of a **single, unified lot.** 

**No lot:** 100 units in stock - 50 units were bought at 2 BGN each, and 50 units were bought at 4 BGN each.

 - Total cost = (50 * 2) + (50 * 4) = 100 BGN + 200 BGN = **300 BGN.**
 - Average cost per unit = 300 BGN / 100 units = **3 BGN** per unit.

Each lot has its own cost calculated separately, and products without a lot are treated as part of a unified cost group.
</details>

## 3 **Average, partitioned by Reserved for document:** 
Used in situations where it is necessary to separate the cost of specific lots related to a given document (e.g., sales order, purchase order, or other). 

The cost is calculated as follows:
- For lots **reserved for the same document,** the cost price is determined by averaging the cost of all available quantities within those lots.

- For the remaining lots **not reserved for any document,** the cost is calculated by treating all of them as part of a single, unified lot and averaging the cost across all these lots.

<details>
  <summary>Click here so see the <b>Example:</b></summary>
  
<br/>- **Product W** has four lots: 
     - **Lot 1:** 10 units in stock at 5 BGN each (Reserved for a sales order).
     - **Lot 2:** 20 units in stock 6 BGN each (Reserved for the same sales order).
     - **Lot 3:** 15 units in stock 7 BGN each (Not reserved for any document).
     - **Lot 4:** 25 units in stock 8 BGN each (Not reserved for any document).
   
To calculate the cost:
 
**For the reserved lots (Lot 1 and Lot 2):**

 These lots are reserved for the same sales order, so their costs are calculated by averaging the cost for both (all) of them:
 
  - Total cost = (10 * 5) + (20 * 6) = 50 BGN + 120 BGN = **170 BGN.**
  - Average cost per unit = 170 BGN / 30 units = **5.67 BGN** per unit.

**For the unreserved lots (Lot 3 and Lot 4):**

 These lots are not reserved for any document, so they are treated as a single unified lot:

  - Total cost = (15 * 7) + (25 * 8) = 105 BGN + 200 BGN = **305 BGN.**
  - Average cost per unit = 305 BGN / 40 units = **7.63 BGN** per unit.

</details>
