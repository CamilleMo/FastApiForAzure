from sqlalchemy import create_engine

SQLALCHEMY_DATABASE_URL = "sqlite:///data/chinook.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

connection = engine.connect()

print("Tables name in chinook.db: ", engine.table_names())

stmt = 'SELECT * FROM customers'

result_proxy = connection.execute(stmt)

results = result_proxy.fetchall()

print(results)
