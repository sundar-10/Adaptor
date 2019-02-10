conn=psycopg2.connect(database="test", user = "postgres", password = "sundar10", host = "localhost") 
cur = conn.cursor()
cur.execute("""
CREATE TABLE stud(
    M1 integer,M2 integer,M3 integer,M4 integer,
    sQ1 integer,sQ2 integer,sQ3 integer,sQ4 integer,sQ5 integer,
    TQ1 integer,TQ2 integer,TQ3 integer,TQ4 integer,TQ5 integer,
   CorrectOutput integer,predictedoutput integer
)
""")
conn.commit()
conn.close()



conn=psycopg2.connect(database="test", user = "postgres", password = "sundar10", host = "localhost") 
cur = conn.cursor()
with open('spectrain.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)  # Skip the header row.
    for row in reader:
        cur.execute(
            "INSERT INTO stud(M1,M2,M3,M4,sQ1,sQ2,sQ3,sQ4,sQ5,TQ1,TQ2,TQ3,TQ4,TQ5,CorrectOutput,id) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,DEFAULT)",
            row
        )
conn.commit()
conn.close()



conn=psycopg2.connect(database="test", user = "postgres", password = "sundar10", host = "localhost") 
cur = conn.cursor()

cur.execute(
       "ALTER TABLE stud ADD COLUMN id SERIAL PRIMARY KEY;"
    
)
conn.commit()
conn.close()