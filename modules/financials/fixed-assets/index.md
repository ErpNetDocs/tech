# Fixed assets

The Fixed Assets submodule is responsible for managing **the full lifecycle of an enterprise's long-term tangible assets** — from acquisition and valuation to depreciation and retirement. It ensures compliance with accounting and tax regulations by maintaining separate valuation models and automating the periodic calculation of depreciation.

## Structure

Fixed Assets supports key documents used to record asset events and periodic operations required for financial accounting.

### Documents and Operations

| Document / Operation | Purpose |
| :--- | :--- |
| **Acquire and Retire Orders** | Documents used to initiate or record the purchase or disposal (sale/retirement) of a fixed asset. |
| **Asset Transactions** | Used to record basic asset value transactions and opening balances related to fixed assets. |
| **Depreciation Plans** | The planning document that allows users to create and define the anticipated depreciation schedules for a specific period or set of assets. |
| **Depreciations** | The periodic operation document that records the actual calculation and booking of asset wear and tear for a financial period. It is typically generated based on the chosen **Valuation Model**. |

### Definitions

| Definition | Purpose |
| :--- | :--- |
| **Fixed Assets** | The core master record for an individual tangible asset (e.g., a specific piece of machinery, a vehicle). |
| **Asset Groups** | User-defined groupings of assets, typically used for reporting or logical organization within the enterprise. |

### Setup

| Setup | Purpose |
| :--- | :--- |
| **Asset Categories** | Systematically categorizes assets based on their nature and required financial treatment. |
| **Depreciation Methods** | Contains both system-defined and user-defined methods for calculating depreciation expense. |
| **Valuation Models** | Stand for the different valuations an asset can have (e.g., Accounting, Tax, External Financial Reports). All asset transactions are linked to a model. |

- **[Depreciation methods](https://docs.erp.net/tech/modules/financials/fixed-assets/depreciation-methods/index.html)**
