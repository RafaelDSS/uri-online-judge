SELECT m.id, m.name FROM movies AS m
    INNER JOIN prices AS p
    ON p.id = m.id_prices AND p.value < 2.00;
