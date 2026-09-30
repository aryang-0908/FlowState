# FlowState — Project Statement

## Project Name

**FlowState**

## Introduction

FlowState is a Python-based terminal productivity application designed to help users manage focused work sessions.

The project provides a simple command-line environment where users can choose different focus techniques and track their completed sessions. The application is designed to be lightweight, easy to use, and accessible without requiring a graphical user interface.

## Problem Statement

Maintaining consistent focus while working or studying can be difficult. Users may lose track of how long they have been working, take unplanned breaks, or lack a simple way to review their previous focus sessions.

FlowState addresses this by providing structured focus timers and a session history system in a single terminal-based application.

## Objectives

The main objectives of FlowState are:

1. Provide a simple terminal-based focus timer.
2. Allow users to choose between different focus techniques.
3. Provide customizable timed focus sessions.
4. Support unlimited focus sessions.
5. Implement the Pomodoro technique.
6. Record focus-session information for later review.
7. Store session data using SQLite.
8. Practice Python programming and modular software development.

## Focus Modes

### Zoned Focus

Zoned Focus allows the user to specify the duration of a focus session.

The application starts a countdown based on the selected duration. When the countdown reaches zero, the session is recorded as completed.

### Infinite Focus

Infinite Focus allows the user to start working without specifying a predefined duration.

The timer continues until the user manually stops the session. The total elapsed time is then recorded.

### Pomodoro Focus

Pomodoro Focus implements a basic Pomodoro workflow.

Each cycle consists of:

```text
25 minutes of focus
5 minutes of break
```

The user can select the number of focus sessions they want to complete.

## Focus History

FlowState uses SQLite to store information about focus sessions.

Each recorded session can contain:

* Unique session ID
* Focus mode
* Start time
* End time
* Duration
* Completion status

This allows users to review their previous focus activity directly from the application.

## Technology Stack

The project uses Python and its standard library.

### Python

Python is used to implement the application's logic, user interaction, timers, and database operations.

### SQLite

SQLite is used as the local database for storing focus-session records.

### Standard Python Modules

The project uses modules including:

* `time`
* `datetime`
* `sqlite3`

No external dependencies are required.

## Project Architecture

FlowState separates different responsibilities into individual Python files.

### `main.py`

Responsible for:

* Displaying the main menu
* Receiving user input
* Selecting the requested feature
* Controlling the overall application flow

### `timer.py`

Responsible for:

* Countdown functionality
* Zoned Focus
* Infinite Focus
* Pomodoro Focus
* Recording completed sessions

### `database.py`

Responsible for:

* Creating the SQLite database
* Creating the sessions table
* Saving session records
* Retrieving focus history

This separation makes the project easier to understand, maintain, and expand.

## Expected Outcome

The expected outcome of FlowState is a functional command-line productivity application that allows users to run focus sessions and maintain a local history of their activity.

The project also demonstrates practical knowledge of Python programming, modular design, exception handling, timers, and database management.

## Learning Outcomes

Through the development of FlowState, the following programming concepts are practiced:

* Variables and data types
* Functions
* Loops
* Conditional statements
* Exception handling
* User input
* Modules and imports
* Date and time operations
* SQLite database operations
* Basic application architecture
* Git and GitHub

## Future Scope

FlowState can be extended with additional functionality in future versions, including:

* Pause and resume controls
* Customizable Pomodoro durations
* Sound notifications
* Daily and weekly focus statistics
* Focus streak tracking
* Productivity summaries
* Improved terminal formatting
* Data visualization
* Additional focus modes

## Conclusion

FlowState is a practical Python project that combines productivity tools with fundamental software-development concepts.

By providing multiple focus modes and persistent session history, the application creates a simple environment for managing focused work while also serving as a hands-on project for learning Python, SQLite, modular programming, and Git-based project management.
