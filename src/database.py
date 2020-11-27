from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# engine = create_engine('sqlite:///data/chinook.db')
# connection = engine.connect()

SQLALCHEMY_DATABASE_URL = "sqlite:///data/chinook.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

connection = engine.connect()

Base = declarative_base()

if __name__ == "__main__":
    stmt = 'SELECT * FROM customers'
    result_proxy = connection.execute(stmt)
    results = result_proxy.fetchall()
    print(results)
