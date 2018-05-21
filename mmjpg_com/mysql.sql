create table big_item(
    id int not null,
    name varchar(20) not null,
    url varchar(50) not null,
    primary KEY(id),
)
create table little_item(
    id int not null,
    p_id int not null,
    name VARCHAR(30) NOT NULL,
    url VARCHAR(50) NOT NULL,
    PRIMARY KEY(id),
    FOREIGN KEY(p_id) REFERENCES big_item(id)
)
CREATE TABLE image
(
    id INT NOT NULL,
    p_id INT NOT NULL,
    p_p_id INT NOT NULL,
    NAME VARCHAR(30),
    url VARCHAR(100) NOT NULL,
    PRIMARY KEY(id),
    FOREIGN KEY(p_id) REFERENCES little_item(id),
    FOREIGN KEY(p_p_id) REFERENCES big_item(id)
)