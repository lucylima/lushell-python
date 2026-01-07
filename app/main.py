import sys


def main():
    while True:
        sys.stdout.write("$ ")
        command = input()
        match command:
            case "cd":
                pass
            case "echo":
                pass
            case "exit":
                sys.exit(0)
            case _:
                sys.stdout.write(f'{command}: command not found\n')


if __name__ == "__main__":
    main()
