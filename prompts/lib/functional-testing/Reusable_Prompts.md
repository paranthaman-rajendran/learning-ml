# Reusable GitHub Copilot Prompts for Financial Domain

This document contains reusable prompts for GitHub Copilot to assist with functional test case generation, development tasks, and more.

---

## Functional Test Case Prompts

### Customer Onboarding

```markdown
Generate a comprehensive set of functional test cases for the 'New Customer Onboarding' process in a Core Banking System. Include scenarios for:

- Successful onboarding with valid KYC documents.
- Rejection due to invalid/incomplete KYC information.
- Verification of duplicate customer checks.
  Output as: Test Case ID | Description | Steps | Expected Results | Test Data Considerations.
```

### Fund Transfer

```markdown
Generate functional test cases for 'Fund Transfer between own accounts' within the Core Banking System. Include:

- Sufficient and insufficient balance scenarios.
- Transfers involving different currency accounts.
- Verification of transaction limits (daily, per transaction).
  Format: Given [Context], When [Action], Then [Verification].
```
# GitHub Copilot Prompts for Financial Domain Functional Test Cases

---

## Key Principles I Swear By for Crafting Effective Prompts:

- **Be Hyper-Specific**: Vague prompts yield vague results. Detail the exact feature, user story, or even a specific business rule.
- **Define the "What" and "How"**: What needs to be tested? And how should Copilot present the test cases (e.g., Gherkin, list of steps, test data ideas)?
- **Incorporate Constraints & Edge Cases**: Explicitly ask for negative scenarios, boundary conditions, and specific compliance checks.
- **Provide Contextual Clues**: Mention the system (e.g., "Core Banking System," "Payments Hub"), the user role, and the expected technologies if relevant (e.g., "API tests," "UI tests").
- **Iterate and Refine**: Your first prompt is a starting point. Use Copilot's output to refine your next prompt for even better results.

---

## I. Core Banking Scenarios: Functional Test Case Prompts

### Customer Onboarding & Management:

1. **New Customer Onboarding**

   ```markdown
   Generate a comprehensive set of functional test cases for the 'New Customer Onboarding' process in a Core Banking System. Include scenarios for:

   - Successful onboarding with all valid individual customer data (KYC documents, minimum deposit).
   - Rejection due to invalid/incomplete KYC information (e.g., expired ID, mismatched address proof).
   - Rejection due to age ineligibility (below 18 years).
   - Scenario for a corporate customer onboarding with necessary business documentation.
   - Verification of duplicate customer checks.
     Output as: Test Case ID | Description | Steps | Expected Results | Test Data Considerations.
   ```

2. **Customer Address Update**

   ```markdown
   Create Gherkin scenarios for the 'Customer Address Update' feature. Cover:

   - Successful update via online banking portal.
   - Update requiring branch verification due to significant change.
   - Rejection of P.O. Box address if not permitted by bank policy.
   - Audit trail verification for address changes.
   ```

3. **Customer Deactivation/Closure**
   ```markdown
   List functional test cases to validate the 'Customer Deactivation/Closure' process, ensuring all linked accounts, standing orders, and fees are handled correctly as per bank policy.
   ```

---

### Account Operations (Savings, Current Accounts):

4. **Fund Transfer Between Own Accounts**

   ```markdown
   Generate functional test cases for 'Fund Transfer between own accounts' within the Core Banking System. Include:

   - Sufficient and insufficient balance scenarios.
   - Transfers involving different currency accounts (if applicable, note FX conversion).
   - Verification of transaction limits (daily, per transaction).
   - Real-time balance updates post-transfer.
     Format: Given [Context], When [Action], Then [Verification].
   ```

5. **Statement Generation**

   ```markdown
   Outline test cases for 'Statement Generation' for a savings account, covering different periods (monthly, quarterly, custom date range), delivery methods (email, view online), and data accuracy (transactions, balances, interest).
   ```

6. **Account Hold/Freeze Scenarios**
   ```markdown
   Generate negative functional test cases for 'Account Hold' and 'Account Freeze' scenarios, detailing triggers (e.g., legal order, suspicious activity) and system behavior (e.g., transaction blocking, notifications).
   ```

---

### Loan Origination & Servicing:

7. **Personal Loan Application**

   ```markdown
   Create functional test case outlines for the 'Personal Loan Application' module. Focus on:

   - Data validation for all input fields (applicant details, income, loan amount, tenure).
   - Credit score integration: scenarios for scores leading to approval, rejection, or manual review.
   - Eligibility checks based on bank's lending criteria (e.g., debt-to-income ratio).
   - Generation of loan agreement and sanction letter.
   ```

8. **Loan Repayment Schedule**
   ```markdown
   Generate test scenarios for 'Loan Repayment Schedule' verification, including EMI calculation, interest vs. principal components, and handling of pre-payments and late fees.
   ```

---

### Term Deposits (Fixed Deposits):

9. **Fixed Deposit Booking**

   ```markdown
   List functional test cases for 'Fixed Deposit Booking' via internet banking. Cover:

   - Various deposit tenures and interest rate applications.
   - Minimum and maximum deposit amount validations.
   - Nominee details capture.
   - Confirmation and FD advice generation.
   ```

10. **Premature Withdrawal of Fixed Deposit**
    ```markdown
    Generate test cases for 'Premature Withdrawal of Fixed Deposit,' including calculation of penal interest and payout to the linked savings account.
    ```

---

## II. Payments Domain (Domestic & Cross-Border): Functional Test Case Prompts

### Domestic Payments (e.g., NEFT, RTGS, IMPS, UPI):

11. **IMPS Payment**

    ```markdown
    Generate functional test cases for an 'IMPS Payment' from a mobile banking app. Include:

    - Successful payment using MMID and mobile number.
    - Successful payment using IFSC and Account number.
    - Payment failure due to incorrect beneficiary details.
    - Handling of transaction timeouts and reconciliation.
    - Validation of per-transaction and daily limits.
      Output should include test data for mobile numbers, MMIDs, and sample account details.
    ```

12. **UPI Payment via QR Code**
    ```markdown
    Create Gherkin scenarios for 'UPI Payment via QR Code scan.' Cover:

    - Successful payment to a merchant.
    - Payment to an individual.
    - Handling of invalid or expired QR codes.
    - Dispute resolution initiation for failed but debited transactions.
    ```

---

**Pro-Tip for Using These Prompts:**  
Don't just copy-paste. Tailor them further. For instance, if your system uses a specific internal name for a feature, use that. If there's a unique regulatory requirement for your region (e.g., RBI guidelines for India), add that constraint. The more context you feed Copilot, the more refined and useful its test case generation will be. Happy prompting!

---

## Development Prompts

### Create a JPA Entity

```markdown
Write a JPA entity for a SavingAccount with fields: accountId, customerId, accountNumber, balance, status, createdDate, modifiedDate. Use Lombok annotations and JPA validation constraints.
```

### API Documentation

```markdown
Generate OpenAPI annotations for SavingAccountController to document all endpoints like createAccount, deposit, withdraw, transfer, getMiniStatement, and closeAccount.
```

---

**Pro-Tip:** Use these prompts as a starting point and tailor them to your specific use case.
