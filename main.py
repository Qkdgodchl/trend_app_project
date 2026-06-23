from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

#1 . fastapi의 기능을 app이라는 이름으로 가져와서 쓰겠다고 선언
app = FastAPI()

#. 우리가 다룰 트렌드 데이터의 절대적인 틀(Schema)를 정의함
class TrendItem(BaseModel):
    title : str  # 제목은 반드시 스트링이어야한다
    category : str # 카테고리도 스트링
    rank : int # 순위는 정수형

#2. 사용자가 기본주소 '/'로 들어오면 환영 인사를 건네라
@app.get("/")
def read_root():
    return {"message" : "시장 트렌드 수집 api 서버에 오신 것을 한영합니다 ! "}

#. 위에서 정의한 틀(TrendItem)의 규칙을 따르는 데이터만 내보내겠다고 선언
@app.get("/trends/today" , response_model = List[TrendItem])
def get_today_trends():
    return[
        {"title" : "엔비디아 주가 폭등" , "category" : "주식" , "rank" : 1},
        {"title" : "삼성전자 신제품 출시" , "category" : "IT" , "rank" : 2},
    ]

# @app.get()부분은 일종의 이정표 역할을 함 사용자가 이 주소로 데이터 주라고 요청(GET)하면 바로 밑에 있는 함수를 실행해서 중괄호 안에 ㅣㅇㅆ는 데이터를 반환하라는 의미

