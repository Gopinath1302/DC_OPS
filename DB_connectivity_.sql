use db_railway;
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
);
select * from users;
CREATE TABLE IF NOT EXISTS stations (station_id INT  PRIMARY KEY, station_name VARCHAR(255));
Insert into stations values (1,"Salem"),
                            (2,"Erode"),
                            (3,"Chennai"),
                            (4,"Coimbatore"),
                            (5,"Trichy"),
                            (6,"Madurai"),
                            (7,"Tiruppur"),
                            (8,"Namakkal");
select * from stations;
drop table stations;
CREATE TABLE IF NOT EXISTS trains (train_no INT primary key, source_name varchar(255), destination_name varchar(255));
drop table trains;
insert into trains values(638,"Salem","Erode"),
                         (344,"Erode","Chennai"),
                         (555,"Chennai","coimbatore"),
                         (678,"Coimbatore","Trichy"),
                         (987,"Trichy","Madurai"),
                         (643,"Madurai","Tiruppur");
Select * from trains;
CREATE TABLE IF NOT EXISTS reservations (reservation_id INT AUTO_INCREMENT PRIMARY KEY, PASSENGER_NAME VARCHAR(255), Train_number INT, status varchar(255));
desc reservations;
select * from reservations;
CREATE TABLE IF NOT EXISTS PAYMENT (card_number INT, expiration_date date, cvv int);
drop table payment;
select * from payment;
alter table trains
add departure_time VARCHAR(255);
alter table trains
add arrival_time VARCHAR(255);
alter table trains
add AC_Sleeper int;
alter table trains
add Sleeper int;
alter table trains
add Sitting int;
truncate table trains;
desc trains;
insert into trains values(638,"Salem     ","Erode     ",7.00,9.00,330,200,150),
                         (344,"Erode     ","Chennai   ",8.00,15.00,400,300,200),
                         (555,"Chennai   ","coimbatore",9.00,18.00,500,380,240),
                         (678,"Coimbatore","Trichy    ",10.00,14.00,350,240,190),
                         (987,"Trichy    ","Madurai   ",11.00,13.30,320,250,180),
                         (643,"Madurai   ","Tiruppur  ",12.00,15.00,310,240,120);
Alter table reservations
add seat_type VARCHAR(255),
ADD no_of_passengers int;
