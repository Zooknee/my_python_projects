import os
from pathlib import Path

project_name = "Demoproject"
folders = ["src", "doc", "tests"]

Path(project_name).mkdir(exist_ok=True)
print(f"Created main folder: {project_name}")


for folder in folders:
    path = Path(project_name) / folder
    path.mkdir(exist_ok=True)
    print(f"Created subfolder: {path}")

for folder in folders:
    readme_path = Path(project_name) / folder / "README.txt"
    with open(readme_path, "w") as f:
        f.write(f"This is the README for the {folder} folder.\n")
    print(f"Created README in: {readme_path}")


print("\nFolder Project Summary:")
for path in Path(project_name).rglob("*"):
    if path.is_dir():
        print(f"DIR : {path}")
    else:
        print(f"FILE: {path}")

summary_path = Path(project_name) / "summary.txt"
with open(summary_path, "w") as summary:
    summary.write("Folder Project Summary\n\n")
    for path in Path(project_name).rglob("*"):
        if path.is_dir():
            summary.write(f"DIR : {path}\n")
        else:
            summary.write(f"FILE: {path}\n")

print(f"\nSaved summary to: {summary_path}")
