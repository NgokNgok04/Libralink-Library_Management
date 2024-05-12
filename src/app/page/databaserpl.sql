-- MariaDB dump 10.19-11.3.2-MariaDB, for Win64 (AMD64)
--
-- Host: localhost    Database: rpldatabase
-- ------------------------------------------------------
-- Server version	11.3.2-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `anggota`
--

DROP TABLE IF EXISTS `anggota`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `anggota` (
  `anggota_id` int(11) NOT NULL AUTO_INCREMENT,
  `nama` char(255) NOT NULL,
  `alamat` char(255) DEFAULT NULL,
  `email` char(255) DEFAULT NULL,
  `telephone` char(255) DEFAULT NULL,
  `status_anggota` tinyint(1) NOT NULL DEFAULT 1,
  PRIMARY KEY (`anggota_id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `anggota`
--

LOCK TABLES `anggota` WRITE;
/*!40000 ALTER TABLE `anggota` DISABLE KEYS */;
INSERT INTO `anggota` VALUES
(1,'Jeremiah Gray','45611 Walker Loop Suite 180 Lake Ellen, DC 37939','jeremiahgray8679@gmail.com','086028857808',1),
(2,'Natasha Carlson','70443 Lopez Summit Apt. 790 New Matthewland, AL 48067','natashacarlson9945@gmail.com','089632107505',1),
(3,'Ashley Boone','4074 Morrow Pike Apt. 340 Lake Julia, WA 67774','ashleyboone0449@gmail.com','081505999037',1),
(4,'Sara Cook','410 Hickman Extensions Suite 946 Josephview, IN 92122','saracook9033@gmail.com','087342753572',1),
(5,'Traci Wagner','639 Valerie Plains Lake Ashley, SD 36124','traciwagner8211@gmail.com','082554503955',1),
(6,'Jesus Myers','789 Foster Knoll South John, NJ 56535','jesusmyers9563@gmail.com','083889265551',1),
(7,'Brenda Taylor','0316 Scott Drive Suite 948 Lake Stevenbury, WI 56294','brendataylor4128@gmail.com','084584923294',1),
(8,'Tina Parker','009 Wallace Keys Farrellmouth, SC 59562','tinaparker9189@gmail.com','088480162036',1),
(9,'Daniel Williams','4334 Smith Parkway Apt. 527 West Tina, FM 28770','danielwilliams7562@gmail.com','089549148270',1),
(10,'Melissa Smith','678 Julia Springs Suite 195 Jenniferfurt, AL 92148','melissasmith6430@gmail.com','080928716278',1),
(11,'Michael Day','0850 Maddox Union Apt. 009 North Nicole, AS 90964','michaelday4920@gmail.com','089436829801',1),
(12,'Brittney Turner','6521 Cole Plains Johnport, MH 51630','brittneyturner3575@gmail.com','080908756714',1),
(13,'Vincent Fuentes','8264 Hopkins Loaf East Markborough, NC 48756','vincentfuentes3550@gmail.com','083604699069',1),
(14,'Courtney Reynolds','3275 Castillo Center East Antoniochester, NJ 34165','courtneyreynolds9234@gmail.com','081365553927',1),
(15,'Cody Harper','76993 Smith Spur Suite 986 Hoodtown, OK 44920','codyharper2104@gmail.com','083285754964',1),
(16,'Robert Vasquez','7688 Anderson Pass Jensenland, MT 58746','robertvasquez2039@gmail.com','080233759059',1),
(17,'Richard Aguilar','432 Melissa Roads Apt. 075 Lake Andrea, ND 00546','richardaguilar4415@gmail.com','088178999598',1),
(18,'Jeffrey Brown','543 Ellis Bypass West Marcus, IA 26809','jeffreybrown6018@gmail.com','082382491928',1),
(19,'Holly Gibson','369 Hart Manors Port Christinahaven, UT 37228','hollygibson8512@gmail.com','083992806684',1),
(20,'Breanna Robertson','89238 Sandoval Villages Apt. 703 Loganhaven, IL 76869','breannarobertson8493@gmail.com','086299305700',1);
/*!40000 ALTER TABLE `anggota` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `buku`
--

DROP TABLE IF EXISTS `buku`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `buku` (
  `buku_id` int(11) NOT NULL AUTO_INCREMENT,
  `judul` char(255) NOT NULL,
  `isbn` char(255) NOT NULL,
  `path` char(255) DEFAULT NULL,
  PRIMARY KEY (`buku_id`)
) ENGINE=InnoDB AUTO_INCREMENT=42 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `buku`
--

LOCK TABLES `buku` WRITE;
/*!40000 ALTER TABLE `buku` DISABLE KEYS */;
INSERT INTO `buku` VALUES
(1,'Moonlight Forest','906516623- 6',NULL),
(2,'Legend Chronicles','010950220- 5',NULL),
(3,'Legend Chronicles','010950220- 5',NULL),
(4,'Legend Chronicles','010950220- 5',NULL),
(5,'Legend Chronicles','010950220- 5',NULL),
(6,'Legend Chronicles','010950220- 5',NULL),
(7,'Legend Chronicles','010950220- 5',NULL),
(8,'Moonlight Legend','243709775- 5',NULL),
(9,'Moonlight Legend','243709775- 5',NULL),
(10,'Moonlight Legend','243709775- 5',NULL),
(11,'Moonlight Legend','243709775- 5',NULL),
(12,'Moonlight Legend','243709775- 5',NULL),
(13,'Moonlight Legend','243709775- 5',NULL),
(14,'Forest Forest','716550905- 9',NULL),
(15,'Forest Forest','716550905- 9',NULL),
(16,'Forest Forest','716550905- 9',NULL),
(17,'Forest Forest','716550905- 9',NULL),
(18,'Forest Forest','716550905- 9',NULL),
(19,'Forest Journey','900262331- 7',NULL),
(20,'Chronicles Legend','670607980- 4',NULL),
(21,'Chronicles Legend','670607980- 4',NULL),
(22,'Chronicles Legend','670607980- 4',NULL),
(23,'Chronicles Legend','670607980- 4',NULL),
(24,'Forest Chronicles','484476832- 1',NULL),
(25,'Forest Chronicles','484476832- 1',NULL),
(26,'Forest Chronicles','484476832- 1',NULL),
(27,'Forest Chronicles','484476832- 1',NULL),
(28,'Moonlight Secret','444181509- 4',NULL),
(29,'Moonlight Secret','444181509- 4',NULL),
(30,'River Forest','281994735- 6',NULL),
(31,'River Forest','281994735- 6',NULL),
(32,'River Forest','281994735- 6',NULL),
(33,'Valley Secret','321601717- 5',NULL),
(34,'Sunset Journey','996097919- 9',NULL),
(35,'Sunset Journey','996097919- 9',NULL),
(36,'Sunset Journey','996097919- 9',NULL),
(37,'Sunset Journey','996097919- 9',NULL),
(38,'Legend Valley','701091022- 8',NULL),
(39,'Legend Valley','701091022- 8',NULL),
(40,'Secret Legend','069814964- 2',NULL),
(41,'Secret Legend','069814964- 2',NULL);
/*!40000 ALTER TABLE `buku` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `data_peminjaman_buku`
--

DROP TABLE IF EXISTS `data_peminjaman_buku`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `data_peminjaman_buku` (
  `anggota_id` int(11) NOT NULL,
  `buku_id` int(11) NOT NULL,
  `tanggal_pinjam` date NOT NULL,
  `tanggal_pengembalian` date NOT NULL,
  PRIMARY KEY (`anggota_id`,`buku_id`),
  KEY `buku_id` (`buku_id`),
  CONSTRAINT `data_peminjaman_buku_ibfk_1` FOREIGN KEY (`anggota_id`) REFERENCES `anggota` (`anggota_id`),
  CONSTRAINT `data_peminjaman_buku_ibfk_2` FOREIGN KEY (`buku_id`) REFERENCES `buku` (`buku_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `data_peminjaman_buku`
--

LOCK TABLES `data_peminjaman_buku` WRITE;
/*!40000 ALTER TABLE `data_peminjaman_buku` DISABLE KEYS */;
INSERT INTO `data_peminjaman_buku` VALUES
(1,4,'2021-01-08','2021-10-05'),
(3,26,'2020-10-26','2022-04-25'),
(4,34,'2022-04-28','2023-03-04'),
(5,7,'2023-03-16','2023-08-07'),
(6,35,'2022-11-12','2023-02-03'),
(8,28,'2023-08-09','2023-11-25'),
(9,39,'2022-12-08','2023-09-23'),
(10,8,'2022-04-08','2023-06-22'),
(10,34,'2022-02-11','2023-10-21'),
(12,38,'2022-02-16','2023-01-14'),
(13,30,'2022-01-29','2023-11-11'),
(13,32,'2020-04-14','2020-07-27'),
(14,38,'2020-01-11','2023-09-25'),
(16,15,'2023-02-03','2023-11-07'),
(17,2,'2021-12-23','2023-04-12'),
(17,39,'2022-06-12','2023-01-31'),
(17,41,'2022-05-21','2023-09-10'),
(18,8,'2020-10-30','2021-04-18'),
(20,27,'2023-05-10','2023-09-10'),
(20,30,'2020-04-02','2021-04-20');
/*!40000 ALTER TABLE `data_peminjaman_buku` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-05-10 22:02:57
