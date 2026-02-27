# Accounting

## Notable features

### **1.Transfer Orders: Line-level posting for additional amounts using calculated attributes**

Accounting templates for **Transfer Orders** now support a new **Amount source**:

- **Transfer Orders – Lines**

When this source is selected, the **Amount on** field can reference a **calculated attribute defined for transfer order lines**. This enables accounting for **additional amounts** (e.g. transport and other costs) **per line**, 
so that the allocated amounts can be posted to different accounts depending on the line context (e.g. product type) — a common requirement for SAF‑T aligned charts of accounts.

**Typical use case**
- You enter additional amounts (transport/overheads) for a transfer.
- You need the distributed portion of these amounts to be posted per line to the correct accounts (e.g. separate accounts for goods/materials/finished goods), without requiring users to split transfers by product type.

**How it works**
1. Define calculated attributes for **Transfer Order Lines** to calculate the desired line-level amount (e.g. allocated transport).
2. In the accounting template for the transfer order, set:
   - **Amount source** = *Transfer Orders – Lines*
   - **Amount on** = the relevant line calculated attribute
3. The generated postings can now reflect the distributed amounts per line.
