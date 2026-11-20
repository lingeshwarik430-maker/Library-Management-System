# Library Management System — GitHub Submission Guide

## Project summary

This Python console application displays a sample book catalog with each book's
name, author, price in INR, and availability. It also lets a user issue an
available book to a named borrower. Issue information is held in memory and is
reset when the program exits.

Run the application from the project folder:

```powershell
python library.py
```

## Important: current project state

The supplied project already contains the complete book-issue functionality.
It is not currently a Git repository and has no commits or GitHub remote. To
show the assignment's requested history (a display-only initial commit followed
by the issue feature on `book-issue`), first save the current `library.py`
outside the project, temporarily use the starter program below for the initial
commit, and restore the saved program on the feature branch.

Run all commands in PowerShell. Replace `<your-username>` with your GitHub
username. Do not include angle brackets in the actual URL.

## 1. Prepare the display-only version

Open PowerShell in the project folder:

```powershell
cd D:\ling\LibraryManagementSystem
Copy-Item .\library.py ..\library-final.py
```

Open `library.py` and replace its contents with this initial catalog-only
program, then save:

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

Check that it runs:

```powershell
python .\library.py
```

## 2. Initialize Git and make the initial commit

```powershell
git init -b main
git status
git add .\library.py .\README.md .\.gitignore .\SUBMISSION_GUIDE.md
git status
git commit -m "Initial library project"
git status
```

If Git does not accept `git init -b main`, run `git init` and then
`git branch -M main`. If Git asks for your identity, set it for this repository
and retry the commit:

```powershell
git config user.name "Your Name"
git config user.email "you@example.com"
```

Use the name and email you want associated with the commit.

## 3. Create the GitHub repository and push `main`

1. Sign in at [GitHub](https://github.com).
2. Select **New repository** and name it `LibraryManagementSystem`.
3. Choose Public or Private. Leave the options to create a README, `.gitignore`,
   or license unchecked; these files already exist locally.
4. Create the repository and copy its HTTPS URL.

Back in PowerShell, connect and push:

```powershell
git remote add origin https://github.com/<your-username>/LibraryManagementSystem.git
git remote -v
git push -u origin main
git log --oneline --decorate
```

Complete GitHub's authentication prompt if one appears. Never put a GitHub
password or access token directly in the remote URL.

## 4. Add and push the book-issue feature

Create the required branch:

```powershell
git switch -c book-issue
```

Restore the complete program that was saved before the initial commit:

```powershell
Copy-Item ..\library-final.py .\library.py
python .\library.py
```

Test displaying the books and issuing an available book. Then commit and push:

```powershell
git status
git add .\library.py
git commit -m "Add book issue functionality"
git log --oneline --decorate
git push -u origin book-issue
```

The feature branch is pushed separately; it is not automatically merged into
`main`.

## 5. Clone the repository into another folder

Run these commands from the parent folder:

```powershell
cd D:\ling
git clone https://github.com/<your-username>/LibraryManagementSystem.git LibraryManagementSystem-clone
cd .\LibraryManagementSystem-clone
git branch --all
```

The clone initially checks out the repository's default branch. To view the
feature branch in the clone:

```powershell
git switch --track origin/book-issue
```

## 6. Make a GitHub edit and pull it locally

On GitHub, switch to the `main` branch, open `README.md`, add a short sentence
such as `Updated on GitHub for the pull exercise.`, and commit the change.

Then update the clone's local `main` branch:

```powershell
git switch main
git pull origin main
git log --oneline --decorate
```

## Screenshot checklist

Capture screenshots from your own terminal and GitHub account; sample outputs
in a guide are not proof that commands were run.

1. Project folder showing `library.py`, `README.md`, and `.gitignore`.
2. Catalog-only program output.
3. `git init` and `git status`.
4. Staged files and the `Initial library project` commit.
5. GitHub repository page with the `main` branch.
6. `git remote -v`, successful `main` push, and `git log`.
7. `book-issue` branch and a successful book-issue interaction.
8. Feature commit, successful feature-branch push, and branch visible on GitHub.
9. The separate `LibraryManagementSystem-clone` folder.
10. The GitHub README edit and successful `git pull origin main`.

## Submission details

- GitHub repository URL: `https://github.com/<your-username>/LibraryManagementSystem`
- Screenshots: attach the screenshots listed above when submitting.
