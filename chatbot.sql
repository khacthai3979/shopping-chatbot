﻿CREATE TABLE [user] (
    id INT PRIMARY KEY IDENTITY(1,1),  
    username VARCHAR(255) NOT NULL,      
    email VARCHAR(255) NOT NULL,         
    password VARCHAR(255) NOT NULL       
);
GO
