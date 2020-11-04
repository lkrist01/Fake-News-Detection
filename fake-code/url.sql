-- MySQL dump 10.13  Distrib 5.7.25, for Linux (x86_64)
--
-- Host: localhost    Database: testing
-- ------------------------------------------------------
-- Server version	5.7.25-0ubuntu0.18.04.2

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
-- Table structure for table `url`
--

DROP TABLE IF EXISTS `url`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `url` (
  `id` int(6) unsigned NOT NULL AUTO_INCREMENT,
  `url` varchar(512) DEFAULT NULL,
  `hash` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=152 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `url`
--

LOCK TABLES `url` WRITE;
/*!40000 ALTER TABLE `url` DISABLE KEYS */;
INSERT INTO `url` VALUES (132,'https://yournewswire.com/puerto-rico-mayor-fraud-disaster/','12066536389135491234'),(133,'http://www2.alabamavotes.gov/electionNight/statewideResultsByContest.aspx?ecode=1000915','18127239644780002910'),(134,'www.thegatewaypundit.com/2018/01/stunning-democrats-boo-parents-girls-murdered-ms-13-killers-new-york-video/','18301748220926296786'),(135,'our.news/2017/08/08/300000-pounds-of-counterfeit-rat-meat-has-been-sold-as-chicken-wings-in-the-u-s/','1374942877397119698'),(136,'https://web.archive.org/web/20170214153057/http://uspoln.com:80/2017/02/07/john-hagee-god-made-lesbians-flat-identified-normal-people-easily-2','15523022216263224883'),(137,'https://www.washingtonpost.com/graphics/politics/2016-election/write-in-votes/','9682853168566811072'),(138,'https://web.archive.org/web/20171228111229/http://defense-usa.xyz/2017/12/15/boom-roy-moore-takes-the-military-vote-pulls-ahead-by-5k-votes/','55656652449206788'),(139,'http://www.puppetstringnews.com/blog/tennessee-gop-twitter-taken-down-after-tweet-exposin-pelosi-involved-in-pedophilia','16825458760271544958'),(140,'usanewscentral.com/bill-clintons-hitman-confesses-on-his-deathbed-source-hannity/','16825458760271544958'),(141,'http://babylonbee.com/news/isis-lays-arms-katy-perrys-impassioned-plea-like-just-co-exist/','16367446527975254401'),(142,'http://pix11.com/2017/01/24/man-pardoned-by-obama-shot-and-killed-by-masked-men-at-halfway-house/','16825458760271544958'),(143,'https://web.archive.org/web/20170314174618/http://wbn12.com/rosenberg-tx/new-star-wars-movie-filming-near-rosenberg-texas-large-number-of-extras-needed/','14346404964433377650'),(144,'https://www.usatoday.com/story/news/politics/onpolitics/2017/07/15/fox-news-shepard-smith-lie-after-lie-after-lie-russia-meeting/481751001/','5434729133948468018'),(145,'www.disclose.tv/australia-becomes-first-country-to-begin-microchipping-its-citizens-313155','14082776743176385462'),(146,'http://londonwebnews.com/2017/06/01/liberal-women-hate-me-because-of-my-striking-beauty-and-intellect-says-kellyanne-conway/','10797416217652855562'),(147,'http://www.breakingnews365.net/59c36cdd7b326/washington-state-legislature-votes-to-change-its-name-because-george-washington-owned-slaves.html','6603952812566151554'),(148,'www.thesun.co.uk/news/5999912/buzz-aldrin-ufo-lie-detector-test-alien-life-exists-convinced/','18206565587778180068'),(149,'https://www.ecfr.gov/cgi-bin/text-idx?gp=&SID=b5df8668c5d53fb99d5c5fd1e20c0ab0&mc=true&tpl=/ecfrbrowse/Title05/5tab_02.tpl','5633310718766827282'),(150,'https://www.inspiringday.com/prince_william_may_not_attend_royal_wedding_leaving_prince_harry_without_a_best_man','3362738721105481247'),(151,'https://www.unilad.co.uk/science/nasa-confirms-15-days-of-darkness-coming-this-month/','863246786061885850');
/*!40000 ALTER TABLE `url` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-04-03 18:45:57
