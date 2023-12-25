create table if not exists users
(
    user_id       SERIAL PRIMARY KEY NOT NULL,
    email    VARCHAR(64) NOT NULL,
    password VARCHAR(256) NOT NULL
);

create table  if not exists courses
(
    course_id       SERIAL PRIMARY KEY,
    author_id int NOT NULL REFERENCES users,
    name VARCHAR(64) NOT NULL,
    description TEXT
);

create table  if not exists modules
(
    module_id       SERIAL PRIMARY KEY,
    course_id int NOT NULL REFERENCES courses,
    name VARCHAR(64) NOT NULL,
    description TEXT
);

create table  if not exists lessons
(
    lesson_id       SERIAL PRIMARY KEY,
    module_id int NOT NULL REFERENCES modules,
    name VARCHAR(64) NOT NULL,
    description TEXT,
    content TEXT NOT NULL
);

create table  if not exists hometasks
(
    hometask_id       SERIAL PRIMARY KEY,
    lesson_id int NOT NULL REFERENCES lessons,
    name VARCHAR(64) NOT NULL,
    description TEXT,
    content TEXT NOT NULL,
    maxPoints SMALLINT NOT NULL
);

create table  if not exists submittedHomeworks
(
    submittedHomework_id       SERIAL PRIMARY KEY,
    hometask_id int NOT NULL REFERENCES hometasks,
    status SMALLINT NOT NULL DEFAULT 0 ,
    file varchar(256) NOT NULL,
    points SMALLINT NOT NULL DEFAULT 0,
    teachersComment TEXT
);

CREATE TABLE if not exists course_student
(
    id        BIGSERIAL PRIMARY KEY,
    student_id INTEGER NOT NULL REFERENCES users,
    course_id   INTEGER NOT NULL REFERENCES courses,
    UNIQUE (student_id, course_id)
);
