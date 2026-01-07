import sys


def main():
    while True:
        sys.stdout.write("$ ")
        command = input()

        command = command.split()

        match command[0]:
            case "cd":
                pass
            case "echo":
                result = " ".join(command[1:])
                sys.stdout.write(f"{result}\n")
                
            case "exit":
                sys.exit(0)
            case _:
                sys.stdout.write(f'{command}: command not found\n')


if __name__ == "__main__":
    main()
