CREATE TABLE Dictonary
(
    id              INT unsigned NOT NULL 
    English         VARCHAR(500) NOT NULL
    PRIMARY KEY     (id)                                
);

CREATE TABLE French 
(
    id              INT unsigned NOT NULL
    translated      VARCHAR(500) NOT NULL   
    PRIMARY KEY     (id)      
);

CREATE TABLE Spanish 
(
    id              INT unsigned NOT NULL
    translated      VARCHAR(500) NOT NULL   
    PRIMARY KEY     (id)      
);

CREATE TABLE Chinese 
(
    id              INT unsigned NOT NULL
    translated      VARCHAR(500) NOT NULL   
    PRIMARY KEY     (id)      
);