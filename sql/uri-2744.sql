SELECT account.id, account.password, MD5(account.password) AS MD5 FROM account;
