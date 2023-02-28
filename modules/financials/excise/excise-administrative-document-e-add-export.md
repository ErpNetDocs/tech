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
| IsForeigner | If(OtherParty.Company.Country.Code='BG',False,True) |
| IdentifyNumber | OtherParty.Company.RegistrationNumber |
| TraderName | OtherParty.PartyName |
|                                                                                     |
| **AddressDetails** |
| Country | OtherParty.@Exc_Country |
| Region | OtherParty.@Exc_Region |
| Municipality | OtherParty.@Exc_Municipality |
| PostCode | OtherParty.ContactMechanism(ContactMechanismType=P) |
| City | OtherParty.@Exc_City |
| District | OtherParty.@Exc_District |
| Street | OtherParty.@Exc_Street |
|                                                                                     |
| **TransportDetails** |
| TransportType | TransportationVehicle.TransportationMode.Code |
| VehicleRegNo | TransportationVehicle.Vehicle.VehicleRegistrationNumber |
|                                                                                     |
| **TransporterTrader** |
| IsForeigner | If(TransportationCarrier.Supplier.Company.Country.Code='BG',False,True) |
| IdentifyNumber | TransportationCarrier.Supplier.Company.RegistrationNumber |
| TraderName | TransportationCarrier.Supplier.Company.PartyName |
|                                                                                     |
| **Driver** |
| Name | @Exc_Driver.Description |
| EGN | @Exc_Driver.Value |
|                                                                                     |
| **DeliveryPlaceDetails** |
| IsOTTGObject | FALSE |
|                                                                                     |
| **DeliveryPlace** |
| Country | OtherParty.@Exc_Country |
| Region | OtherParty.@Exc_Region |
| Municipality | OtherParty.@Exc_Municipality |
| PostCode | OtherParty.ContactMechanism(ContactMechanismType=P) |
| City | OtherParty.@Exc_City |
| District | OtherParty.@Exc_District |
| Street | OtherParty.@Exc_Street |
|                                                                                     |
| **eADDGoods** |
| eADDGood |
| BrandName | Product.ExciseProductType@Exc_BrandName.Value |
| TradeMark | Product.ProductName |
| APCode | ExciseProduct.Code |
| CNCode | Product.ExciseProductType.CommodityCode.CommodityCodeField |
| AdditionalCode | Product.ProductCodes. ProductCodeField(Where CodingSystem. Name=”ExciseAdditionalCode”) |
| QuantityOfGoods | ExciseQuantity |
| MissingLabelsCnt | Null |
| OtherMeasure | ExciseQuantityUnit.Code |
| Degree | ExciseAlcoholicStrengt |
| Pieces | Product.ExciseProductType.Capacity |
| NumberOfPackages | Quantity |
| TotalAmountPrice | Quantity*Product.@Exc_LabelPrice |


