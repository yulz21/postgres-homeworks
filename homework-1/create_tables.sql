-- SQL-команды для создания таблиц
CREATE TABLE employees
(
	first_name varchar(100) NOT NULL,
 	last_name varchar(100) NOT NULL,
 	title varchar (100) NOT NULL,
 	birth_date date,
	notes text
);
CREATE TABLE customers
(
	customer_id varchar(100) PRIMARY KEY,
	company_name varchar(100) NOT NULL,
	contact_name varchar(100)
);

CREATE TABLE orders
(
	order_id serial PRIMARY KEY,
	customer_id varchar(100) REFERENCES customers(customer_id),
	employee_id int,
	order_date date,
	ship_city varchar(100)
);
