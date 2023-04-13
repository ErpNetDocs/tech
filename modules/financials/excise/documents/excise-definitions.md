### Excise Definitions

##### Tax Warehouses

Tax Warehouses are a basic nomenclature in the Excise module. It reflects the licensed tax warehouses of the trader. A Tax Warehouse is associated with one or more warehouses from the Inventory module. This way, the movements in these warehouses trigger the creation of excise documents for the tax warehouse.

The following are specified in the definition of Tax Warehouse:

- Tax Warehouse Excise Number - The excise identification number of the tax warehouse issued by the competent authorities.
- Trader Excise Number - The excise identification number of the owner of the Tax Warehouse.
- Customs Office - The customs office to which the warehouse is headed.

Even if goods that do not require a licensed tax warehouse are taken into account, the definition of Tax Warehouse must be present because it specifies the Trader Excise Number.

https://docs.erp.net/model/entities/Finance.Excise.TaxWarehouses.html



##### Excise Purpose Codes

Excise Purpose Codes are used to specify the different purposes recognized by authorities when determining the excise rate. Along with the Excise Product, Purpose Codes play a role in calculating the excise rate based on the Excise Duty Rate table issued by the competent authorities.

https://docs.erp.net/model/entities/Finance.Excise.ExcisePurposeCodes.html



##### Excise Duty Rate

Duty rates are specified by the taxation and customs authorities. They are the basis for the calculation of the excise amount (based on the  calculation algorithm, specified in the Product Category). 

Duty rates are determined based on Excise Products, Excise Purpose Codes, and Excise Measurement Units.

https://docs.erp.net/model/entities/Finance.Excise.ExciseDutyRates.html



##### Excise Product Types

Excise Product Type is a definition that describes the attributes of products related to the excise module. An Excise Product Type can be used in many products if they have the same excise properties.

The main excise attributes are:

- [Category](https://docs.erp.net/model/entities/Finance.Excise.ExciseProductTypes.html#category) - Specifies the excise product category of the excise stamp - alcohol, tobacco, and others.

- [ExciseProduct](https://docs.erp.net/model/entities/Finance.Excise.ExciseProductTypes.html#exciseproduct) - Excise product according to the EU nomenclature for products subject to excise duty. 
- [ExciseMeasurementUnit](https://docs.erp.net/model/entities/Finance.Excise.ExciseProductTypes.html#measurementunit) - The unit of measure in which the product is reported. 
- [CommodityCode](https://docs.erp.net/model/entities/Finance.Excise.ExciseProductTypes.html#commoditycode) - Code from The Combined Nomenclature used within the European Union countries. 
- [AlcoholicStrength](https://docs.erp.net/model/entities/Finance.Excise.ExciseProductTypes.html#alcoholicstrength) - Percentage of pure alcohol used in excise duty reporting. 
- [Capacity](https://docs.erp.net/model/entities/Finance.Excise.ExciseProductTypes.html#capacity) - Package capacity - number of cigarettes or volume of alcohol in liters.
- [ExciseAmountPerStamp](https://docs.erp.net/model/entities/Finance.Excise.ExciseProductTypes.html#exciseamountperstamp) - The excise duty, which is charged with one excise label. 



##### Excise Stamp Operation Types

Excise Stamp Operation Types define the operation with excise stamps and how it reflects on the three summing boxes - Box1 Effect, Box2 Effect, and Box3 Effect. The definition of Excise Stamp Operation Types sets the specific operation to either add the Quantity to the corresponding Box, subtract it, or leave it unchanged. The summing boxes, Box1 Effect, Box2 Effect, and Box3 Effect, indicate the available quantities of excise stamps in the respective reporting centers required by the customs authorities.

https://docs.erp.net/model/entities/Finance.Excise.ExciseStampOperationTypes.html



##### Excise Stamp Lots

The Excise Stamp Lots are a series of stamps that are obtained from customs authorities. When received, the Quantity,  Start Number and End Number, the Batch number, which describes the attributes of the issue by the customs authorities, and the Purchase batch, which provides a unique identifier for each receipt in the tax warehouse, are recorded.

With excise stamp operations, the movement of each batch is tracked in the relevant reporting centers, including the quantity, initial and final number.

https://docs.erp.net/model/entities/Finance.Excise.ExciseStampLots.html



##### Commodity Codes

Contains the approved commodity codes for each period from The Combined  Nomenclature used within the European Union countries. They are used for reporting Intrastat and Excise. 

https://docs.erp.net/model/entities/Finance.Intrastat.CommodityCodes.html