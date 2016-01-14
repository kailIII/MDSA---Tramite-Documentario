--Base de Datos
CREATE DATABASE Tramite_Documentario ON PRIMARY
(
NAME= Tramite_Documentario_Data,
FILENAME= 'C:\Tramite_Documentario_Data.mdf',   --Ruta donde es creada la BD
SIZE=5mb,			          --Tama�o Inicial de la BD
MAXSIZE=10mb,			      --Tama�o m�ximo de la BD
FILEGROWTH=1mb  		      --Incremento de la BD
)
LOG ON
(
NAME= Tramite_Documentario_Log,
FILENAME='C:\Tramite_Documentario_Log.ldf',	--Ruta donde es creado el LOG
SIZE=5mb,			        --Tama�o Inicial del LOG	
MAXSIZE=10mb,			    --Tama�o m�ximo del LOG
FILEGROWTH=1mb 			    --Incremento del LOG
)
GO

SET LANGUAGE SPANISH
GO
SET DATEFORMAT DMY
GO
USE Tramite_Documentario
GO