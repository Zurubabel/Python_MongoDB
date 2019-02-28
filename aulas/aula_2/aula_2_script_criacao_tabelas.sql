/*
	Autor: Zurubabel
	Data: 27/02/2019

	Script para criação da base e tabela de dados para as aulas de Python + MongoDB

	Execute uma linha de cada vez
*/

USE MASTER;
-- Dropa (apaga) a base de dados caso ela exista.
DROP DATABASE Estudo_MongoDB

-- Cria a base de dados Estudo_MongoDB na pasta padrão do SQL Server
CREATE DATABASE Estudo_MongoDB;

-- Muda para a tabela Estudo_MongoDB
USE Estudo_MongoDB

-- Cria o usuário das aulas
USE [master]
GO
CREATE LOGIN [aula_mongodb] WITH PASSWORD=N'abc123', DEFAULT_DATABASE=[Estudo_MongoDB], CHECK_EXPIRATION=OFF, CHECK_POLICY=OFF
GO
USE [Estudo_MongoDB]
GO
CREATE USER [aula_mongodb] FOR LOGIN [aula_mongodb]
GO
USE [Estudo_MongoDB]
GO
ALTER ROLE [db_datareader] ADD MEMBER [aula_mongodb]
GO
USE [Estudo_MongoDB]
GO
ALTER ROLE [db_datawriter] ADD MEMBER [aula_mongodb]
GO

-- Tabela para teste da conexão de dados
CREATE TABLE tbl_Teste (
	id INT
);

INSERT INTO tbl_Teste
VALUES (1),(12), (500), (-222)