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
Description|The limit of the script which can be entered in a user business rule is **10000** characters. <br> This validation is required for protective purposes.
Message|_The Script text attribute exceeds its limit of 10000 characters._ <br>_Please, shorten the text in the Script text attribute._
Introduced in version|2018.1
Revocable|NO
