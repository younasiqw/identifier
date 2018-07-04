-- phpMyAdmin SQL Dump
-- version 4.0.10deb1


CREATE DATABASE IDENTIFIER;

USE IDENTIFIER;

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;




CREATE TABLE IF NOT EXISTS `administrator` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `ALLOW_IP_LIST` varchar(65000) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT= 9;


INSERT INTO `administrator` (`id`, `ALLOW_IP_LIST`) VALUES
(1, '::1 <br> 127.0.0.1  <br> ');


CREATE TABLE IF NOT EXISTS `backup_devices` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `device_id` varchar(64) NOT NULL,
  `last_ip` varchar(64) NOT NULL,
  `instant` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `latitude` varchar(128) NOT NULL,
  `longitude` varchar(128) NOT NULL,
  `address` varchar(128) NOT NULL,
  `fingerprint` varchar(32) NOT NULL,
  `all_info` varchar(256) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;



CREATE TABLE IF NOT EXISTS `devices` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `device_id` varchar(64) NOT NULL,
  `last_ip` varchar(64) NOT NULL,
  `instant` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `latitude` varchar(128) NOT NULL,
  `longitude` varchar(128) NOT NULL,
  `address` varchar(128) NOT NULL,
  `fingerprint` varchar(32) NOT NULL,
  `all_info` varchar(256) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;



CREATE TABLE IF NOT EXISTS `devices_blocked` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `device_id` varchar(64) NOT NULL,
  `instant` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=13 ;



CREATE TABLE IF NOT EXISTS `system_settings` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `mode` varchar(4) NOT NULL,
  `time_of_renewal` varchar(32) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  UNIQUE KEY `mode` (`mode`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;


INSERT INTO `system_settings` (`id`, `mode`, `time_of_renewal`) VALUES
(1, 'on', '30');

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
