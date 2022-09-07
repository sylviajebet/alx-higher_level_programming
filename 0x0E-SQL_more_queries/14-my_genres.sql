-- Script that uses the hbtn_0d_tvshows to list all genres of the show Dexter
-- Each record displays: tv_genres.name
-- Ordered by genre name ASC; Only one SELECT statement
-- tv_shows has only one record where title = Dexter, Different id

SELECT DISTINCT name FROM tv_genres
INNER JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id
INNER JOIN tv_shows
ON tv_show_genres.show_id = tv_shows.id
WHERE tv_shows.title = 'Dexter'
ORDER BY name ASC;