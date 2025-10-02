# GitHub Knowledge Hub Structure

```
📦 vendor-app-knowledge-hub
 ┣ 📂 docs
 ┃ ┣ 📜 README.md
 ┃ ┣ 📜 process-guidelines.md
 ┃ ┣ 📜 leadership-presentation-outline.md
 ┣ 📂 configuration
 ┃ ┣ 📜 config-guidelines.md
 ┃ ┣ 📜 sample-configurations.md
 ┃ ┗ 📜 troubleshooting.md
 ┣ 📂 custom-development
 ┃ ┣ 📜 feature-template.md
 ┃ ┣ 📜 coding-standards.md
 ┃ ┗ 📜 sample-features.md
 ┣ 📂 functional-testing
 ┃ ┣ 📜 test-case-template.md
 ┃ ┣ 📜 test-execution-samples.md
 ┃ ┗ 📜 defect-tracking.md
 ┣ 📂 test-automation
 ┃ ┣ 📜 automation-framework.md
 ┃ ┣ 📜 automation-scripts-sample.md
 ┃ ┗ 📜 test-data-strategy.md
 ┣ 📂 knowledge-examples
 ┃ ┣ 📜 copilot-usage-examples.md
 ┃ ┣ 📜 prompts-library.md
 ┃ ┗ 📜 best-practices.md
 ┗ 📜 CONTRIBUTING.md
```

---

# Sample Markdown Templates

## 1. Custom Feature Development (`custom-development/feature-template.md`)

````markdown
# Feature: <Feature Name>

## Overview
Brief description of the feature and its purpose.

## Design
- Architecture diagram (if applicable)
- Dependencies
- Data flow

## Development Steps
1. Step 1
2. Step 2
3. Step 3

## Code Snippet (Generated with GitHub Copilot)
```java
// Example Java snippet
public class SampleFeature {
    public void execute() {
        System.out.println("Feature executed!");
    }
}
````

## Testing

* Unit test cases
* Integration test considerations

````

---

## 2. Application Configuration (`configuration/config-guidelines.md`)  
```markdown
# Configuration Guidelines

## Objective
Standard practices for configuring vendor application modules.

## Steps
1. Navigate to [Module/Screen]
2. Apply configuration: <example>
3. Save and validate changes

## Example
```json
{
  "parameter": "timeout",
  "value": "300s"
}
````

## Troubleshooting

* Common errors
* Workarounds

````

---

## 3. Functional Testing (`functional-testing/test-case-template.md`)  
```markdown
# Test Case Template

## Test Case ID
FT-001

## Title
Verify <functionality>

## Pre-Conditions
- Configuration applied
- Test data available

## Steps
1. Navigate to <screen>
2. Enter <input>
3. Validate <expected output>

## Expected Result
System should return <expected outcome>

## Actual Result
To be filled after execution

## Status
Pass/Fail
````

---

## 4. Test Automation (`test-automation/automation-framework.md`)

````markdown
# Test Automation Framework

## Objective
Standardize automation using GitHub Copilot-generated code.

## Structure
- Framework: Selenium + TestNG / JUnit
- Language: Java / Python
- CI/CD Integration: GitHub Actions

## Example Script
```python
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://vendor-app.com/login")

assert "Login" in driver.title
driver.quit()
````

## Best Practices

* Reuse page objects
* Maintain separate config files
* Log execution results

````

---

## 5. GitHub Copilot Prompts Library (`knowledge-examples/prompts-library.md`)  
```markdown
# GitHub Copilot Prompts Library

## Purpose
Provide reusable prompts for team members to generate consistent outputs.

## Examples

### Custom Feature Development
*Prompt:*  
"Generate a Spring Boot REST API endpoint for loan application with GET and POST methods, including validation."

### Configuration
*Prompt:*  
"Create a JSON sample for vendor app timeout configuration with default and override values."

### Functional Testing
*Prompt:*  
"Generate test cases in Markdown format for verifying login functionality with valid and invalid credentials."

### Test Automation
*Prompt:*  
"Write a Selenium test in Python to validate login functionality using Chrome driver."
````
