# Ingest AI – Intelligent Import of Purchase Invoices

## 1. What is Ingest AI?

**Ingest AI** is an application in the ERP.net web client that automatically reads and imports purchase invoices into the system.

Instead of manually retyping data from paper or PDF invoices, users can:

- **Snap a photo** of the invoice with their smartphone, or  
- **Upload a file** (image or PDF) from their computer,

Ingest AI converts it into a **structured purchase invoice document** in ERP.net.

![Snap to Doc](snap_to_doc.png)

![Ingest Desktop](ingest-desktop.png)

Ingest AI works:

- On **mobile** – ideal for operational staff and accountants on the go.
- On **desktop** – for office users who drag & drop or select files from their computer.

The result is:

- Less manual data entry  
- Fewer typing mistakes  
- More time for higher-value, expert work instead of repetitive keying  

---

## 2. Primary use case: service purchase invoices

Ingest AI is optimized for **service purchase invoices**, where:

- Suppliers often send **multi-line** invoices, broken down by their internal products/services.
- For accounting and reporting, the customer usually needs **one standard internal product or expense** (e.g. _“External services expense”_, _“Software subscription”_, _“Maintenance fee”_), not the supplier’s detailed breakdown.

### Smart mapping to your internal service product

When a new invoice from a known supplier is imported, Ingest AI:

1. Finds the **most recent purchase invoice** from the same supplier (for up to one year back).
2. If that previous invoice is **single-line**, Ingest AI:
   - Reuses the **internal product** from that line (e.g. your standard “External services” product).
   - Copies the **quantity** and any **user-defined attributes**, if applicable.
   - Uses the **net amount** from the newly recognized invoice.
   - Copies relevant header settings such as:
     - Deal type  
     - Expense center (and revenue center if used)  
     - Notes / description  

This means:

> Even if the supplier sends a multi-line invoice, ERP.net can work with a **single, standardized line** using **your** internal product for that service, while the detailed supplier structure remains in the attached original document.

### Why this is a good practice

From an accounting and process perspective, this approach:

- Reduces complexity by using **standard internal products** and expense categories.  
- Simplifies **reporting and analysis** – you always see consistent categories, rather than dozens of supplier-specific items.  
- Keeps all supplier detail **accessible but not intrusive** – it stays in the scanned/attached document instead of cluttering your accounting lines.

As long as the invoice in the system has:

- Correct supplier and customer  
- Correct invoice number and date  
- Correct totals (net, VAT, currency)  
- The original document attached  

you do **not** need to replicate the supplier’s line breakdown exactly inside ERP.net.

---

## 3. How Ingest AI works – end-to-end flow

### 3.1. Accessing the application

Ingest AI is available in the ERP.net web client:

- From the **main menu** (as a business app).
- On both **desktop** and **mobile view**.
- As an installed mobile app (where applicable), for quick access.

> **Licensing:** Ingest AI requires the **X13 – Advanced AI** license and an active AI server configuration.

---

### 3.2. Capturing or uploading the invoice

You can provide the invoice to Ingest in several ways:

- **Mobile:**
  - Choose **Camera** and take a photo of a paper invoice.
  - Or pick an existing photo from your gallery.
- **Desktop:**
  - Use **Select File** to browse and upload.
  - Or simply **drag & drop** the file onto the Ingest screen.

Supported formats include:

- Photos (e.g. from a smartphone camera)  
- PDF and other common image formats  

> **Recommendation:** Each file should contain **exactly one invoice**.  
> For multi-page invoices, include **all pages in a single file**.

---

### 3.3. AI recognition

Once the file is uploaded, Ingest AI sends it to the AI model, which reads and structures the data. It recognizes core fields such as:

- Document type (e.g. Purchase Invoice, Credit Note)
- Invoice number  
- Invoice date  
- Supplier name  
- Customer (your company)  
- Registration / Tax number  
- Address  
- Total net amount  
- VAT and total amount (depending on configuration)  
- Currency  

The AI is designed to work reliably even with:

- **Scanned** paper invoices  
- **Hand-written** or partially hand-written invoices (where legible)

Names of companies are normalized to avoid problems with:

- Extra dots and dashes  
- Different quote characters  
- Mixed case or spacing  

This improves matching to existing supplier records.

---

### 3.4. Reviewing recognized data

After recognition, Ingest AI displays a **“Recognized data”** panel where the user can:

- Review the extracted fields.
- Correct any values (e.g. date, number, supplier match, amount, currency).
- Add or edit notes.

Key fields such as:

- Supplier  
- Customer  
- Document number  
- Date  
- Net amount  
- Currency  

are visible and editable, so the accountant has full control before importing.

In most cases, the user simply reviews and presses **Import**, because the recognition accuracy is very high.

---

### 3.5. Validation and safety checks

Before creating the purchase invoice in ERP.net, Ingest AI performs several checks:

1. **Recipient company check**  
   - Ensures that the **customer on the invoice equals the current enterprise company** in ERP.net.  
   - If there is a mismatch, import is stopped with a clear error message.

2. **Duplicate invoice check**  
   - Checks whether there is an existing, non-voided purchase invoice for:
     - The same supplier  
     - The same document number  
     - The same enterprise company  
   - If a match is found, Ingest AI **blocks** creation of a duplicate invoice.

3. **Document validity**  
   - If the AI cannot recognize the document as a valid purchase invoice (missing supplier, customer, number, date, etc.), the import is not allowed.

These controls ensure that automation **does not** introduce duplicates or incorrect company mappings.

---

### 3.6. Creating the purchase invoice

If validation passes and the user confirms:

1. A new **Purchase Invoice** document is created in ERP.net.  
2. Header fields are filled with the recognized and/or corrected data.  
3. Ingest applies the **smart mapping logic**:
   - Looks up the most recent invoice for this supplier.
   - Reuses the internal product and key settings if that invoice is single-line.
   - Copies deal type, cost center, and notes.
   - Sets the line amount to the net amount of the newly recognized invoice.
4. The original file (image or PDF) is **attached** to the invoice.
5. VAT and other distributed amounts are recalculated automatically based on the totals.

The user then sees:

- The fully created purchase invoice with:
  - VAT and totals  
  - Service line(s)  
- The attached invoice file that can be opened directly in the web client without downloading.

The accountant can do a final review and post the document as usual.

---

## 4. Desktop and mobile experience

Ingest AI is designed to work consistently across devices:

- **Mobile view**
  - Perfect for operational staff, field teams, and administrative personnel.
  - Take a photo of a paper invoice immediately when it is received.
- **Desktop view**
  - Ideal for back-office accountants who receive invoices by email.
  - Drag & drop from a folder or mail attachment, or select the file manually.

No matter the device, the workflow is the same:

1. Provide the file (camera or upload).  
2. Review recognized data.  
3. Import and get a direct link to the created invoice.  

This ensures that all users can work in a unified way, regardless of their device or operating system.

---

## 5. Best practices for using Ingest AI

To get the best results from Ingest AI, we recommend:

### 5.1. Standardize internal service products

- Define clear **standard products/expenses** for recurring services, such as:
  - External services  
  - Software subscription  
  - Maintenance and support  
- Use these standardized products on invoices imported with Ingest AI.
- Make sure the latest invoice from each supplier uses the desired internal product – Ingest will reuse it automatically.

### 5.2. Configure cost centers and deal types

- On the last “reference” invoice for a supplier, set:
  - The correct deal type  
  - The appropriate cost center (and revenue center if needed)  
- Ingest AI will copy these settings for future invoices, ensuring consistent allocation.

### 5.3. Use Ingest AI as the primary entry channel

- Encourage operational and accounting staff to:
  - Use Ingest AI instead of manually entering invoices.
  - Rely on the **review screen** to make small corrections, rather than retyping everything.

### 5.4. Keep supplier detail in the attachment

- Do not try to mirror the supplier’s complex line structure inside ERP.net unless absolutely necessary.
- Let Ingest AI create a **clean, standardized service line**, and use the attached invoice whenever you need to see the supplier’s detailed breakdown.

### 5.5. Ensure good image quality

- For paper invoices:
  - Take photos in good lighting, without glare or strong shadows.
  - Make sure the entire invoice is visible and not cut off.
- Poor image quality can reduce recognition accuracy and may lead to misread values.

---

## 6. Limitations and known behaviors

- Each uploaded file should contain **one invoice**.  
- Multi-page invoices must be in a **single file** (multi-page PDF or multi-page image).  
- Some environments (like the **new Outlook web interface**) may limit drag & drop directly from email; in such cases, save the file locally first and then upload it to Ingest AI.  
- Response time depends on the AI service; slow or unstable connections to the AI server can increase processing time.
