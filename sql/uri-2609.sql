SELECT c.name, sum(p.amount) FROM products as p
    INNER JOIN categories as c
    ON c.id = p.id_categories GROUP BY c.id;
