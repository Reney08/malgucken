-- MySQL dump 10.19  Distrib 10.2.44-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: BarbotDB
-- ------------------------------------------------------
-- Server version       10.2.44-MariaDB-1:10.2.44+maria~bionic

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Cocktail`
--

DROP TABLE IF EXISTS `Cocktail`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Cocktail` (
  `CocktailID` int(11) NOT NULL AUTO_INCREMENT,
  `Name` varchar(30) NOT NULL,
  `Beschreibung` varchar(250) DEFAULT NULL,
  `ExtLink` varchar(200) DEFAULT NULL,
  `Bild` blob DEFAULT NULL,
  `verfuegbar` tinyint(1) NOT NULL DEFAULT 1,
  PRIMARY KEY (`CocktailID`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Cocktail`
--

LOCK TABLES `Cocktail` WRITE;
/*!40000 ALTER TABLE `Cocktail` DISABLE KEYS */;
INSERT INTO `Cocktail` VALUES (1,'Mojito','Ein erfrischender kubanischer Cocktail mit Minze und Limette.','https://example.com/mojito',NULL,1),(2,'Caipirinha','Brasilianischer Cocktail mit Limette und Cachaa.','https://example.com/caipirinha',NULL,1),(3,'Gin Tonic','Klassischer Longdrink mit Gin und Tonic Water.','https://example.com/gin-tonic',NULL,0),(4,'Kiba','ein bunter Mix aus Kirschen und Bananensaft','https://example.com/kiba',NULL,1);
/*!40000 ALTER TABLE `Cocktail` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Rezept`
--

DROP TABLE IF EXISTS `Rezept`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Rezept` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `CocktailID` int(11) NOT NULL,
  `RezeptPos` int(11) NOT NULL,
  `ZutatID` int(11) NOT NULL,
  `Menge` int(11) DEFAULT NULL,
  PRIMARY KEY (`ID`),
  KEY `FK_RezeptCocktail` (`CocktailID`),
  KEY `FK_RezeptZutat` (`ZutatID`),
  CONSTRAINT `FK_RezeptCocktail` FOREIGN KEY (`CocktailID`) REFERENCES `Cocktail` (`CocktailID`),
  CONSTRAINT `FK_RezeptZutat` FOREIGN KEY (`ZutatID`) REFERENCES `Zutat` (`ZutatID`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Rezept`
--

LOCK TABLES `Rezept` WRITE;
/*!40000 ALTER TABLE `Rezept` DISABLE KEYS */;
INSERT INTO `Rezept` VALUES (1,1,1,1,4),(2,1,2,2,6),(3,1,3,3,2),(4,1,4,4,2),(5,1,5,5,8),(6,2,1,6,5),(7,2,2,3,2),(8,2,3,4,2),(9,3,1,7,4),(10,3,2,8,10),(11,4,1,13,100),(12,4,1,9,100);
/*!40000 ALTER TABLE `Rezept` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Zapfstelle`
--

DROP TABLE IF EXISTS `Zapfstelle`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Zapfstelle` (
  `ZapfstelleID` int(11) NOT NULL AUTO_INCREMENT,
  `SchienenPos` int(11) NOT NULL,
  `Pumpe` tinyint(1) DEFAULT NULL,
  `PumpenNR` int(11) DEFAULT NULL,
  `Fuellmenge` int(11) DEFAULT NULL,
  PRIMARY KEY (`ZapfstelleID`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Zapfstelle`
--

LOCK TABLES `Zapfstelle` WRITE;
/*!40000 ALTER TABLE `Zapfstelle` DISABLE KEYS */;
INSERT INTO `Zapfstelle` VALUES (1,0,NULL,NULL,NULL),(2,5107,NULL,NULL,NULL),(3,5000,NULL,0,0),(4,25,NULL,NULL,25),(5,525,NULL,NULL,25),(6,1025,NULL,NULL,25),(7,1525,NULL,NULL,25),(8,2025,NULL,NULL,25),(9,2525,NULL,NULL,25),(10,3025,1,0,NULL),(11,3025,1,1,NULL),(12,3025,1,2,NULL),(13,3025,1,3,NULL),(14,3025,1,4,NULL),(15,3025,1,5,NULL),(16,3025,1,6,NULL);
/*!40000 ALTER TABLE `Zapfstelle` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Zutat`
--

DROP TABLE IF EXISTS `Zutat`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Zutat` (
  `ZutatID` int(11) NOT NULL AUTO_INCREMENT,
  `Name` varchar(30) DEFAULT NULL,
  `Zapfstelle` int(11) DEFAULT NULL,
  `Alkohol` tinyint(1) NOT NULL,
  PRIMARY KEY (`ZutatID`),
  KEY `FK_ZutatenZapfstelle` (`Zapfstelle`),
  CONSTRAINT `FK_ZutatenZapfstelle` FOREIGN KEY (`Zapfstelle`) REFERENCES `Zapfstelle` (`ZapfstelleID`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Zutat`
--

LOCK TABLES `Zutat` WRITE;
/*!40000 ALTER TABLE `Zutat` DISABLE KEYS */;
INSERT INTO `Zutat` VALUES (1,'Vodka',4,1),(2,'Tequila',5,1),(3,'Barcardi',6,1),(4,'Rum',7,1),(5,'Korn',8,1),(6,'Gin',9,1),(7,'Cola',10,0),(8,'Orangensaft',11,0),(9,'Bananensaft',12,0),(10,'Tonic-Water',13,0),(11,'Fanta',14,0),(12,'Sprite',15,0),(13,'Kirschsaft',16,0);
/*!40000 ALTER TABLE `Zutat` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) DEFAULT NULL,
  `agb_accepted` tinyint(1) NOT NULL DEFAULT 0,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (5,'test','scrypt:32768:8:1$AtU1QzeNr3txKFwM$090d537d43a092ac528bd0b9553a97fcdadc9230bd1c5abcf7ac4f16df45a61dfc88573cd0990a41d5f23462cecd464adfec47b49f27aa12b8291c18662b417f',1);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-08-21  8:48:41