## ✅ Application Flow - High Level Overview

```mermaid
graph TD
    A[User Access Web App] --> B{Is User Logged In?}
    B -- Yes --> C[Show Dashboard]
    B -- No --> D[Show Login Page]
    C --> E[Perform Actions]
    D --> F[User Login Attempt]
```

---

## ✅ User Login Flow

```mermaid
graph TD
    A[User enters credentials] --> B{Username exists?}
    B -- Yes --> C{Is password correct?}
    C -- Yes --> D[Login Successful]
    C -- No --> E[Show Incorrect Password Error]
    B -- No --> F[Show User Not Found Error]
    D --> G[Redirect to Dashboard]
```

---

## ✅ Data Submission Flow

```mermaid
graph TD
    A[User Submits Form Data] --> B[Validate Data]
    B --> C{Is Data Valid?}
    C -- Yes --> D[Store Data in Database]
    D --> E[Show Success Message]
    C -- No --> F[Show Validation Errors]
```

---

## ✅ Error Handling Workflow

```mermaid
graph TD
    A[Application Error Occurs] --> B[Log Error Details]
    B --> C[Show Generic Error Message to User]
    C --> D[Redirect to Support Page]
```

---

## ✅ Logout Workflow

```mermaid
graph TD
    A[User Clicks Logout] --> B[Clear Session Data]
    B --> C[Redirect to Login Page]
```

---

## 📌 Notes

- All diagrams use Mermaid syntax.
- Previewable in VS Code via **Markdown Preview Mermaid Support** extension.
- Can be visualized via [Mermaid Live Editor](https://mermaid-js.github.io/mermaid-live-editor/).