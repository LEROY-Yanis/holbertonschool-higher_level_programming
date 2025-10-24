-- Lists all genres and the number of shows linked to each one

SELECT g.name AS genre,
       COUNT(sg.show_id) AS number_of_shows
FROM tv_genres AS g
JOIN tv_show_genres AS sg ON g.id = sg.genre_id
GROUP BY g.name
HAVING COUNT(sg.show_id) > 0
ORDER BY number_of_shows DESC;

