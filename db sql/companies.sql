-- job_portal.companies definition

CREATE TABLE `companies` (
  `company_id` int NOT NULL AUTO_INCREMENT,
  `employer_id` int DEFAULT NULL,
  `company_name` varchar(100) NOT NULL,
  `industry` varchar(50) DEFAULT NULL,
  `company_description` text,
  `location` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`company_id`),
  KEY `employer_id` (`employer_id`),
  CONSTRAINT `companies_ibfk_1` FOREIGN KEY (`employer_id`) REFERENCES `users` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;