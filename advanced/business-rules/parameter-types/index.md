
# User Business Rules Actions - Parameter Types

The type of the parameter specifies how to obtain the parameter value. Several types are available:
- Constant - when used, indicates that the Value for this parameter type would be a constant every time the rule is activated;
- Attribute -  the value of the system or user-defined attribute;
- Reference -  reference to another object; usually used with the Attribute parameter type as a second parameter - and the attributes would be attributes of the referenced object and not of the current repository;
- ChildList - detailed objects, related to the current master object.
- Formatted String - A text which supports multi-line, variable interpolation, and variable formatting. For more detailed information, see **FormattedString**.
