---
uid: domain-with-property-allowed-values
---

## Domain with property allowed values

Domain is the range of the allowed values of the particular custom property. It is determined in one of the following ways - sorted by priority:

1. If Limit To Allowed Values does NOT have a check mark, then any value is valid and the domain is a range of all possible values.

2. If the Allowed Values Entity Name has a value, then the domain is the set of all records of the specified data type.

   

> [!Note]
>This field should have a value ONLY if Limit To Allowed Values has a check mark and Allowed Values Property does not have a value.

3. If the field Allowed Values Property has a value, then the domain of the current custom property is equal to the domain of the custom property specified in this field.

   CustomProperty.Domain = CustomProperty.AllowedValuesProperty.Domain

   

> [!Note]
>This field should have a value ONLY if Limit To Allowed Values has a check mark and Allowed Values Entity Name does NOT have a value.

4. (Default, Lowest Priority) The domain is the range of the"Property Allowed Values listed in the Gen_Property_Allowed_Values sub-table.

   

***Example 1:***

Let's assume that we have the following properties:

property 1 (entity name = Products)

property 2 (allowed values property = Property 1)

property 3 (entity name = Products)

property 4 (entity name = Companies)

property 5 (allowed values property = Property 2)

property 6 (limit to allowed values = False)



In this case, the domains are:

property 1 - Products

property 2 - Products

property 3 - Products

property 4 - Companies

property 5 - Products

property 6 – all possible values

## Compatible custom properties

Two custom properties are copy compatible when then and only then their domains are the same. The compatibility allows us to copy values from one custom property to another. It is still possible the copying to throw an error, but this would be caused by different reasons – additional filters set in the definition, for example

An important note is that the additional filters do not change the domain of the custom property. They just reduce the range with allowed values. It is also possible future procedures or rules to be added – but they won’t change the actual domain of the custom properties either. In general, we can accept that the domain of the allowed values, from a programming point of view, could be defined as a kind of custom property type.

***Example 2:***

If we use the description of Example 1, we can conclude that Property 1 is compatible with Property 2.

Both of them are compatible with Property 3 and Property 5.

On the other hand Property 1, Property 2, Property 3 and Property 5 are compatible with each other.

Property 4 in not compatible with none of the above.

Property 6, although it could receive any possible value, is also noncompatible with other custom properties.

## Inheriting and hereditary root

 A custom property inherits another custom property by indicating a (hereditary) parent property in the Allowed Values Property field. The hereditary root is the grand-parent, which does not have a hereditary root on its own. The hereditary root of a custom property clearly defines its domain and is a prerequisite for automatic copying of its allowed values.

A hereditary root is defined as follows:

1. If Allowed Values Property does not have a value, then the hereditary root is the custom property itself

2. Otherwise, the hereditary root is equal to the hereditary root of the parent custom property.
   This means that:
   HereditaryRoot (Property) = HereditaryRoot(Property. AllowedValuesProperty)
   i.e. we look recursively in the relation Allowed Values Property.

   

***Example 3:***

If we use the example above, custom properties have the following hereditary roots:

Property 1: Property 1

Property 2: Property 1

Property 3: Property 3

Property 4: Property 4

Property 5: Property 1

Property 6: Property 6

## Copying

Hereditary roots are used to determine the most appropriate 'partner' for the automatic copying of the allowed values of the custom properties.

We will look at an example in which we want to copy custom properties from a customer to a sales order document:

***Example 4:*** 

Let’s assume that:

- the customer has the following custom properties:

FAVORITE-PRODUCT: (entity name = Products)

ADVANCE-PRODUCT: (entity name = Products)

- In the sales order document type are set the following custom properties:

FAVORITE-PRODUCT-CUSTOMER: Allowed Values Property = CUSTOMER. FAVORITE-PRODUCT

SALE-ADVANCE-PRODUCT: Allowed Values Property = CUSTOMER.ADVANCE-PRODUCT



In this case:

- All 4 custom properties are 'compatible'. They could inherit values from one another.
- At the same time, only the following pairs have the same hereditary root:

​    A) FAVORITE-PRODUCT-CUSTOMER and FAVORITE-PRODUCT

​    B) SALE-ADVANCE-PRODUCT and ADVANCE-PRODUCT

Copying: Accordingly, when specifying a customer in sales order, only the custom properties that have the same hereditary root will be automatically copied from the customer to the document.

## Custom properties value priorities (when copying to a document)

The priority for automatic copying of custom properties to a document is determined according to the following priorities (from the highest to the lowest priority):



>[!Note]
>The priorities represent the following logic. If for a custom property is found a value with a higher priority, then – copy the value. If not – search for values with lower priorities

1. Inherited values from the parent document. (Priority 80)

1. The values set in the panel Copy Customer Properties (valid only for sale orders, but the same priority applies if there is a similar table for other types of data). (Priority 70)

1. Values from custom properties with the same hereditary root in the definition of the 'main contractor' of the document. In general cases, this is the party loaded in the field To Party (an exception are purchase invoices, where the supplier is considered as a 'main contractor'). (Priority 50)

1. The default values specified in the document type. (Priority 20)

1. If none of the above contains a value for the custom property, but it is specified in the document type – set an empty (NULL) value. (Priority 10)



>[!Note]
>Every manual change of value of custom property, should be done after being entered values in all relevant nomenclatures (enterprise company, customer, parent document etc.)
