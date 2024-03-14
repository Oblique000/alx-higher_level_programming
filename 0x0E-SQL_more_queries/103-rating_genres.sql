-- List all genres in the hbtn_0d_tvshows_rate database ordered by their respective ratings.
-- Retrieve all records from the database that are linked to another table.
SELECT name, SUM(tv_show_ratings.rate) AS rating
FROM tv_genres
INNER JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
INNER JOIN tv_show_ratings ON tv_show_genres.show_id = tv_show_ratings.show_id
GROUP BY name
ORDER BY rating DESC;
