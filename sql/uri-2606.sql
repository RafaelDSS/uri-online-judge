SELECT p.id, p.name FROM products AS p
    JOIN categories AS c ON c.id = p.id_categories AND c.name LIKE 'super%';
