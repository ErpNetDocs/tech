# R28545 Script text max length

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
Description|The limit of the script which can be entered in<br> a user business rule is 10000 characters. This<br> validation is required for protective purposes.
Message|The Script text attribute exceeds its limit of 10000 characters. <br>Please, shorten the text in the Script text attribute.
Introduced In Version|2018.1
Revocable|NO
