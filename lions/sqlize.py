import psycopg2

class LIONS():
    def __init__(self, address, user=None, password=None):
        self.address = address
        self.conn = psycopg2.connect(host="localhost", database="postgres")


def create_table(name, table_dict, table_keys):
    s =  "CREATE TABLE " + name + "("
    s += "    ID varchar(10)"
    s += ")"

def initialize_db():
    conn = None
    try:
        conn = psycopg2.connect(host="localhost", database="postgres")
        cur = conn.cursor()
        for command in commands:
            cur.execute(command)

        cur.close()
        conn.commit()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
