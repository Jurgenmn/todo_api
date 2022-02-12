DROP DATABASE IF EXISTS to_do_api;
CREATE DATABASE to_do_api;

\c to_do_api;

CREATE TABLE person(
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    user_name TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL
);

CREATE TABLE activity(
    id SERIAL PRIMARY KEY,
    activity_details TEXT NOT NULL,
    person_id INT NOT NULL,
    CONSTRAINT FK_person FOREIGN KEY (person_id)
    REFERENCES person(id) ON DELETE CASCADE --delete all activities of the user (if we delete a person (user))
);

INSERT INTO person(name, user_name, password) VALUES('John', 'j123', 'a123');
INSERT INTO person(name, user_name, password) VALUES('David', 'd123', 'b123');
INSERT INTO person(name, user_name, password) VALUES('Don', 'do123', 'd123');
INSERT INTO person(name, user_name, password) VALUES('Mathhew', 'm123', 'm123');

INSERT INTO activity(activity_details, person_id) VALUES('Clean the car', 1);
INSERT INTO activity(activity_details, person_id) VALUES('Clean the house', 1);
INSERT INTO activity(activity_details, person_id) VALUES('Go out on a run', 2);
INSERT INTO activity(activity_details, person_id) VALUES('Prepare dinner', 4);