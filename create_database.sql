-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema spotify
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema spotify
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `spotify` DEFAULT CHARACTER SET utf8 ;
USE `spotify` ;

-- -----------------------------------------------------
-- Table `spotify`.`track`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `spotify`.`track` (
  `track_id` CHAR(22) NOT NULL,             -- "6PFoEnjp0PAe5siGswjH9i"
  `track_name` VARCHAR(666) NULL,           -- "Dancing's Not a Crime"
  `track_number` TINYINT UNSIGNED NOT NULL, -- 6
  `collab` TINYINT UNSIGNED NOT NULL,       -- 0
  `explicit` TINYINT UNSIGNED NOT NULL,     -- 0
  PRIMARY KEY (`track_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `spotify`.`album`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `spotify`.`album` (
  `album_id` CHAR(22) NOT NULL,                   -- "6ApYSpXF8GxZAgBTHDzYge"
  `album_name` VARCHAR(666) NULL,                 -- "Pray for the Wicked"
  `album_img` BLOB NULL,                          -- 
  `album_type` VARCHAR(666) NOT NULL,             -- "album"
  `album_label` VARCHAR(666) NULL,                -- "DCD2 / Fueled By Ramen"
  `album_track_number` TINYINT UNSIGNED NOT NULL, -- 6
  PRIMARY KEY (`album_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `spotify`.`artist`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `spotify`.`artist` (
  `artist_id` CHAR(22) NOT NULL,        -- "20JZFwl6HVl6yg8a4H3ZqK"
  `artist_name` VARCHAR(666) NOT NULL,  -- "Panic! At The Disco"
  `artist_img` CHAR(40) NOT NULL,       -- "ab6761610000e5ebb256ae9a4b82bfff97776ae2"
  PRIMARY KEY (`artist_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `spotify`.`track_feature_metrics`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `spotify`.`track_feature_metrics` (
  `feature_id` INT NOT NULL,            -- 0
  `feature_name` VARCHAR(666) NOT NULL, -- "danceability"
  PRIMARY KEY (`feature_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `spotify`.`track_features`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `spotify`.`track_features` (
  `track_id` CHAR(22) NOT NULL, -- "6PFoEnjp0PAe5siGswjH9i"
  `feature_id` INT NOT NULL,    -- 0
  `value` FLOAT NOT NULL,       -- 0.526
  PRIMARY KEY (`track_id`, `feature_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `spotify`.`appears_on`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `spotify`.`appears_on` (
  `album_id` CHAR(22) NOT NULL,   -- "6ApYSpXF8GxZAgBTHDzYge"
  `artist_id` CHAR(22) NOT NULL,  -- "20JZFwl6HVl6yg8a4H3ZqK"
  PRIMARY KEY (`album_id`, `artist_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `spotify`.`artist_genre_metrics`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `spotify`.`artist_genre_metrics` (
  `genre_id` INT NOT NULL,            -- 63
  `genre_name` VARCHAR(666) NOT NULL, -- "modern rock"
  PRIMARY KEY (`genre_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `spotify`.`artist_genres`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `spotify`.`artist_genres` (
  `artist_id` CHAR(22) NOT NULL,  -- "20JZFwl6HVl6yg8a4H3ZqK"
  `genre_id` INT NOT NULL,        -- 63
  PRIMARY KEY (`artist_id`, `genre_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `spotify`.`weekly_track`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `spotify`.`weekly_track` (
  `week` CHAR(8) NOT NULL,                      -- 06292018
  `rank` TINYINT UNSIGNED NOT NULL,             -- 172
  `streams` INT UNSIGNED NOT NULL,              -- 4166609
  `track_id` CHAR(22) NOT NULL,                 -- "6PFoEnjp0PAe5siGswjH9i"
  `track_popularity` TINYINT UNSIGNED NOT NULL, -- 54
  PRIMARY KEY (`week`, `track_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `spotify`.`exists_on`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `spotify`.`exists_on` (
  `track_id` CHAR(22) NOT NULL,   -- "6PFoEnjp0PAe5siGswjH9i"
  `album_id` CHAR(22) NOT NULL,   -- "6ApYSpXF8GxZAgBTHDzYge"
  PRIMARY KEY (`album_id`, `track_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `spotify`.`creator`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `spotify`.`creator` (
  `album_id` CHAR(22) NOT NULL,   -- "6ApYSpXF8GxZAgBTHDzYge"
  `create_date` DATE NULL,        -- 2018-06-22
  `artist_id` CHAR(22) NOT NULL,  -- "20JZFwl6HVl6yg8a4H3ZqK"
  PRIMARY KEY (`album_id`, `artist_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `spotify`.`weekly_album`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `spotify`.`weekly_album` (
  `week` CHAR(8) NOT NULL,                      -- 06292018
  `album_popularity` TINYINT UNSIGNED NOT NULL, -- 72
  `album_id` CHAR(22) NOT NULL,                 -- "6ApYSpXF8GxZAgBTHDzYge"
  PRIMARY KEY (`week`, `album_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `spotify`.`weekly_artist`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `spotify`.`weekly_artist` (
  `week` CHAR(8) NOT NULL,                        -- 06292018
  `artist_popularity` TINYINT UNSIGNED NOT NULL,  -- 79
  `artist_followers` INT NOT NULL,                -- 11488092
  `artist_id` CHAR(22) NOT NULL,                  -- "20JZFwl6HVl6yg8a4H3ZqK" 
  PRIMARY KEY (`week`, `artist_id`))
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
