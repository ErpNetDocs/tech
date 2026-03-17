---
items: CalculatedAttributeExamples
---

# Calculate the minute difference between StartTime and EndTime within the hour

With this calculated attribute, you can calculate the difference between the minute components of the StartTime and EndTime attributes. The result is determined by extracting the minute part of each time value, converting it to an integer, and subtracting the StartTime minute from the EndTime minute. If the result is negative, 60 is added so the final value remains in the range from 0 to 59.

You can also use this attribute in a business rule or another formula when you need to work with the minute offset within an hour instead of the full duration between two time values.

```text
5: IIF EXP:70 EXP:90 EXP:10
10: ADD EXP:50 EXP:20
20: MULTIPLY EXP:30 CONST:-1
30: CONVERT EXP:40 CONST:System.Int32
40: FORMATSTRING ATTRIB:StartTime CONST:mm
50: CONVERT EXP:60 CONST:System.Int32
60: FORMATSTRING ATTRIB:EndTime CONST:mm
70: LT EXP:10 CONST:0
90: ADD EXP:10 CONST:60
```

**Explanation:**

5: Conditional result:  
	If EXP:70 is true → return EXP:90  
	Else → return EXP:10   
10: Adds EXP:50 and EXP:20, effectively computing: EndMinute + (−StartMinute) → EndMinute − StartMinute  
20: Multiplies EXP:30 by −1 (negates the StartTime minutes): −StartMinute  
30: Converts EXP:40 (minutes as text) to System.Int32  
40: Formats StartTime with "mm" to extract the minute component as text  
50: Converts EXP:60 (minutes as text) to System.Int32  
60: Formats EndTime with "mm" to extract the minute component as text  
70: Checks whether the minute difference is negative: EXP:10 < 0  
90: If the minute difference is negative, add 60 to wrap it into the 0..59 range: EXP:10 + 60
