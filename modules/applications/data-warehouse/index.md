
# Data warehouse

Data warehouse is a large storage of data coming from a wide range of company sources and used to guide management decisions.

It helps in reporting and data analysis and is considered a core component of business intelligence. 

Currently, in the @@name platform, the following tools are implemented:

- **data measures**, grouped into data measure groups.
- **data values**, entered in for the different measures.

1. Data measure groups are accompanying attributes, allowing data to be ordered by the users and structured in a hierarchy.

Data measures are declared for a **period**. The period may be a day, month or year.</br>
It defines the allowed spread: a +/- percent by which the goal could be missed but still considered achieved.

2. Data value is actually a fact. It represents the real value of a data measure for a specified date. Usually, this is the first day of the period of the data measure. It also holds a target value and an actual value. 

Data values support **enterprise companies** (for more information, see [Multi-company](https://docs.erp.net/tech/concepts/multi-company.html)).

As all entities, Data measures and Data values support **custom properties**, which allows entering additional information.

Values may be entered on a daily, monthly or yearly basis by the user, an application or other. They may also be entered by multiple sources at the same time.

Data warehouse is after that used in the @@name BI or external BI solution.

### Further reference:

- **Data measure groups business rules**
