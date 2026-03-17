---
items: CalculatedAttributeExamples
---

# Calculate integer hour difference between EndTime and StartTime

With this calculated attribute, you can calculate the integer hour difference between the EndTime and StartTime attributes. The result is determined by the hour values of the two time attributes.

You can also use this attribute in a business rule when you need to fill or compare a value based on the difference in hours between two time attributes.

```text
10: ADD EXP:50 EXP:20
20: MULTIPLY EXP:30 CONST:-1
30: CONVERT EXP:40 CONST:System.Int32
40: FORMATSTRING ATTRIB:StartTime CONST:hh
50: CONVERT EXP:60 CONST:System.Int32
60: FORMATSTRING ATTRIB:EndTime CONST:hh
```

**Explanation:**

10: Adds EXP:50 and EXP:20, effectively computing: EndHour + (−StartHour) → EndHour − StartHour  
20: Multiplies EXP:30 by −1 (negates the StartTime hour): −StartHour  
30: Converts EXP:40 (a formatted string) to `System.Int32` to get an integer hour value  
40: Formats StartTime using the format string `hh` to extract the hour part as text  
50: Converts EXP:60 (a formatted string) to `System.Int32` to get an integer hour value  
60: Formats EndTime using the format string `hh` to extract the hour part as text
