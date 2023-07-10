create schema appdata;
use appdata;

-- create

create table credentials
(
cus_id varchar(10),
username varchar(20),
password varchar(64),
phoneno varchar(10),
emailid varchar(50),
joindate date
);  
create table userdata
(
cus_id varchar(10),
username varchar(30),
fname varchar(20),
lname varchar(20),
dob date,
emailid varchar(40),
phone varchar(10),
zip_code varchar(10),
timestamp varchar(20)
);
create table address
(
cus_id varchar(10),
door_no varchar(5),
street varchar(50),
city varchar(30),
state varchar(20),
country varchar(30),
zip_code varchar(10),
timestamp varchar(20)
);

create table service 
(
cus_id varchar(10),
service_name varchar(20),
price int,
timestamp varchar(20)
);

-- insert

insert into credentials values
(
'CUSAD44674','Adminroot','d4b3f9751121384100e588e183d977833de810512dbe60735ee52d88164ad0e9','4467404000','info-india@aspiresys.com','2023-07-02'
);
insert into userdata values
(
'CUSAD44674','Adminroot',null,null,null,'info-india@aspiresys.com','4467404000',null,'2023-07-02'
);
insert into address values
(
'CUSAS44674',null,null,null,null,null,null
);

-- truncate

truncate table credentials;
truncate table userdata;
truncate table address;
truncate table service;

-- drop

drop table credentials;
drop table userdata;
drop table address;
drop table service;

-- select

Select * from credentials; 
Select * from userdata; 
select * from address;
select * from service;
Select * from credentials, userdata, address where credentials.cus_id = userdata.cus_id and userdata.cus_id = address.cus_id;
select sum(price) from service where cus_id = 'CUSAG90800';

-- Update

update userdata set timestamp ='2023-07-08 02:31:53' where cus_id='CUSAG90800';
update address set timestamp ='2023-07-08 02:31:53' where cus_id='CUSAG90800';

-- describe

desc credentials;
desc userdata;
desc address;

-- underdevelopment

create table service_request
(
cus_id varchar(10) primary key not null,
ser_id varchar(10)not null,
device varchar(50)not null,
model varchar(40)not null,
defect varchar(100)not null,
usaage varchar (10)not null,
rstatus varchar(11)not null,
time varchar(20) not null
);

select * from service_request;
truncate table service_request;
drop table Service_request;