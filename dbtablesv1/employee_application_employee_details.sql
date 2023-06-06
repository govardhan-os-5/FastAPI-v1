-- MySQL dump 10.13  Distrib 8.0.33, for Linux (x86_64)
--
-- Host: 127.0.0.1    Database: employee_application
-- ------------------------------------------------------
-- Server version	8.0.33

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `employee_details`
--

DROP TABLE IF EXISTS `employee_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employee_details` (
  `id` varchar(45) NOT NULL,
  `first_name` varchar(45) NOT NULL,
  `last_name` varchar(45) NOT NULL,
  `gender` varchar(10) NOT NULL,
  `mobile_number` varchar(15) NOT NULL,
  `email` varchar(45) NOT NULL,
  `date_of_birth` date NOT NULL,
  `joining_date` date NOT NULL,
  `qualifications` varchar(45) NOT NULL,
  `designation` varchar(45) NOT NULL,
  `department` varchar(45) NOT NULL,
  `blood_group` varchar(10) NOT NULL,
  `address` varchar(100) NOT NULL,
  `role` varchar(45) NOT NULL,
  `password` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `employee_id_UNIQUE` (`id`),
  UNIQUE KEY `email_UNIQUE` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employee_details`
--

LOCK TABLES `employee_details` WRITE;
/*!40000 ALTER TABLE `employee_details` DISABLE KEYS */;
INSERT INTO `employee_details` VALUES ('MM001','Vikas','Sunkari','Male','8341022458','vikas.sunkari@mm.com','2023-01-01','2023-01-01','BTech','Dev','Dev','A+','Hyd','Employee','$2b$12$Eky6T2AL3dsy4ozerB0T7.tUBr19iEwqP61nymR8w4E4h6LgOB/F.'),('OS001','Govardhan','Gottemukkula','Male','8465964234','govardhan.gottemukkula@openskale.com','2000-09-05','2023-04-26','BTech','Developer','Development','O+','SRPT','Employee',''),('OS0010','manoj','tester','Male','8801992370','manojtester@openskale.com','2023-01-01','2023-01-01','B.tech','Testing Engineer','Development','A+','hyderabd','Admin','$2b$12$Er.gcyRm7WBsYDb9DiwZvecUBbOUL6WmGkawdl0leZvNxDKkpnmuy'),('OS002','Harish','Reddyshetty','Male','8801992370','harish.redyshetty@openskale.com','1996-07-16','2023-05-29','BTech','React developer','Development','O+','HYD','Employee','1234'),('OS003','Santosh','Naruje','Male','6305008070','santosh.naruje@openskale.com','2001-08-05','2023-05-24','BCA','React developer','Devolopment','O+','HYD','Employee',''),('OS005','rahul','attuliri','Male','**********','rahulAttuluri@gmail.con','2023-01-01','2023-01-01','Btech','Director','development','A+','chennai,Kodaikkanla,Hyd,telangana','Employee',''),('OS006','manoj','tester','Male','8801992372','xyz@gmail.com','2023-01-01','2023-01-01','B.tech','Testing Engineer','Development','A-','Hyderabad','Employee',''),('OS007','kiran','ramu','Male','8922412233','kiran@gmail.com','2023-01-01','2023-01-01','B.tech','Python Developer','Tester','A+','hyderabd','employee','kiran@open'),('OS008','ganesh','tester','Male','789456123','ganesh@gmail.com','2023-01-01','2023-01-01','B.tech','Testing Engineer','Tester','A+','hyderabd','Employee','ganesh@123'),('OS009','manoj','tester','Male','8801992370','harish.redyshetty@gmail.com','2023-01-01','2023-01-01','B.tech','Testing Engineer','Tester','A+','hyderabd','Admin','$2b$12$rDSsOwgtQ3.YXHy3e4p4LuCsLUJeIbNneLzFXZz446TDNLII5Mab2'),('OW004','Suresh','Salloju','Male','9988776655','suresh.salloju@openskale.com','2023-01-01','2023-01-01','BTech','Dev','Dev','A+','Hyd','Admin','$2b$12$nKPbZuOM/xJaAVIgxT/i8.Ni02/mYyz/6TAejmh6GgU6S99U2.vuK');
/*!40000 ALTER TABLE `employee_details` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-06-06 17:42:00
