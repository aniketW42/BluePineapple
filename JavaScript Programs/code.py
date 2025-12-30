import os

for i in range(1, 13):
    file_path = f"assignment{i}"

    os.mkdir(file_path)
    print(f"File '{file_path}' created successfully.")
