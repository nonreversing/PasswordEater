SELECT Password, COUNT(DISTINCT Directory) AS DirectoryCount
FROM Passwords
/* Put exceptions for null/irrelevant entries here. The common example from my database is commented out below as an example. */
/* WHERE Password != '[NOT_SAVED]' */
GROUP BY Password
HAVING DirectoryCount > 1
ORDER BY DirectoryCount DESC;