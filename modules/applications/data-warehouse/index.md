
# Data Warehouse

Data Warehouse is a large storage of data coming from a wide range of company sources and used to guide management decisions.

It helps in reporting and data analysis and is considered a core component of business intelligence. 

Currently, in the @@name platform, the following tools are implemented:

- **data measures**, grouped into data measure groups.
- **data values**, entered in for the different measures.

1. Data Measure Groups are accompanying attributes, allowing data to be ordered by the users and structured in a hierarchy.

Data Measures are declared for a **period**. The period may be a day, month or year.</br>
It defines the allowed spread: a +/- percent by which the goal could be missed but still considered achieved.

2. Data Value is actually a fact. It represents the real value of a data measure for a specified date. Usually, this is the first day of the period of the data measure. It also holds a target value and an actual value. 

Data Values support **enterprise companies** (for more information, see [Multi-company](https://github.com/ErpNetDocs/tech/blob/master/concepts/multi-company.md)).

Together, Data Measures and Data Values support **custom properties**.

Values may be entered on a daily, monthly or yearly basis by the user, an application or other. They may also be entered by multiple sources at the same time.

Data Warehouse is after that used in the @@name BI. An external BI also may be used.

### Further reference:

- **Data Measure Groups Business Rules**
