Got it 👍 You want a 30-min session content in Markdown for showcasing GitHub Copilot’s code review features in VS Code, with:
	•	A sample Java code snippet containing problems.
	•	How Copilot detects issues and suggests improvements.
	•	A custom code review checklist (instructions for Copilot).
	•	A before-and-after demo flow for participants.

Here’s a ready-to-use draft 👇

⸻

🚀 Session Plan: Code Review with GitHub Copilot in VS Code (Java Example)

⏰ Duration: 30 minutes

⸻

1. 🎯 Learning Objectives

By the end of this session, participants will:
	•	Understand how to use GitHub Copilot’s code review feature inside VS Code.
	•	Learn to apply custom review instructions for consistent code quality.
	•	See a live demo of problematic Java code → Copilot review → fixing issues → re-review.

⸻

2. 📌 Agenda (30 min)

Time	Activity
0–5 min	Introduction to Copilot Code Review
5–15 min	Demo: Review problematic Java code
15–25 min	Apply Copilot’s suggestions, re-run review
25–30 min	Wrap-up + Q&A


⸻

3. 🛠️ Setup
	•	Install Visual Studio Code.
	•	Enable GitHub Copilot & Copilot Chat extensions.
	•	Use a sample Java project (.java file).

⸻

4. 🧑‍💻 Sample Problematic Java Code

Create a file: UserService.java

import java.util.*;

public class UserService {
    private List<String> users = new ArrayList<>();

    public void addUser(String user) {
        users.add(user); // No validation
    }

    public String getUser(int index) {
        return users.get(index); // Risk: IndexOutOfBounds
    }

    public void removeUser(String user) {
        users.remove(user); // Case-sensitive, may fail silently
    }

    public void printUsers() {
        for (int i = 0; i <= users.size(); i++) { // Bug: <= instead of <
            System.out.println(users.get(i));
        }
    }
}

Issues in the code:
	•	No input validation (null or empty user).
	•	Possible IndexOutOfBoundsException in getUser.
	•	Bug in loop condition (<= instead of <).
	•	Inefficient remove logic (case sensitivity not handled).
	•	No logging / error handling.

⸻

5. 🔍 Asking Copilot for Review

In VS Code, open Copilot Chat and run:

/review

👉 Copilot will generate review comments:
	•	Identify bugs (<= loop condition).
	•	Warn about missing validations.
	•	Suggest handling exceptions.
	•	Recommend better practices.

⸻

6. 📋 Custom Review Checklist (Instruction for Copilot)

Create a .github/copilot-instructions.md (or paste into Chat before review):

# Custom Code Review Checklist for Java

When reviewing code, check for:
1. **Correctness**
   - Validate inputs (null, empty, out of bounds).
   - Ensure loops and conditions are correct.
   - Avoid silent failures.
2. **Error Handling**
   - Catch exceptions where necessary.
   - Provide meaningful error messages or logs.
3. **Code Quality**
   - Use proper naming conventions.
   - Follow Java best practices.
   - Ensure methods are single responsibility.
4. **Performance**
   - Avoid inefficient operations (e.g., unnecessary loops).
   - Consider case-insensitive matching if relevant.
5. **Maintainability**
   - Add comments for complex logic.
   - Ensure code readability.

Then run in VS Code:

/review with checklist from copilot-instructions.md


⸻

7. ✅ Fixed Java Code (After Copilot Suggestions)

import java.util.*;

public class UserService {
    private List<String> users = new ArrayList<>();

    public void addUser(String user) {
        if (user == null || user.trim().isEmpty()) {
            throw new IllegalArgumentException("User cannot be null or empty");
        }
        users.add(user.trim());
    }

    public Optional<String> getUser(int index) {
        if (index < 0 || index >= users.size()) {
            return Optional.empty();
        }
        return Optional.of(users.get(index));
    }

    public boolean removeUser(String user) {
        return users.removeIf(u -> u.equalsIgnoreCase(user));
    }

    public void printUsers() {
        for (int i = 0; i < users.size(); i++) {
            System.out.println(users.get(i));
        }
    }
}


⸻

8. 📝 Wrap-up
	•	Copilot review → detected bugs, risks, and improvements.
	•	Using a custom checklist makes review consistent across teams.
	•	Demo showed before-and-after improvement cycle.

⸻

9. 💡 Takeaway

“Copilot is not just for code generation — it’s a helpful reviewer that enforces coding standards and best practices when guided with a proper checklist.”

⸻

Do you want me to also prepare a step-by-step demo script (spoken lines) for you to deliver during the 30-min session? That way, you’ll have exact narration along with code flow.