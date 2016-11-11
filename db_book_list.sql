/*
Navicat MySQL Data Transfer

Source Server         : mysql
Source Server Version : 50611
Source Host           : localhost:3306
Source Database       : doubandb

Target Server Type    : MYSQL
Target Server Version : 50611
File Encoding         : 65001

Date: 2016-11-11 17:53:30
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for db_book_list
-- ----------------------------
DROP TABLE IF EXISTS `db_book_list`;
CREATE TABLE `db_book_list` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tag_id` int(11) DEFAULT NULL,
  `title` varchar(255) DEFAULT NULL,
  `pub` varchar(255) DEFAULT NULL,
  `star` varchar(255) DEFAULT NULL,
  `comment` int(11) DEFAULT NULL,
  `desc` varchar(255) DEFAULT NULL,
  `create_time` varchar(255) DEFAULT NULL,
  `update_time` varchar(255) DEFAULT NULL,
  `status` tinyint(4) DEFAULT '1',
  PRIMARY KEY (`id`),
  KEY `title` (`title`) USING BTREE,
  KEY `tag_id` (`tag_id`,`title`) USING BTREE
) ENGINE=MyISAM AUTO_INCREMENT=5156 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for db_tag_list
-- ----------------------------
DROP TABLE IF EXISTS `db_tag_list`;
CREATE TABLE `db_tag_list` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tag_name` varchar(255) DEFAULT NULL,
  `create_time` datetime DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  `update_time` datetime DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  `status` tinyint(4) DEFAULT '1',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;
