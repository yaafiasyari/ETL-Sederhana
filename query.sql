

/* SELECT dwh_fact_orders*/

SELECT
	u.ID,
	oi.order_id,
	concat ( u.first_name, ' ', u.last_name ) AS NAME,
	u.age,
	u.gender,
	u.STATE,
	u.street_address,
	u.postal_code,
	u.city,
	u.country,
	o.num_of_item,
	P.COST,
	P.category,
	P.brand,
	P.retail_price,
	P.department,
	oi.status,
	oi.created_at,
	oi.returned_at,
	oi.shipped_at,
	oi.delivered_at,
	ii.sold_at,
	ii.product_name 
FROM
	users AS u
	INNER JOIN orders AS o ON o.user_id = u.
	ID INNER JOIN order_item AS oi ON o.order_id = oi.order_id
	INNER JOIN products AS P ON P.ID = oi.product_id
	INNER JOIN inventory_items AS ii ON oi.inventory_item_id = ii.ID 

/* Create Table dwh_fact_orders*/

CREATE TABLE dwh_fact_orders (
"id"	INT NOT NULL,
order_id	INT NOT NULL,
"name"	VARCHAR(255) NOT NULL,
age	INT	NOT	NULL,
gender VARCHAR(2) NOT NULL,
"state" VARCHAR(255) NOT NULL,
street_address VARCHAR(255) NOT NULL,
postal_code	VARCHAR(255) NOT NULL,
city	VARCHAR(255) NOT NULL,
country VARCHAR(255) NOT NULL,
num_of_item INT NOT NULL,
"cost"	FLOAT NOT NULL,
category VARCHAR(255) NOT NULL,
brand	VARCHAR(255),
retail_price	FLOAT	NOT	NULL,
department	VARCHAR(255) NOT NULL,
status VARCHAR(255) NOT NULL,
created_at DATE NOT NULL,
returned_at DATE,
shipped_at DATE,
delivered_at DATE,
sold_at DATE,
product_name VARCHAR(255) NOT NULL);]

---------------------------------------------------------------------------------

/*SELECT dwh_fact_activityUsers*/

SELECT
	u.ID,
	concat ( u.first_name, ' ', u.last_name ) AS NAME,
	u.age,
	u.gender,
	u.STATE,
	u.street_address,
	u.postal_code,
	u.city,
	u.country,
	e.ip_address,
	e.browser,
	e.traffic_source,
	e.event_type 
FROM
	users AS u
	INNER JOIN events AS e ON e.user_id = u.ID


/* Create Table dwh_fact_activityUsers*/


CREATE TABLE dwh_fact_activityUsers (
"id"	INT NOT NULL,
order_id	INT NOT NULL,
"name"	VARCHAR(255) NOT NULL,
age	INT	NOT	NULL,
"Gender" VARCHAR(2) NOT NULL,
"state" VARCHAR(255) NOT NULL,
street_address VARCHAR(255) NOT NULL,
postal_code	VARCHAR(255) NOT NULL,
city	VARCHAR(255) NOT NULL,
country VARCHAR(255) NOT NULL,
ip_address VARCHAR(255) NOT NULL,
browser VARCHAR(255) NOT NULL,
traffic_source VARCHAR(255) NOT NULL,
event_type VARCHAR(255) NOT NULL);

---------------------------------------------------------------------------------
/*SELECT dwh_fact_employees*/

SELECT
	concat ( em."Fisrt_Name", ' ', em."Last_Name" ) AS FullName,
	em."Gender",
	round( em."Age" ) AS "Age",
	round( em."Length_Service" ) AS "Length_Service",
	round( em."Absent_Hours" ) AS "Absent_Hours",
	dc."name" AS city 
FROM
	employees AS em
	INNER JOIN distribution_centers AS dc ON dc."id" = em.distribution_centers_id

/* Create Table dwh_fact_employees*/

CREATE TABLE dwh_fact_employees (
fullname	VARCHAR(255) NOT NULL,
"Gender" VARCHAR(2) NOT NULL,
Age INT	NOT	NULL,
Length_Service INT	NOT	NULL,
Absent_Hours INT	NOT	NULL,
city	VARCHAR(255) NOT NULL);
