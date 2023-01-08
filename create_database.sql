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
  `track_id` CHAR(22) NOT NULL,
  `track_name` VARCHAR(666) NULL,
  `track_number` TINYINT UNSIGNED NOT NULL,
  `collab` TINYINT UNSIGNED NOT NULL,
  `explicit` TINYINT UNSIGNED NOT NULL,
  PRIMARY KEY (`track_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `spotify`.`album`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `spotify`.`album` (
  `album_id` CHAR(22) NOT NULL,
  `album_name` VARCHAR(666) NULL,
  `album_img` BLOB NULL,
  `album_type` VARCHAR(666) NOT NULL,
  `album_label` VARCHAR(666) NULL,
  `album_track_number` TINYINT UNSIGNED NOT NULL,
  PRIMARY KEY (`album_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `spotify`.`artist`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `spotify`.`artist` (
  `artist_id` CHAR(22) NOT NULL,
  `artist_name` VARCHAR(666) NOT NULL,
  `artist_img` CHAR(40) NOT NULL,
  PRIMARY KEY (`artist_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `spotify`.`track_feature_metrics`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `spotify`.`track_feature_metrics` (
  `feature_id` INT NOT NULL,
  `feature_name` VARCHAR(666) NOT NULL,
  PRIMARY KEY (`feature_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `spotify`.`track_features`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `spotify`.`track_features` (
  `track_id` CHAR(22) NOT NULL,
  `feature_id` INT NOT NULL,
  `value` FLOAT NOT NULL,
  PRIMARY KEY (`track_id`, `feature_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `spotify`.`appears_on`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `spotify`.`appears_on` (
  `album_id` CHAR(22) NOT NULL,
  `artist_id` CHAR(22) NOT NULL,
  PRIMARY KEY (`album_id`, `artist_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `spotify`.`artist_genre_metrics`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `spotify`.`artist_genre_metrics` (
  `genre_id` INT NOT NULL,
  `genre_name` VARCHAR(666) NOT NULL,
  PRIMARY KEY (`genre_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `spotify`.`artist_genres`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `spotify`.`artist_genres` (
  `artist_id` CHAR(22) NOT NULL,
  `genre_id` INT NOT NULL,
  PRIMARY KEY (`artist_id`, `genre_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `spotify`.`weekly_track`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `spotify`.`weekly_track` (
  `week` CHAR(8) NOT NULL,
  `rank` TINYINT UNSIGNED NOT NULL,
  `streams` INT UNSIGNED NOT NULL,
  `track_id` CHAR(22) NOT NULL,
  `track_popularity` TINYINT UNSIGNED NOT NULL,
  PRIMARY KEY (`week`, `track_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `spotify`.`exists_on`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `spotify`.`exists_on` (
  `album_id` CHAR(22) NOT NULL,
  `track_id` CHAR(22) NOT NULL,
  PRIMARY KEY (`album_id`, `track_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `spotify`.`creator`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `spotify`.`creator` (
  `album_id` CHAR(22) NOT NULL,
  `create_date` DATE NULL,
  `artist_id` CHAR(22) NOT NULL,
  PRIMARY KEY (`album_id`, `artist_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `spotify`.`weekly_album`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `spotify`.`weekly_album` (
  `week` CHAR(8) NOT NULL,
  `album_popularity` TINYINT UNSIGNED NOT NULL,
  `album_id` CHAR(22) NOT NULL,
  PRIMARY KEY (`week`, `album_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `spotify`.`weekly_artist`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `spotify`.`weekly_artist` (
  `week` CHAR(8) NOT NULL,
  `artist_popularity` TINYINT UNSIGNED NOT NULL,
  `artist_followers` INT NOT NULL,
  `artist_id` CHAR(22) NOT NULL,
  PRIMARY KEY (`week`, `artist_id`))
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
