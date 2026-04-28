
-- SQL script for creating the necessary tables in a MySQL database.
-- This ensures a clean setup for storing chat conversations.

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for conversations
-- ----------------------------
DROP TABLE IF EXISTS `conversations`;
CREATE TABLE `conversations` (
  `id` VARCHAR(36) NOT NULL COMMENT 'UUID for the conversation',
  `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Timestamp of conversation creation',
  `updated_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT 'Timestamp of last update',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ----------------------------
-- Table structure for messages
-- ----------------------------
DROP TABLE IF EXISTS `messages`;
CREATE TABLE `messages` (
  `id` INT AUTO_INCREMENT NOT NULL,
  `conversation_id` VARCHAR(36) NOT NULL COMMENT 'Foreign key to conversations table',
  `sender_type` ENUM('user', 'bot') NOT NULL COMMENT 'Indicates if the message is from the user or the bot',
  `content` TEXT NOT NULL COMMENT 'The text content of the message',
  `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Timestamp of message creation',
  PRIMARY KEY (`id`),
  INDEX `idx_conversation_id` (`conversation_id`),
  FOREIGN KEY (`conversation_id`) REFERENCES `conversations` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

SET FOREIGN_KEY_CHECKS = 1;
