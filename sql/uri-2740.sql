SELECT CONCAT('Podium: ', league.team) AS name FROM league
    WHERE league.position IN (SELECT league.position FROM league ORDER BY league.position ASC LIMIT 3)
UNION ALL
SELECT CONCAT('Demoted: ', league.team) AS name FROM league
    WHERE league.position IN (SELECT league.position FROM league ORDER BY league.position DESC LIMIT 2);
