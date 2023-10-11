# Forms with activated domain front-end logic

When a domain front-end logic is activated for a particular form, this means that it is activated for all referent panels in this form which are a part of the [aggregate](xref:aggregates).

E.i. if it is activated for the sales ordes form - it is also activated for panels such as Sales orders lines and Payment plan which are a part of the sales order's aggregate, but not for panels such as Document amounts which are a part of the document's aggregate.



| **Module**                           |                               |             |
| ------------------------------------ | ----------------------------- | ----------- |
| **Form**                             | **Activated BindDomainLogic** | **Version** |
| **Sales module**                     |                               |             |
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
| Deals                                | YES                           | 22.1        |
| Line Discounts                       | YES                           | 22.1        |
| Product Prices                       | YES                           | 22.1        |
| Promotional Packages                 | YES                           | 22.1        |
| **POS module**                       |                               |             |
| POS Devices                          | YES                           | 20.1        |
| POS Locations                        | YES                           | 20.1        |
| POS Operators                        | YES                           | 20.1        |
| POS Roles                            | YES                           | 20.1        |
| POS Work Terminals                   | YES                           | 20.1        |
| Product Types - Tax Groups           | YES                           | 20.1        |
| **Invoicing module**                 |                               |             |
| Invoice Orders                       | YES                           | 20.1        |
| Invoices                             | YES                           | 20.1        |
| **Products module**                  |                               |             |
| Coding Systems                       | YES                           | 20.1        |
| Measurement Categories               | YES                           | 20.1        |
| Measurement Units                    | YES                           | 20.1        |
| Product - Pictures                   | YES                           | 20.1        |
| Product Groups                       | YES                           | 20.1        |
| Product Types                        | YES                           | 20.1        |
| Products                             | YES                           | 20.1        |
| Products - Codes                     | YES                           | 20.1        |
| Products - Dimensions                | YES                           | 20.1        |
| Products - Distribution channels     | YES                           | 20.1        |
| Products - Variants                  | YES                           | 2017.1      |
| Product variants - Colors            | YES                           | 22.1        |
| Product variants - Sizes             | YES                           | 22.1        |
| Product variants - Styles            | YES                           | 22.1        |
| **Configurator module**              |                               |             |
| Product Groups                       | YES                           | 20.1        |
| Products                             | YES                           | 20.1        |
| Product group - Required properties  | YES                           |             |
| Product - Custom properties          | YES                           |             |
| **Contacts & Tasks module**          |                               |             |
| Activities                           | YES                           | 20.1        |
| ActivityParticipants                 | YES                           | 22.1        |
| Areas                                | YES                           | 20.1        |
| Call detail                          | YES                           | 20.1        |
| Companies                            | YES                           | 20.1        |
| Companies - Departments              | YES                           | 20.1        |
| Company EU configurator              | YES                           | 20.1        |
| Contact Mechanisms                   | YES                           | 20.1        |
| Party - Pictures                     | YES                           | 20.1        |
| Party Relationship Types             | YES                           | 20.1        |
| Party Relationships                  | YES                           | 20.1        |
| Reminders                            | YES                           | 20.1        |
| Resources                            | YES                           | 22.1        |
| Resources - Availability             | YES                           | 20.1        |
| Resources - Resource instances       | YES                           | 20.1        |
| Resource Groups                      | YES                           | 22.1        |
| Activities - Time intervals          | YES                           | 22.1        |
| Companies - Divisions                | YES                           | 22.1        |
| Companies - Employees                | YES                           | 22.1        |
| Companies - Locations                | YES                           | 22.1        |
| Parties                              | YES                           | 22.1        |
| Persons                              | YES                           | 22.1        |
| **Marketing module**                 |                               |             |
| Bonus Programs                       | YES                           | 20.1        |
| Campaingns                           | YES                           | 20.1        |
| Distribution Channels                | YES                           | 20.1        |
| Forecast Items                       | YES                           | 20.1        |
| Marketing Activities                 | YES                           | 20.1        |
| Product Catalogs                     | YES                           | 20.1        |
| Target Groups                        | YES                           | 20.1        |
| **Distribution module**              |                               |             |
| Customers - Products                 | YES                           | 20.1        |
| Sales Person Groups                  | YES                           | 20.1        |
| Sales Person Targets                 | YES                           | 22.1        |
| Sales Persons                        | YES                           | 20.1        |
| **Pricing module**                   |                               |             |
| Pricing Models                       | YES                           | 20.1        |
| Products                             | YES                           | 20.1        |
| Types                                | YES                           |             |
| **Shipment module**                  |                               |             |
| Shipment Orders                      | YES                           | 20.1        |
| Shipments                            | YES                           | 20.1        |
| **Inventory Management module**      |                               |             |
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
| Cost Corrections                     | YES                           | 22.1        |
| Reconciliations                      | YES                           | 22.1        |
| Transfer Orders                      | YES                           | 22.1        |
| **Logistics Planning module**        |                               |             |
| Product Supply                       | YES                           | 22.1        |
| **Procurement module**               |                               |             |
| Receiving Orders                     | YES                           | 20.1        |
| Suppliers                            | YES                           | 20.1        |
| Suppliers - Companies                | YES                           | 20.1        |
| Suppliers - Persons                  | YES                           | 20.1        |
| Purchase Control Documents           | YES                           | 22.1        |
| Purchase Operation Types             | YES                           | 22.1        |
| Purchase Orders                      | YES                           | 22.1        |
| Purchase Price Lists                 | YES                           | 22.1        |
| Purchase Product Prices              | YES                           | 22.1        |
| Requisitions                         | YES                           | 22.1        |
| Supplier Types                       | YES                           | 22.1        |
| **Products and Technologies module** |                               |             |
| Products                             | YES                           | 20.1        |
| Principal Recipies                   | YES                           | 22.1        |
| Recipies                             | YES                           | 2015        |
| **Production Planning module**       |                               |             |
| Product Supply                       | YES                           | 22.1        |
| **Resources module**                 |                               |             |
| Function Groups                      | YES                           | 22.1        |
| Functions                            | YES                           | 22.1        |
| Operation Groups                     | YES                           | 22.1        |
| Operations                           | YES                           | 22.1        |
| Resource Groups                      | YES                           | 22.1        |
| Resources                            | YES                           | 22.1        |
| Workgroups                           | YES                           | 22.1        |
| Workgroups - Resources               | YES                           | 22.1        |
| Work Schedules                       | YES                           | 22.1        |
| **Shop Floor module**                |                               |             |
| Consumption Orders                   | YES                           | 22.1        |
| Output Orders                        | YES                           | 22.1        |
| Work Orders                          | YES                           | 22.1        |
| **Projects Management module**       |                               |             |
| Project Tasks                        | YES                           | 22.1        |
| Projects                             | YES                           | 22.1        |
| Projects - Risks                     | YES                           | 22.1        |
| **Projects Budgeting module**        |                               |             |
| Resources                            | YES                           | 22.1        |
| Resource Groups                      | YES                           | 22.1        |
| Gen_Resources - Resource Instances   | YES                           | 20.1        |
| Resources - Availability             | YES                           | 20.1        |
| Product Variants                     | YES                           | 22.1        |
| **Projects Executuion module**       |                               |             |
| Work Reports                         | YES                           | 22.1        |
| **Projects Setup module**            |                               |             |
| Project Types                        | YES                           | 22.1        |
| Project Types - Participants Roles   | YES                           | 22.1        |
| Project Types - Work Elements        | YES                           | 22.1        |
| Project Types - Work Types           | YES                           | 22.1        |
| Task Types                           | YES                           | 22.1        |
| **Payments module**                  |                               |             |
| Bulk Payment Orders                  | YES                           | 20.1        |
| Parties - Bank Accounts              | YES                           | 20.1        |
| Payment Accounts                     | YES                           | 20.1        |
| Payment Orders                       | YES                           | 20.1        |
| Payment Reasons                      | YES                           | 20.1        |
| Payment Slips                        | YES                           | 20.1        |
| Payment Transfers                    | YES                           | 20.1        |
| Payment Types                        | YES                           | 20.1        |
| Payment Transactions                 | YES                           | 22.1        |
| **Expenses module**                  |                               |             |
| Supliers                             | YES                           | 20.1        |
| Supliers - Companies                 | YES                           | 20.1        |
| Supliers - Persons                   | YES                           | 20.1        |
| Purchase Invoice                     | YES                           | 22.1        |
| **Accounting module**                |                               |             |
| Account Groups                       | YES                           |             |
| Accounts                             | YES                           | 22.1        |
| Cost Centers                         | YES                           |             |
| Operations                           | YES                           |             |
| Profit Centers                       | YES                           |             |
| Templates                            | YES                           | 22.1        |
| Vouchers                             | NO                            | -           |
| **Cost Accounting module**           |                               |             |
| Cost Distributions                   | YES                           |             |
| Cost Types                           | YES                           |             |
| Financial Statements                 | YES                           |             |
| **VAT module**                       |                               |             |
| Deal Types                           | YES                           | 22.1        |
| Declaring Person                     | YES                           | 22.1        |
| Document Type VAT Codes              | YES                           |             |
| Entries                              | YES                           | 22.1        |
| VAT Declarations                     | YES                           |             |
| **Intrastat module**                 |                               |             |
| Intrastat Declarations               | YES                           | 22.1        |
| **Fixed Assets module**              |                               |             |
| Acquire and Retire Orders            | YES                           | 22.1        |
| Asset Categories                     | YES                           | 22.1        |
| Asset Groups                         | YES                           | 22.1        |
| Asset Transactions                   | YES                           | 22.1        |
| Assets                               | YES                           | 22.1        |
| Depreciation Methods                 | YES                           | 22.1        |
| Depreciation Plans                   | YES                           | 22.1        |
| Depreciations                        | YES                           | 22.1        |
| Valuation Methods                    | YES                           | 22.1        |
| **Lease-Out Management module**      |                               |             |
| Asset Groups                         | YES                           | 22.1        |
| Asset Types - Consumables            | YES                           | 22.1        |
| Asset Types - Properties             | YES                           | 22.1        |
| Assets                               | YES                           | 22.1        |
| Assets - Consumables                 | YES                           | 22.1        |
| Assets Types                         | YES                           | 22.1        |
| **Service module**                   |                               |             |
| Service Activities                   | YES                           | 22.1        |
| Service Agreements                   | YES                           | 22.1        |
| Service Object Types                 | YES                           | 22.1        |
| Service Objects                      | YES                           | 22.1        |
| Service Orders                       | YES                           | 22.1        |
| Service Types                        | YES                           | 22.1        |
| Services                             | YES                           | 22.1        |
| Services - Ivoicing                  | YES                           | 22.1        |
| **Vehicles module**                  |                               |             |
| Crews                                | YES                           | 22.1        |
| Equipment Types                      | YES                           | 22.1        |
| Map Points                           | YES                           | 22.1        |
| Trips                                | YES                           | 22.1        |
| Vehicle Equipment                    | YES                           | 22.1        |
| Vehicle Sets                         | YES                           | 22.1        |
| Vehicles                             | YES                           | 22.1        |
| **Mail module**                      |                               |             |
| Mail Messages                        | YES                           | 22.1        |
| Mailboxes                            | YES                           | 22.1        |
| **Data Warehouse module**            |                               |             |
| Data Measures                        | YES                           |             |
| Data Measures Groups                 | YES                           |             |
| Data Values                          | YES                           |             |
| **Personal Data (GDPR) module**      |                               |             |
| Personal Data Management Processes   | YES                           | 22.1        |
| Processing Consents                  | YES                           | 22.1        |
| Rights Requests                      | YES                           | 22.1        |
| **Asset Maintenance module**         |                               |             |
| Maintenance Orders                   | YES                           | 22.1        |
| Maintenance Types Groups             | YES                           | 22.1        |
| Maintenance Types                    | YES                           | 22.1        |
| Managed Asset Groups                 | YES                           | 22.1        |
| Managed Asset Types                  | YES                           | 22.1        |
| Managed Assets                       | YES                           | 22.1        |
| Service Centers                      | YES                           | 22.1        |
| Tracked Parameters                   | YES                           | 22.1        |
| **General**                          |                               |             |
| Administrative Regions               | YES                           | 22.1        |
| Countries                            | YES                           | 22.1        |
| Currencies                           | YES                           | 22.1        |
| Currency Directories                 | YES                           |             |
| Custom Properties                    | YES                           | 22.1        |
| Custom Properties Categories         | YES                           | 22.1        |
| Enterprise Companies                 | YES                           | 22.1        |
| **Communities**                      |                               |             |
| Notification Settings                | YES                           | 22.1        |
| Notifications                        | YES                           | 22.1        |
| **Document Model**                   |                               |             |
| Document Amount Types                | YES                           | 22.1        |
| Document Types - Amounts             | YES                           |             |
| Document Types                       | YES                           | 22.1        |
| Document Types - Security Conditions | YES                           |             |
| Printouts                            | YES                           |             |
| Printouts - Layouts                  | YES                           | 22.1        |
| Processes                            | YES                           | 22.1        |
| Routes                               | YES                           | 22.1        |
| Sales Orders - Default Payment Plans | YES                           | 22.1        |
| Sequence Generators                  | YES                           |             |
| Sequences                            | YES                           |             |
| **Business Rules**                   |                               |             |
| Calculated Attributes                | YES                           | 2018.1      |
| User Business Rules                  | YES                           | 2018.1      |
| **Business Processes**               |                               |             |
| Business Processes                   | YES                           | 22.1        |
| Process Elements                     | YES                           |             |
| Process Groups                       | YES                           | 22.1        |
| Process Instance                     | YES                           | 22.1        |
| Process Lanes                        | YES                           | 22.1        |
| **Security**                         |                               |             |
| Access Keys                          | YES                           |             |
| Audit Log Entries                    | YES                           | 22.1        |
| Column Permissions                   | YES                           | 22.1        |
| Domains                              | YES                           |             |
| Entities                             | YES                           |             |
| Groups                               | YES                           |             |
| Roles                                | YES                           |             |
| Roles - Users                        | YES                           |             |
| Trusted Applications                 | YES                           |             |
| User Groups                          | YES                           |             |
| Users                                | YES                           |             |
| **Tools**                            |                               |             |
| Data Sources                         | YES                           | 22.1        |
| Document Jobs                        | YES                           |             |
| External Applications                | YES                           |             |
| Jobs                                 | YES                           |             |
| Reports                              | YES                           | 22.1        |
| Translations                         | YES                           | 22.1        |
| Web Hosts                            | YES                           |             |
| Web Sites                            | YES                           |             |
