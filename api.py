import os
import sqlalchemy
from dotenv import load_dotenv
from os.path import join, dirname

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

db_name = os.environ.get('DB_NAME')
db_user = os.environ.get('DB_USER')
db_password = os.environ.get('DB_PASSWORD')
db_host = os.environ.get('DB_HOST')

engine = sqlalchemy.create_engine(
    "mariadb+mariadbconnector://" + db_user + ":" + db_password + "@" + db_host + ":3306/" + db_name)
