# Акцизен документ за Електричество



За отчитане на приходите и разходите в данъчния склад се използва формата Акцизен данъчен документ.

https://docs.erp.net/model/entities/Finance.Excise.ExciseAdministrativeDocuments.html

Тук ще опишем как се въвевеждат най често използваните документи за отчитане към митничиските власти.



### 1. Първоначални настройки



1.1. В Категория акцизни продукти в Алгоритъм за изчисление се указва Количество

1.2. Трябва да се дефинира данъчен склад, дори и регистрацията да не е Данъчен склад. В данъчния склад се записват основните дефиниции на регистрираното лице:

- **Акцизен номер на търговеца**
- **Акцизен номер на данъчния склад** - попълва се същия, като на търговеца, ако регистрацията не е за данъчен скрлад

- **Тип на лицето** - това на типа на регистрацията на търговеца.
- **Митническо управление** - това е кода на митническото управление

1.3. Дефитиране на Тип акцизен продукт

- **Акцизен продукт** - Акцизен продукт спорен номенкатурата. Най често това е E12
- **Мерна единица** – Акцизна мерна единиза от номенклатурата на митниците.  Мерна единица с код KWH.
- **Хармонизиран стоков код** – Код по КН от номенклатурата на митниците.
- **Вместимост** - оставя се празно
- **Търговско наименование** - незадължително.

### 2. Изготвяне на e-ADD

##### 2.1. Данни в шапката на Акцизен документ

- **AdministrativeReferenceCode** - Референтен код, който се връща от митниците, когато документът се изнася до тях, или референтен код в получени документи - UCN. Попълва се с колекция на документа след като сме получили този номер след експорта.

- **TaxWarehouse** - Нашият лицензиран Данъчен склад, за което докладваме на митническите органи.

- **Direction = Issue.**  Посоката на движение на стоките. Определя дали стоките влизат или излизат от Данъчния склад.

- **AccrueExciseDuty = True.**  Поле за отметка, което указва, че митническите задължения се начисляват при изписване на стоките от Данъчния склад.

- **IsDeferredSubmission** - Означава дали движението е започнало на хартиен административен документ.

- **OtherParty** - Партито на собствената фирма

- **DeliveryParty** - Празно

- **TransportationCarrier** - Празно

- **TransportationVehicle** - Празно

- **ReportingPerson** - Това е лицет, подаващо документа. 

- **@Exc_Purpose** - Предназначениe на E-ADD. Номенклатура CL200

  



<BR>

------



**2.2. Данни в линиите на Акцизен документ**

- **Product** - Продуктът, който изписваме от данъчния склад. Копира се от складовия документ.
- **Quantity** - Количество в мерна единица от складовия документ. Копира се от генериращия складов документ.
- **QuantityUnit** - Мерна единица от складовия документ. Например брой бутилки, кашони и други. Може да се избира в логистичните документи според необходимостта.
- **QuantityBase** - Кобичество в Базова мерна единица. Основната мерна единица в която се отчитат наличностите в склада. Задава се в дефиницията на продукта. Изчислява се автоматично.
- **ExciseQuantity** - Количество в Акцизната мерна единица. Изчислява се автоматично. 
- **ExciseQuantityUnit** - Акцизна мерна единица. Това е мерната единица, в която се отчитат акцизните продукти пред митническите власти. Определя се от дължавата и зе задава в Тип акцизен продукт. 
- **MeasuringTransaction** - Транзакция за вход или изход на продукт, измерена със специализирано измервателно устройство за цели на акцизното облагане. Зарежда се автоматично при генериране на партидата в складовата разписка.
- **ExciseProduct** - Кодът на Акцизния продукт, дефиниран от данъчните и митническите органи. Той е зададен в типовете на акцизните продукти, които са част от дефиницията на продукта. Зарежда се автоматично при избор на продукта, но може да бъде променен ръчно.
- **ExcisePurposeCode** - Предназначението определя различните цели, признати от органите за определяне на ставката на акциза. Задължително.
- **ExciseAmountBase** - Основата, върху която се изчислява ставката на акциза. Автоматично се изчислява чрез алгоритъм, дефиниран в категориите на акцизните продукти. Категориите на акцизните продукти са част от дефиницията на акцизния продукт.
- **ExciseDutyRate** - Справка към конкретната ставка в таблицата за акцизни ставки ExciseDutyRates, която се определя въз основа на избраните Акцизни Продукти, Предназначение и Акцизни мерни единици.
- **ExciseDutyRateValue** - Стойността на определената ставка на акциза ExciseDutyRate.
- **ExciseAmount** - Изчислената стойност на акциза въз основа на ExciseAmountBase и ExciseDutyRateValue.
- **@Exc_Payment** - Код на  плащането. Задължително.

<BR>

**1.4. Parties**
Полета в избраните субекти - Собствена фирма, Данъчен склад:

- **ContactMechanisms.PostalCode** - Пощенски код.

- **@Exc_Country** – Държава
- **@Exc_Region** – Район
- **@Exc_Municipality** – Община
- **@Exc_City** – Град
- **@Exc_District** – Квартал
- **@Exc_Street** – Улица, Номер



**Субектът на данъчния склад е Складът с най малък Номер на субект измежду складовете в този данъчен склад.**
Тоест задължително трябва да се направи склад, въпреки, че електричеството не се складира.



**1.7. Експорт на e-ADD файл**

​	Експорта на e-ADD файл се прави от WEB панел в Акцизния документ със следния адрес:

​	**{$rooturl}/legal/customs/exciseduties/{Id}**

​	Където /legal e относителният URL на сайта Legal BG. 

​	Необходимо е да има активен Legal BG сайт за да може да се прави експорт на e-ADD файлове.



