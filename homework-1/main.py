"""Скрипт для заполнения данными таблиц в БД Postgres."""
import csv

import psycopg2

conn = psycopg2.connect(host="localhost", database="north", user="postgres", password="12345")

with conn.cursor() as cur:
    with open('./north_data/employees_data.csv', newline='') as f:
        reader = csv.DictReader(f, delimiter=',')
        for row in reader:
            cur.execute("INSERT INTO employees VALUES (%s, %s, %s, %s, %s)",
                        (f'{row["first_name"]}', f'{row["last_name"]}', f'{row["title"]}',
                         f'{row["birth_date"]}', f'{row["notes"]}'))
    cur.close()

with conn.cursor() as cur:
    with open("./north_data/customers_data.csv", newline='') as f:
        reader = csv.DictReader(f, delimiter=',')
        for row in reader:
            cur.execute("INSERT INTO customers VALUES (%s, %s, %s)", (row["customer_id"], row["company_name"],
                                                                      row["contact_name"]))

    cur.close()

with conn.cursor() as cur:
    with open("./north_data/orders_data.csv", newline='') as f:
        reader = csv.DictReader(f, delimiter=',')
        for row in reader:
            cur.execute("INSERT INTO orders VALUES (%s, %s, %s, %s, %s)",
                        (row["order_id"], row["customer_id"], row["employee_id"], row["order_date"], row["ship_city"]))

    cur.close()

conn.commit()
