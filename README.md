# PasswordEater
Parses 'stealer logs' and outputs a SQLite .db. 


This contains a Python script intended to parse through all subdirectories from a 'Stealer Log' dump. By default, it recurses for "All Passwords.txt" and saves the password (following 'PASS:' in the .txt) as well as the folder in which the "All Passwords.txt" was found.

Included are SQL script - mostly for my own interest and example - which groups the password and provides a count to find the most frequent occurrence, or parse for the most common final symbol of a password (or whatever else I may include later).

Please review the Python script to ensure delimiters and regex are congruent with your data. Possible variations would be to change:
```
pattern = re.compile(r"^PASS:\s*(.+)$", re.MULTILINE)
```
to
```
pattern = re.compile(r"^PASSWORD:\s*(.+)$", re.MULTILINE)
```
if your folders are formatted like:
```
USERNAME: NONREVERSING
PASSWORD: PEPSICOWORLDWIDE1!
```
Rather than the
```
USER:
PASS:
```
nomenclature this was tested on.

Have fun.
