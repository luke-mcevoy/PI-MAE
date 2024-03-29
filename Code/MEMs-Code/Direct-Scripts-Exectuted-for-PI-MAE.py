import subprocess

file_path = "Direct-scripts.txt"

with open(file_path, "w") as file:
    for item in scripts:
        file.write(item + "\n")

file.close()

print(f"The list has been written to {file_path}")

try:
    with open(file_path, "r") as file:
        # Read all lines from the file into a list
        lines = file.readlines()

    # Remove trailing newline characters from each line and create a list
    commands = [line.strip() for line in lines]

    # Print or use the list as needed
    print("Lines as a list:")
    print(commands)
    
    for command in commands:
        try:
            # Execute the command in the shell
            subprocess.run(command, shell=True, check=True)
        except subprocess.CalledProcessError as e:
            print(f"Command failed with error: {e}")


except FileNotFoundError:
    print(f"The file '{file_path}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")
