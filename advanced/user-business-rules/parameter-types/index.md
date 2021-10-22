# Parameter Types

Parameter types specify how to obtain a parameter value:

- Constant - when used, indicates that the Value for this parameter type would be a constant every time the rule is activated;
- Attribute -  the value of the system or user-defined attribute;
- Reference -  reference to another object; usually used with the attribute parameter type as a second parameter - and the attributes would be attributes of the referenced object and not of the current repository;
- ChildList - detailed objects, related to the current master object.
- [FormattedString](https://docs.erp.net/tech/advanced/user-business-rules/parameter-types/formattedstring.html) - A text which supports multi-line, variable interpolation, and variable formatting.

