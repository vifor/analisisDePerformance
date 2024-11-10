CREATE TABLE IF NOT EXISTS `languages` (
  `repo_name` char(80) DEFAULT NULL,
  `language_name` char(20) DEFAULT NULL,
  `language_bytes` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci