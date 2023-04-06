import os
import sqlite3

db_path = os.path.join(os.getcwd(), 'chinook.db')
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

def get_profit():
    cursor.execute('SELECT SUM(UnitPrice * Quantity) FROM invoice_items')
    result = cursor.fetchone()[0]
    return result

def get_duplicate_names():
    cursor.execute('SELECT FirstName, COUNT(*) FROM customers GROUP BY FirstName HAVING COUNT(*) > 1')
    result = cursor.fetchall()
    return result

profit = get_profit()
print('Прибыль:', profit)

duplicates = get_duplicate_names()
print('Повторяющиеся имена:')
for name, count in duplicates:
    print(name, count)

conn.close()
