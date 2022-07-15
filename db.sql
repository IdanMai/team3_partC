create table orders
(
    id           int auto_increment
        primary key,
    email        varchar(255) not null,
    order_time   datetime     not null,
    time_wanted  time         not null,
    address      varchar(255) not null,
    phone_number varchar(20)  not null,
    pizza        varchar(255) not null,
    amount       int          not null,
    total_price  int          not null,
    cc_number    varchar(20)  not null,
    cc_exp       date         not null,
    cvv          varchar(20)  not null,
    constraint orders_id_uindex
        unique (id)
);

create table pizza
(
    id          int auto_increment
        primary key,
    name        varchar(50)  not null,
    price       int          not null,
    description varchar(255) null,
    constraint pizza_id_uindex
        unique (id),
    constraint pizza_name_uindex
        unique (name)
);

create table users
(
    email      varchar(255)  not null
        primary key,
    username   varchar(255)  not null,
    birthday   date          not null,
    password   varchar(255)  not null,
    date_added date          not null,
    points     int default 0 not null,
    constraint users_email_uindex
        unique (email)
);


INSERT INTO pizza (id, name, price, description) VALUES (1, 'mexican', 70, 'the best one');

INSERT INTO users (email, username, birthday, password, date_added, points) VALUES ('idan@email.com', 'idanM', '1993-06-26', 'password', '2022-06-27', 673);