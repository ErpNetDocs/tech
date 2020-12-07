# Period Determination Methods

## From next month to last month

## From current month to last but one month

## By days

Method of calculation

1. The Month quote = Depreciable amount / Int(Month(Depreciation End Date - Depreciation Start Date -1))
2. For the first month: First month Depreciation =  Month quote * ((Number of Days in First month - Depreciation Start Date)/Number of Days in First month)
3. For every next month but last one: Depreciation =  Month quote
4. For the last month: Depreciation = Mont quote - First month Depreciation

Example:

Asset 1 with Usefull life = 6 months and Depreciable amount = 120
Depreciation Plan = 14.01 - 14.07
Mont quote = 120 / 6 months = 20 
First month Depreciation = 20 * ((31-14)/31) = 10.97
For 2,3,4,5 and 6 th month Depreciation = 20
Last month Depreciation = 20 - 10.97 = 9.03
