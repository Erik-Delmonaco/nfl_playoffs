import sqlite3

conn = sqlite3.connect('teams_database.db')

cursor = conn.cursor()

query = """
    INSERT INTO teams (city,name)
    VALUES ('Buffalo','Bills'),
           ('Denver','Broncos'),
           ('San Francisco','49ers'),
           ('Seattle','Seahawks'),
           ('Houston','Texans'),
           ('New England','Patriots'),
           ('Los Angeles','Rams'),
           ('Chicago','Bears');
"""

cursor.execute(query)
conn.commit()
conn.close()