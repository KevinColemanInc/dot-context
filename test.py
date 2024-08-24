import sys


def main():
    print("Arguments passed to the script:")
    for i, arg in enumerate(sys.argv):
        print(f"Argument {i}: {arg}")


if __name__ == "__main__":
    main()
