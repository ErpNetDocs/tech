
# Data Warehouse

Data Warehouse is a large storage of data, accumulated from a wide range of sources within a company and used to guide management decisions.

Data Warehouse is used for reporting and data analysis and is considered a core component of business intelligence. 

Currently, in the @@name platform the following tools are implemented:
- data measures, grouped into data measure groups.
- data values, entered in for the different measures.

Data Measure Groups are accompanying attributes, helping the data to be ordered by the users. The data may also be structured in a hierarchy.

Data Measures are declared for a period. The period may be a Day, Month or a Year. It defines the allowed spread - a +/- percent by which the goal can be missed but still considered achieved.

Data Value is actually a fact. It represents the real value of a Data Measure for a specified date (usually this is the first day of the period of the Data Measure). It also holds a target value and an actual value. 

Data Values support enterprise companies. (for more information see **[Multi-company](https://github.com/ErpNetDocs/tech/blob/master/concepts/multi-company.md)**).

Data Measures and Data Values support custom properties.


The values may be entered on a daily, monthly or yearly basis by the user, an application or other. Actually, they may be entered by different sources at the same time.

Data Warehouse is after that used in the @@name BI. An external BI also may be used.

### Further information:

- **Data Measure Groups Business Rules**
