-- lists records from second_table with a non-null name ordered by score
SELECT score, name FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
