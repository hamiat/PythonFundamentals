CREATE DATABASE assessment;

CREATE TABLE flights (id SERIAL PRIMARY KEY, flight_number varchar(255) NOT NULL, departure_time timestamp default NULL, arrival_time timestamp default NULL, departure_airport varchar(255) NOT NULL, destination_airport varchar(255));

INSERT INTO flights (flight_number, departure_time, arrival_time, departure_airport, destination_airport) VALUES ('E353TU', '2025-08-14 02:15 PM', '2025-08-14 05:24 PM', 'Stockholm Arlanda Airport', 'Kiruna Airport');

INSERT INTO flights (flight_number, departure_time, arrival_time, departure_airport, destination_airport) VALUES ('A743TE', '2025-11-12 02:10 AM', '2025-11-12 04:45 PM', 'Kiruna Airport', 'Helsingfors-Vanda Airport');

INSERT INTO flights (flight_number, departure_time, arrival_time, departure_airport, destination_airport) VALUES ('B246UE', '2025-12-10 08:10 AM', '2025-12-11 04:02 AM', 'Stockholm Arlanda Airport', 'Hazrat Shahjalal International Airport');

