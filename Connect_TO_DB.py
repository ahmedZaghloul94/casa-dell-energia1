import psycopg2
import psycopg2.extras
from abbrevationdictionary import *
def Connect_TO_DB(Querey:str,data=None):
    try:
        con = psycopg2.connect(dbname=DB_name, user=DB_user,
                            password=DB_pass, host=DB_Host)
        cur = con.cursor(cursor_factory=psycopg2.extras.DictCursor)
        Set_path="show search_path; set search_path to casa_della_energia ;"
        Querey=Set_path+Querey
        cur.execute(Querey, data)
        res = cur.fetchall()
        con.commit()
        cur.close()
        return res
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)   

    finally:  
        if con is not None:
            con.close()   