from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


DATABASE_URL = "sqlite:///./database/cyriq.db"


engine = create_engine(
    DATABASE_URL,
    connect_args={
        "check_same_thread": False
    }
)


SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


Base = declarative_base()


def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


def execute_query(query, params=None):

    """
    Execute a raw SQL query.
    """

    with engine.connect() as connection:

        result = connection.exec_driver_sql(
            query,
            params or {}
        )

        return result.fetchall()