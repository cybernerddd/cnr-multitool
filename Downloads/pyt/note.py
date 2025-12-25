import os

path = input("What's your folder path: ")

items = os.listdir(path)

with open("results.txt", "w") as results:
    for item in items:
        full_path = os.path.join(path, item)
        results.write(full_path + "\n")

print("Done! saved as results.txt")