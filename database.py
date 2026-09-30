import sqlite3


DATABASE_NAME = "focus_history.db"


def create_database():

    connection = sqlite3.connect(DATABASE_NAME)

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sessions (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            mode TEXT NOT NULL,

            start_time TEXT NOT NULL,

            end_time TEXT NOT NULL,

            duration INTEGER NOT NULL,

            completed INTEGER NOT NULL

        )
    """)

    connection.commit()

    connection.close()


def save_session(
    mode,
    start_time,
    end_time,
    duration,
    completed
):

    connection = sqlite3.connect(DATABASE_NAME)

    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO sessions (
            mode,
            start_time,
            end_time,
            duration,
            completed
        )

        VALUES (?, ?, ?, ?, ?)
    """, (
        mode,
        start_time.isoformat(),
        end_time.isoformat(),
        duration,
        int(completed)
    ))

    connection.commit()

    connection.close()


def show_history():

    connection = sqlite3.connect(DATABASE_NAME)

    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            id,
            mode,
            start_time,
            duration,
            completed
        FROM sessions
        ORDER BY id DESC
    """)

    sessions = cursor.fetchall()

    connection.close()

    print("\n======================================")
    print("             FOCUS HISTORY")
    print("======================================")

    if not sessions:

        print("\nNo focus sessions recorded yet.\n")

        return

    for session in sessions:

        session_id = session[0]
        mode = session[1]
        start_time = session[2]
        duration = session[3]
        completed = session[4]

        minutes = duration // 60
        seconds = duration % 60

        if completed:
            status = "Completed"
        else:
            status = "Stopped"

        print(f"""
ID:       {session_id}
Mode:     {mode}
Started:  {start_time}
Duration: {minutes}m {seconds}s
Status:   {status}
--------------------------------------
""")


# Create the database when this file is loaded.

create_database()