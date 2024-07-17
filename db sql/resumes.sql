-- job_portal.resumes definition

CREATE TABLE `resumes` (
  `resume_id` int NOT NULL AUTO_INCREMENT,
  `job_seeker_id` int DEFAULT NULL,
  `resume_file_path` varchar(255) NOT NULL,
  `date_uploaded` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`resume_id`),
  KEY `job_seeker_id` (`job_seeker_id`),
  CONSTRAINT `resumes_ibfk_1` FOREIGN KEY (`job_seeker_id`) REFERENCES `users` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;