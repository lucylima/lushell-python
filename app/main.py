import sys


def main():
    builtin_commands = ['cd', 'echo', 'type', 'exit']
    while True:
        sys.stdout.write("$ ")
        user_input = input()

        user_input = user_input.split()

        command = user_input[0]
        args = user_input[1:]

        match command:
            case "cd":
                pass
                
            case "echo":
                result = " ".join(args)
                sys.stdout.write(f"{result}\n")

            case "exit":
                sys.exit(0)

            case "type":
                if args[0] in builtin_commands:
                    sys.stdout.write(f"{args[0]} is a shell builtin\n")
                else:
                    sys.stdout.write(f"{args[0]} not found\n")
            
            case _:
                sys.stdout.write(f'{command}: command not found\n')


if __name__ == "__main__":
    main()
