SELECT loan.name, CAST(EXTRACT(DAY FROM loan.payday) AS NUMERIC) AS day FROM loan;
