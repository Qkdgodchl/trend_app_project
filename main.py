from fastapi import FastAPI , Depends
from sqlalchemy import Column , Integer, String
from sqlalchemy.orm import Session
from database import Base, engine , SessionLocal
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["http://localhost:5173"],
    allow_credentials = True ,
    allow_methods = ['*'],
    allow_headers = ['*'],
)

# . DB 설계도 - postgresql에 꽂아 넣을 테이블 구조 선언
class DBTrendItem(Base) :
    __tablename__ = "trends"

    id = Column(Integer , primary_key = True , index = True)
    title = Column(String , index = True)
    category = Column(String)
    rank = Column(Integer)

#서버가 켜질 때 위에서 정의한 설계도를 바탕으로 DB에 진짜 테이블을 만들기
Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try :
        yield db
    finally :
        db.close()

@app.post("/trends/db")
def create_trend_in_db(title : str , category : str , rank : int , db : Session = Depends(get_db)) :
    # db에 넣을 객체 만들기
    new_trend = DBTrendItem(title = title , category = category , rank = rank)

    db.add(new_trend)

    db.commit()

    db.refresh(new_trend)
    return {"message" : "DB 저장 성공" , "data" : {"id" : new_trend.id , "title" : new_trend.title}}

@app.get("/trends/db/all")
def get_all_trends_from_db(db : Session = Depends(get_db)):
    trends_in_db = db.query(DBTrendItem).all()

    return{
        "source" : "진짜 postgresql 데이터베이스",
        "total_count" : len(trends_in_db),
        "trends" : trends_in_db,
    }