-- MySQL dump 10.13  Distrib 8.0.23, for Win64 (x86_64)
--
-- Host: localhost    Database: cms
-- ------------------------------------------------------
-- Server version	8.0.23

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `add_bus`
--

DROP TABLE IF EXISTS `add_bus`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `add_bus` (
  `id` int NOT NULL AUTO_INCREMENT,
  `loc` varchar(50) DEFAULT NULL,
  `busno` varchar(50) DEFAULT NULL,
  `re` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `add_route`
--

DROP TABLE IF EXISTS `add_route`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `add_route` (
  `id` int NOT NULL AUTO_INCREMENT,
  `route` varchar(50) DEFAULT NULL,
  `price` varchar(50) DEFAULT NULL,
  `ress` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `alloteroomno`
--

DROP TABLE IF EXISTS `alloteroomno`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `alloteroomno` (
  `id` int NOT NULL AUTO_INCREMENT,
  `roomno` varchar(50) DEFAULT NULL,
  `stuid` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `ap`
--

DROP TABLE IF EXISTS `ap`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ap` (
  `id` int NOT NULL AUTO_INCREMENT,
  `regno` varchar(50) DEFAULT NULL,
  `ap` varchar(50) DEFAULT NULL,
  `sem` varchar(50) DEFAULT NULL,
  `date` varchar(50) DEFAULT NULL,
  `time` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=57 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `book_author`
--

DROP TABLE IF EXISTS `book_author`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `book_author` (
  `id` int NOT NULL AUTO_INCREMENT,
  `author` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `book_publication`
--

DROP TABLE IF EXISTS `book_publication`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `book_publication` (
  `id` int NOT NULL AUTO_INCREMENT,
  `publication` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `branch`
--

DROP TABLE IF EXISTS `branch`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `branch` (
  `idbranch` int NOT NULL AUTO_INCREMENT,
  `course_id` int DEFAULT NULL,
  `branchname` varchar(45) DEFAULT NULL,
  `branchfees` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idbranch`),
  KEY `branch_idx` (`course_id`),
  CONSTRAINT `branch` FOREIGN KEY (`course_id`) REFERENCES `course` (`idcourse`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `busno`
--

DROP TABLE IF EXISTS `busno`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `busno` (
  `id` int NOT NULL AUTO_INCREMENT,
  `busno` varchar(50) DEFAULT NULL,
  `busname` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `busstu`
--

DROP TABLE IF EXISTS `busstu`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `busstu` (
  `id` int NOT NULL AUTO_INCREMENT,
  `route` varchar(52) DEFAULT NULL,
  `bus_no` varchar(52) DEFAULT NULL,
  `price` varchar(52) DEFAULT NULL,
  `stuid` varchar(52) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `codereg`
--

DROP TABLE IF EXISTS `codereg`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `codereg` (
  `id` int NOT NULL AUTO_INCREMENT,
  `crid` varchar(50) DEFAULT NULL,
  `subject` varchar(50) DEFAULT NULL,
  `sem` varchar(32) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=76 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `company`
--

DROP TABLE IF EXISTS `company`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `company` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL,
  `es` varchar(50) DEFAULT NULL,
  `ten` varchar(50) DEFAULT NULL,
  `tw` varchar(50) DEFAULT NULL,
  `diploma` varchar(50) DEFAULT NULL,
  `gap` varchar(50) DEFAULT NULL,
  `descc` varchar(500) DEFAULT NULL,
  `role` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `companydrive`
--

DROP TABLE IF EXISTS `companydrive`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `companydrive` (
  `id` int NOT NULL AUTO_INCREMENT,
  `cid` varchar(50) DEFAULT NULL,
  `eventdate` varchar(50) DEFAULT NULL,
  `eventtime` varchar(50) DEFAULT NULL,
  `venue` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `course`
--

DROP TABLE IF EXISTS `course`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `course` (
  `idcourse` int NOT NULL AUTO_INCREMENT,
  `name` varchar(45) DEFAULT NULL,
  `years` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idcourse`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `coursereg`
--

DROP TABLE IF EXISTS `coursereg`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `coursereg` (
  `id` int NOT NULL AUTO_INCREMENT,
  `course_name` varchar(50) DEFAULT NULL,
  `year` varchar(50) DEFAULT NULL,
  `sem` varchar(50) DEFAULT NULL,
  `branch` varchar(50) DEFAULT NULL,
  `fess` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `fees`
--

DROP TABLE IF EXISTS `fees`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `fees` (
  `id` int NOT NULL AUTO_INCREMENT,
  `regno` varchar(50) DEFAULT NULL,
  `fees` varchar(50) DEFAULT NULL,
  `fee_purpose` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `grop`
--

DROP TABLE IF EXISTS `grop`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `grop` (
  `id` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `hroom`
--

DROP TABLE IF EXISTS `hroom`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `hroom` (
  `id` int NOT NULL AUTO_INCREMENT,
  `room_no` varchar(50) DEFAULT NULL,
  `stuid` varchar(50) DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `issue_book`
--

DROP TABLE IF EXISTS `issue_book`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `issue_book` (
  `id` int NOT NULL AUTO_INCREMENT,
  `book_id` varchar(52) DEFAULT NULL,
  `book_no` varchar(52) DEFAULT NULL,
  `issue_no` varchar(52) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `issued_book`
--

DROP TABLE IF EXISTS `issued_book`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `issued_book` (
  `id` int NOT NULL AUTO_INCREMENT,
  `issue_book_no` varchar(50) DEFAULT NULL,
  `issue_book_code` varchar(50) DEFAULT NULL,
  `regno` varchar(50) DEFAULT NULL,
  `issue_date` varchar(50) DEFAULT NULL,
  `return_date` varchar(50) DEFAULT NULL,
  `book_id` varchar(52) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=61 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `issued_book_archive`
--

DROP TABLE IF EXISTS `issued_book_archive`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `issued_book_archive` (
  `id` int NOT NULL AUTO_INCREMENT,
  `issue_book_no` varchar(50) DEFAULT NULL,
  `issue_book_code` varchar(50) DEFAULT NULL,
  `issue_date` varchar(50) DEFAULT NULL,
  `return_date` varchar(50) DEFAULT NULL,
  `regno` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `library`
--

DROP TABLE IF EXISTS `library`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `library` (
  `id` int NOT NULL AUTO_INCREMENT,
  `bname` varchar(50) DEFAULT NULL,
  `bauthor` varchar(50) DEFAULT NULL,
  `bedition` varchar(50) DEFAULT NULL,
  `bpublisher` varchar(50) DEFAULT NULL,
  `book_stock` int DEFAULT NULL,
  `issue` int DEFAULT NULL,
  `code` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `mess`
--

DROP TABLE IF EXISTS `mess`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `mess` (
  `id` int NOT NULL AUTO_INCREMENT,
  `breakfast` varchar(500) DEFAULT NULL,
  `lunch` varchar(500) DEFAULT NULL,
  `dinner` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `notice`
--

DROP TABLE IF EXISTS `notice`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `notice` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL,
  `details` varchar(1000) DEFAULT NULL,
  `date` varchar(50) DEFAULT NULL,
  `category` varchar(50) DEFAULT NULL,
  `flag` varchar(50) DEFAULT NULL,
  `file` varchar(50) DEFAULT NULL,
  `timestamp` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `parents`
--

DROP TABLE IF EXISTS `parents`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `parents` (
  `idparents` int NOT NULL AUTO_INCREMENT,
  `stuis` varchar(50) DEFAULT NULL,
  `Fathername` varchar(45) DEFAULT NULL,
  `father_occ` varchar(45) DEFAULT NULL,
  `mothername` varchar(45) DEFAULT NULL,
  `motherocc` varchar(45) DEFAULT NULL,
  `fatheridl` varchar(45) DEFAULT NULL,
  `mobno` varchar(45) DEFAULT NULL,
  `passcode` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idparents`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `result`
--

DROP TABLE IF EXISTS `result`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `result` (
  `id` int NOT NULL AUTO_INCREMENT,
  `regno` varchar(50) DEFAULT NULL,
  `sem` varchar(50) DEFAULT NULL,
  `subject` varchar(50) DEFAULT NULL,
  `mode` varchar(50) DEFAULT NULL,
  `marks` varchar(50) DEFAULT NULL,
  `ev` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `role`
--

DROP TABLE IF EXISTS `role`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `role` (
  `id` int NOT NULL AUTO_INCREMENT,
  `fname` varchar(50) DEFAULT NULL,
  `lname` varchar(50) DEFAULT NULL,
  `dob` varchar(50) DEFAULT NULL,
  `qualification` varchar(50) DEFAULT NULL,
  `salary` varchar(50) DEFAULT NULL,
  `gender` varchar(50) DEFAULT NULL,
  `aano` varchar(50) DEFAULT NULL,
  `bg` varchar(50) DEFAULT NULL,
  `role` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=64 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `student`
--

DROP TABLE IF EXISTS `student`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `student` (
  `id` int NOT NULL AUTO_INCREMENT,
  `frname` varchar(50) DEFAULT NULL,
  `lname` varchar(50) DEFAULT NULL,
  `dob` varchar(50) DEFAULT NULL,
  `p_id` varchar(50) DEFAULT NULL,
  `address` varchar(50) DEFAULT NULL,
  `city` varchar(50) DEFAULT NULL,
  `state` varchar(50) DEFAULT NULL,
  `mob_no` varchar(50) DEFAULT NULL,
  `gender` varchar(50) DEFAULT NULL,
  `aadhar` varchar(50) DEFAULT NULL,
  `course` varchar(50) DEFAULT NULL,
  `branch` varchar(50) DEFAULT NULL,
  `bg` varchar(50) DEFAULT NULL,
  `reg_no` varchar(50) DEFAULT NULL,
  `ten` varchar(20) DEFAULT NULL,
  `tenb` varchar(20) DEFAULT NULL,
  `tw` varchar(20) DEFAULT NULL,
  `twb` varchar(20) DEFAULT NULL,
  `dip` varchar(20) DEFAULT NULL,
  `dm` varchar(20) DEFAULT NULL,
  `bd` varchar(20) DEFAULT NULL,
  `buc` varchar(20) DEFAULT NULL,
  `jy` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `timetable`
--

DROP TABLE IF EXISTS `timetable`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `timetable` (
  `id` int NOT NULL AUTO_INCREMENT,
  `sub_name` varchar(50) DEFAULT NULL,
  `fac_name` varchar(50) DEFAULT NULL,
  `ab` varchar(50) DEFAULT NULL,
  `classcode` varchar(50) DEFAULT NULL,
  `sem` varchar(52) DEFAULT NULL,
  `branch` varchar(52) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=252 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL,
  `user_id` varchar(50) DEFAULT NULL,
  `passwd` varchar(50) DEFAULT NULL,
  `role` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=61 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-06-05 12:06:30
