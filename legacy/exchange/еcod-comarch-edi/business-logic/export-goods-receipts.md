## Експорт на стокови разписки

Този тип задачи позволява експорт на Commarch-bg ECOD Despatch Advices xml файлове от ERP.net база данни.

Данните се експортират от документ тип Експедиция.

### Алгоритъм за определяне на полетата BuyerILN, SellerILN, DeliveryPointILN и UltimateConsigneeILN при експорт на стокови разписки
> **_NOTE:_** Този алгоритъм се използва, когато е отметната отметката "Използване на Номер на локация на субект". Ако не е отметната се гледат полетата GLN в субектите.

**1.** BuyerILN = Location Number в таблица Gen_Party_Location_Numbers., където Party Id е фирмата на която е обектът указан в полето "Към субект" в експедицията и Location Coding System = GLN.

**2.** SellerILN = Location Number в таблица Gen_Party_Location_Numbers, където:

    2.1. Party Id = От направление / Party_Id

    Partner Location Number = BuyerILN от т.1

    и Location Coding System = GLN.

    2.2. Ако не се намери запис в т.2.1 то

    Party Id = От направление / Party_Id

    Partner Location Number = Null

    и Location Coding System = GLN.

    2.3 Ако не се намери запис в т. 2.2 то

      Party Id = Собствената фирма

    Partner Location Number = BuyerILN от т.1

    и Location Coding System = GLN.

    2.4. Ако не се намери запис в т.2.3 то

    Party Id = Собствената фирма

    Partner Location Number = Null

    и Location Coding System = GLN.

**3.** DeliveryPointILN = Location Number в таблица Gen_Party_Location_Numbers, където:

    Party Id = Към субект

    и Location Coding System е GLN.

**4.** UltimateConsigneeILN = Location Number в таблица Gen_Party_Location_Numbers, където:

    Party Id = Към субект

    и Location Coding System е GLN.
