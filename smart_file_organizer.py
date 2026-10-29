from pathlib import Path  # Files aur folders ke paths handle karne ke liye
import shutil  # Files ko ek jagah se doosri jagah move karne ke liye
# File extensions ke mutabiq folders define kar rahe hain
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".csv"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi"],
    "Audio": [".mp3", ".wav", ".aac", ".m4a"],
    "Code": [".py", ".js", ".html", ".css", ".json"],
    "Archives": [".zip", ".rar", ".7z", ".tar"]
}
def organize_files(folder_path):
    # Diye gaye path ko Path object mein convert karna
    folder = Path(folder_path)
    # Check karna ke folder mojood hai ya nahi
    if not folder.exists() or not folder.is_dir():
        print("Error: Folder nahi mila!")
        return
    # Count rakhne ke liye variables
    moved_files = 0
    skipped_files = 0
    # Folder ke andar mojood items par loop chalana
    for file in folder.iterdir():
        # Sirf files ko process karna, folders ko nahi
        if not file.is_file():
            continue
        # File ki extension lowercase mein lena
        extension = file.suffix.lower()
        # File ke liye destination folder dhoondhna
        destination_name = "Others"
        for category, extensions in FILE_TYPES.items():
            if extension in extensions:
                destination_name = category
                break
        # Destination folder ka complete path banana
        destination_folder = folder / destination_name
        # Agar destination folder nahi hai toh banana
        destination_folder.mkdir(exist_ok=True)
        # Destination mein file ka path banana
        destination_file = destination_folder / file.name
        # Agar isi naam ki file pehle se mojood hai toh skip karna
        if destination_file.exists():
            print(f"Skipped: {file.name} (same naam ki file mojood hai)")
            skipped_files += 1
            continue
        # File ko destination folder mein move karna
        try:
            shutil.move(str(file), str(destination_file))
            print(f"Moved: {file.name} -> {destination_name}/")
            moved_files += 1
        except OSError as error:
            # Agar file move karte waqt error aaye
            print(f"Error moving {file.name}: {error}")
    # Aakhir mein project ki summary dikhana
    print("\n===== ORGANIZATION COMPLETE =====")
    print(f"Files moved: {moved_files}")
    print(f"Files skipped: {skipped_files}")
# Program yahan se start hota hai
if __name__ == "__main__":
    print("===== SMART FILE ORGANIZER =====")
    print("Apne test folder ka complete path enter karein.")
    # User se folder ka path lena
    user_path = input("Folder path: ").strip().strip('"')
    # Files organize karne wala function call karna
    organize_files(user_path)
    