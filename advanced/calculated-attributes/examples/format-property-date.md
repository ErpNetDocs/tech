---
items: CalculatedAttributeExamples
---

# Format custom property date

The current example shows how you can format a date which is saved as a custom property value.


```
10:	FORMATSTRING	EXP:20	CONST:yyyy MM dddd		
20:	CONVERT	EXP:30	CONST:System.DateTime		
30:	CONCAT	EXP:40	EXP:50		
40:	SUBSTRING	EXP:100	CONST:0	CONST:4
50:	CONCAT	CONST:-	EXP:60		
60:	CONCAT	EXP:70	EXP:80		
70:	SUBSTRING	EXP:100	CONST:4	CONST:2
80:	CONCAT	CONST:-	EXP:90		
90:	SUBSTRING	EXP:100	CONST:6	CONST:2
100:	FORMATSTRING	ATTRIB	@Property1	CONST	V		

```



Explanation:
<br/>// We assume that the value of the custom poperty is 20200315

- 10: Format the date returned from EXP:20 apllyig the date format type 'yyyy MM dddd' e.g. '2020 03 Sunday'.
- 20: Convert the type of the value returned from EXP:30 to datetime	
- 30: Concatenate the text from EXP:40 to the text from EXP:50 e.g. '2021' + '-03-15'
- 40: Get the first 4 characters from the string from EXP:100 e.g. '2021'
- 50: Concatenate the character '-' to the text from EXP:60 e.g. '-' + '03-15'
- 60: Concatenate the text from EXP:70 to the text from EXP:80 e.g. '09' + '-15'
- 70: Get the first 2 characters from the string from EXP:100, stating from character 4 e.g. '03'
- 80: Concatenate the character '-' to the text from EXP:80 e.g. '-' + '15'
- 90: Get the first 2 characters from the string from EXP:100, stating from character 6 e.g. '15'
- 100: Get the value of custom property "Property1"
