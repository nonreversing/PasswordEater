import os
import sqlite3
import re

# Creates the .db file.
db_name = input("Enter the name for the SQLite database (without extension): ").strip()
if not db_name.endswith(".db"):
    db_name += ".db"

# Save location. CHANGE db_dir TO YOUR OWN FOLDER.
# Example: db_dir = r"C:\Users\Nonreversing\Downloads\PasswordEater"
db_dir = r"PUT YOUR .DB FILE PATH HERE"
os.makedirs(db_dir, exist_ok=True)  # Fail-check!
db_path = os.path.join(db_dir, db_name)

print(f"Creating database: {db_path}")
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Passes through to SQL to create the .db.
cursor.execute("""
CREATE TABLE IF NOT EXISTS Passwords (
    Directory TEXT,
    Password TEXT
)
""")
conn.commit()

# Root search directory. SET THIS TO YOUR STEALER LOG/COMBOLIST DIRECTORY!
# Example: root_dir = "C:\Users\Nonreversing\Downloads\@NEW_DAISYCLOUD-CHAMPIONING! - 09_JAN_1962_ON_CHANNEL"
root_dir = r"PUT YOUR STEALER LOG/COMBOLIST MASTER DIRECTORY PATH HERE"

# Regex for the password.
# For all lines beginning with the word 'PASS:' it will take the remainder of this line until it terminates at \n,
# then continue recursion through the file.
pattern = re.compile(r"^PASS:\s*(.+)$", re.MULTILINE)

# Recurse through all sub-directories.
for dirpath, dirnames, filenames in os.walk(root_dir):
    if "All Passwords.txt" in filenames:
        file_path = os.path.join(dirpath, "All Passwords.txt")
        folder_name = os.path.basename(dirpath)  # Only extracts folder names, not full directory (e.g. C:/User/etc).
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            matches = pattern.findall(content)
            for password in matches:
                cursor.execute("INSERT INTO Passwords (Directory, Password) VALUES (?, ?)", (folder_name, password.strip()))

# Commits, closes.
conn.commit()
conn.close()

print(f"Password records successful: {db_path}")
