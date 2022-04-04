CREATE TABLE english
(
    idEnglish       INT unsigned NOT NULL 
    English         VARCHAR(500) NOT NULL
    PRIMARY KEY     (idEnglish)                                
);

CREATE TABLE french 
(
    idFrench        INT unsigned NOT NULL
    translated      VARCHAR(500) NOT NULL   
    PRIMARY KEY     (idFrench)      
);

CREATE TABLE spanish 
(
    idSpanish       INT unsigned NOT NULL
    translated      VARCHAR(500) NOT NULL   
    PRIMARY KEY     (idSpanish)      
);

CREATE TABLE chinese 
(
    idChinese       INT unsigned NOT NULL
    translated      VARCHAR(500) NOT NULL   
    PRIMARY KEY     (idChinese)      
);