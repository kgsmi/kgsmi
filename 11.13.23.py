pip install xlwings

import sqlite3
import time

# connect to the database
conn = sqlite3.connect('timers.db')

# get a cursor
cur = conn.cursor()

# add a new timer
start_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
end_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
cur.execute("INSERT INTO TIMERS (ID, START_TIME, END_TIME) VALUES (?, ?, ?)", (1, start_time, end_time))

# commit the changes
conn.commit()

# close the connection
conn.close()