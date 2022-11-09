# Host: localhost  (Version 5.7.17-log)
# Date: 2019-04-24 15:58:00
# Generator: MySQL-Front 6.1  (Build 1.26)


#
# Structure for table "dazhongoutput"
#

CREATE TABLE `dazhongoutput` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `city` varchar(255) DEFAULT NULL COMMENT '城市',
  `shopName` varchar(255) DEFAULT NULL COMMENT '商铺名称',
  `shopId` varchar(255) DEFAULT NULL COMMENT '商品编号',
  `shopPower` varchar(255) DEFAULT NULL COMMENT '商铺星级',
  `mainRegionName` varchar(255) DEFAULT NULL COMMENT '所在区域名称',
  `mainCategoryName` varchar(255) DEFAULT NULL COMMENT '分类名称',
  `tasteScore` varchar(255) DEFAULT NULL COMMENT '口味评分',
  `environmentScore` varchar(255) DEFAULT NULL COMMENT '环境评分',
  `serviceScore` varchar(255) DEFAULT NULL COMMENT '服务评分',
  `avgPrice` varchar(255) DEFAULT NULL COMMENT '人均消费',
  `shopAddress` varchar(255) DEFAULT NULL COMMENT '详细地址',
  PRIMARY KEY (`Id`),
  UNIQUE KEY `shopId` (`shopId`),
  KEY `city` (`city`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COMMENT='大众点评美食表';

#
# Data for table "dazhongoutput"
#

