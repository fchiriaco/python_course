import os

print(os.getcwd())
print(os.listdir("."))

file_path = "data.csv"
if os.path.exists(file_path):
    print(f"File found: {file_path}")
else:
    print(f"File not found: {file_path}")

print(os.path.join("data", "sales", "2026.csv"))