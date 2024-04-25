-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: localhost    Database: courier_management_system
-- ------------------------------------------------------
-- Server version	8.0.36

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
-- Table structure for table `order_details`
--

DROP TABLE IF EXISTS `order_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `order_details` (
  `order_id` bigint NOT NULL,
  `user_id` int DEFAULT NULL,
  `weight` varchar(255) DEFAULT NULL,
  `date_time` datetime DEFAULT NULL,
  `source` varchar(255) DEFAULT NULL,
  `s_address` varchar(255) DEFAULT NULL,
  `s_pin` varchar(255) DEFAULT NULL,
  `destination` varchar(255) DEFAULT NULL,
  `d_address` varchar(255) DEFAULT NULL,
  `d_pin` varchar(255) DEFAULT NULL,
  `current` varchar(255) DEFAULT NULL,
  `status` varchar(255) DEFAULT NULL,
  `package_type` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`order_id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `order_details_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user_login_details` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `order_details`
--

LOCK TABLES `order_details` WRITE;
/*!40000 ALTER TABLE `order_details` DISABLE KEYS */;
INSERT INTO `order_details` VALUES (170740580190619,10,'less than 1 kg','2024-02-08 20:53:21','Mysore','1st Floor, Atlanta Building, Nariman Point, Mysore','570001','Kodagu','B 116, 88, Pharma Apartment, Patparganj, Kodagu','571221','Mysore','Dispatched','Inter City'),(170740588625575,10,'between 1kg and 10kg','2024-02-08 20:54:46','Mandya','385, Kalbadevi Road, Opp Khadi Bhandar, Mandya','557901','Hassan','Kundalini Complex, Vastrapur','542321','Mandya','Booked','Inter City'),(170740617541804,2,'between 10kg and 25kg','2024-02-08 20:59:35','Tumakuru','22/3, Shamraocompound,missionroadb27, Mission Road, Tumakuru','512902','Mandya',' 74, Darya Ganj, Mandya','563124','Tumakuru','Booked','Inter City'),(170740623440097,2,'more than 50kgs','2024-02-08 21:00:34','Kodagu','Kanti Terrace, Sv Road, Kandivali (west), Kadagu','571235','Tumakuru','16, Broadway Shopping Centre, T.t. Dadar, Dadar(e), tumakuru','589013','Kodagu','Booked','Inter City'),(170740659737035,4,'less than 1 kg','2024-02-08 21:06:37','Mysore','291 Phase 2, Udyog Vihar, Mysore','570025','Mysore','2761/248, Hans Puri Road, Tri Nagar, Mysore','570072','Mysore','Booked','Local'),(170740665140346,4,'more than 50kgs','2024-02-08 21:07:31','Hassan','7, Oriental House, J Tata Road, Nr Eros Theatre, Churchgat, Hassan','542289','Hassan','26, Periyar Pathai West, Choolaimedu, Hassan','549182','Hassan','Booked','Local'),(170740691114911,5,'between 1kg and 10kg','2024-02-08 21:11:51','Kodagu','4, Rayfreda Bldg, Mahakali Caves Road, Nr Holy Family Church, Chakala, Kodagu','578923','Hassan','Shop No L/5935, Ground Floor, Laxmi House, 60 Feet Road, Hassan','539293','Kodagu','Booked','Inter City'),(170740695173224,5,'more than 50kgs','2024-02-08 21:12:31','Mandya',' 11/5b 2nd Floor, Param Tower, Pusa Road Chowk, Mandya','590123','Mysore','Village, Near Deer Park, Hauz Khas, Mysore','578829','Mandya','Booked','Inter City'),(170740701417756,8,'between 1kg and 10kg','2024-02-08 21:13:34','Tumakuru','209, Ground Floor, Dr. D N Road, Fort, Tumakuru','589232','Tumakuru','Pl#29,shop.10, Karkhana, Tumakuru','589249','Tumakuru','Booked','Local'),(170741570285196,3,'between 10kg and 25kg','2024-02-08 23:38:22','Hassan',' 11 A, Savitri Nagar, Main Road, Hassan','547291','Kodagu',' Shop No 1, Mani Baug, L.b.s Marg, Opp Damani Estate, Naupada, Kodagu','572311','Hassan','Booked','Inter City'),(170741583543685,6,'more than 50kgs','2024-02-08 23:40:35','Hassan',' 609, J K Chambers, Sector-17, Vashi, Hassan','542832','Hassan','6, 6,kumbarpetblr-2, Ds Lane, Kumbarpet, Hassan','542123','Hassan','Booked','Local');
/*!40000 ALTER TABLE `order_details` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `update_package_type` BEFORE INSERT ON `order_details` FOR EACH ROW BEGIN
  IF NEW.source = NEW.destination THEN
    SET NEW.`package_type` = 'Local';
  ELSE
    SET NEW.`package_type` = 'Inter City';
  END IF;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-02-08 23:50:00
