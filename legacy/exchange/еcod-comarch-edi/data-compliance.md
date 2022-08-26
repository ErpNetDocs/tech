## Съответствие на данните с ERP.net
### Описание на съответствията между експортните и импортните файлове от една страна и ERP.net от друга

##### 1. Експорт на фактури
 
Следващите тагове се взимат от свързаната Експедиция.

**\<CodeBySeller>11223344\</CodeBySeller>** в секцията /Document-Invoice/Invoice-Parties/Buyer

\<CodeBySeller>\ = General_PartyLocationNumber.LocationNumber WHERE  Logistics_Shipment_Shipment.ShipToPartyContactMechanism.Party = General_PartyLocationNumber.Party And LocationCodingSystem = INT

**\<Name>BUYER COMPANY\</Name>** в секцията /Document-Invoice/Invoice-Header/Delivery

\<Name> = Logistics_Shipment_Shipment.ShipToPartyContactMechanism.Party.. CompanyLocation.Company.PartyName (bg part)

**\<StreetAndNumber>Main Street 1\</StreetAndNumber>** в секцията </Document-Invoice/Invoice-Header/Delivery

\<StreetAndNumber> - Logistics_Shipment_Shipment.ShipToPartyContactMechanism.Name - стринга след първата запетайка.

**\<CityName>Sofia\</CityName>** в секцията </Document-Invoice/Invoice-Header/Delivery

\<CityName> - Logistics_Shipment_Shipment.ShipToPartyContactMechanism.Name - стринга преди първата запетайка.

**\<PostalCode>1112\</PostalCode>** в секцията </Document-Invoice/Invoice-Header/Delivery

\<PostalCode> - Logistics_Shipment_Shipment.ShipToPartyContactMechanism.Party.Area.Code

**\<Country>BG</Country>** в секцията \</Document-Invoice/Invoice-Header/Delivery

\<Country> - Logistics_Shipment_Shipment.ShipToPartyContactMechanism.Party.. CompanyLocation.Company.Country
