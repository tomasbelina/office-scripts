import os
import sqlalchemy
from dotenv import load_dotenv
from os.path import join, dirname

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

db_name = os.environ.get('MYSQL_DATABASE')
db_user = os.environ.get('MYSQL_USER')
db_password = os.environ.get('MYSQL_PASSWORD')
db_host = os.environ.get('MYSQL_HOST')

engine = sqlalchemy.create_engine(
    "mariadb+mariadbconnector://" + db_user + ":" + db_password + "@" + db_host + ":3306/" + db_name)

def get_session():
    Session = sqlalchemy.orm.sessionmaker()
    Session.configure(bind=engine)
    session = Session()