"""
간단히 동작하는 웹 프로그램을 만들어 봅니다.

TODO - OSI 7계층에 대해 학습합니다.
TODO - http 프로토콜에 대해 학습합니다.(request/header/body, response/header/body, cookie, etc)
TODO - TCP/IP 에 대해 학습합니다.
TODO - FTP/TELNET/SSH 에 대해 학습합니다.

TODO - RESTful API Server 의 개념에 대해 학습합니다.
TODO - Flask 라이브러리를 설치해 http://localhost:8000/ 서버를 구축합니다.
TODO - 웹 브라우저를 통해 http://localhost:8000/ 페이지에 접속하면 웹 브라우저에 Hello world! 를 보여줍니다.

TODO - http://localhost:8000/{id}/ 페이지에 접속하면 웹 브라우저에 Welcome, {id}! 를 보여줍니다.
예) http://localhost:8000/guest/     =>  Welcome, guest!
예) http://localhost:8000/visitor/   =>  Welcome, visitor!

TODO - SQLite3 DB에 accumulation (집계) 이라는 이름의 테이블을 생성합니다.
idx(auto increment index), keyword(문자열), count(숫자)

TODO - 위에서 방문한 id를 keyword 로, 각 방문자의 방문 횟수를 DB(데이터베이스)의 집계 테이블에 저장합니다.
예) http://localhost:8000/guest/ 를 5번 방문하면 SQLite3 의 accumulation 테이블에
DataGrip 등을 통해 열어 보았을 때

1, guest, 5

이와 같이 조회 되어야 합니다. (단 인덱스는 순차적 자동 생성이라 다를 수 있음)

TODO - http://localhost:8000/accumulation/ 페이지에 접속하면 해당 집계 내용 중 방문 횟수 상위 10건을,
방문 횟수 순으로 내림차순 정렬해서 화면에 keyword, count 짝으로 보여줍니다.

"""