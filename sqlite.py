import sqlite3

conn = sqlite3.connect('order_data.sqlite')
cur = conn.cursor()

fields = sorted(['Frozen_Frappe INTEGER', 'Hot_chocolate INTEGER', 'Instant_coffee INTEGER',
                 'Ice_Latte INTEGER', 'Cappucino INTEGER', 'Coffee_with_ice_cream INTEGER', 'Total INTEGER'])

q = 'CREATE TABLE IF NOT EXISTS Orders(id INTEGER PRIMARY KEY, person_name TEXT, person_ph INTEGER, '
q += ", ".join(fields) + ")"

cur.execute(q)
conn.commit()


def add_order(name, ph, ordered_nums):
    conn = sqlite3.connect('order_data.sqlite')
    cur = conn.cursor()
    q = "INSERT INTO Orders(person_name, person_ph) VALUES(?, ?)"
    cur.execute(q, (name, ph))
    q = "SELECT id FROM Orders WHERE person_name = ? AND person_ph = ?"
    cur.execute(q, (name, ph))
    id = cur.fetchone()[0]

    q = "UPDATE Orders SET "
    q += ", ".join([i.split(' ')[0]+" = ?" for i in fields]) + " WHERE id = ?;"

    cur.execute(q, (*ordered_nums, id))
    conn.commit()
