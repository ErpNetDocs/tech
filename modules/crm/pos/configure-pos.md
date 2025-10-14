# Configuring the POS submodule

In order for POS to work correctly in @@name, initial settings are required.

### Define a POS location

A POS location defines a given **Enterpise Company Location** as a POS object. The Enterpise Company Location must be specified in advance. 

After determining the POS location, you can proceed to define POS operators and terminals for it.

### Define a POS terminal

Each location can have one or more **terminals** defined for it. A POS terminal is the place where a sale is registered and where various POS devices can be defined, such as fiscal devices, payment terminals, scales, and others.

One POS device can be specified by default and it will be loaded when creating a new sale on this terminal.

### Define a POS device

POS devices are defined for a specific POS terminal.

1. For enterprise companies working with **EnterpriseOne POS**, it is necessary to specify **"Applicable legislation" = "Bulgaria"**

   ![mceclip0.png](pictures/mceclip0.png)

2. You need to define a corresponding **POS location** for each branch that is a commercial entity.

   ![mceclip1.png](pictures/mceclip1.png)

   Once a POS location is set, it **cannot** be deleted or changed. It can only be **deactivated**.

3. For terminals, where necessary, fiscal devices are defined:

   ![mceclip2.png](pictures/mceclip2.png)

- **Device type**: Fiscal printer
- **Registration number**: Registration number of the fiscal printer - in capital letters, since some devices require strictly capital letters.
- **Communication protocol**: FP
- **The fiscal device email address** is set in the format: "http://Address:8001/printers/Printer Id".
- **The library** can be downloaded from **[here](https://github.com/erpnet/ErpNet.FP)**.

### Define a POS operator

In the definition of POS operators, a **user** who is associated with a person must be specified.

By default, the numbering of POS operators starts from **0001** for each location. However, if it is necessary to access fiscal devices from other locations, the operator numbers must be made unique within the enterprise company.

### Define POS roles

It is necessary to define **POS roles** - for example, Manager or Storekeeper.

## Additional configurations

1. A **POS series** must be defined for each fiscal device - a 7-digit number starting from the UNP.

   Example: 0000001.
   
   ![mceclip3.png](pictures/mceclip3.png)

2. A **tax group** must be specified in the product type definitions. If not specified, **tax group 2** is taken by default.

   ![mceclip4.png](pictures/mceclip4.png)

   The correspondence with the groups in fiscal devices in Bulgaria is:
    
   - Group A – Group 1
   - Group B – Group 2
   - Group C – Group 3
   - Group C – Group 4

3. In the payment methods that require printing of the fiscal device, "**Requires fiscal receipt**" and "**System payment method**" must be checked.

   ![mceclip5.png](pictures/mceclip5.png)

   Currently, the supported one-time payment methods for printing of a fiscal device are **In cash**, **By card**, and **By check**

   This setting is **one-time** and **cannot** be changed later.
    
4. For the return document type, in the sales settings, check **"Allowed directions" = "Sales return"**. This is the way by which it is recognized if a sale is a return or not.

5. For the NRA reports, the following preliminary settings must be made:

- Set up an **ID site**
- Set up a **Legal_BG site**
- Create an **external user** in the ID site - achieved through the site interface.
- Give this user access to **System rights** / Access to **reports in Legal_BG**
- Give the user rights to the enterprise company
- For reports inside the system, another **internal user** must be created with the appropriate rights - preferably to all modules, without Admin privileges or the right to edit documents.
    
Then:

1. Install **"EnterpriseOne POS"**.

   Your database must have a license to work with EnterpriseOne POS.

2. If you want to print from the Sales form, all documents in the document flow must be generated as **Released**. Otherwise, after printing, the program will terminate the flow.

   In the document flow, the generations of invoice orders and accounting vouchers from store transactions as **Next Documents** so they can remain Released upon completion of the flow. 

   This will allow for a correction of the warehouse cost and the creation of invoices subsequently. The generation of an accounting voucher must occur in the Completed status to be re-accounted upon correction.

----

## Настройки за работа с ПОС модула

За да работи коректно **POS модулът** са необходими първоначални настройки.

### Дефиниране на POS Локация

**ПОС локацията** е дефиниция, която определя даден **Enterprise Company Location** като **ПОС обект**. Трябва предварително да е дефиниран самият **Enterprise Company Location**.

След дефиниране на **POS Location** към нея се дефинират **POS Operators** и **POS Terminals**.

### Дефиниране на POS Терминали

Във всяка локация можем да дефинираме един или повече **POS Terminals**.

**ПОС Терминалът** е мястото, където се регистрира продажбата и където се дефинират различните **POS Devices**, които се използват там. Например фискални устройства, платежни терминали, везни и други.

Едно **POS Devices** може да се укаже **по подразбиране** и то се зарежда при създаване на нова продажба на този терминал.

### Дефиниране на POS Устройства

**POS устройствата** се дефинират за конкретен **POS Terminal**.

### Допълнителни стъпки и изисквания

1.  В собствените фирми, които трябва да работят с **EnterpriseOne POS**, е необходимо да се укаже **„Приложимо законодателство“ = „България“**.

   ![mceclip0.png](pictures/mceclip0.png)

2.  Необходимо е за всеки **Филиал**, който е търговски обект, да се дефинира съответна **ПОС Локация**.

   ![mceclip4.png](pictures/mceclip4.png)

    Веднъж зададена, ПОС локацията **не може** да се изтрие или променя. Може само да се **деактивира**.

3.  Необходимо е да се дефинират **ПОС роли** – например **Управител** и **Магазинер**.

4.  За всяка ПОС локация се дефинират **ПОС терминали** и **ПОС оператори**.

    В дефиницията на ПОС операторите трябва да се укаже **потребител**, който задължително е свързан с **лице**.

    По подразбиране номерацията на **ПОС операторите** започва от **0001** за всяка локация. Ако е необходимо обаче да се достъпват **ФУ** от други локации, то номерата на операторите трябва да се направят **уникални** в рамките на собствената фирма.

5.  За терминалите, където е необходимо, се дефинират **Фискални устройства**.

   ![mceclip2.png](pictures/mceclip2.png)

   * **Тип устройство**: Фискален принтер
   * **Регистрационен номер**: Регистрационен номер на **ФУ** – с **главни букви**, тъй като някои устройства изискват точно **главни букви**.
   * **Протокол за връзка**: FP
   * **Електронният адрес** на **ФУ** се задава във формат: `„http://Address:8001/printers/Printer Id“`
   * Самата библиотека може да се свали от **[тук](https://github.com/erpnet/ErpNet.FP)**.

6.  За всяко фискално устройство трябва да се дефинира една **ПОС поредица** – **7-цифрен** номер, от който започва **УНП**.

   Пример: **0000001**.

   ![mceclip3.png](pictures/mceclip3.png)

7.  В дефинициите на типовете продукти трябва да се укаже **данъчна група**.

   ![mceclip4.png](pictures/mceclip4.png)

    Ако не е указана, по подразбиране се взима **данъчна група 2**.

    Съответствието с групите във фискалните устройства в България е:

      * **Група А – Група 1**
      * **Група Б – Група 2**
      * **Група В – Група 3**
      * **Група С – Група 4**

8.  В **начините на плащане**, които изискват печат на ФУ, трябва да се отбележи **„Изисква фискален бон“** и **„Системен начин на плащане“**.

   ![mceclip5.png](pictures/mceclip5.png)

    В момента от еднократните начини на плащане за печат на ФУ се поддържат **В брой**, **Чрез карта** и **С Чек**.

    Настройката е еднократна и **не подлежи** на промяна впоследствие.

9.  В **типа документ за връщане**, в настройки за продажби, да се отбележи **"Разрешени посоки" = "Връщане на продажба"**. Това е критерият, по който се разпознава дали една продажба е връщане или не е.

11. За **справките за НАП** трябва да се направят следните настройки:

      * Да се настрои **ID сайт**
      * Да се настрои **Legal\_BG сайт**
      * Да се създаде **външен потребител** в **ID сайта** – създава се през интерфейса на сайта.
      * Да се дадат права на този потребител до **Системни права / Достъп до справките в Legal\_BG**.
      * Да се дадат права на този потребител до **собствената фирма**.
      * За справките вътре в системата трябва да се създаде друг **вътрешен потребител**, който да има съответните права - най-добре **пълни** до всички модули, **без право за редакция на документи** и **без да е администратор**.

12. Необходимо е да се инсталира **„EnterpriseOne POS“**.

13. Необходимо е базата да има **лиценз** за работа с **EnterpriseOne POS**.

14. Ако ще се печата от **форма Продажба**, трябва всички документи в потока да се генерират **Пуснати**, защото след печат програмата завършва потока.

15. Необходимо е в потока генерациите на **Нареждане за фактуриране от продажба** и **Счетоводна статия от складовата разписка** да се дефинират като **Следващ документ**, за да останат пуснати при завършване на потока. Това ще позволи да се направи **корекция на себестойност на склада** и **създаване на фактури** впоследствие. Съответно генерацията на счетоводна статия трябва да се случва на статус **Завършен**, за да се преосчетоводи при корекция.
