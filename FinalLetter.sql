SELECT 
    SUBSTR(Password, -1) AS FinalChar, 
    COUNT(DISTINCT Directory || Password) AS Count
FROM Passwords
GROUP BY FinalChar
HAVING Count >= 5
ORDER BY Count DESC;