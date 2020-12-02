## Domain with Property Allowed Values

Domain is the range of the allowed values of the particular Custom Property. It is determined in one of the following ways - sorted by priority:

1. If "Limit To Allowed Values" does NOT have a check mark, then any value is valid and the domain is a range of all possible values.

2. If the "Allowed Values Entity Name" has a value, then the domain is the set of all records of the specified data type.

   

>[!Note]
>This field should have a value ONLY if "Limit To Allowed Values" has a check mark and "Allowed Values Property" does not have a value.

3. If the field "Allowed Values Property" has a value, then the domain of the current custom property is equal to the domain of the custom property specified in this field.

   CustomProperty.Domain = CustomProperty.AllowedValuesProperty.Domain

   

   **Note:** This field should have a value ONLY if "Limit To Allowed Values" has a check mark and "Allowed Values Entity Name" does NOT have a value.

4. (Default, Lowest Priority) The domain is the range of the "Property Allowed Values" listed in the Gen_Property_Allowed_Values sub-table.

   

***Example 1:***

Let's assume that we have the following properties:

Property 1 (Entity Name = Products)

Property 2 (Allowed Values Property = Property 1)

Property 3 (Entity Name = Products)

Property 4 (Entity Name = Companies)

Property 5 (Allowed Values Property = Property 2)

Property 6 (Limit To Allowed Values = False)



In this case, the domains are:

Property 1 - Products

Property 2 - Products

Property 3 - Products

Property 4 - Companies

Property 5 - Products

Property 6 – All possible values

## Compatible Custom Properties

Two custom properties are copy compatible when then and only then their domains are the same. The compatibility allows us to copy values from one custom property to another. It is still possible the copying to throw an error, but this would be caused by different reasons – additional filters set in the definition, for example

An important note is that the additional filters do not change the domain of the custom property. They just reduce the range with allowed values. It is also possible future procedures or rules to be added – but they won’t change the actual domain of the custom properties either. In general, we can accept that the domain of the allowed values, from a programming point of view, could be defined as a kind of custom property type.

***Example 2:***

If we use the description of Example 1, we can conclude that Property 1 is compatible with Property 2.

Both of them are compatible with Property 3 and Property 5.

On the other hand Property 1, Property 2, Property 3 and Property 5 are compatible with each other.

Property 4 in not compatible with none of the above.

Property 6, although it could receive any possible value, is also noncompatible with other custom properties.

## Inheriting and hereditary root

 A custom property inherits another custom property by indicating a (hereditary) parent property in the "Allowed Values Property" field. The hereditary root is the grand-parent, which does not have a hereditary root on its own. The hereditary root of a custom property clearly defines its domain and is a prerequisite for automatic copying of its allowed values.

A hereditary root is defined as follows:

1. If "Allowed Values Property" does not have a value, then the hereditary root is the custom property itself

2. Otherwise, the hereditary root is equal to the hereditary root of the parent custom property.
   This means that:
   HereditaryRoot (Property) = HereditaryRoot(Property. AllowedValuesProperty)
   i.e. we look recursively in the relation “Allowed Values Property”.

   

***Example 3:***

If we use the example above, custom properties have the following hereditary roots:

Property 1: Property 1

Property 2: Property 1

Property 3: Property 3

Property 4: Property 4

Property 5: Property 1

Property 6: Property 6

## Copying

Hereditary roots are used to determine the most appropriate "partner" for the automatic copying of the allowed values of the custom properties.

We will look at an example in which we want to copy custom properties from a Customer to a Sales Order document:

***Example 4:*** 

Let’s assume that:

- the Customer has the following custom properties:

FAVORITE-PRODUCT: (Entity Name = Products)

ADVANCE-PRODUCT: (Entity Name = Products)

- In the Sales Order document type are set the following custom properties:

FAVORITE-PRODUCT-CUSTOMER: Allowed Values Property = CUSTOMER. FAVORITE-PRODUCT

SALE-ADVANCE-PRODUCT: Allowed Values Property = CUSTOMER.ADVANCE-PRODUCT



In this case:

- All 4 custom properties are "compatible". They could inherit values from one another.
- At the same time, only the following pairs have the same hereditary root:

​    A) FAVORITE-PRODUCT-CUSTOMER and FAVORITE-PRODUCT

​    B) SALE-ADVANCE-PRODUCT and ADVANCE-PRODUCT

Copying: Accordingly, when specifying a Customer in Sales Order, only the custom properties that have the same hereditary root will be automatically copied from the Customer to the Document.

## Custom properties value priorities (when copying to a document)

The priority for automatic copying of custom properties to a document is determined according to the following priorities (from the highest to the lowest priority):



[!Note 
>The priorities represent the following logic. If for a custom property is found a value with a higher priority, then – copy the value. If not – search for values with lower priorities

\1. Inherited values from the parent document. (Priority 80)

\2. The values set in the panel "Copy customer properties" (valid only for Sale Orders, but the same priority applies if there is a similar table for other types of data). (Priority 70)

\3. Values from custom properties with the same hereditary root in the definition of the „main contractor” of the document. In general cases, this is the party loaded in the field "To Party" (an exception are Purchase Invoices, where the Supplier is considered as a "main contractor" ). (Priority 50)

\4. The default values specified in the document type. (Priority 20)

\5. If none of the above contains a value for the custom property, but it is specified in the document type – set an empty (NULL) value. (Priority 10)



**Note:** Every manual change of value of custom property, should be done after being entered values in all relevant nomenclatures (Enterprise Company, Customer, Parent document etc.)
