with open("random_file.txt", "r") as f:
    print(f.read())

# Encoding UTF-8
with open("random_file.txt", "r", encoding="utf-8") as f:
    print(f.read())
# Reading line by line
with open("random_file.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line)

# Writing to a file
with open("random_file_w.txt", "w") as f:
    f.write("Hello World")
# Appending to a file
with open("random_file_a.txt", "a") as f:
    f.write("Hello World")