#database.py

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# DB 연결 주소 설정
DATABASE_URL = "postgresql://tatata:1234@localhost:5432/postgres"

# DB와 대화할 엔진 및 세션 생성
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit = False , autoflush = False , bind = engine)

# 나중에 테이블 만들 때 상속받을 기본 클래스
Base = declarative_base()