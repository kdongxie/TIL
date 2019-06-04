\# Intro to WEB Service

웹? 서비스? 월배우는 것인가요?

## 우리는 Web Service를 만든다?

## Web Service

### World Wide Web. www. w3

### Web 

- 컴퓨터 간의 정보를 주고 받는 공간을 칭한다.

### Service 

- 요청(request)에 상응하는 응답(response)을 받는 것
- 요청: client 多 > 브라우저
  - 요청의 종류
    1. 줘라(Get): 물건을 달라/html문서를 달라 > html문서를 받는다
    2. 받아라(Post): 우편물을 처리요청/정보를 처리요청 > 처리결과
- 응답: server 少

### [flask](<http://flask.pocoo.org/>)

서버를 껐다키지 않아도 사용가능케 하는 명령어 

FLASK_DEBUG=1 FLASK_APP=hello.py flask run

@ : python 에서 decorator라고 하며 