ALTER TABLE users
    ADD first_name varchar(32) NOT NULL default '',
    ADD last_name varchar(32) NOT NULL default '',
    ADD patronymic varchar(32) NOT NULL default '',
    ADD birth_date date NOT NULL default '2000-01-01'
;