CREATE DATABASE faithful;
GO
USE faithful;
GO

SET ANSI_NULLS ON;
GO

SET QUOTED_IDENTIFIER ON;
GO

CREATE TABLE geysers(
	Id int NOT NULL,
	Eruption_length float NOT NULL,
	Eruption_wait int NOT NULL);
GO