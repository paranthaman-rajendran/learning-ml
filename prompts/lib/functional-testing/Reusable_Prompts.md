# GitHub Copilot Prompts for Financial Domain Functional Test Cases

---

## Key Principles I Swear By for Crafting Effective Prompts:

- **Be Hyper-Specific**: Vague prompts yield vague results. Detail the exact feature, user story, or even a specific business rule.
- **Define the "What" and "How"**: What needs to be tested? And how should Copilot present the test cases (e.g., Gherkin, list of steps, test data ideas)?
- **Incorporate Constraints & Edge Cases**: Explicitly ask for negative scenarios, boundary conditions, and specific compliance checks.
- **Provide Contextual Clues**: Mention the system (e.g., "Core Banking System," "Payments Hub"), the user role, and the expected technologies if relevant (e.g., "API tests," "UI tests").
- **Iterate and Refine**: Your first prompt is a starting point. Use Copilot's output to refine your next prompt for even better results.
- **Include System Information**: Add details about the system architecture, database, APIs, and validation mechanisms to ensure accurate test generation.
- **Test Data Generation**: Specify the type of test data required (e.g., valid, invalid, edge cases) to cover all scenarios comprehensively.

---

## Functional Test Generation Instructions:

When generating functional test cases, follow these guidelines:

1. **System Context**:

   - Clearly define the system or module being tested (e.g., "Core Banking System," "Payments Module").
   - Mention the technologies involved (e.g., Spring Boot, PostgreSQL, Kafka).

2. **Test Case Categories**:

   - **Positive Scenarios**: Focus on expected behavior with valid inputs.
   - **Negative Scenarios**: Test invalid inputs, missing data, or boundary violations.
   - **Edge Cases**: Include scenarios that test system limits or unusual conditions.

3. **Output Format**:

   - Use structured formats like Gherkin (`Given-When-Then`) or tabular formats (`Test Case ID | Description | Steps | Expected Results | Test Data`).

4. **Test Data Requirements**:

   - Specify the type of test data needed (e.g., valid KYC documents, invalid account numbers, maximum field lengths).
   - Include examples of test data for each scenario.

5. **Validation Points**:
   - Ensure test cases validate all critical aspects, such as database updates, API responses, and UI behavior.
   - Include checks for error messages, logs, and audit trails.

---

## I. Core Banking Scenarios: Functional Test Case Prompts

### Customer Onboarding & Management:

1. **New Customer Onboarding**

   ```markdown
   Generate a comprehensive set of functional test cases for the 'New Customer Onboarding' process in a Core Banking System. Include scenarios for:

   **System Information**:

   - The system uses Spring Boot microservices for customer onboarding.
   - Data is stored in PostgreSQL, and validations are performed using Spring Validation.
   - REST APIs are exposed for integration with external KYC providers.

   **Positive Cases**:

   - Successful onboarding with all valid individual customer data (KYC documents, minimum deposit).
   - Successful onboarding for a corporate customer with necessary business documentation.
   - Verification of duplicate customer checks to prevent duplicate entries.

   **Negative Cases**:

   - Rejection due to invalid/incomplete KYC information (e.g., expired ID, mismatched address proof).
   - Rejection due to age ineligibility (below 18 years).
   - Rejection due to missing mandatory fields (e.g., name, address, or contact details).

   **Edge Cases**:

   - Onboarding a customer with a name containing special characters or non-Latin alphabets.
   - Onboarding a customer with an address in a remote or unlisted location.
   - Handling of extremely large or small deposit amounts during onboarding.
   - Onboarding a customer with borderline age eligibility (e.g., exactly 18 years old).

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

   **System Information:**

   - The system uses Spring Boot microservices for transaction processing.
   - Transactions are logged in Kafka for audit purposes.
   - PostgreSQL is used for account balance storage, and transaction limits are configured in the database.

   **Positive Cases:**

   - Sufficient balance scenarios for successful transfers.
   - Transfers involving different currency accounts with FX conversion.
   - Real-time balance updates post-transfer.

   **Negative Cases:**

   - Insufficient balance scenarios resulting in transfer failure.
   - Transfers exceeding daily or per-transaction limits.

   **Edge Cases:**

   - Transfers with maximum allowed field lengths for account numbers.
   - Transfers involving accounts with special conditions (e.g., dormant accounts).
   - Transfers during system maintenance or downtime.

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

**System Information**:

- The system integrates with NPCI's IMPS gateway via REST APIs.
- Payment requests are validated using Spring Security and logged in Kafka.
- Daily and per-transaction limits are enforced at the database level.

**Positive Cases**:

- Successful payment using MMID and mobile number.
- Successful payment using IFSC and account number.

**Negative Cases**:

- Payment failure due to incorrect beneficiary details.
- Payment exceeding daily or per-transaction limits.

**Edge Cases**:

- Payments with maximum allowed field lengths for beneficiary details.
- Payments during peak transaction hours or system downtime.

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
Include system-specific details like database configurations, API integrations, and validation mechanisms to generate more accurate and relevant test cases.
