-- MySQL dump 10.13  Distrib 8.0.13, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: benchmark
-- ------------------------------------------------------
-- Server version	8.0.13

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `pc`
--

DROP TABLE IF EXISTS `pc`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `pc` (
  `idPC` int(11) NOT NULL,
  `model` varchar(200) NOT NULL,
  `score` double NOT NULL,
  PRIMARY KEY (`idPC`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pc`
--

LOCK TABLES `pc` WRITE;
/*!40000 ALTER TABLE `pc` DISABLE KEYS */;
INSERT INTO `pc` VALUES (1,'Intel(R) Core(TM) i7-5500U CPU @ 2.40GHz',1),(2,'Intel(R) Core(TM) i7-5500U CPU @ 2.40GHz',0.8789448067802872),(3,'Intel(R) Core(TM) i7-5500U CPU @ 2.40GHz',0.9586836844461659),(4,'Intel(R) Core(TM) i7-5500U CPU @ 2.40GHz',1.0605536765565329);
/*!40000 ALTER TABLE `pc` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pcexectime`
--

DROP TABLE IF EXISTS `pcexectime`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `pcexectime` (
  `idPC` int(11) NOT NULL AUTO_INCREMENT,
  `execTimeChaos` double NOT NULL,
  `execTimeDeltaBlue` double NOT NULL,
  `execTimeDjangoTemplate` double NOT NULL,
  `execTimeFloat` double NOT NULL,
  `execTimeGo` double NOT NULL,
  `execTimeHexiom` double NOT NULL,
  `execTimeJsonDumps` double NOT NULL,
  `execTimeJsonLoads` double NOT NULL,
  `execTimeMdp` double NOT NULL,
  `execTimeMeteorContest` double NOT NULL,
  `execTimeNbody` double NOT NULL,
  `execTimeNqueens` double NOT NULL,
  `execTimePidigits` double NOT NULL,
  `execTimePyflate` double NOT NULL,
  `execTimeRaytrace` double NOT NULL,
  `execTimeRegexDna` double NOT NULL,
  `execTimeRichards` double NOT NULL,
  `execTimeScimark` double NOT NULL,
  `execTimeSpectralNorm` double NOT NULL,
  `execTimeSqliteSynth` double NOT NULL,
  PRIMARY KEY (`idPC`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pcexectime`
--

LOCK TABLES `pcexectime` WRITE;
/*!40000 ALTER TABLE `pcexectime` DISABLE KEYS */;
INSERT INTO `pcexectime` VALUES (1,6.101127468421988,6.911109438506698,6.273862695523652,6.705759993431229,7.061041698028003,6.5706596485706115,8.636475254197862,7.251597717351146,10.338900825202195,10.432476342150991,10.427492456173965,8.525395837039667,7.48825660640729,7.432309129226937,10.825129921448422,6.854358826105411,7.386272973601734,9.586679587535741,9.181935359161372,5.71191736345844),(2,6.821727929604642,7.961792915988121,12.895643312167284,8.629123872702642,8.38481937582965,8.397782440162572,10.50637162495039,8.929232582486016,11.948870906490768,11.524956208175382,9.324015453724357,9.022043453122222,7.606039936091307,7.591393195845242,11.216559553460229,7.132037055410336,7.961866900223072,10.022492918040882,9.841993622815522,5.966034821343044),(3,6.927321822013602,7.527969462044805,6.149531119565367,7.082193491440066,7.3864196591080145,6.6260729852339395,8.891068263927849,7.747154814363718,11.00622836068041,10.308006633777183,9.199440542334386,8.565186525802957,7.746384180887603,7.3761482524325,11.166963601467032,7.11800528238885,7.852419412779,9.921882911608918,10.695647246589033,6.804166723687274),(4,6.132016527992555,6.5994626093085,6.127310617464728,6.657251994580761,6.751794438438274,5.957532193833565,8.304218042231739,7.432618323457369,9.72583238679129,9.311292731241366,7.776147653716151,7.560085462482718,6.869356670726532,6.756267704897837,10.45460276025345,6.803139497488814,6.945117382617383,9.17734106646779,9.435192376117016,5.399930548903143);
/*!40000 ALTER TABLE `pcexectime` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `server`
--

DROP TABLE IF EXISTS `server`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `server` (
  `idServer` int(11) NOT NULL,
  `model` varchar(200) NOT NULL,
  `score` double NOT NULL,
  PRIMARY KEY (`idServer`),
  CONSTRAINT `IDServer` FOREIGN KEY (`idServer`) REFERENCES `serverexectime` (`idserver`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `server`
--

LOCK TABLES `server` WRITE;
/*!40000 ALTER TABLE `server` DISABLE KEYS */;
INSERT INTO `server` VALUES (1,'Intel(R) Xeon(R) CPU X5660 @ 2.80GHz',1);
/*!40000 ALTER TABLE `server` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `serverexectime`
--

DROP TABLE IF EXISTS `serverexectime`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `serverexectime` (
  `idServer` int(11) NOT NULL AUTO_INCREMENT,
  `execTimeChaos` double NOT NULL,
  `execTimeDeltaBlue` double NOT NULL,
  `execTimeDjangoTemplate` double NOT NULL,
  `execTimeFloat` double NOT NULL,
  `execTimeGo` double NOT NULL,
  `execTimeHexiom` double NOT NULL,
  `execTimeJsonDumps` double NOT NULL,
  `execTimeJsonLoads` double NOT NULL,
  `execTimeMdp` double NOT NULL,
  `execTimeMeteorContest` double NOT NULL,
  `execTimeNbody` double NOT NULL,
  `execTimeNqueens` double NOT NULL,
  `execTimePidigits` double NOT NULL,
  `execTimePyflate` double NOT NULL,
  `execTimeRaytrace` double NOT NULL,
  `execTimeRegexDna` double NOT NULL,
  `execTimeRichards` double NOT NULL,
  `execTimeScimark` double NOT NULL,
  `execTimeSpectralNorm` double NOT NULL,
  `execTimeSqliteSynth` double NOT NULL,
  PRIMARY KEY (`idServer`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `serverexectime`
--

LOCK TABLES `serverexectime` WRITE;
/*!40000 ALTER TABLE `serverexectime` DISABLE KEYS */;
INSERT INTO `serverexectime` VALUES (1,4,4.5,5,3.5,4,4,6,6,7,8,7,6,6,6,8,5,6,7.5,7.5,4.5);
/*!40000 ALTER TABLE `serverexectime` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-12-18 19:07:45
