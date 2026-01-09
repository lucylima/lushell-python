import sys
import os
import subprocess

builtin_commands = ['cd', 'echo', 'type', 'exit', 'pwd']

def main():
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
                    continue

                env = os.getenv("PATH", "Path not found")
                env = env.split(':')

                for folder in env:
                    arg_exec = os.path.join(folder, args[0])

                    if os.access(arg_exec, os.X_OK):
                        sys.stdout.write(f"{args[0]} is {arg_exec}\n")
                        break
                    else:
                        continue
                else:
                    sys.stdout.write(f"{args[0]} not found\n")

            case "pwd":
                current_working_directory = os.getcwd()
                sys.stdout.write(f"{current_working_directory}\n")

            case _:
                result = find_exec(command, args)
                if result == 1:
                    sys.stdout.write(f'{command}: command not found\n')
                elif result == 2:
                    sys.stdout.write("System path not found\n")

def find_exec(command, args):
    env = os.getenv("PATH", "Path not found")

    if env == "Path not found":
        return 2

    env = env.split(':')

    for folder in env:
        exec = os.path.join(folder, command)

        full_command = [command, *args]

        if os.access(exec, os.X_OK):
            subprocess.run(full_command)
            return 0
        else:
            continue
    return 1
 

if __name__ == "__main__":
    main()
