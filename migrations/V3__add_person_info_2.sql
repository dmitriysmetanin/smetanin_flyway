ALTER TABLE users
    ADD job varchar(64) not null default 'Не указана',
    ADD nation varchar(32) not null default 'Не указана',
    add phone varchar(16) not null default 'Не указан';
