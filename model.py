#!python3

def get_distribution_centers():
    sql = """
            select * from public.distribution_centers
    """
    return sql

def get_employees():
    sql = """
            select * from public.employees
    """
    return sql

def get_events():
    sql = """
            select * from public.events
    """
    return sql

def get_inventory_items():
    sql = """
            select * from public.inventory_items
    """
    return sql

def get_order_item():
    sql = """
            select * from public.order_item
    """
    return sql

def get_orders():
    sql = """
            select * from public.orders
    """
    return sql

def get_products():
    sql = """
            select * from public.products
    """
    return sql

def get_users():
    sql = """
            select * from public.users
    """
    return sql

def list_tables():
    tables = [("users",get_users()),
              ("products",get_products()),
              ("distribution_centers",get_distribution_centers()),
              ("employees",get_employees()),
              ("events",get_events()),
              ("inventory_items",get_inventory_items()),
              ("order_item",get_order_item()),
              ("orders",get_orders())]

    return tables

def dwh_fact_orders():
    sql = """
            SELECT
                u.ID AS user_id,
                oi.order_id,
                concat ( u.first_name, ' ', u.last_name ) AS NAME,
            CASE 
                    WHEN u.gender = 'F' THEN
                    'FEMALE' ELSE'MALE' 
                END AS gender,
                u.age,
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
                ii.product_name 
            FROM
                users AS u
                INNER JOIN orders AS o ON o.user_id = u.
                ID INNER JOIN order_item AS oi ON o.order_id = oi.order_id
                INNER JOIN products AS P ON P.ID = oi.product_id
                INNER JOIN inventory_items AS ii ON oi.inventory_item_id = ii.ID 
    """

    return sql

def dwh_fact_employees():
    sql = """
            
            SELECT
                concat ( em."Fisrt_Name", ' ', em."Last_Name" ) AS FullName,
                CASE 
                    WHEN em."Gender" = 'F' THEN
                    'FEMALE' ELSE'MALE' 
                END AS gender,
                round( em."Age" ) AS "Age",
                round( em."Length_Service" ) AS "Length_Service",
                round( em."Absent_Hours" ) AS "Absent_Hours",
                dc."name" AS city 
            FROM
                employees AS em
                INNER JOIN distribution_centers AS dc ON dc."id" = em.distribution_centers_id
 
    """

    return sql

def dwh_fact_activityusers():
    sql = """
            
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
 
    """

    return sql

    






