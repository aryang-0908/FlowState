from timer import zoned_focus, infinite_focus, pomodoro_focus
from database import show_history


def show_menu():
    print("\n" + "=" * 40)
    print("            FOCUS PROGRAM")
    print("=" * 40)
    print()
    print("1.) Zoned Focus")
    print("2.) Infinite Focus")
    print("3.) Pomodoro Focus")
    print("4.) View History")
    print("5.) Exit")
    print()


def main():

    while True:

        show_menu()

        choice = input("Choose an option: ").strip()

        if choice == "1":
            zoned_focus()

        elif choice == "2":
            infinite_focus()

        elif choice == "3":
            pomodoro_focus()

        elif choice == "4":
            show_history()

        elif choice == "5":
            print("\nGoodbye - Stay Focused!")
            break

        else:
            print("\nInvalid option. Please choose 1-5.")


if __name__ == "__main__":
    main()