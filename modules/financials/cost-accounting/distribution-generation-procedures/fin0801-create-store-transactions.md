# FIN0801 Create Store Transactions
The generation procedure generates new Store transactions. Their purpose is to distribute the cost, calculated in the Results table of the Distribution document, in the store transaction lines from the Outputs table. 

https://github.com/ErpNetDocs/model/blob/master/generations/FIN0801.md
## General information
|**Module**|Finance.CostAccounting
|:----|:-----
|**Code**|FIN0801
|**Parent document**|Distribution
|**Sub-document**|Store transactions
|**Full name**|Create store transactions for the distributed amounts
|**Status**|**NEW**
|**Supports Transitional documents**|NO
|**Replaces**|FIN0801
|**Orphan rows**|Ignore<br>
|**Split function**|Output[DistributionResult.OutputLineNo].StoreTransactionLine.StoreTransaction.Store<br> * find the Store of the StoreTransaction of the StoreTransactionLine of the Output with LineNo equal to the DistributionResult.OutputLineNo
|**Introduced in version**|
|**Date of suspension**|**-**
 
## Business Logic
The generation procedure is used to create cost store transactions from Distribution documents. When the Distribution document calculates the cost distribution amounts for all cost types and all cost objects, these amounts are added in the store for the same product as it is in the original store transaction line (all parameters are copied from the original store transaction - like lots, product variants, serial numbers, store bins and measurement units). The cost store transaction has quantities of **0** and LineCost carrying the amount from the Distribution. The new store transaction movement type is always **Receipt**. When created, the document notes are filled with the automatic message of "*Generated for cost distribution purposes.*"

The generation procedure creates a separate document for each store from the Distribution document cost objects. 

The header of the Store transaction is created with the following data:

StoreTransaction.Store = DistributionResult.Output[OutputLineNo == Output.LineNo; Distribution == Output.CostDistribution].StoreTransactionLine.StoreTransaction.Store
StoreTransaction.DocumentDate = Distribution.DocumentDate
StoreTransaction.MovementType = Receipt 
StoreTransaction.ParentStoreOrder = null 
StoreTransaction.CostSource = Document
StoreTransaction.IsScrap = false
StoreTransaction.FromParty = Distribution.EnterpriseCompany.Party
StoreTransaction.ScrapType = null
StoreTransaction.IssuingPerson = null
StoreTransaction.ReceivingPerson = null
StoreTransaction.DocumentCurrency = Distribution.EnterpriseCompany.BaseCurrency
StoreTransaction.ToParty = null
StoreTransaction.DocumentNotes = "Generated for cost distribution purposes."

* *the attributes which are not specified here are filled in as described in* ***Standard Document Attributes***

> [!NOTE]
> The new store transaction is saved only if it has at least one row.
 
# Fulfillments

|**Name**|DistributionResultToStoreTransactionLine
|:----|:----
|**Parent entity**|Distribution Result
|**Child entity**|StoreTransactionLine
|**Parent/Child relationship**|StoreTransactionLine.ParentDocument = DistributionResult.Distribution;<br><br>StoreTransactionLine.ParentLineNo = DistributionResult.LineNo
 
|Fulfillment name|Metric name|Measurement unit|Parent value|Child value|New record
|:----|:----|:-----|:----|:----|:----
| DistributionResultToStoreTransactionLine| DistributedAmountBase|Distribution.EnterpriseCompany.BaseCurrency| DistributionResult.DistributedAmountBase| StoreTransactionLine.LineCost| YES

The *DistributionResultToStoreTransactionLine* fulfilment creates StoreTransactionLines as follows:

StoreTransactionLine.Quantity = 0

StoreTransactionLine.QuantityBase = 0
StoreTransactionLine.Product = DistributionResult.DistributionOutput[LineNo=OutputLineNo].StoreTransactionLine.Product
StoreTransactionLine.OriginalProduct = DistributionResult.DistributionOutput[LineNo=OutputLineNo].StoreTransactionLine.Product

StoreTransactionLine.TransactionTimestamp = DistributionResult.DistributionOutput[LineNo=OutputLineNo].StoreTransactionLine.TransactionTimestamp

StoreTransactionLine.MeasurementUnit = DistributionResult.DistributionOutput[LineNo=OutputLineNo].StoreTransactionLine.MeasurementUnit

StoreTransactionLine.ProductVariant = DistributionResult.DistributionOutput[LineNo=OutputLineNo].StoreTransactionLine.ProductVariant

StoreTransactionLine.SerialNumber = DistributionResult.DistributionOutput[LineNo=OutputLineNo].StoreTransactionLine.SerialNumber

StoreTransactionLine.Lot = DistributionResult.DistributionOutput[LineNo=OutputLineNo].StoreTransactionLine.Lot

StoreTransactionLine.StoreBin = DistributionResult.DistributionOutput[LineNo=OutputLineNo].StoreTransactionLine.StoreBin

StoreTransactionLine.LineCost = REMAINING(DistributedAmountBase)

StoreTransactionLine.LineBaseCost = StoreTransaction.StoreTransactionLine.LineCost

StoreTransactionLine.ParentDocument = Distribution

StoreTransactionLine.ParentLineNo = DistributionResult.LineNo
 
 

