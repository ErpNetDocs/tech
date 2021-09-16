# Forms with Activated Domain Front-End Logic



When a Domain Front-End Logic is activated for a particular form, this means that it is activated for all referent panels in this form which are a part of the [Aggregate](xref:aggregates).

E.i. if it is activated for the Sales Ordes form - it is also activated for panels such as Sales Orders Lines and Payment Plan which are a part of the Sales Order's aggregate, but not for panels such as Document Amounts which are a part of the Document's aggregate.



| **Module**                           |                               |             |
| ------------------------------------ | ----------------------------- | ----------- |
| **Form**                             | **Activated BindDomainLogic** | **Version** |
| **Sales Module**                     |                               |             |
| Customer Types                       | YES                           | 20.1        |
| CustomerCompanyLocations             | YES                           | 20.1        |
| Customers                            | YES                           | 20.1        |
| Customers - Companies                | YES                           | 20.1        |
| Customers - Persons                  | YES                           | 20.1        |
| Dealers                              | YES                           | 20.1        |
| Dealers - Companies                  | YES                           | 20.1        |
| Dealers - Persons                    | YES                           | 20.1        |
| Offers                               | YES                           | 2017.1      |
| Price Lists                          | YES                           | 20.1        |
| Price Types                          | YES                           | 20.1        |
| Sales Orders                         | YES                           | 2017.1      |
| Sales Persons                        | YES                           | 20.1        |
| Deals                                | YES                           | 21.1        |
| Line Discounts                       | YES                           | 21.1        |
| Product Prices                       | YES                           | 21.1        |
| Promotional Packages                 | YES                           | 21.1        |
| **POS Module**                       |                               |             |
| POS Devices                          | YES                           | 20.1        |
| POS Locations                        | YES                           | 20.1        |
| POS Operators                        | YES                           | 20.1        |
| POS Roles                            | YES                           | 20.1        |
| POS Work Terminals                   | YES                           | 20.1        |
| Product Types - Tax Groups           | YES                           | 20.1        |
| **Invoicing Module**                 |                               |             |
| Invoice Orders                       | YES                           | 20.1        |
| Invoices                             | YES                           | 20.1        |
| **Products Module**                  |                               |             |
| Coding Systems                       | YES                           | 20.1        |
| Measurement Categories               | YES                           | 20.1        |
| Measurement Units                    | YES                           | 20.1        |
| Product - Pictures                   | YES                           | 20.1        |
| Product Groups                       | YES                           | 20.1        |
| Product Types                        | YES                           | 20.1        |
| Products                             | YES                           | 20.1        |
| Products - Codes                     | YES                           | 20.1        |
| Products - Dimensions                | YES                           | 20.1        |
| Products - Distribution Channels     | YES                           | 20.1        |
| Products - Variants                  | YES                           | 2017.1      |
| Product Variants - Colors            | YES                           | 21.1        |
| Product Variants - Sizes             | YES                           | 21.1        |
| Product Variants - Styles            | YES                           | 21.1        |
| **Configurator Module**              |                               |             |
| Product Groups                       | YES                           | 20.1        |
| Products                             | YES                           | 20.1        |
| Product - Custom Properties          | NO                            | -           |
| Product Group - Required Properties  | NO                            | -           |
| **Contacts & Tasks Module**          |                               |             |
| Activities                           | YES                           | 20.1        |
| Areas                                | YES                           | 20.1        |
| Call Detail                          | YES                           | 20.1        |
| Companies                            | YES                           | 20.1        |
| Companies - Departments              | YES                           | 20.1        |
| Company EU Configurator              | YES                           | 20.1        |
| Contact Mechanisms                   | YES                           | 20.1        |
| Party - Pictures                     | YES                           | 20.1        |
| Party Relationship Types             | YES                           | 20.1        |
| Party Relationships                  | YES                           | 20.1        |
| Reminders                            | YES                           | 20.1        |
| Resources                            | YES                           | 21.1        |
| Resources - Availability             | YES                           | 20.1        |
| Resources - Resource Instances       | YES                           | 20.1        |
| Resource Groups                      | YES                           | 21.1        |
| Activities - Time Intervals          | NO                            | -           |
| Companies - Divisions                | NO                            | -           |
| Companies - Employees                | NO                            | -           |
| Companies - Locations                | NO                            | -           |
| Parties                              | NO                            | -           |
| Persons                              | NO                            | -           |
| **Marketing Module**                 |                               |             |
| Bonus Programs                       | YES                           | 20.1        |
| Campaingns                           | YES                           | 20.1        |
| Distribution Channels                | YES                           | 20.1        |
| Forecast Items                       | YES                           | 20.1        |
| Marketing Activities                 | YES                           | 20.1        |
| Product Catalogs                     | YES                           | 20.1        |
| Target Groups                        | YES                           | 20.1        |
| **Distribution Module**              |                               |             |
| Customers - Products                 | YES                           | 20.1        |
| Sales Person Groups                  | YES                           | 20.1        |
| Sales Person Targets                 | NO                            | -           |
| Sales Persons                        | NO                            | -           |
| **Pricing Module**                   |                               |             |
| Pricing Models                       | YES                           | 20.1        |
| Products                             | YES                           | 20.1        |
| Types                                | NO                            | -           |
| **Shipment Module**                  |                               |             |
| Shipment Orders                      | YES                           | 20.1        |
| Shipments                            | YES                           | 20.1        |
| **Inventory Management Module**      |                               |             |
| Lots                                 | YES                           | 20.1        |
| Products - Default Store Bins        | YES                           | 20.1        |
| Products - Valuation Groups          | YES                           | 20.1        |
| Scrap Types                          | YES                           | 20.1        |
| Serial Numbers                       | YES                           | 20.1        |
| Store Bins                           | YES                           | 20.1        |
| Store Groups                         | YES                           | 20.1        |
| Store Orders                         | YES                           | 20.1        |
| Stores                               | YES                           | 20.1        |
| Transactions                         | YES                           | 20.1        |
| Cost Corrections                     | YES                           | 21.1        |
| Reconciliations                      | NO                            | -           |
| Transfer Orders                      | NO                            | -           |
| **Logistics Planning Module**        |                               |             |
| Product Supply                       | YES                           | 21.1        |
| **Procurement Module**               |                               |             |
| Receiving Orders                     | YES                           | 20.1        |
| Suppliers                            | YES                           | 20.1        |
| Suppliers - Companies                | YES                           | 20.1        |
| Suppliers - Persons                  | YES                           | 20.1        |
| Purchase Control Documents           | YES                           | 21.1        |
| Purchase Operation Types             | YES                           | 21.1        |
| Purchase Orders                      | NO                            | -           |
| Purchase Price Lists                 | YES                           | 21.1        |
| Purchase Product Prices              | YES                           | 21.1        |
| Requisitions                         | NO                            | -           |
| Supplier Types                       | YES                           | 21.1        |
| **Products and Technologies Module** |                               |             |
| Products                             | YES                           | 20.1        |
| Principal Recipies                   | YES                           | 21.1        |
| Recipies                             | YES                           | 2015        |
| **Production Planning Module**       |                               |             |
| Product Supply                       | NO                            | -           |
| **Resources Module**                 |                               |             |
| Function Groups                      | YES                           | 21.1        |
| Functions                            | YES                           | 21.1        |
| Operation Groups                     | YES                           | 21.1        |
| Operations                           | YES                           | 21.1        |
| Resource Groups                      | YES                           | 21.1        |
| Resources                            | YES                           | 21.1        |
| Workgroups                           | YES                           | 21.1        |
| Workgroups - Resources               | YES                           | 21.1        |
| Work Schedules                       | YES                           | 21.1        |
| **Shop Floor Module**                |                               |             |
| Consumption Orders                   | NO                            | -           |
| Output Orders                        | YES                           | 21.1        |
| Work Orders                          | YES                           | 21.1        |
| **Projects Management Module**       |                               |             |
| Project Tasks                        | NO                            | -           |
| Projects                             | NO                            | -           |
| Projects - Risks                     | YES                           | 21.1        |
| **Projects Budgeting Module**        |                               |             |
| Resources                            | YES                           | 21.1        |
| Resource Groups                      | YES                           | 21.1        |
| Gen_Resources - Resource Instances   | YES                           | 20.1        |
| Resources - Availability             | YES                           | 20.1        |
| Product Variants                     | YES                           | 21.1        |
| **Projects Executuion Module**       |                               |             |
| Work Reports                         | YES                           | 21.1        |
| **Projects Setup Module**            |                               |             |
| Project Types                        | YES                           | 21.1        |
| Project Types - Participants Roles   | YES                           | 21.1        |
| Project Types - Work Elements        | YES                           | 21.1        |
| Project Types - Work Types           | YES                           | 21.1        |
| Task Types                           | YES                           | 21.1        |
| **Payments Module**                  |                               |             |
| Bulk Payment Orders                  | YES                           | 20.1        |
| Parties - Bank Accounts              | YES                           | 20.1        |
| Payment Accounts                     | YES                           | 20.1        |
| Payment Orders                       | YES                           | 20.1        |
| Payment Reasons                      | YES                           | 20.1        |
| Payment Slips                        | YES                           | 20.1        |
| Payment Transfers                    | YES                           | 20.1        |
| Payment Types                        | YES                           | 20.1        |
| Payment Transactions                 | NO                            | -           |
| **Expenses Module**                  |                               |             |
| Supliers                             | YES                           | 20.1        |
| Supliers - Companies                 | YES                           | 20.1        |
| Supliers - Persons                   | YES                           | 20.1        |
| Purchase Invoice                     | NO                            | -           |
| **Accounting Module**                |                               |             |
| Account Groups                       | NO                            | -           |
| Accounts                             | NO                            | -           |
| Cost Centers                         | NO                            | -           |
| Operations                           | NO                            | -           |
| Profit Centers                       | NO                            | -           |
| Templates                            | NO                            | -           |
| Vouchers                             | NO                            | -           |
| **Cost Accounting Module**           |                               |             |
| Cost Distributions                   | NO                            | -           |
| Cost Types                           | NO                            | -           |
| Financial Statements                 | NO                            | -           |
| Finanse Analisys Module              | NO                            | -           |
| **VAT Module**                       |                               |             |
| Deal Types                           | YES                           | 21.1        |
| Declaring Person                     | NO                            | -           |
| Document Type VAT Codes              | NO                            | -           |
| Entries                              | NO                            | -           |
| VAT Declarations                     | NO                            | -           |
| **Intrastat Module**                 |                               |             |
| Intrastat Declarations               | YES                           | 21.1        |
| **Fixed Assets Module**              |                               |             |
| Acquire and Retire Orders            | YES                           | 21.1        |
| Asset Categories                     | YES                           | 21.1        |
| Asset Groups                         | YES                           | 21.1        |
| Asset Transactions                   | NO                            | -           |
| Assets                               | YES                           | 21.1        |
| Depreciation Methods                 | YES                           | 21.1        |
| Depreciation Plans                   | YES                           | 21.1        |
| Depreciations                        | YES                           | 21.1        |
| Valuation Methods                    | YES                           | 21.1        |
| **Lease-Out Management Module**      |                               |             |
| Asset Groups                         | YES                           | 21.1        |
| Asset Types - Consumables            | YES                           | 21.1        |
| Asset Types - Properties             | YES                           | 21.1        |
| Assets                               | NO                            | -           |
| Assets - Consumables                 | YES                           | 21.1        |
| Assets Types                         | YES                           | 21.1        |
| **Service Module**                   |                               |             |
| Service Activities                   | YES                           | 21.1-       |
| Service Agreements                   | YES                           | 21.1        |
| Service Object Types                 | YES                           | 21.1        |
| Service Objects                      | YES                           | 21.1        |
| Service Orders                       | YES                           | 21.1        |
| Service Types                        | YES                           | 21.1        |
| Services                             | YES                           | 21.1        |
| Services - Ivoicing                  | YES                           | 21.1        |
| **Vehicles Module**                  |                               |             |
| Crews                                | YES                           | 21.1        |
| Equipment Types                      | YES                           | 21.1        |
| Map Points                           | YES                           | 21.1        |
| Trips                                | YES                           | 21.1        |
| Vehicle Equipment                    | YES                           | 21.1        |
| Vehicle Sets                         | YES                           | 21.1        |
| Vehicles                             | YES                           | 21.1        |
| **Mail Module**                      |                               |             |
| Mail Messages                        | NO                            | -           |
| Mailboxes                            | NO                            | -           |
| **Data Warehouse Module**            |                               |             |
| Data Measures                        | NO                            | -           |
| Data Measures Groups                 | NO                            | -           |
| Data Values                          | NO                            | -           |
| **Personal Data (GDPR) Module**      |                               |             |
| Personal Data Management Processes   | YES                           | 21.1        |
| Processing Consents                  | YES                           | 21.1        |
| Rights Requests                      | YES                           | 21.1        |
| **Asset Maintanance Module**         |                               |             |
| Maintenance Orders                   | YES                           | 21.1        |
| Maintenance Types Groups             | YES                           | 21.1        |
| Maintenance Types                    | YES                           | 21.1        |
| Managed Asset Groups                 | YES                           | 21.1        |
| Managed Asset Types                  | YES                           | 21.1        |
| Managed Assets                       | YES                           | 21.1        |
| Service Centers                      | YES                           | 21.1        |
| Tracked Parameters                   | YES                           | 21.1        |
| **General**                          |                               |             |
| Administrative Regions               | YES                           | 21.1        |
| Countries                            | YES                           | 21.1        |
| Currencies                           | YES                           | 21.1        |
| Currency Directories                 | NO                            | -           |
| Custom Properties                    | YES                           | 21.1        |
| Custom Properties Categories         | YES                           | 21.1        |
| Enterprise Companies                 | NO                            | -           |
| **Communities**                      |                               |             |
| Notification Settings                | YES                           | 21.1        |
| Notifications                        | YES                           | 21.1        |
| **Document Model**                   |                               |             |
| Document Amount Types                | YES                           | 21.1        |
| Document Types - Amounts             | NO                            | -           |
| Document Types                       | YES                           | 21.1        |
| Document Types - Security Conditions | NO                            | -           |
| Printouts                            | NO                            | -           |
| Printouts - Layouts                  | NO                            | -           |
| Processes                            | NO                            | -           |
| Routes                               | NO                            | -           |
| Sales Orders - Default Payment Plans | YES                           | 21.1        |
| Sequence Generators                  | NO                            | -           |
| Sequences                            | NO                            | -           |
| **Business Rules**                   |                               |             |
| Calculated Attributes                | YES                           | 2018.1      |
| User Business Rules                  | YES                           | 2018.1      |
| **Business Processes**               |                               |             |
| Business Processes                   | YES                           | 21.1        |
| Process Connections                  | NO                            | -           |
| Process Elements                     | NO                            | -           |
| Process Groups                       | YES                           | 21.1        |
| Process Instance                     | YES                           | 21.1        |
| Process Lanes                        | YES                           | 21.1        |
| **Security**                         |                               |             |
| Access Keys                          | NO                            | -           |
| Audit Log Entries                    | YES                           | 21.1        |
| Column Permissions                   | YES                           | 21.1        |
| Domains                              | NO                            | -           |
| Entities                             | NO                            | -           |
| Groups                               | NO                            | -           |
| Roles                                | NO                            | -           |
| Roles - Users                        | NO                            | -           |
| Trusted Applications                 | NO                            | -           |
| User Groups                          | NO                            | -           |
| Users                                | NO                            | -           |
| **Tools**                            |                               |             |
| Data Sources                         | NO                            | -           |
| Document Jobs                        | NO                            | -           |
| External Applications                | NO                            | -           |
| Jobs                                 | NO                            | -           |
| Reports                              | NO                            | -           |
| Translations                         | YES                           | 21.1        |
| Web Hosts                            | NO                            | -           |
| Web Sites                            | NO                            | -           |
