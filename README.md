실행 
----

python app.py


!!!아래의 문제는 다음과 같이 처리됨.
----
1. lib 디렉토리에 werkzeug wheel 을 직접 배포하고 app.py 시작시
sys.path를 추가하여 처리함.

2. 시간도 app.py 시작시 임의의 시간으로 설정하여 처리함.


현재 문제점
----
웹세션을 사용할 수 없는 문제로 로그인에 사용된 사용자의 아이디와 패스워드를 세션에 저장할 수 없음.
=> 현재 개별화면 로딩시 로긴여부체크를 풀어놓았음.

웹세션을 사용하기 위해서는 두가지가 선행되어야 합니다.

1. 웹세션에 저장되는 정보가 system time을 가지고 암호화를 진행하므로 먼저 system time 이 설정되어야 합니다.
(이것은 웹화면의 시간 변경부분에서 변경가능합니다.)
2. 그리고 아래의 에러가 발생하는것을 핸들링하기 위해서는 아래 패키지들의 버전을 변경해 주셔야 합니다.

제일 먼저 Flask의 버전을 update 할 수 있으면 그것 부터 해보는게 좋을것 같습니다.

1. Flask update, 2 Werkzeug

아래의 Flask-Login 은 위의 두 패키지 업데이트 이후에 동작하는 지 확인해보고, 마저 업데이트 해보시기 바랍니다.

=== 아래 == 
Exception 

"SAMESITE" when using set session,

Required Version

Flask>=1.0.2
Flask-Login==0.4.1
Werkzeug==0.14.1



https://stackoverflow.com/questions/53603025/typeerror-set-cookie-got-an-unexpected-keyword-argument-samesite-flask
