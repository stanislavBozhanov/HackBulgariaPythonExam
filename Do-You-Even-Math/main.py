from sqlalchemy import create_engine
from connection import Base


def main():
    engine = create_engine("sqlite:///do_you_even_math.db")
    Base.metadata.create_all(engine)

if __name__ == '__main__':
    main()
