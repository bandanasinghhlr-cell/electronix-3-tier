import pymysql
import os
from dotenv import load_dotenv

load_dotenv('/home/jenkins/.env')

def create_database():
    connection = pymysql.connect(
        host=os.getenv('DB_HOST'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        port=int(os.getenv('DB_PORT', 3306)),
        connect_timeout=5
    )
        
    connection.close()
    print("[PASS]✅ Database Connectivity Check")

if __name__ == "__main__":
    try:
        test_database()
        print ("Smoke Test Passed.. ✅")
    except Exception as e:
        print ("Smoke Test Failed.. ❌" ,e)
        sys.exit(1)