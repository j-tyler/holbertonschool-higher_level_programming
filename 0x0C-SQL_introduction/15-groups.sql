-- list the number of records with same score
SELECT score, Count(score) AS number
FROM second_table
GROUP BY score
ORDER BY score DESC;
