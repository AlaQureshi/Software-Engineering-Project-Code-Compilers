-- job_portal.savedjobs definition

CREATE TABLE `savedjobs` (
  `saved_job_id` int NOT NULL AUTO_INCREMENT,
  `job_id` int DEFAULT NULL,
  `job_seeker_id` int DEFAULT NULL,
  `date_saved` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`saved_job_id`),
  KEY `job_id` (`job_id`),
  KEY `job_seeker_id` (`job_seeker_id`),
  CONSTRAINT `savedjobs_ibfk_1` FOREIGN KEY (`job_id`) REFERENCES `joblistings` (`job_id`),
  CONSTRAINT `savedjobs_ibfk_2` FOREIGN KEY (`job_seeker_id`) REFERENCES `users` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;