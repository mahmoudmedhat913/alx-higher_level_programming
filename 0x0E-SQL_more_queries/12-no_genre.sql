-- lists all shows
SELECT s.`title`, g.`genre_id` FROM `tv_shows` AS s LEFt JOIN `tv_show_genres` AS g
	ON s.`id` = g.`show_id` WHERE g.`genre_id` IS NULL ORDER BY s.`title`, g.`genre_id`;
