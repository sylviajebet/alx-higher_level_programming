-- Script to import a table dump in hbtn_0c_0
SELECT state, MAX(value) AS max_temp
FROM temperatures
GROUP BY state
ORDER BY state;