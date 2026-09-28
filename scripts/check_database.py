from sqlalchemy import text

from app.config.database import engine


def main() -> None:
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))
        print(f"PostgreSQL OK: {result.scalar()}")


if __name__ == "__main__":
    main()