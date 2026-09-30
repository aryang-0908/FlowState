# FlowState

**FlowState** is a Python-based terminal productivity application designed to help users maintain focused work sessions directly from the command line.

The application provides three different focus modes: **Zoned Focus**, **Infinite Focus**, and **Pomodoro Focus**. It also records focus sessions using a local SQLite database, allowing users to review their focus history.

FlowState is built entirely with Python's standard library and does not require a graphical user interface or external Python packages.

## Features

### Zoned Focus

Set a specific amount of time for a focus session.

For example, you can choose a 30-minute session, and FlowState will run a countdown until the session is complete.

### Infinite Focus

Start a focus session without setting a time limit.

The timer continues until the user manually stops the session using `Ctrl + C`.

### Pomodoro Focus

Use the Pomodoro technique with:

* 25 minutes of focused work
* 5 minutes of break
* Multiple sessions can be selected

A break is provided between focus sessions, but the final session does not start an additional break.

### Focus History

FlowState stores session information in an SQLite database.

The history includes:

* Session ID
* Focus mode
* Start time
* End time
* Duration
* Completion status

## Project Structure

```text
FlowState/
│
├── main.py
├── timer.py
├── database.py
├── .gitignore
├── README.md
└── statement.md
```

### File Description

| File           | Purpose                                                  |
| -------------- | -------------------------------------------------------- |
| `main.py`      | Contains the main menu and controls the application flow |
| `timer.py`     | Contains the focus modes and timer functionality         |
| `database.py`  | Handles SQLite database creation, storage, and history   |
| `.gitignore`   | Specifies files that should not be tracked by Git        |
| `README.md`    | Project documentation                                    |
| `statement.md` | Project statement and overview                           |

The SQLite database file `focus_history.db` is generated automatically when the application runs.

## Main Menu

When FlowState starts, the user is presented with the following menu:

```text
========================================
            FOCUS PROGRAM
========================================

1.) Zoned Focus
2.) Infinite Focus
3.) Pomodoro Focus
4.) View History
5.) Exit

Choose an option:
```

The user can select a focus mode, view their previous sessions, or exit the application.

## Technologies Used

* **Python 3**
* **SQLite**
* `time`
* `datetime`
* `sqlite3`

No external Python packages are required.

## Requirements

To run FlowState, you need:

* Python 3.x
* A terminal or command-line environment

FlowState can be used with:

* VS Code Terminal
* Windows Command Prompt
* PowerShell
* Linux Terminal
* macOS Terminal

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/FlowState.git
```

Enter the project directory:

```bash
cd FlowState
```

Run the application:

```bash
python main.py
```

On some systems, use:

```bash
python3 main.py
```

## How to Use

### 1. Start FlowState

Run:

```bash
python main.py
```

### 2. Select a Focus Mode

Choose one of the available options from the main menu.

### 3. Complete Your Focus Session

Follow the timer and focus on your work.

For Infinite Focus, use:

```text
Ctrl + C
```

to stop the session.

### 4. View Your History

Select:

```text
4.) View History
```

to see previously recorded sessions.

## Database

FlowState uses SQLite to store focus-session data.

The database is created automatically when the application starts. No manual database setup is required.

The database stores information such as:

```text
ID
Mode
Start Time
End Time
Duration
Completion Status
```

The database file is intentionally excluded from Git so that personal focus history is not uploaded to the repository.

## Learning Objectives

FlowState was developed as a practical Python project to learn and apply:

* Functions
* Loops
* Conditional statements
* Exception handling
* User input validation
* Python modules
* Date and time handling
* Countdown timers
* SQLite databases
* File and project organization
* Git and GitHub

## Future Improvements

Possible future improvements include:

* Pause and resume functionality
* Sound notifications
* Custom Pomodoro durations
* Daily and weekly statistics
* Focus streaks
* Productivity reports
* Improved terminal interface
* More detailed session analytics

## License

This project is currently intended for personal and educational use.

---

**FlowState — Focus. Work. Repeat.**
