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
    eventFlag int NOT NULL,
    eventEndTime varchar(15),
    userId varchar(100) NOT NULL
);

CREATE TABLE TB_USER(
    userId varchar(100) NOT NULL UNIQUE PRIMARY KEY,
    userPassword varchar(200) NOT NULL
);

CREATE TABLE TB_LOCATION(
    curLocation varchar(100) NOT NULL UNIQUE PRIMARY KEY
) CHARACTER SET = utf8;

ALTER DATABASE hackforchristmas CHARACTER SET utf8 COLLATE utf8_general_ci;
ALTER TABLE TB_USER CONVERT TO CHARACTER SET utf8 COLLATE utf8_general_ci;
ALTER TABLE TB_EVENT CONVERT TO CHARACTER SET utf8 COLLATE utf8_general_ci;
ALTER TABLE TB_LOCATION CONVERT TO CHARACTER SET utf8 COLLATE utf8_general_ci;