---
items: CalculatedAttributeExamples
---

# Count outstanding invoices based on Sales Order To Party  

This calculated attribute counts how many Payment Balances exist for the party from the current Sales Order (the order’s ToParty), where the remaining amount is greater than 0 (i.e., there is still an outstanding balance).
If the expression fails for any reason, it returns the constant text "Error".

```
5:   IFERROR EXP:10 EXP:100
10:  COUNT EXP:20
20:  SELECT  REPO:Finance.Payments.PaymentBalances EXP:30
30:  WHERE EXP:40 EXP:70
40:  EQUAL  ATTRIB:PartyId EXP:50
50:  GETOBJVALUE INPUT:5 ATTRIB:ToPartyId
70:  GT EXP:80 EXP:90
80:  GETVALUE ATTRIB:RemainingAmountValue
90:  CAST CONST:0 CONST:System.Decimal
100: GETVALUE CONST:Error
```

**Explanation:**

5 (IFERROR): Returns EXP:10; if an error occurs, returns EXP:100 (the text “Грешка”)  
10 (COUNT): Counts the records returned by EXP:20  
20 (SELECT): Queries the repository Finance.Payments.PaymentBalances  
30 (WHERE): Filters the Payment Balances by two conditions:  
	EXP:40 (party match)  
	EXP:70 (remaining amount > 0)  
  
**Filter 1: same party as the Sales Order “To Party”**  
40 (EQUAL): Keeps balances where PartyId = EXP:50  
(Conceptually: PaymentBalance.Party equals the SalesOrder.ToParty.)  
50 (GETOBJVALUE): Gets the current Sales Order’s ToPartyId from the input object (INPUT:5) 

**Filter 2: outstanding amount exists**  
70 (GT): Checks RemainingAmountValue > 0  
80 (GETVALUE): Gets RemainingAmountValue (the numeric value of the RemainingAmount)  
90 (CAST): Casts constant 0 to System.Decimal for type-compatible comparison  
100: Returns the constant string "Error" when an error happens 
