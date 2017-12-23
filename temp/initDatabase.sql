grant all privileges on *.* to root@'%' identified by "123456";
flush privileges;
CREATE DATABASE hackforchristmas;

USE hackforchristmas;

CREATE TABLE TB_EVENT (
    eventId varchar(50) NOT NULL UNIQUE PRIMARY KEY,
    eventName varchar(100) NOT NULL,
    eventStarttime varchar(15),
    eventLocation varchar(200) NOT NULL,
    eventPeriod varchar(15) NOT NULL,
    eventFlag int NOT NULL
);

CREATE TABLE TB_USER (
    userId varchar(100) NOT NULL UNIQUE PRIMARY KEY,
    userPassword varchar(200) NOT NULL
);
