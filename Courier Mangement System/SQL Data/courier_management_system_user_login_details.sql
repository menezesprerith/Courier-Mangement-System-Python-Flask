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
-- Table structure for table `user_login_details`
--

DROP TABLE IF EXISTS `user_login_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_login_details` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `phone` varchar(255) DEFAULT NULL,
  `address` varchar(512) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_login_details`
--

LOCK TABLES `user_login_details` WRITE;
/*!40000 ALTER TABLE `user_login_details` DISABLE KEYS */;
INSERT INTO `user_login_details` VALUES (2,'Luke Thompson','lukethompson@gmail.com','$2b$12$ZW/fjQwipL63AEuktLBteuZLrdA0osE2gUwG6ZHhyKE0qc.hEhGNy','+915961673101','Suite 203 66852 Hackett Trace, New Nikki, NE 96534'),(3,'Emerson Baxter','emersonbaxter@gmail.com','$2b$12$hYd3rYvkMPDhJEti3WIZ0OmKT5o2ndNbjmJkCaGqjNh9.65rIh/36','+919680799586','Apt. 576 513 Merlene Flat, Marvinburgh, AK 17659-6229'),(4,'Jasper Newton','jaspernewton@gmail.com','$2b$12$tEzB31jqZHwEXBSo14HZGeMGYm58orx9BvcCundnxdwcplqrTb2jW','+911411262357','Apt. 878 619 Porter Causeway, North Jermainestad, CO 88440-8096'),(5,'Melody Matthews','melodymatthews@gmail.com','$2b$12$D42pCiIti6pW832ejsGqieib6neZX9lCh2X55u94PYT7/5lVG1ZY2','+918012358788','Apt. 168 Jl. Kartini No. 89, Kepulauan Meranti, JI 71835'),(6,'Leopold Becker','leopoldbecker@gmail.com','$2b$12$FalLISqBxUNyglXdkVwne.3ep2fj4qm9f4Yy6dsy0doVAMLBRZYgW','+918677415022','Rampa Cecilia Dueñas, 59, Ciudad Real, Leo 45425'),(7,'Gerard Madron','gerardmadron@gmail.com','$2b$12$caSnHdnD77EzGE1poadyr.IkzX.3BMV5vtPHdvlPQ63R/MCl96HW6','+913562448810','Poblado Maricarmen Campos, 38 Esc. 382, Barcelona, Mur 88838'),(8,'Lizzie Watts','lizziewatts@gamil.com','$2b$12$5Tgxl3BKJ9TnGEw1JVHBT.zRwwx.JO4jjFXLVnbKw9ROWJZnBTilu','+916101577624','Escalinata Conchita 2 Esc. 972, Fuenlabrada, Leo 14556'),(9,'Roger Vega','rogervega@gmail.com','$2b$12$PWiaGjGM75juk1KzPwpOve/WR3OWQF83X5Ccxkv4ERQT9KE5BS9MK','+918080727176','Puerta 674 Sección Ricardo Aparicio 3 Puerta 911, Hospitalet de LLobregat, Man 32580'),(10,'Amanda Ryan','amandaryan@gmail.com','$2b$12$ffy5yCD23ogkcoqB/PbB7OofGrGbaFbj4UzkBqzxgSI7biw.BXGLa','+913865166646','Partida Antonio, 1, Molina de Segura, Mur 70915');
/*!40000 ALTER TABLE `user_login_details` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-02-08 23:50:00
