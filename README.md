# Library Management System

A small, dependency-free Python console application that displays a book catalog and lets a user issue an available book to a named borrower.

## Requirements and run

- Python 3.8 or newer
- Git for the version-control exercises
- A GitHub account for the remote-repository exercises

Run from this folder:

```powershell
python library.py
```

The sample catalog is stored in memory. An issue changes the book's status for the current run only; the application does not write to a database or file.

## Project structure

```text
LibraryManagementSystem/
|-- .gitignore
|-- README.md
`-- library.py
```

## Git and GitHub exercise

Run the commands below in PowerShell. Replace `<your-username>` with your GitHub username. The displayed outputs are examples; Git's exact wording, hashes, and branch names can differ.

### 1. Create the project directory and initialize Git

If you are starting from outside the project folder:

```powershell
mkdir LibraryManagementSystem
cd LibraryManagementSystem
git init -b main
```

If you are using the already-created project folder, instead run:

```powershell
cd D:\ling\LibraryManagementSystem
git init -b main
```

Example:

```text
Initialized empty Git repository in .../LibraryManagementSystem/.git/
```

If an older Git version does not support `git init -b main`, use `git init` followed by `git branch -M main`.

### 2. Create and run the initial catalog program

For the first commit in this exercise, use this starter `library.py`:

```python
books = [
    {"name": "The Hobbit", "author": "J. R. R. Tolkien", "price": 499.00},
    {"name": "Pride and Prejudice", "author": "Jane Austen", "price": 350.00},
    {"name": "The Alchemist", "author": "Paulo Coelho", "price": 299.00},
]

for book in books:
    print(f"Book Name: {book['name']}")
    print(f"Author: {book['author']}")
    print(f"Price (INR): {book['price']:.2f}")
    print()
```

Save and run it with `python library.py`. The complete final version is the `library.py` included in this project and is introduced on the `book-issue` branch in step 8.

### 3. Check status and make the initial commit

```powershell
git status
git add library.py
git status
git commit -m "Initial library project"
```

Example status before staging:

```text
On branch main
Untracked files:
  library.py
```

Example status after staging:

```text
On branch main
Changes to be committed:
  new file:   library.py
```

Example commit:

```text
[main (root-commit) a1b2c3d] Initial library project
 1 file changed, 14 insertions(+)
```

If Git reports that your identity is unknown, configure your own identity for this repository and retry:

```powershell
git config user.name "Your Name"
git config user.email "you@example.com"
```

Use the email you want associated with this commit. You can omit `--global` to set the identity only for this repository.

### 4. Create the GitHub repository

1. Sign in at [github.com](https://github.com).
2. Select **New repository** (or **+** > **New repository**).
3. Enter **LibraryManagementSystem** as the repository name.
4. Choose Public or Private.
5. To avoid a first-push history conflict, leave **Add a README**, **Add .gitignore**, and **Choose a license** unchecked. The local project already has a README and `.gitignore`.
6. Select **Create repository**.

### 5. Connect the local repository and push `main`

Copy the HTTPS URL shown by GitHub, then run:

```powershell
git remote add origin https://github.com/<your-username>/LibraryManagementSystem.git
git remote -v
git push -u origin main
```

Example remote listing:

```text
origin  https://github.com/<your-username>/LibraryManagementSystem.git (fetch)
origin  https://github.com/<your-username>/LibraryManagementSystem.git (push)
```

On success, Git reports that `main` is tracking `origin/main`. GitHub may ask you to authenticate using a browser, Git Credential Manager, or another configured credential helper; do not put a password or token directly into the remote URL.

### 6. Display commit history

```powershell
git log --oneline --decorate
```

Example:

```text
a1b2c3d (HEAD -> main, origin/main) Initial library project
```

### 7. Create and switch to `book-issue`

```powershell
git switch -c book-issue
```

Example:

```text
Switched to a new branch 'book-issue'
```

### 8. Add book-issue functionality and commit

Replace the starter `library.py` with the complete `library.py` supplied in this project. It uses `display_books`, `issue_book`, and `main` functions; prompts the user for a menu selection, book ID, and borrower name; and reports unavailable or invalid books.

Run and test it:

```powershell
python library.py
```

Then stage and commit the change:

```powershell
git status
git add library.py
git commit -m "Add book issue functionality"
git log --oneline --decorate
```

Example history:

```text
b2c3d4e (HEAD -> book-issue) Add book issue functionality
a1b2c3d (origin/main, main) Initial library project
```

### 9. Push the feature branch

```powershell
git push -u origin book-issue
```

Example:

```text
branch 'book-issue' set up to track 'origin/book-issue'.
```

This pushes the branch; it does not merge it into `main`. To include the feature in `main`, open a pull request on GitHub and merge it.

### 10. Clone into another folder

Run this from the parent directory where you want the clone created. The following example clones the repository's default branch (`main`):

```powershell
cd D:\ling
git clone https://github.com/<your-username>/LibraryManagementSystem.git LibraryManagementSystem-clone
cd LibraryManagementSystem-clone
git branch --all
```

Example:

```text
Cloning into 'LibraryManagementSystem-clone'...
* main
  remotes/origin/HEAD -> origin/main
  remotes/origin/book-issue
  remotes/origin/main
```

To check out the feature branch in the clone:

```powershell
git switch --track origin/book-issue
```

### 11. Simulate a change on GitHub and pull it

To demonstrate pulling a remote update, make a small edit directly on GitHub (for example, add a sentence to `README.md`) and select **Commit changes** on the repository's `main` branch. Then, in the local clone, run:

```powershell
git switch main
git pull origin main
```

Example:

```text
From https://github.com/<your-username>/LibraryManagementSystem
 * branch            main       -> FETCH_HEAD
Updating a1b2c3d..c3d4e5f
Fast-forward
 README.md | 1 +
 1 file changed, 1 insertion(+)
```

`git pull` fetches remote commits and integrates them into the currently checked-out branch. If you made conflicting local edits, Git will report a merge conflict that must be resolved before completing the pull.

## Sample console session

```text
Library Management System
1. Display books
2. Issue a book
3. Exit
Choose an option (1-3): 2
Enter the book ID to issue: B001
Enter the borrower's name: Alex
Issued 'The Hobbit' to Alex.
```

## Sample screenshots to capture

These are descriptions for screenshots to capture during the exercise; no screenshots are included in this repository.

1. **Project folder:** File Explorer showing `LibraryManagementSystem` with `library.py`, `README.md`, and `.gitignore`.
2. **Program run:** Terminal showing the menu and the displayed book names, authors, INR prices, and availability.
3. **Git initialization/status:** Terminal showing `git init -b main` and `git status` before staging.
4. **Staging and initial commit:** Terminal showing staged `library.py` and the `Initial library project` commit.
5. **GitHub repository:** Browser showing the repository named `LibraryManagementSystem` and its `main` branch.
6. **Remote and history:** Terminal showing `git remote -v`, a successful push, and `git log --oneline`.
7. **Feature branch:** Terminal showing the `book-issue` branch and a successful issue interaction.
8. **Feature push:** Terminal showing `git push -u origin book-issue` and the branch on GitHub.
9. **Clone:** Terminal and File Explorer showing the separate `LibraryManagementSystem-clone` folder.
10. **Pull:** GitHub showing the README edit and the clone terminal showing `git pull origin main`.

