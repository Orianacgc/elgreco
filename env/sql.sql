-- MySQL Script generated by MySQL Workbench
-- Wed May 24 17:34:53 2023
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema elgreco
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `elgreco` ;

-- -----------------------------------------------------
-- Schema elgreco
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `elgreco` DEFAULT CHARACTER SET utf8 ;
USE `elgreco` ;

-- -----------------------------------------------------
-- Table `elgreco`.`cliente`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `elgreco`.`cliente` ;

CREATE TABLE IF NOT EXISTS `elgreco`.`cliente` (
  `idcliente` INT NOT NULL AUTO_INCREMENT,
  `aPaterno` VARCHAR(45) ,
  `aMaterno` VARCHAR(45) ,
  `nombres` VARCHAR(45) ,
  `telefono` INT ,
  `email` VARCHAR(45),
  `calle` VARCHAR(45),
  `numero_exterior` VARCHAR(45),
  `numero_interior` VARCHAR(45),
  `colonia` VARCHAR(45) ,
  `CP` VARCHAR(45),
  `RFC` VARCHAR(45),
  `regimen` VARCHAR(45),
  PRIMARY KEY (`idcliente`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `elgreco`.`categoria`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `elgreco`.`categoria` ;

CREATE TABLE IF NOT EXISTS `elgreco`.`categoria` (
  `idcategoria` INT NOT NULL AUTO_INCREMENT,
  `descripcion` VARCHAR(255),
  `estado` VARCHAR(45),
  PRIMARY KEY (`idcategoria`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `elgreco`.`catalogo`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `elgreco`.`catalogo` ;

CREATE TABLE IF NOT EXISTS `elgreco`.`catalogo` (
  `idcatalogo` INT NOT NULL AUTO_INCREMENT,
  `idcategoria` INT ,
  `nombre` VARCHAR(45) ,
  `descripcion` VARCHAR(255),
  `caracteristicas` VARCHAR(2555) ,
  `estado` VARCHAR(45) ,
  `imagen` VARCHAR(45) ,
  PRIMARY KEY (`idcatalogo`),
  CONSTRAINT `fk_catalogo_categoria1`
    FOREIGN KEY (`idcategoria`)
    REFERENCES `elgreco`.`categoria` (`idcategoria`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `elgreco`.`producto`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `elgreco`.`producto` ;

CREATE TABLE IF NOT EXISTS `elgreco`.`producto` (
  `idproducto` INT NOT NULL auto_increment,
  `idcatalogo` INT ,
  `codigo` VARCHAR(45) ,
  `nombre` VARCHAR(45) ,
  `stock` INT ,
  `descripcion` VARCHAR(255) ,
  `medida` DECIMAL(11,2) ,
  `imagen` VARCHAR(45),
  `costo_venta` DECIMAL(11,2),
  `estado` VARCHAR(45) ,
  PRIMARY KEY (`idproducto`),
  CONSTRAINT `fk_producto_catalogo1`
    FOREIGN KEY (`idcatalogo` )
    REFERENCES `elgreco`.`catalogo` (`idcatalogo` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `elgreco`.`rol_usuario`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `elgreco`.`rol_usuario` ;

CREATE TABLE IF NOT EXISTS `elgreco`.`rol_usuario` (
  `idtipo_usuario` INT NOT NULL AUTO_INCREMENT,
  `descripcion` VARCHAR(255),
  PRIMARY KEY (`idtipo_usuario`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `elgreco`.`usuario`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `elgreco`.`usuario` ;

CREATE TABLE IF NOT EXISTS `elgreco`.`usuario` (
  `idUsuario` INT NOT NULL AUTO_INCREMENT,
  `usuario` VARCHAR(45),
  `password` VARCHAR(45),
  `nombre` VARCHAR(45),
  `apellido` VARCHAR(45),
   `imagen` VARCHAR(45),
  `estado` VARCHAR(45),
  `idtipo_usuario` INT,
  PRIMARY KEY (`idUsuario`),
  CONSTRAINT `fk_usuario_tipo_usuario1`
    FOREIGN KEY (`idtipo_usuario`)
    REFERENCES `elgreco`.`rol_usuario` (`idtipo_usuario`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `elgreco`.`estado`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `elgeco`.`estado` ;

CREATE TABLE IF NOT EXISTS `elgreco`.`estado` (
  `idestado` INT NOT NULL AUTO_INCREMENT,
  `descripcion` VARCHAR(255) ,
  PRIMARY KEY (`idestado`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `elgreco`.`forma_pago`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `elgreco`.`forma_pago` ;

CREATE TABLE IF NOT EXISTS `elgreco`.`forma_pago` (
  `idforma_pago` INT NOT NULL,
  `nombre_forma_pago` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idforma_pago`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `elgreco`.`comprobante_pago`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `elgreco`.`comprobante_pago` ;

CREATE TABLE IF NOT EXISTS `elgreco`.`comprobante_pago` (
  `idcomprobante_pago` INT NOT NULL AUTO_INCREMENT,
  `idforma_pago` INT ,
  `precio_venta` DECIMAL(11,2) ,
  `cantidad` INT ,
  PRIMARY KEY (`idcomprobante_pago`, `idforma_pago`),
  INDEX `fk_comprobante_pago_forma_pago1_idx` (`idforma_pago` ASC) VISIBLE,
  CONSTRAINT `fk_comprobante_pago_forma_pago1`
    FOREIGN KEY (`idforma_pago`)
    REFERENCES `elgreco`.`forma_pago` (`idforma_pago`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `elgreco`.`venta`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `elgreco`.`venta` ;

CREATE TABLE IF NOT EXISTS `elgreco`.`venta` (
  `idventa` INT NOT NULL AUTO_INCREMENT,
  `idcliente` INT,
  `idUsuario` INT ,
  `idestado` INT ,
  `idcomprobante_pago` INT,
  `fecha_venta` DATE,
  `fecha_entrega` DATE ,
  `total_venta` DOUBLE,
  `hora` TIME ,
  `anticipo` DECIMAL (11,2) ,
  `adeudo` DECIMAL(11,2) ,
  `IVA` DECIMAL(11,2),
  `valorUnitario` DECIMAL (11,2) ,
  `descripcion` VARCHAR(255) ,
  `subtotal` DECIMAL(11,2) ,
  PRIMARY KEY (`idventa`),
  INDEX `fk_venta_cliente1_idx` (`idcliente` ASC) VISIBLE,
  INDEX `fk_venta_usuario1_idx` (`idUsuario` ASC) VISIBLE,
  INDEX `fk_venta_estado1_idx` (`idestado` ASC) VISIBLE,
  INDEX `fk_venta_comprobante_pago1_idx` (`idcomprobante_pago` ASC) VISIBLE,
  CONSTRAINT `fk_venta_cliente1`
    FOREIGN KEY (`idcliente`)
    REFERENCES `elgreco`.`cliente` (`idcliente`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_venta_usuario1`
    FOREIGN KEY (`idUsuario`)
    REFERENCES `elgreco`.`usuario` (`idUsuario`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_venta_estado1`
    FOREIGN KEY (`idestado`)
    REFERENCES `elgreco`.`estado` (`idestado`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_venta_comprobante_pago1`
    FOREIGN KEY (`idcomprobante_pago` )
    REFERENCES `elgreco`.`comprobante_pago` (`idcomprobante_pago` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `elgreco`.`proveedor`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `elgreco`.`proveedor` ;

CREATE TABLE IF NOT EXISTS `elgreco`.`proveedor` (
  `idproveedor` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) ,
  `personaContacto` VARCHAR(45) ,
  `telefono` VARCHAR(45) ,
  `email` VARCHAR(45) ,
  `calle` VARCHAR(45) ,
  `numero_exterior` VARCHAR(45) ,
  `numero_interior` VARCHAR(45) ,
  `colonia` VARCHAR(45) ,
  `CP` VARCHAR(45) ,
  `estado` VARCHAR(45) ,
  `municipio` VARCHAR(45) ,
  PRIMARY KEY (`idproveedor`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `elgreco`.`compras`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `elgreco`.`compras` ;

CREATE TABLE IF NOT EXISTS `elgreco`.`compras` (
  `idcompras` INT NOT NULL AUTO_INCREMENT,
  `idproveedor` INT,
  `codigo` INT ,
  `nombre` VARCHAR(45),
  `descripcion` VARCHAR(255) ,
  `hora` TIME ,
  `fecha_compra` DATE ,
  `total` DECIMAL(11,2) ,
  PRIMARY KEY (`idcompras`),
  CONSTRAINT `fk_compras_proveedor1`
    FOREIGN KEY (`idproveedor`)
    REFERENCES `elgreco`.`proveedor` (`idproveedor`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `elgreco`.`detalle_compras`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `elgreco`.`detalle_compras` ;

CREATE TABLE IF NOT EXISTS `elgreco`.`detalle_compras` (
  `iddetalle_compras` INT NOT NULL AUTO_INCREMENT,
  `idcompras` INT ,
  `idproducto` INT,
  `cantidad` INT ,
  `precio_compra` DECIMAL(11,2) ,
  PRIMARY KEY (`iddetalle_compras`),
  INDEX `fk_detalle_compras_compras1_idx` (`idcompras` ASC) VISIBLE,
  INDEX `fk_detalle_compras_producto1_idx` (`idproducto` ASC) VISIBLE,
  CONSTRAINT `fk_detalle_compras_compras1`
    FOREIGN KEY (`idcompras` )
    REFERENCES `elgreco`.`compras` (`idcompras`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_detalle_compras_producto1`
    FOREIGN KEY (`idproducto`)
    REFERENCES `elgreco`.`producto` (`idproducto`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `elgreco`.`detalle_venta`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `elgreco`.`detalle_venta` ;

CREATE TABLE IF NOT EXISTS `elgreco`.`detalle_venta` (
  `iddetalle_venta` INT NOT NULL AUTO_INCREMENT,
  `idproducto` INT ,
  `cantidad` INT ,
  `precio_venta` DECIMAL(11,2) ,
  `descuento` DECIMAL(11,2) ,
  `idventa` INT ,
  PRIMARY KEY (`iddetalle_venta`),
  INDEX `fk_detalle_venta_producto1_idx` (`idproducto` ASC) VISIBLE,
  INDEX `fkdetalleaventa_idx` (`idventa` ASC) VISIBLE,
  CONSTRAINT `fk_detalle_venta_producto1`
    FOREIGN KEY (`idproducto`)
    REFERENCES `elgreco`.`producto` (`idproducto`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fkdetalleaventa`
    FOREIGN KEY (`idventa`)
    REFERENCES `elgreco`.`venta` (`idventa`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `elgreco`.`detalle_cotizacion`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `elgreco`.`detalle_cotizacion` ;

CREATE TABLE IF NOT EXISTS `elgreco`.`detalle_cotizacion` (
  `iddetalle_cotizacion` INT NOT NULL AUTO_INCREMENT,
  `cantidad` INT ,
  `precio_venta` DECIMAL(11,2) ,
  `descuento` DECIMAL(11,2) ,
  PRIMARY KEY (`iddetalle_cotizacion`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `elgreco`.`cotizacion`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `elgreco`.`cotizacion` ;

CREATE TABLE IF NOT EXISTS `elgreco`.`cotizacion` (
  `idcotizacion` INT NOT NULL AUTO_INCREMENT,
  `idcliente` INT ,
  `iddetalle_cotizacion` INT,
  `codigo` INT ,
  `fecha_cotizacion` DATE ,
  `descripcion` VARCHAR(255) ,
  `total` DECIMAL(11,2) ,
  `estado` VARCHAR(45) ,
  PRIMARY KEY (`idcotizacion`),
  INDEX `fk_cotizacion_cliente1_idx` (`idcliente` ASC) VISIBLE,
  INDEX `fk_cotizacion_detalle_cotizacion1_idx` (`iddetalle_cotizacion` ASC) VISIBLE,
  CONSTRAINT `fk_cotizacion_cliente1`
    FOREIGN KEY (`idcliente`)
    REFERENCES `elgreco`.`cliente` (`idcliente`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_cotizacion_detalle_cotizacion1`
    FOREIGN KEY (`iddetalle_cotizacion`)
    REFERENCES `elgreco`.`detalle_cotizacion` (`iddetalle_cotizacion`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
