Herramientas

python vesion 3.10
driver conexion base de datos: mysql-connector-python
guia de estilos : flake8
consulta REST: Postman
modelado DB Mysql : Mysql Workbench

Desarrollo prueba:

1.crear repositorio
2.validar conexion a base de datos
3.explorar tablas y datos

SERVICIO CONSULTA:
4.crear conector a base de datos y validar
5.desarrollar consulta de porpiedades
6.realizar pruebas de consulta con filtros
7.realizar test

SERVICIO DE "ME GUSTA":
5. con la herramienta Workbench ejecutar funcionalidad de modelamiento de la base de datos
6. crear tabla pivot para almacenamiento de likes por usuario

Explicacion modelo:
Se realiza creación de una tabla pivot llamada like_history que almacenara los likes realizados por cada usuario registrado a cada propiedad, se establece una relación muchos a muchos entre usuarios y propiedades. Esto permite que un usuario pueda dar like a múltiples propiedades y que una propiedad pueda recibir likes de múltiples usuarios, de igual forma se almacena la fecha de cada like.

Se establece de esta manera teniendo encuenta normalizacion y flexibilidad.


codigo SQL:

-- -----------------------------------------------------
-- Table `habi_db`.`like_history`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `habi_db`.`like_history` (
  `id` INT NOT NULL,
  `property_id` INT(11) NOT NULL,
  `auth_user_id` INT(11) NOT NULL,
  `like_date` DATE NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_property_has_auth_user_auth_user1_idx` (`auth_user_id` ASC) VISIBLE,
  INDEX `fk_property_has_auth_user_property1_idx` (`property_id` ASC) VISIBLE,
  CONSTRAINT `fk_property_has_auth_user_property1`
    FOREIGN KEY (`property_id`)
    REFERENCES `habi_db`.`property` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_property_has_auth_user_auth_user1`
    FOREIGN KEY (`auth_user_id`)
    REFERENCES `habi_db`.`auth_user` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;