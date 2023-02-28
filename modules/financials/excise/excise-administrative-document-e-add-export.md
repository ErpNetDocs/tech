# Excise administrative document: e-ADD export

EU Excise

|**e-ADD tags**                                               |**Excise Product Code**|
| ------------------------------------------------------------ | ------------------- |
|**Header**                                             |
|DocumentNumber                                       | Document.DocumentNumber    |
| DocumentDate             | Document.DocumentDate               |
| IsDelayedReporting                                       |IsDeferredSubmission     |
| IsExciseNote                                                       | @Exc_Purpose  |
| TotalAmountOfExciseDuty |SUM(Lines.ExciseAmount)           |
|                                                                                 |
|**PlaceOfIssue**       |
|Region                                       | TaxWarehouse.First(Store.@Exc_Region)   |
|Municipality                        | TaxWarehouse.First(Store.@Exc_Municipality) |
| PostCode   |TaxWarehouse.First(Store.ContactMechanism(ContactMechanismType=P))  |
| City                  | TaxWarehouse.First(Store.@Exc_City)   |
| District | TaxWarehouse.First(Store.@Exc_District)  |
| Street | TaxWarehouse.First(Store.@Exc_Street)|
| StreetNumber  | TaxWarehouse.First(Store.@Exc_StreetNumber) |
|                                                                                    |
|**PersonalDetails**   |
| Name                                           | ReportingPerson.PartyName           |
| EGN                                           | ReportingPerson.NationalNumber |
|                                             |
| **ConsignorTrader**                 |
| Heavy fuel oil                                               | E470                |
| Products failing within CN codes 2710 11 21, 2710 11 25, 2710 19  29 in bulk commercial movements | E480                |
| Products failing within CN codes 2710 11 to 2710 19 69, not  specified above | E490                |
| Liquefied petroleum gases and other gaseous hydrocarbons (LPG) | E500                |
| Saturated acyclic hydrocarbons                               | E600                |
| Cyclic hydrocarbons                                          | E700                |
| Methanol (methyl alcohol)                                    | E800                |
| Mixture of acyclic hydrocarbons - "FAMAE"                    | E910                |
| Mixture of acyclic hydrocarbons - others                     | E920                |
