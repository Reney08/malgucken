-- Datenbank erzeugen
CREATE DATABASE IF NOT EXISTS BarbotDB
  DEFAULT CHARACTER SET utf8mb4
  DEFAULT COLLATE utf8mb4_general_ci;

USE BarbotDB;

-- Table Cocktail
CREATE TABLE `Cocktail` (
  `CocktailID` int(11) NOT NULL AUTO_INCREMENT,
  `Name` varchar(30) NOT NULL,
  `Beschreibung` varchar(250) DEFAULT NULL,
  `ExtLink` varchar(200) DEFAULT NULL,
  `Bild` blob DEFAULT NULL,
  `verfuegbar` tinyint(1) NOT NULL DEFAULT 1,
  PRIMARY KEY (`CocktailID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Table Zapfstelle
CREATE TABLE `Zapfstelle` (
  `ZapfstelleID` int(11) NOT NULL AUTO_INCREMENT,
  `SchienenPos` int(11) NOT NULL,
  `Pumpe` tinyint(1) DEFAULT NULL,
  `PumpenNR` int(11) DEFAULT NULL,
  `Fuellmenge` int(11) DEFAULT NULL,
  PRIMARY KEY (`ZapfstelleID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Table Zutat
CREATE TABLE `Zutat` (
  `ZutatID` int(11) NOT NULL AUTO_INCREMENT,
  `Name` varchar(30) DEFAULT NULL,
  `Zapfstelle` int(11) DEFAULT NULL,
  `Alkohol` tinyint(1) NOT NULL,
  PRIMARY KEY (`ZutatID`),
  KEY `FK_ZutatenZapfstelle` (`Zapfstelle`),
  CONSTRAINT `FK_ZutatenZapfstelle` FOREIGN KEY (`Zapfstelle`) REFERENCES `Zapfstelle` (`ZapfstelleID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Table Rezept
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Table users
CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) DEFAULT NULL,
  `agb_accepted` tinyint(1) NOT NULL DEFAULT 0,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
