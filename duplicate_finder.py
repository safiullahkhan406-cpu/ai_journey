import hashlib
from pathlib import Path
from collections import defaultdict

# Folder select kiya
folder = Path("my_files")

# Duplicate files store karne ke liye
file_hashes = defaultdict(list)

# Folder ki tamam files check karo
for file in folder.rglob("*"):

    if file.is_file():

        # File ka hash calculate karo
        file_hash = hashlib.sha256(
            file.read_bytes()
        ).hexdigest()

        # Hash ke against file save karo
        file_hashes[file_hash].append(str(file))

# Duplicate report
with open("duplicate_report.txt", "w") as report:

    for files in file_hashes.values():

        if len(files) > 1:

            print("\nDuplicate Found:")

            report.write("Duplicate Found:\n")

            for file in files:

                print(file)
                report.write(file + "\n")

print("\nDuplicate checking completed!")
