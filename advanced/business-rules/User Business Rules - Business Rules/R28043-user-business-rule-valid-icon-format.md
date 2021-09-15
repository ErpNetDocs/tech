# R28043 UserBusinessRule - Valid Icon Format

Code|R28043
|:----|:----
Entity|UserBusinessRule
Name|ValidIconFormat
Attribute|Icon
Layer|Back-End
Events|Commit
Priority|Normal
Modify|Normal
Action|Validate that:<br> UserBusinessRule.Icon.File.Extension == ".JPG"<br>UserBusinessRule.Icon.File.Extension ==".PNG"<br>UserBusinessRule.Icon.File.Extension ==".SVG"<br>UserBusinessRule.Icon.File.Extession == ".ICO"<br>
Description|There are certain recommendations for the right format of the icon image. <br> Valid file formats are .JPG, .PNG, .SVG, .ICO. All other formats are not allowed.
Message|"The icon must be .JPG,.PNG, .SVG or .ICO. <br> Please, use only images of those types."
Introduced In Version|2018.2
Revocable|NO
