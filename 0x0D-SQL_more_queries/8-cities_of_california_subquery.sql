-- list all the cities in Cali in hbtn_0d_usa
SELECT cities.id, cities.name
FROM cities
WHERE cities.state_id = 1
ORDER BY id ASC;
