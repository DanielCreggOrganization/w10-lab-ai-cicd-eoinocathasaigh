# Lab: AI-Powered CI/CD with GitHub Actions (Python Edition)

-----

**Module:** Modern Software Development  
**Tech Stack:** Python 3.10+, pip, pytest, GitHub Actions, GitHub Copilot

-----

## 🚀 Introduction

Continuous Integration (CI) is the practice of automating the build and testing of your code every time a change is made. Traditionally, writing CI pipelines required memorising complex YAML syntax and obscure shell commands.

In this lab, you will use **GitHub Copilot** to:

1.  **Generate** a complete CI/CD pipeline from scratch using Agent Mode.
2.  **Script** complex automation tasks using natural language in the terminal.
3.  **Debug** and fix broken builds using AI assistance.
4.  **Embed** AI directly into your workflow to automate issue management.
5.  **Delegate** coding tasks to an AI Agent and get automated Code Reviews.

-----

## 🏗️ Architecture

We are building a standard Python "Lint & Test" pipeline.

```mermaid
flowchart LR
    subgraph "Developer Environment"
        A[💻 Student Code]
        AI[🤖 Copilot Agent]
    end

    subgraph "GitHub Cloud"
        R[📂 Repository]
        W[⚙️ Actions Workflow]
        PR[👀 AI Code Review]
    end

    subgraph "CI Pipeline Runner"
        S1[📦 Install Deps pip]
        S2[✨ Lint Flake8 Ruff]
        S3[🧪 Test pytest]
        S4[🧠 AI Inference]
    end

    A -- "Pushes Code" --> R
    AI -- "Creates Files" --> A
    R -- "Triggers" --> W
    W --> S1 --> S2 --> S3
    W -.-> S4
    R -- "Pull Request" --> PR
```

-----

## ✅ Prerequisites

  * **GitHub Account** with Copilot enabled (Student/Education pack works perfectly).
  * **No local installation required**: We will use **GitHub Codespaces**.

-----

## Part 1: Project Setup (10 Mins)

We need a Python application to test. Your instructor has provided a starter repository via GitHub Classroom.

1.  **Accept the Assignment**: Click the following link to create your repository.
2.  **Open Your Repository**: Once the repository is created, click the link to open it on GitHub.

3.  **Launch Codespaces**:
    * Click the green **Code** button.
    * Select the **Codespaces** tab.
    * Click **Create codespace on main**.

4.  Wait for the environment to load. It creates a full Linux VM with Python pre-installed.

### Verify Copilot

1.  Locate the **Copilot Icon** in the bottom right of VS Code (inside the browser).
2.  Ensure it is active.

-----

## Part 2: Generative CI/CD (20 Mins)

*Goal: Use Copilot Agent Mode to generate the pipeline files automatically.*

Instead of writing YAML manually or copy-pasting, we will ask the AI Agent to create the file for us.

### Step 1: The Agent Prompt

1.  Open **Copilot Chat** **Agent** mode.

2.  Enter the following prompt. Be specific about the filename and requirements!  
**Prompt:**  

    > Create a GitHub Actions workflow file named python-app.yml. It should run on push to the 'main' branch. It needs to install dependencies from requirements.txt, run flake8 for linting, and run tests using pytest. Name the workflow 'Python CI'.

3.  **Review the Plan:** The Agent will analyse your workspace and propose creating a new file path: `.github/workflows/python-app.yml`.

4.  **Accept the Changes:** Click **Keep** or **Accept** (or the checkmark icon) to confirm. The AI will create the folder structure and the file instantly.

### Step 2: Commit and Run

1.  Open the **Source Control** tab (left side).
2.  Stage, Commit ("Add CI pipeline"), and Sync Changes.
3.  Go to your repository on **GitHub.com** (leave the Codespace open).
4.  Click the **Actions** tab.
5.  You should see your "Python CI" workflow running! 🟢

-----

## Part 3: AI in the Terminal (20 Mins)

*Goal: Use Copilot CLI to write shell scripts without knowing the syntax.*

Often, CI pipelines need to do "scripty" things, like verifying specific package versions. This is usually hard to remember.

### Step 1: Enable CLI Helper

In your Codespace terminal, type:

```bash
gh copilot --help
```

If prompted to authenticate, follow the steps. If it says "command not found", standard Copilot Chat can also help here, but the CLI tool is specifically optimised for shell commands.

### Step 2: The "How do I..." Challenge

We want to add a step to our pipeline that prints the version of Flask currently installed.

1.  In the terminal, ask Copilot for the command:

    ```bash
    gh copilot suggest "Command to print the installed version of Flask using pip"
    ```

    *(Or ask Copilot Chat: "Write a bash command to grep the Flask version from pip freeze")*

2.  Copilot will offer a command (likely `pip show Flask` or `pip freeze | grep Flask`). Select **Copy to clipboard**.

### Step 3: Update the Workflow

1.  Open `.github/workflows/python-app.yml`.
2.  **Agent Shortcut:** You can also highlight the file content and ask Copilot Edits: *"Add a step to the build job that prints the Flask version"*.
3.  Alternatively, paste the command manually:
    ```yaml
    - name: Check Flask Version
      run: <PASTE_YOUR_COMMAND_HERE>
    ```
4.  Commit and push.
5.  Watch the Action run on GitHub. Expand the "Check Flask Version" step in the logs to see if it worked.

-----

## Part 4: The "Fix It" Loop (20 Mins)

*Goal: Simulate a failure and use AI to diagnose it.*

A CI pipeline is useless if you can't fix it when it breaks.

### Step 1: Break the Code

1.  Open a test file (e.g., `hello_app/views.py` or create a new test file `tests/test_basic.py`).
      * *If the repo has no tests, use Copilot Agent: "Create a simple failing test for a flask app named tests/test_fail.py"*
2.  Add a failing assertion:
    ```python
    def test_math_fail():
        assert 1 + 1 == 3
    ```
3.  Commit and Push: "Breaking the build".

### Step 2: Analyse with Copilot

1.  Go to the **Actions** tab on GitHub.
2.  Click the failed run 🔴.
3.  Click the **build** job and scroll to the red error lines.
4.  **Highlight the error log** directly in the browser (or copy it).
5.  Go back to VS Code / Codespaces.
6.  Paste the error into Copilot Chat and ask:
    > **Prompt:** "Here is a pytest error from my CI logs. Explain why it failed and point me to the file I need to fix."

### Step 3: The Fix

1.  Copilot should identify that `test_math_fail` failed.
2.  Navigate to that file.
3.  Highlight the broken code and ask Copilot: "Fix this test so it passes."
4.  Accept the fix, commit, and push.
5.  Verify the pipeline turns green 🟢.

-----

## Part 5: Advanced - Security & Autofix (15 Mins)

*Goal: Use AI to find security vulnerabilities.*

If your repository is public (or you have GitHub Advanced Security), you can enable **CodeQL**.

1.  In the **Actions** tab, click **New workflow**.
2.  Search for "CodeQL Analysis".
3.  Copilot can explain what this file does.
    > **Prompt:** "Explain what the 'Analyse' step does in this CodeQL workflow."
4.  Commit this workflow. It will scan your code for vulnerabilities.
5.  **Simulate a Vulnerability:** Add a hardcoded secret to your python file:
    ```python
    # In app.py
    AWS_SECRET_KEY = "AKIA1234567890"
    ```
6.  When CodeQL runs, it will alert you in the **Security** tab.
7.  **Autofix:** Look for the **"Copilot Autofix"** button (if available) to have AI rewrite the code securely automatically (e.g., by suggesting you use an environment variable).

-----

## Part 6: Extension - AI Engineering in CI/CD

*Goal: Use the `ai-inference` action to "think" inside your pipeline.*

We will create a workflow that uses an LLM to automatically categorise new Issues opened in your repository.

### Step 1: The "Triage" Workflow

1.  Open **Copilot Edits / Agent Mode** (`Ctrl+Shift+I`).

2.  Enter the prompt:

    > **Prompt:** "Create a new GitHub Action workflow file named ai-triage.yml. It should trigger when an issue is opened. It should use the 'actions/ai-inference@v1' action to analyse the issue title and body, determining if it is a Bug, Feature, or Question. Print the result to the logs."

3.  **Refine the Code:** If needed, paste this YAML configuration:

    ```yaml
    name: AI Issue Triage
    on:
      issues:
        types: [opened]

    jobs:
      triage:
        runs-on: ubuntu-latest
        permissions:
          issues: write
        steps:
          - name: Check Issue Context
            run: echo "New issue opened: ${{ github.event.issue.title }}"

          - name: AI Classification
            uses: actions/ai-inference@v1
            id: classify
            with:
              model: 'gpt-4o-mini' 
              prompt: |
                Analyse this issue:
                Title: ${{ github.event.issue.title }}
                Body: ${{ github.event.issue.body }}
                
                Is this a 'Bug', 'Feature', or 'Question'? Respond with only one word.
            env:
              GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          
          - name: Print Classification
            run: echo "The AI thinks this is a ${{ steps.classify.outputs.answer }}"
    ```

4.  Commit and test by creating a new issue.

-----

## Part 7: The AI Teammate (Issues & PRs)

*Goal: Delegate tasks to Copilot and get automated code reviews.*

In this section, we will treat Copilot not just as a chat bot, but as an agent that can perform work on its own.

### Step 1: Assign an Issue to Copilot

1.  Go to the **Issues** tab on GitHub.
2.  Click **New Issue**.
3.  **Title:** "Create a README file"
4.  **Description:** "Please add a README.md file to the repository. It should explain that this is a Python Flask app for a CI/CD lab. Include instructions on how to install requirements and run the tests."
5.  **Submit** the issue.
6.  **Assign it:** Look at the right-hand sidebar. Click **Assignees** and select **Copilot** (or type `@copilot` in a comment).
7.  **Watch the Magic:**
      * Refresh the page after 10-20 seconds.
      * Copilot will comment with a plan.
      * Copilot will automatically open a **Pull Request** with the code written!

### Step 2: Automated Copilot Review

Now, let's see if Copilot can critique *our* code.

1.  Go back to VS Code (Codespaces).
2.  Create a new branch: `git checkout -b bad-code-branch`.
3.  Add some "questionable" code to `app.py` (or any python file):
    ```python
    # Adding a debug print that shouldn't be in production
    def potentially_slow_function():
        print("DEBUG: Starting function...") 
        import time
        time.sleep(1) # Hardcoded delay
        return True
    ```
4.  Commit and Push:
    ```bash
    git add .
    git commit -m "Add feature with debug logs"
    git push origin bad-code-branch
    ```
5.  Go to GitHub and **Open a Pull Request**.
6.  **Request a Review:**
      * On the PR page, look at the **Reviewers** sidebar on the right.
      * Click the gear icon and select **Copilot**.
      * *(Note: If you don't see Copilot in the list, ensure you have a paid Copilot seat or Student Pack active).*
7.  **Read the Review:** Copilot will analyse your diff and post comments about the `print` statement (suggesting logging instead) and the `time.sleep` (performance warning).

-----

## 📝 Summary Checklist

  - [ ] Created a workflow using **Copilot Agent Mode**.
  - [ ] Used `gh copilot` to write a shell script step.
  - [ ] Diagnosed a CI log error using Copilot Chat.
  - [ ] Assigned a GitHub Issue to `@copilot` and merged the resulting PR.
  - [ ] Received an automated Code Review from Copilot on a Pull Request.

-----