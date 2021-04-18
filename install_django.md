## Django 설치하기
1. pip install 및 upgrade
python -m pip install --upgrade pip
pip --version

2. Django 설치
pip install Django
python -m django --version
pip install Django --upgrade

3. Django 삭제
먼저 설치 경로 확인 후, 해당 \django 전까지 이동 후, django & django --- dist-info 폴더 2개 삭제
python -c "import django; print(django.__path__)"

## Django 프로젝트 시작하기
1. 프로젝트 폴더 생성
2. cmd 창에서 해당 폴더로 이동
3. 프로젝트 이름으로 django 생성
django_admin startproject tempPjt (프로젝트 이름)
4. 폴더창에서 프로젝트 이름으로 된 파일 생성 되었나 확인
5. cmd 창에서 해당 프로젝트 이름으로 된 폴더로 이동 후, 어플리케이션 생성
python manage.py startapp students
6. 사용자 및 그룹데이터 생성
python manage.py migrate
7. DB 변경사항 반영
python manage.py makemigrations
python manage.py migrate
8. 관리계정 생성
python manage.py createsuperuser
9. 서버구동
python manage.py runserver
10. 웹브우저에서 주소창에 
http://127.0.0.1:8000/
http://127.0.0.1:8000/admin (관리)

cmd창에서 Ctrl+C 누르면 서버 종료됨


