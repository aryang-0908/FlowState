import time
from datetime import datetime

from database import save_session


def format_time(seconds):
    """
    Convert seconds into MM:SS format.
    """

    minutes = seconds // 60
    seconds = seconds % 60

    return f"{minutes:02d}:{seconds:02d}"


def countdown(seconds, label):
    """
    Run a countdown timer.
    """

    while seconds > 0:

        print(
            f"\r{label}: {format_time(seconds)}",
            end="",
            flush=True
        )

        time.sleep(1)

        seconds -= 1

    print(f"\r{label}: 00:00")


def zoned_focus():

    print("\n========== ZONED FOCUS ==========")

    while True:

        try:

            minutes = int(
                input("Enter focus duration in minutes: ")
            )

            if minutes <= 0:
                print("Duration must be greater than 0.")
                continue

            break

        except ValueError:

            print("Please enter a valid number.")

    print(f"\nStarting {minutes}-minute focus session.")
    print("Press Ctrl+C if you want to stop.\n")

    start_time = datetime.now()

    try:

        countdown(
            minutes * 60,
            "Focus"
        )

        end_time = datetime.now()

        save_session(
            mode="Zoned Focus",
            start_time=start_time,
            end_time=end_time,
            duration=minutes * 60,
            completed=True
        )

        print("\n✓ Focus session completed!")

    except KeyboardInterrupt:

        end_time = datetime.now()

        elapsed = int(
            (end_time - start_time).total_seconds()
        )

        save_session(
            mode="Zoned Focus",
            start_time=start_time,
            end_time=end_time,
            duration=elapsed,
            completed=False
        )

        print("\n\nSession stopped.")


def infinite_focus():

    print("\n========== INFINITE FOCUS ==========")
    print("Press Ctrl+C to end the session.\n")

    start_time = datetime.now()

    seconds = 0

    try:

        while True:

            print(
                f"\rFocus Time: {format_time(seconds)}",
                end="",
                flush=True
            )

            time.sleep(1)

            seconds += 1

    except KeyboardInterrupt:

        end_time = datetime.now()

        print("\n\n✓ Focus session ended!")

        save_session(
            mode="Infinite Focus",
            start_time=start_time,
            end_time=end_time,
            duration=seconds,
            completed=True
        )


def pomodoro_focus():

    print("\n========== POMODORO FOCUS ==========")

    while True:

        try:

            sessions = int(
                input("How many Pomodoro sessions? ")
            )

            if sessions <= 0:
                print("Number of sessions must be greater than 0.")
                continue

            break

        except ValueError:

            print("Please enter a valid number.")

    total_focus_time = 0

    for session in range(1, sessions + 1):

        print(
            f"\n========== SESSION {session}/{sessions} =========="
        )

        # -------------------------
        # 25 MINUTE FOCUS
        # -------------------------

        print("\nFocus period started.")

        start_time = datetime.now()

        try:

            countdown(
                25 * 60,
                "Focus"
            )

        except KeyboardInterrupt:

            print("\n\nPomodoro stopped.")

            return

        end_time = datetime.now()

        total_focus_time += 25 * 60

        save_session(
            mode="Pomodoro Focus",
            start_time=start_time,
            end_time=end_time,
            duration=25 * 60,
            completed=True
        )

        print("\n✓ Focus period completed!")

        # -------------------------
        # 5 MINUTE BREAK
        # -------------------------

        # Don't start a break after the final session

        if session < sessions:

            print("\nBreak period started.")

            try:

                countdown(
                    5 * 60,
                    "Break"
                )

            except KeyboardInterrupt:

                print("\n\nPomodoro stopped.")

                return

            print("\n✓ Break completed!")

    print("\n======================================")
    print("       POMODORO COMPLETED!")
    print("======================================")

    print(
        f"Total focus time: "
        f"{total_focus_time // 60} minutes"
    )