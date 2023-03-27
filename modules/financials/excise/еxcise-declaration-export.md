# Excise declaration export

The table below lists the sources for the tags of the e-ADD xml file:

|**Excise declaration**|**Source**|
| ------------------------------------------------------------ | ------------------- |
|**Declaration**||
| KindOfDeclaration |EXC00|
| TypeOfDeclaration| EXC002BG |
| IsCorrectionDeclaration|IsCorrectionDeclaration = !(IsNullOrEmptyValue(RefNumberOfCorrectedDeclaration ))|
| RefNumberOfCorrectedDeclaration|RefNumberOfCorrectedDeclaration = ExcDeclarations.@Exc_RefNumberOfCorrectedDeclaration.Value |
| IsDelayedReporting |IF NOT(IsNullOrEmpty(@Exc_RefNumberOfCorrectedDeclaration))   THEN {RefNumberOfCorrectedDeclaration = @Exc_RefNumberOfCorrectedDeclaration.Value; IsCorrectionDeclaration = True}|
|^ ||IF IsNullOrEmpty(@Exc_RefNumberOfCorrectedDeclaration)  THEN  {RefNumberOfCorrectedDeclaration - MISSING; IsCorrectionDeclaration = false}|
|                                                                                   ||
|**PlaceOfIssue**||
| Region | TaxWarehouse.First(Store.@Exc_Region) |
| Municipality | TaxWarehouse.First(Store.@Exc_Municipality) |
| PostCode   |TaxWarehouse.First(Store.ContactMechanism(ContactMechanismType=P))  |
| City | TaxWarehouse.First(Store.@Exc_City)|
| District | TaxWarehouse.First(Store.@Exc_District) |
| Street | TaxWarehouse.First(Store.@Exc_Street)|
| StreetNumber | TaxWarehouse.First(Store.@Exc_StreetNumber) |
|                                                                                    ||
|**PersonalDetails**||
| Name | ReportingPerson.PartyName|
| EGN | ReportingPerson.NationalNumber |
|                                                                                    ||
| **ConsignorTrader**                 ||
| Bulstat   | EnterpriseCompany.Company.RegistrationNumber |
| TraderName | EnterpriseCompany.Company.PartyName |
| TraderExciseNumber | TaxWarehouse.TraderExciseNumber|
| TaxWarehouseExciseNumber|TaxWarehouse.TaxWarehouseExciseNumber|
|                                                                                    ||
| **AddressDetails**||
| Country |EnterpriseCompany.Company.@Exc_Country|
| Region|EnterpriseCompany.Company.@Exc_Region|
| Municipality|EnterpriseCompany.Company.@Exc_Municipality|
| PostCode| EnterpriseCompany.Company.ContactMechanism(ContactMechanismType=P)|
| City | EnterpriseCompany.Company.@Exc_City |
| District | EnterpriseCompany.Company.@Exc_District <br/> District = Right(@Exc_District,2) |
| Street | EnterpriseCompany.Company.@Exc_Street |
|                                                                                     ||
| **ConsigneeTrader** ||
| IsForeigner | If(OtherParty.Company.Country.Code='BG',False,True) |
| IdentifyNumber | OtherParty.Company.RegistrationNumber |
| TraderName | OtherParty.PartyName |
|                                                                                     ||
| **AddressDetails** ||
| Country | OtherParty.@Exc_Country |
| Region | OtherParty.@Exc_Region |
| Municipality | OtherParty.@Exc_Municipality |
| PostCode | OtherParty.ContactMechanism(ContactMechanismType=P) |
| City | OtherParty.@Exc_City |
| District | OtherParty.@Exc_District |
| Street | OtherParty.@Exc_Street |
|                                                                                     ||
| **TransportDetails** ||
| TransportType | TransportationVehicle.TransportationMode.Code |
| VehicleRegNo | TransportationVehicle.Vehicle.VehicleRegistrationNumber |
|                                                                                     ||
| **TransporterTrader** ||
| IsForeigner | If(TransportationCarrier.Supplier.Company.Country.Code='BG',False,True) |
| IdentifyNumber | TransportationCarrier.Supplier.Company.RegistrationNumber |
| TraderName | TransportationCarrier.Supplier.Company.PartyName |
| TransporterCertificateNumber | TransportationCarrier.@Exc_TransporterCertificateNumber |
| CertificateDateOfIssue | TransportationCarrier.@Exc_TransporterCertificateDateOfIssue |
| CertificateExperationDate | TransportationCarrier.@Exc_TransporterCertificateExperationDate |
|                                                                                     ||
| **Driver** ||
| Name | @Exc_Driver.Description |
| EGN | @Exc_Driver.Value |
|                                                                                     ||
| **DeliveryPlaceDetails** ||
| IsOTTGObject | FALSE |
|                                                                                     ||
| **DeliveryPlace** ||
| Country | If(DeliveryParty != Null, DeliveryParty.@Exc_Country, OtherParty.@Exc_Country) |
| Region | If(DeliveryParty != Null, DeliveryParty.@Exc_Region, OtherParty.@Exc_Region) |
| Municipality | If(DeliveryParty != Null, DeliveryParty.@Exc_Municipality, OtherParty.@Exc_Municipality) |
| PostCode | If(DeliveryParty != Null, DeliveryParty.ContactMechanism(ContactMechanismType=P), OtherParty.ContactMechanism(ContactMechanismType=P)) |
| City | If(DeliveryParty != Null, DeliveryParty.@Exc_City, OtherParty.@Exc_City) |
| District | If(DeliveryParty != Null, DeliveryParty.@Exc_District, OtherParty.@Exc_District) |
| Street | If(DeliveryParty != Null, DeliveryParty.@Exc_Street, OtherParty.@Exc_Street) |
|                                                                                     ||
| **eADDGoods** ||
| eADDGood ||
| BrandName | Product.ExciseProductType @Exc_BrandName.Value |
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
| TotalAmountPrice | Quantity\*Product.@Exc_LabelPrice |
| TaxBase | ExciseAmountBase |
| ExciseDuty | ExciseDutyRateValue |
| DutyAmount |ExciseAmount |
| Payment | @Exc_Payment |
| Purpose | ExcisePurposeCode.Code |
|                                                                                      ||
| **MeasureValues**||
| ControlPoint | MeasuringTransaction.MeasuringDeviceCode |
| TransactionNumber | MeasuringTransaction. Transaction number |
| DocumentType | IIF(ExciseAdministrativeDocumentLine.@Exc_InputDocumentTypeLine != NULL AND ExciseAdministrativeDocumentLine.@Exc_InputDocumentTypeLine != "", ExciseAdministrativeDocumentLine.@Exc_InputDocumentTypeLine, ExciseAdministrativeDocument.@Exc_InputDocumentType) |
| DocumentNumber | IIF(ExciseAdministrativeDocumentLine.@Exc_InputDocumentNumberLine != NULL AND ExciseAdministrativeDocumentLine.@Exc_IInputDocumentNumberLine != "", ExciseAdministrativeDocumentLine.@Exc_InputDocumentNumberLine, ExciseAdministrativeDocument.@Exc_InputDocumentNumber) |
|                                                                                      ||



The symbol "." is used to indicate that a field or data type is being referenced.


The symbol "@xxxx" is used to indicate a custom property with the code "xxxx". If no field reference is specified after it, the custom property's value is used.


The symbol "*" denotes multiplication.
