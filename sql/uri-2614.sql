SELECT name, rentals_date FROM customers
    INNER JOIN rentals
    ON customers.id = rentals.id_customers
    WHERE rentals.rentals_date BETWEEN '2016-08-31' AND '2016-10-1';
