# R28545 UserBusinessRule - Script Text Max Length

Code|R28545
|:----|:----
Entity|UserBusinessRule
Name|ScriptTextMaxLength
Attribute|ScriptText
Layer|Back-End
Events|Commit
Priority|Normal
Modify|NO
Action|Validate that: <br> ScriptText.Length() <= 10000 
Description|The limit of the script which can be entered in<br> a User Business Rule is 10000 characters. This<br> validation is required for protective purposes.
Message|The Script Text attribute exceeds its limit of 10000 characters. <br>Please, shorten the text in the Script Text attribute.
Introduced In Version|2018.1
Revocable|NO
