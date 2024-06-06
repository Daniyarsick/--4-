# Проект База Данных 4 семестр МЧС

> Выполнили проект Аннануров Даниил, Жуйков Алексей, Угарин Никита.

SQL запрос на базу данных
```
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 ;
USE `mydb` ;

-- -----------------------------------------------------
-- Table `mydb`.`GDZS`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`GDZS` (
  `Yes or No` VARCHAR(45) NOT NULL,
  `Comment` VARCHAR(255) NULL,
  PRIMARY KEY (`Yes or No`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Atestat`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Atestat` (
  `idAtestation` INT NOT NULL,
  `TypeAtestat` VARCHAR(45) NOT NULL,
  `YesorNo` VARCHAR(45) NULL,
  `DateAtestat` DATE NULL,
  `DateProfosm` DATE NULL,
  `Comments` VARCHAR(45) NULL,
  PRIMARY KEY (`idAtestation`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Owner`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Owner` (
  `id` INT NOT NULL,
  `FirstrName` VARCHAR(45) NOT NULL,
  `SecondName` VARCHAR(45) NOT NULL,
  `GDZS` VARCHAR(45) NOT NULL,
  `Position` VARCHAR(45) NULL,
  `Rank` VARCHAR(45) NULL,
  `Birthday` DATE NULL,
  `PerInitialTraning` VARCHAR(45) NULL,
  `Attestation` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `Emp_GDZS_idx` (`GDZS` ASC) VISIBLE,
  INDEX `Owner_Atest_idx` (`Attestation` ASC) VISIBLE,
  CONSTRAINT `Emp_GDZS`
    FOREIGN KEY (`GDZS`)
    REFERENCES `mydb`.`GDZS` (`Yes or No`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `Owner_Atest`
    FOREIGN KEY (`Attestation`)
    REFERENCES `mydb`.`Atestat` (`idAtestation`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Manometr`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Manometr` (
  `idManometr` INT NOT NULL,
  `DateofCreate` DATE NULL,
  `DateofInstallation` DATE NULL,
  `LifetimeM` VARCHAR(45) NULL,
  `periodSurveys` VARCHAR(45) NULL,
  `DateSurveys` DATE NULL,
  PRIMARY KEY (`idManometr`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Reductor`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Reductor` (
  `idReductor` INT NOT NULL,
  `DateofCreate` DATE NULL,
  `UsedDate` DATE NULL,
  `LifeTime` VARCHAR(45) NULL,
  PRIMARY KEY (`idReductor`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`FaultPart`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`FaultPart` (
  `idFaultPart` INT NOT NULL,
  `NameofPart` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idFaultPart`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`ConditionDASV/K`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`ConditionDASV/K` (
  `idCondition` INT NOT NULL,
  `NameType` VARCHAR(45) NOT NULL,
  `BaseorWay` VARCHAR(255) NULL,
  PRIMARY KEY (`idCondition`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`DASV/K-TYPE`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`DASV/K-TYPE` (
  `typeID(number)` INT NOT NULL,
  `Name` VARCHAR(45) NOT NULL,
  `DateofCreate` DATE NULL,
  `DateExpluatation` DATE NULL,
  `LifeTime` VARCHAR(45) NULL,
  `Condition` INT NOT NULL,
  `Ownerid` INT NOT NULL,
  `Faultypart` INT NOT NULL,
  `MonometrNum` INT NOT NULL,
  `ReductorNum` INT NOT NULL,
  `inBaseGDZS` VARCHAR(45) NULL,
  `countProperly` INT NOT NULL,
  `countFault` INT NOT NULL,
  PRIMARY KEY (`typeID(number)`),
  INDEX `DasvTypetoOwner_idx` (`Ownerid` ASC) VISIBLE,
  INDEX `DasvtoManometr_idx` (`MonometrNum` ASC) VISIBLE,
  INDEX `DasvtoReduct_idx` (`ReductorNum` ASC) VISIBLE,
  INDEX `DasvtoFault_idx` (`Faultypart` ASC) VISIBLE,
  INDEX `DasvtoCondit_idx` (`Condition` ASC) VISIBLE,
  CONSTRAINT `DasvTypetoOwner`
    FOREIGN KEY (`Ownerid`)
    REFERENCES `mydb`.`Owner` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `DasvtoManometr`
    FOREIGN KEY (`MonometrNum`)
    REFERENCES `mydb`.`Manometr` (`idManometr`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `DasvtoReduct`
    FOREIGN KEY (`ReductorNum`)
    REFERENCES `mydb`.`Reductor` (`idReductor`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `DasvtoFault`
    FOREIGN KEY (`Faultypart`)
    REFERENCES `mydb`.`FaultPart` (`idFaultPart`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `DasvtoCondit`
    FOREIGN KEY (`Condition`)
    REFERENCES `mydb`.`ConditionDASV/K` (`idCondition`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`OFSPStatistic`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`OFSPStatistic` (
  `idOFSP` INT NOT NULL,
  `WorkDate` VARCHAR(45) NULL,
  `WorkPlace` VARCHAR(45) NULL,
  `Adress` VARCHAR(45) NULL,
  `ActivationNum` VARCHAR(45) NOT NULL,
  `TimeActiv` VARCHAR(45) NULL,
  `RankCommander` VARCHAR(45) NOT NULL,
  `Saved` INT NOT NULL,
  `Evacuated` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idOFSP`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`ZvenoStatistic`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`ZvenoStatistic` (
  `idZvenoStatistic` INT NOT NULL,
  `NameofZveno` VARCHAR(45) NOT NULL,
  `Comments` VARCHAR(45) NULL,
  PRIMARY KEY (`idZvenoStatistic`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`14OFSP-Zveno`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`14OFSP-Zveno` (
  `idZveno` INT NOT NULL,
  `NameOtryad` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idZveno`),
  CONSTRAINT `OPSP-gd`
    FOREIGN KEY (`idZveno`)
    REFERENCES `mydb`.`OFSPStatistic` (`idOFSP`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `ZvenotoStat`
    FOREIGN KEY (`idZveno`)
    REFERENCES `mydb`.`ZvenoStatistic` (`idZvenoStatistic`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`OtdelenieStat`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`OtdelenieStat` (
  `idOtdelenieStat` INT NOT NULL,
  `NameofOtdelenie` VARCHAR(45) NOT NULL,
  `Comments` VARCHAR(45) NULL,
  PRIMARY KEY (`idOtdelenieStat`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`14OFSP-Otrdelenie`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`14OFSP-Otrdelenie` (
  `idOtdelenie` INT NOT NULL,
  `NameOtr` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idOtdelenie`),
  CONSTRAINT `OFSP-7P`
    FOREIGN KEY (`idOtdelenie`)
    REFERENCES `mydb`.`OFSPStatistic` (`idOFSP`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `OtdelenietoStat`
    FOREIGN KEY (`idOtdelenie`)
    REFERENCES `mydb`.`OtdelenieStat` (`idOtdelenieStat`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Ballons`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Ballons` (
  `idBallonsNum` INT NOT NULL,
  `DateCreated` DATE NOT NULL,
  `DateStartUsed` DATE NOT NULL,
  `LifeTime` VARCHAR(45) NULL,
  `FaulorNot` VARCHAR(45) NULL,
  `DateFirstSurvey` DATE NULL,
  `DateSurvey` DATE NULL,
  `PeriodSurvey` VARCHAR(45) NULL,
  `DateReplValve` DATE NULL,
  `BallonName` VARCHAR(45) NOT NULL,
  `BallonBrand` VARCHAR(45) NOT NULL,
  `Ballonscol` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idBallonsNum`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`DASK`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`DASK` (
  `idDASK` INT NOT NULL,
  `Name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idDASK`),
  CONSTRAINT `DasktoType`
    FOREIGN KEY (`idDASK`)
    REFERENCES `mydb`.`DASV/K-TYPE` (`typeID(number)`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `DasktoBallons`
    FOREIGN KEY (`idDASK`)
    REFERENCES `mydb`.`Ballons` (`idBallonsNum`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`DASV`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`DASV` (
  `idDASV` INT NOT NULL,
  `Name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idDASV`),
  CONSTRAINT `DasvtoType`
    FOREIGN KEY (`idDASV`)
    REFERENCES `mydb`.`DASV/K-TYPE` (`typeID(number)`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `DasvtoBallons`
    FOREIGN KEY (`idDASV`)
    REFERENCES `mydb`.`Ballons` (`idBallonsNum`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`ShtatnCount`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`ShtatnCount` (
  `idShtatnCount` INT NOT NULL,
  `ShtatnCountName` VARCHAR(45) NOT NULL,
  `ShtatnCount` INT NOT NULL,
  PRIMARY KEY (`idShtatnCount`),
  CONSTRAINT `ShtatnC_to_owners`
    FOREIGN KEY (`idShtatnCount`)
    REFERENCES `mydb`.`Owner` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`FactCount`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`FactCount` (
  `idFactCount` INT NOT NULL,
  `FactCountName` VARCHAR(45) NOT NULL,
  `CountFact` INT NOT NULL,
  PRIMARY KEY (`idFactCount`),
  CONSTRAINT `FactC_to_owners`
    FOREIGN KEY (`idFactCount`)
    REFERENCES `mydb`.`Owner` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Lessons`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Lessons` (
  `idLessons` INT NOT NULL,
  `DASVorDASK` VARCHAR(45) NOT NULL,
  `typeLessons` VARCHAR(45) NOT NULL,
  `DatePerf` DATE NULL,
  `Adress` VARCHAR(45) NULL,
  `ReasonsorComments` VARCHAR(255) NULL,
  `Lessonscol` VARCHAR(45) NULL,
  PRIMARY KEY (`idLessons`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Automobile`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Automobile` (
  `id` INT NOT NULL,
  `Brand` VARCHAR(45) NOT NULL,
  `CreatedDate` DATE NULL,
  `UsedDate` DATE NULL,
  `LifeTime` VARCHAR(45) NULL,
  `Staffing` VARCHAR(45) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`FaceDevice`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`FaceDevice` (
  `idFaceDevice` INT NOT NULL,
  `NameFaceDevice` VARCHAR(45) NOT NULL,
  `Count` INT NOT NULL,
  `FaultorNot` VARCHAR(255) NULL,
  PRIMARY KEY (`idFaceDevice`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`PointGDZS`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`PointGDZS` (
  `idPointGDZS` INT NOT NULL,
  `Name` VARCHAR(45) NOT NULL,
  `CreateDate` DATE NULL,
  `UsedDate` DATE NULL,
  `LifeTime` VARCHAR(45) NULL,
  `FaultorNot` VARCHAR(255) NULL,
  PRIMARY KEY (`idPointGDZS`),
  CONSTRAINT `PointtoDevice`
    FOREIGN KEY (`idPointGDZS`)
    REFERENCES `mydb`.`FaceDevice` (`idFaceDevice`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

USE `mydb` ;

-- -----------------------------------------------------
-- Placeholder table for view `mydb`.`view1`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`view1` (`id` INT);

-- -----------------------------------------------------
-- View `mydb`.`view1`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`view1`;
USE `mydb`;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;


```

**Выполнение удаление строки:**

![image](https://github.com/Daniyarsick/--4-/assets/124454981/7b87c22e-ff64-422a-aba7-8416b19d0d5f)

**Выполнение добавление строки:**

![image](https://github.com/Daniyarsick/--4-/assets/124454981/e5869a61-cc23-4905-bd15-889058260acf)
