import os
from dotenv import load_dotenv
import oracledb


load_dotenv()


def main():
    print(os.getenv("DATABASE_URL"))
    print(os.getenv("DATABASE_PASSWORD"))


if __name__ == "__main__":
    main()