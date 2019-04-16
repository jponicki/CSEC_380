CREATE DATABASE IF NOT EXISTS `webapp`;
USE `webapp`;

CREATE TABLE IF NOT EXISTS `Users` (
  User_ID varchar(45) NOT NULL,
  Username varchar(45) DEFAULT NULL,
  Password varchar(64) DEFAULT NULL,
  PRIMARY KEY (User_ID)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE IF NOT EXISTS `Video` (
  User_ID varchar(45) NOT NULL,
  VideoName varchar(256) NOT NULL,
  VideoLoc varchar(256) DEFAULT NULL,
  PRIMARY KEY (User_ID,VideoName)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
