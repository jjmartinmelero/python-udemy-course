file_name = "my_file.txt"

with open(file_name, "w") as file:

    file.write("Hello, how are you ?")
    file.write("\nMore info")

print(f"{file_name} has been created")


file_name_exclusive = "my_file_exclusive.txt"

try:

    with open(file_name_exclusive, "x") as file_exclusive:
        file_exclusive.write("Hello, how are you ?")
        file_exclusive.write("\nMore info")

    print("file exclusive created !")

except FileExistsError as e:
    print("File exist")
    print(f"detail: {e}")


# read file
with open(file_name, "r") as file:
    lines = file.readlines()
    
    for line in lines:
        print(line.strip())

## use read
with open(file_name, "r") as file:
    print(file.read().strip())

try:
    # append file
    with open(file_name_exclusive, "a") as file:
        file.write("append info")
except Exception as e:
    print(e)

print("append info to file")

