-- MySQL dump 10.13  Distrib 8.0.43, for macos15 (arm64)
--
-- Host: localhost    Database: esquema_publicaciones
-- ------------------------------------------------------
-- Server version	8.0.43

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
-- Table structure for table `publicaciones`
--

DROP TABLE IF EXISTS `publicaciones`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `publicaciones` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  `fecha` date NOT NULL,
  `lugar` varchar(100) NOT NULL,
  `descripcion` text NOT NULL,
  `usuario_id` int NOT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `usuario_id` (`usuario_id`),
  CONSTRAINT `publicaciones_ibfk_1` FOREIGN KEY (`usuario_id`) REFERENCES `usuarios` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `publicaciones`
--

LOCK TABLES `publicaciones` WRITE;
/*!40000 ALTER TABLE `publicaciones` DISABLE KEYS */;
INSERT INTO `publicaciones` VALUES (1,'Constelación de Orión','2026-07-15','San Pedro de Atacama','Observé la constelación de Orión durante una noche muy despejada.',1,'2026-08-08 11:28:18','2026-08-08 11:28:18'),(2,'Venus al atardecer','2026-07-20','Antofagasta','Venus se podía observar claramente poco después de la puesta de sol.',2,'2026-08-08 11:28:18','2026-08-08 11:28:18'),(3,'Luna llena','2026-07-25','Calama','La luna estaba muy brillante y se podían distinguir varios detalles de su superficie.',3,'2026-08-08 11:28:18','2026-08-08 11:28:18'),(4,'Júpiter','2026-07-29','Valle de la Luna','Júpiter se observó claramente durante varias horas.',1,'2026-08-08 11:28:18','2026-08-08 11:28:18'),(5,'Cielo estrellado','2026-08-01','Taltal','La ausencia de contaminación lumínica permitió observar una gran cantidad de estrellas.',4,'2026-08-08 11:28:18','2026-08-08 11:28:18'),(6,'Saturno','2026-08-03','San Pedro de Atacama','Observación de Saturno durante una noche despejada.',5,'2026-08-08 11:28:18','2026-08-08 11:28:18'),(7,'Vía Láctea','2026-08-05','Desierto de Atacama','La Vía Láctea era visible a simple vista durante gran parte de la noche.',2,'2026-08-08 11:28:18','2026-08-08 11:28:18'),(8,'Lluvia de estrellas','2026-08-07','Antofagasta','Durante la madrugada fue posible observar varios meteoros.',1,'2026-08-08 11:28:18','2026-08-08 11:28:18');
/*!40000 ALTER TABLE `publicaciones` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuarios`
--

DROP TABLE IF EXISTS `usuarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuarios` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(45) NOT NULL,
  `apellido` varchar(45) NOT NULL,
  `email` varchar(100) NOT NULL,
  `contrasena` varchar(255) NOT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuarios`
--

LOCK TABLES `usuarios` WRITE;
/*!40000 ALTER TABLE `usuarios` DISABLE KEYS */;
INSERT INTO `usuarios` VALUES (1,'Daniela','González','daniela@test.com','usuario_prueba','2026-08-08 11:28:13','2026-08-08 11:28:13'),(2,'Camila','Rojas','camila@test.com','usuario_prueba','2026-08-08 11:28:13','2026-08-08 11:28:13'),(3,'Martín','Soto','martin@test.com','usuario_prueba','2026-08-08 11:28:13','2026-08-08 11:28:13'),(4,'Valentina','Muñoz','valentina@test.com','usuario_prueba','2026-08-08 11:28:13','2026-08-08 11:28:13'),(5,'Nicolás','Pérez','nicolas@test.com','usuario_prueba','2026-08-08 11:28:13','2026-08-08 11:28:13');
/*!40000 ALTER TABLE `usuarios` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-08-08 11:29:29
