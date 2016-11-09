/*
Navicat MySQL Data Transfer

Source Server         : phpstudy
Source Server Version : 50540
Source Host           : localhost:3306
Source Database       : doubandb

Target Server Type    : MYSQL
Target Server Version : 50540
File Encoding         : 65001

Date: 2016-11-09 17:59:29
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for db_book_list
-- ----------------------------
DROP TABLE IF EXISTS `db_book_list`;
CREATE TABLE `db_book_list` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(255) DEFAULT NULL,
  `pub` varchar(255) DEFAULT NULL,
  `star` varchar(255) DEFAULT NULL,
  `desc` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
