# Automatic File Backup System

from pathlib import Path
import shutil
from datetime import datetime

# Original folder ka path
source_folder = Path("my_files")

# Backup folder ka path
backup_folder = Path("backups")

# Backup function
def create_backup():

    try:
        # Agar original folder nahi hai
        if not source_folder.exists():
            print("Source folder not found!")
            return

        # Backup folder create karna
        backup_folder.mkdir(exist_ok=True)

        # Current date aur time lena
        backup_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

        # Naya backup folder banana
        new_backup = backup_folder / backup_time
        new_backup.mkdir()

        # Original folder ki files read karna
        files = list(source_folder.iterdir())

        # Har file ki copy banana
        for file in files:

            if file.is_file():

                shutil.copy2(file, new_backup / file.name)

                print("Backed up:", file.name)

        print("\nBackup completed successfully!")

    except Exception as error:

        print("Error:", error)


# Function call karna
create_backup()
