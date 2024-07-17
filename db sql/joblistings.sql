-- job_portal.joblistings definition

CREATE TABLE `joblistings` (
  `job_id` int NOT NULL AUTO_INCREMENT,
  `employer_id` int DEFAULT NULL,
  `job_title` varchar(100) NOT NULL,
  `job_description` text NOT NULL,
  `location` varchar(100) DEFAULT NULL,
  `salary` decimal(10,2) DEFAULT NULL,
  `date_posted` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `application_deadline` date DEFAULT NULL,
  `job_type` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `application_link` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`job_id`),
  KEY `employer_id` (`employer_id`),
  CONSTRAINT `joblistings_ibfk_1` FOREIGN KEY (`employer_id`) REFERENCES `users` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;