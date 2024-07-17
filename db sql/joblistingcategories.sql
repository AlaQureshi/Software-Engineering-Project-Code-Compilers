-- job_portal.joblistingcategories definition

CREATE TABLE `joblistingcategories` (
  `job_listing_category_id` int NOT NULL AUTO_INCREMENT,
  `job_id` int DEFAULT NULL,
  `category_id` int DEFAULT NULL,
  PRIMARY KEY (`job_listing_category_id`),
  KEY `job_id` (`job_id`),
  KEY `category_id` (`category_id`),
  CONSTRAINT `joblistingcategories_ibfk_1` FOREIGN KEY (`job_id`) REFERENCES `joblistings` (`job_id`),
  CONSTRAINT `joblistingcategories_ibfk_2` FOREIGN KEY (`category_id`) REFERENCES `jobcategories` (`category_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;