create table pizza
(
    id          int auto_increment
        primary key,
    name        varchar(50)  not null,
    price       int          not null,
    description varchar(255) null,
    picture     varchar(100) null,
    alt         varchar(50)  not null,
    constraint pizza_id_uindex
        unique (id),
    constraint pizza_name_uindex
        unique (name)
);

INSERT INTO `web-project-g3`.pizza (id, name, price, description, picture, alt) VALUES (1, 'Corny', 70, 'Corn, tomato, bell pepper and olive pizza', 'pizza1.png', 'pizza1');
INSERT INTO `web-project-g3`.pizza (id, name, price, description, picture, alt) VALUES (2, 'Popeye', 60, 'Spinach, pineapple, onion and bell pepper pizza', 'pizza2.jpg', 'pizza2');
INSERT INTO `web-project-g3`.pizza (id, name, price, description, picture, alt) VALUES (4, 'Not Kosher', 18, 'Feta cheese, mushroom, ham and tomato pizza', 'pizza3.jpg', 'pizza3');
INSERT INTO `web-project-g3`.pizza (id, name, price, description, picture, alt) VALUES (5, 'Pepperoni', 65, 'Classic pepperoni and tomato pizza', 'pizza4.jpg', 'pizza4');
INSERT INTO `web-project-g3`.pizza (id, name, price, description, picture, alt) VALUES (6, 'Marshall', 100, 'Sweet s''mores pizza', 'pizza5.jpg', 'pizza5');
INSERT INTO `web-project-g3`.pizza (id, name, price, description, picture, alt) VALUES (7, 'Hawaiin', 73, 'Pineapple and ham pizza', 'pizza6.jpg', 'pizza6');
INSERT INTO `web-project-g3`.pizza (id, name, price, description, picture, alt) VALUES (8, 'Mexican', 55, 'Guacamole, jalapeno and mozzarella pizza', 'pizza7.jpg', 'pizza7');
INSERT INTO `web-project-g3`.pizza (id, name, price, description, picture, alt) VALUES (9, 'Bad Breath', 50, 'Onion and tomato pizza', 'pizza8.jpg', 'pizza8');



create table `web-project-g3`.users
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





INSERT INTO `web-project-g3`.users (email, username, birthday, password, date_added, points) VALUES ('idan@email.com', 'idanM', '1993-06-26', 'password', '2022-06-27', 673);
INSERT INTO `web-project-g3`.users (email, username, birthday, password, date_added, points) VALUES ('wda@das.com', 'asdf', '2022-07-17', 'sad', '2022-07-17', 124);


create table `web-project-g3`.orders
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





INSERT INTO `web-project-g3`.orders (id, email, order_time, time_wanted, address, phone_number, pizza, amount, total_price, cc_number, cc_exp, cvv) VALUES (1, 'idan@email.com', '2022-07-05 12:51:37', '18:51:37', 'mefalsim', '0508856994', 'mexican', 2, 134, '1111111111111111', '2023-07-19', '111');
INSERT INTO `web-project-g3`.orders (id, email, order_time, time_wanted, address, phone_number, pizza, amount, total_price, cc_number, cc_exp, cvv) VALUES (2, 'idan@email.com', '2022-07-17 19:28:08', '14:34:33', 'bash', '0657834465', 'hawaiian', 4, 455, '2222333344445555', '2022-07-29', '123');
INSERT INTO `web-project-g3`.orders (id, email, order_time, time_wanted, address, phone_number, pizza, amount, total_price, cc_number, cc_exp, cvv) VALUES (3, 'wda@das.com', '2022-08-17 19:33:20', '12:34:22', 'safd', '0508856995', 'asdfsad', 3, 123, '1111111111111111', '2022-07-08', '777');