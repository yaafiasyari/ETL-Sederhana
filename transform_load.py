#!python3

import pandas
import connection
import model

from sqlalchemy import create_engine
from hdfs import InsecureClient
from datetime import datetime

if __name__ == "__main__":
    time = datetime.now().strftime("%Y%m%d")

    engine = create_engine('postgresql://postgres:buyung12345@localhost:5432/dwh_FinalProject')

    conf_hadoop = connection.param_config("hadoop")["ip"]
    client = InsecureClient(conf_hadoop)


    conf_postgresql = connection.param_config("postgresql")
    conn = connection.postgres_conn(conf_postgresql)
    cur = conn.cursor()

    sql = model.dwh_fact_orders()
    cur.execute(sql)
    data = cur.fetchall()
    df = pandas.DataFrame(data, columns= [col[0] for col in cur.description])
    df.to_sql("dwh_fact_orders", engine, if_exists='replace', index=False)  

    sql = model.dwh_fact_employees()
    cur.execute(sql)
    data = cur.fetchall()
    df = pandas.DataFrame(data, columns= [col[0] for col in cur.description])
    df.to_sql("dwh_fact_employees", engine, if_exists='replace', index=False) 

    sql = model.dwh_fact_activityusers()
    cur.execute(sql)
    data = cur.fetchall()
    df = pandas.DataFrame(data, columns= [col[0] for col in cur.description])
    df.to_sql("dwh_fact_activityusers", engine, if_exists='replace', index=False) 