DROP DATABASE IF EXISTS sistema_seguros;
CREATE DATABASE sistema_seguros;
USE sistema_seguros;

CREATE TABLE catalogo_tipo_poliza (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE catalogo_estatus_poliza (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE catalogo_metodo_pago (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE catalogo_tipo_siniestro (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE clientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    apellidos VARCHAR(100) NOT NULL,
    fecha_nacimiento VARCHAR(20) NOT NULL,
    genero VARCHAR(30),
    curp VARCHAR(30) NOT NULL UNIQUE,
    telefono VARCHAR(10),
    correo VARCHAR(100),
    ocupacion VARCHAR(100),
    ingreso_mensual DECIMAL(10,2)
);

CREATE TABLE polizas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    numero_poliza INT NOT NULL UNIQUE,
    fecha_inicio DATE NOT NULL,
    fecha_fin DATE NOT NULL,
    prima_mensual DECIMAL(10,2) NOT NULL,
    suma_asegurada DECIMAL(10,2) NOT NULL,
    tipo_poliza_id INT NOT NULL,
    estatus_id INT NOT NULL,
    cliente_id INT NOT NULL,
    FOREIGN KEY (tipo_poliza_id) REFERENCES catalogo_tipo_poliza(id),
    FOREIGN KEY (estatus_id) REFERENCES catalogo_estatus_poliza(id),
    FOREIGN KEY (cliente_id) REFERENCES clientes(id)
);

CREATE TABLE beneficiarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    apellidos VARCHAR(100) NOT NULL,
    fecha_nacimiento VARCHAR(20) NOT NULL,
    parentesco VARCHAR(50),
    porcentaje_asignado DECIMAL(5,2) NOT NULL,
    poliza_id INT NOT NULL,
    FOREIGN KEY (poliza_id) REFERENCES polizas(id)
);

CREATE TABLE pagos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    fecha_pago DATE NOT NULL,
    monto_pagado DECIMAL(10,2) NOT NULL,
    metodo_pago_id INT NOT NULL,
    referencia VARCHAR(100),
    poliza_id INT NOT NULL,
    FOREIGN KEY (metodo_pago_id) REFERENCES catalogo_metodo_pago(id),
    FOREIGN KEY (poliza_id) REFERENCES polizas(id)
);

CREATE TABLE siniestros (
    id INT AUTO_INCREMENT PRIMARY KEY,
    fecha_reporte DATE NOT NULL,
    fecha_ocurrencia DATE NOT NULL,
    tipo_siniestro_id INT NOT NULL,
    monto_reclamado DECIMAL(10,2) NOT NULL,
    monto_aprobado DECIMAL(10,2) NOT NULL,
    estatus_siniestro VARCHAR(50),
    poliza_id INT NOT NULL,
    FOREIGN KEY (tipo_siniestro_id) REFERENCES catalogo_tipo_siniestro(id),
    FOREIGN KEY (poliza_id) REFERENCES polizas(id)
);

INSERT INTO catalogo_tipo_poliza (nombre) VALUES
('Vida'),
('Auto'),
('Gastos médicos'),
('Hogar');

INSERT INTO catalogo_estatus_poliza (nombre) VALUES
('Vigente'),
('Vencida'),
('Cancelada');

INSERT INTO catalogo_metodo_pago (nombre) VALUES
('Efectivo'),
('Tarjeta'),
('Transferencia');

INSERT INTO catalogo_tipo_siniestro (nombre) VALUES
('Accidente'),
('Robo'),
('Daño'),
('Enfermedad'),
('Fallecimiento');