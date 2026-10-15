# Additional Data JSON

`AdditionalDataJson` is an optional attribute available on aggregate root entities. It is stored in the entity's [Extensible Data Object (EDO)](edo.md), rather than in the entity's primary table.

It is an independent extension point for per-record integration data. Use it when an application needs to persist unmodeled state with an @@name record, whether the record originates in an external system, in @@name itself, or in an internal automation.

The field is similar to a small, per-record NoSQL document slot: an integration can keep arbitrary keys and nested values without changing the standard relational data model. For example, it can hold synchronization metadata or source-specific flags for a product, customer, or document.

## Limitations and appropriate use

The field does not support JSON-path queries, filtering, sorting, grouping, indexing, or partial JSON updates.

- The value is limited to **32,000 characters**. A client save that exceeds the limit is rejected by [business rule R101790](https://docs.erp.net/model/business-rules/R101790.html).
- Empty values are allowed. Nonblank values must contain a valid JSON object; otherwise the save is rejected by [business rule R101839-1](https://docs.erp.net/model/business-rules/R101839-1.html).
- The attribute is hidden by default in the user interface and is primarily intended for integrations and technical scenarios.

The complete JSON document can be viewed and edited through the client JSON editor, subject to permissions. For individual business fields that need their own controls, filtering, grouping, or reporting, use [Stored Attributes (Custom Properties)](../stored-attributes/index.md) or a dedicated entity instead.

## Integration ownership convention

When more than one application or service stores data for the same entity, each one must use a separate top-level object in `AdditionalDataJson`. Name the object after the external application or service, or after the functional domain that owns the data. Use a stable logical identifier that clearly identifies its owner.

For example:

```json
{
  "erpnet-retail-pos": {
    "listingId": "P-1042",
    "status": "approved"
  },
  "calendarSync": {
    "lastSynchronizedUtc": "2026-08-19T10:15:00Z"
  }
}
```

An application may create and update only its own top-level object. It must preserve the objects owned by other applications when saving the complete JSON value.

## Availability

`AdditionalDataJson` is available only on aggregate root entities. It is loaded only when requested, so ordinary reads of an entity do not transfer its payload.

In Desktop Client, the field can be added under the aggregate root in the field selector for a single-record form. It is excluded from Desktop navigators to avoid loading the JSON payload for every listed record.

The complete value can be cleared. In the Domain API, explicitly send `null` or an empty string to clear it; omitting the property from a PATCH request leaves the stored value unchanged. Sending `"{}"` stores an empty JSON object. When other applications also own data in the document, remove only your application's top-level object and preserve the rest.

For implementation details and Domain API examples, see [Additional Data JSON in Domain API](https://docs.erp.net/dev/domain-api/data-sync/additional-data-json.html).
