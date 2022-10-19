from sqlalchemy import Column, Integer, String
from pydantic import BaseModel
from db import Base
from db import ENGINE

class Words(Base):
    __tablename__ = 'words'
    id = Column(Integer, primary_key=True, autoincrement=True)
    kata = Column(String(255))
    jenis = Column(String(255))

def main():
    Base.metadata.create_all(bind=ENGINE)


if __name__ == "__main__":
    main()
