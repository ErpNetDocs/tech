# Excise administrative document: e-ADD export

EU Excise

|**e-ADD tags**|**Excise Product Code**|
| ------------------------------------------------------------ | ------------------- |
|**Header**|
| DocumentNumber|Document.DocumentNumber|
| DocumentDate| Document.DocumentDate |
| IsDelayedReporting |IsDeferredSubmission|
| IsExciseNote | @Exc_Purpose |
| TotalAmountOfExciseDuty |SUM(Lines.ExciseAmount)|
|                                                                                   |
|**PlaceOfIssue**|
| Region | TaxWarehouse.First(Store.@Exc_Region) |
| Municipality | TaxWarehouse.First(Store.@Exc_Municipality) |
| PostCode   |TaxWarehouse.First(Store.ContactMechanism(ContactMechanismType=P))  |
| City | TaxWarehouse.First(Store.@Exc_City)|
| District | TaxWarehouse.First(Store.@Exc_District) |
| Street | TaxWarehouse.First(Store.@Exc_Street)|
| StreetNumber | TaxWarehouse.First(Store.@Exc_StreetNumber) |
|                                                                                    |
|**PersonalDetails**|
| Name | ReportingPerson.PartyName|
| EGN | ReportingPerson.NationalNumber |
|                                                                                    |
| **ConsignorTrader**                 |
| Bulstat   | EnterpriseCompany.Company.RegistrationNumber |
| TraderName | EnterpriseCompany.Company.PartyName |
| TraderExciseNumber | TaxWarehouse.TraderExciseNumber|
| TaxWarehouseExciseNumber|TaxWarehouse.TaxWarehouseExciseNumber|
|                                                                                    |
| **AddressDetails**|
| Country |EnterpriseCompany.Company.@Exc_Country|
| Region|EnterpriseCompany.Company.@Exc_Region|
| Municipality|EnterpriseCompany.Company.@Exc_Municipality|
| PostCode| EnterpriseCompany.Company.ContactMechanism(ContactMechanismType=P)|
| City | EnterpriseCompany.Company.@Exc_City |
| District | EnterpriseCompany.Company.@Exc_District ___ District = Right(@Exc_District,2) |
| Street | EnterpriseCompany.Company.@Exc_Street |
|                                                                                     |
| **ConsigneeTrader** | 
