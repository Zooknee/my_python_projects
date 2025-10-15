import os

path = "/etc"  # Linux folder to analyze
extensions = [".conf", ".sh", ".service"]

for ext in extensions:                 # Outer loop: file types
    count = 0
    for file in os.listdir(path):      # Inner loop: files in folder
        if file.endswith(ext):
            count += 1
    print(f"{ext} files: {count}")
