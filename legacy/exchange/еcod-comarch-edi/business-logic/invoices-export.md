## Експорт на фактури

Този тип задачи позволява експорт на Commarch-bg ECOD Invoices xml файлове от ERP.net база данни.

Данните се експортират от документ тип Фактури.

# Алгоритъм за определяне на полетата BuyerILN, SellerILN и InvoiceeILN при експорт на фактури от EnterpriseOne

**Определянето на BuyerILN, SellerILN и InvoiceeILN се прави по следния алгоритъм:**

> **_NOTE:_** Алгоритъм за определяне на полетата BuyerILN, SellerILN и InvoiceeILN при експорт на фактури от EnterpriseOne.  Този алгоритъм се използва, когато е отметната отметката "Използване на Номер на локация на субект". Ако не е отметната се гледат полетата GLN в субектите.

**1.** BuyerILN = Location Number в таблица Gen_Party_Location_Numbers., където Party_Id е фирмата на Клиента указан в полето "Клиент" в във фактурата и Location Coding System = GLN.

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

**3.** InvoiceeILN = Location Number в таблица Gen_Party_Location_Numbers., където Party Id е фирмата на Клиента указан в полето "Клиент" в във фактурата и Location Coding System = GLN.

**4.** DeliveryLocationNumber = Location Number в таблица Gen_Party_Location_Numbers, където:

    Party Id = Към Субект

    Document Id е свързаната експедиция към тази фактура
