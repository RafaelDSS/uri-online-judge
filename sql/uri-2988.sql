SELECT t.name, t.matches, t.victories, t.defeats, t.draws, (t.victories * 3 + t.draws) AS score
FROM (
  SELECT teams.name, COUNT(teams.name) AS matches,
    COUNT((matches.team_1_goals > matches.team_2_goals AND teams.id = matches.team_1 OR NULL) OR (matches.team_2_goals > matches.team_1_goals AND teams.id = matches.team_2 OR NULL)) AS victories,
    COUNT((matches.team_1_goals > matches.team_2_goals AND teams.id = matches.team_2 OR NULL) OR (matches.team_2_goals > matches.team_1_goals AND teams.id = matches.team_1 OR NULL)) AS defeats,
    COUNT((matches.team_1_goals = matches.team_2_goals AND teams.id = matches.team_1 OR NULL) OR (matches.team_2_goals = matches.team_1_goals AND teams.id = matches.team_2 OR NULL)) AS draws
  FROM teams
    INNER JOIN matches
    ON teams.id = matches.team_1 OR teams.id = matches.team_2
  GROUP BY teams.name
) t
ORDER BY score DESC, t.name ASC
