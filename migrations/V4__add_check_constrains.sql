ALTER TABLE users
add check (date_part('year', current_date) - date_part('year', birth_date) < 120)