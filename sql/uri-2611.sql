SELECT m.id, m.name FROM movies AS m
    INNER JOIN genres AS g
    ON g.id = m.id_genres AND g.description = 'Action';
