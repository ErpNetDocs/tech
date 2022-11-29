# Currency revaluation algorithm





1. Input data 

   - Document Operation

   - Accounts - accounts in the rows of accounting template of Operation
   - Date of revaluation = Date of the document Operation
   - Currency directory - Currency Directory set in Operation
   - Accounting vouchers

2. Revaluation is made for each currency included in the Currency directory

3. Calculate Balance и BalanceBase for the Date of revaluation for each Account, Currency, Item Key, CostCenter, ProfutCenter and ReferencedDocument.

   1.1. If [CurrencyValuationMethod](https://docs.erp.net/model/entities/Finance.Accounting.Accounts.html#currencyvaluationmethod) <> Balance_Reference_Document.

     Then data is grouped by Account, Currency, Item Key, CostCenter, ProfutCenter. (ReferencedDocument = NULL).

   1.2. If [CurrencyValuationMethod](https://docs.erp.net/model/entities/Finance.Accounting.Accounts.html#currencyvaluationmethod) = Balance_Reference_Document

     Then data is grouped by Account, Currency, Item Key, CostCenter, ProfutCenter and ReferencedDocument.


2. Calculate the Amount of the Exchange difference for the each group in Base Currency.
    **`Amount = RoundAmount(BaseCurrency, Balance * CurrencyDirectoryLine.RateMultiplier / CurrencyDirectoryLine.RateDivisor) - BalanceBase)`**

3. Create Accounting voucher with these differences in BaseCurrency for each group.
    Amount (Currency, Account, ItemKey, CostCenter, ProfitCenterI, ReferencedDocument)
