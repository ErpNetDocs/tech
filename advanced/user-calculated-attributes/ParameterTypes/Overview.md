# Parameter Types

The type of the parameter specifies how to obtain the parameter value. Several types are available:

- CONST - when used, indicates that the Value for this parameter type would be a constant for every calculation of the calculated attribute. For more  information, see [Parameter Type CONST](ParameterTypeCONST.md).
- ATTRIB - the value of system or user-defined attribute;
- REF - reference to another object;
- CHILD - detailed objects, related to the current master object;
- EXP - the value of the expression with the specified number (the user specifies the number in the Value field);
- INPUT - the input parameter for the specified expression number (the user specifies the number in the Value field);
- REPO - a repository;
- SYS - the value of a particular system variable as Login, Today, EnterpriseCompanyId and others.

The Parameter Types are used in every calculated attributes. For examples see [Calculated Attributes - Examples](../examples/toc.yml).
