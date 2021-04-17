1. 장고패키지 설치
https://www.djangoproject.com/download/

Django-1.8.3.tar.gz 파일 다운 원하는 폴더에 이동 후, 압축 풀기

2. cmd 관리자 권한 -> django 다운 받은 폴더로 이동 -> python setup.py install
3. Django-1.8.3/django/bin에 django-admin 파일 있음, 그 파일은 "Djangp-1.8.3'으로 이동
4. cmd로 가서 Django-1.8.3 폴더로 이동 후, django-admin.py –version 으로 버전 확인 1.8.3이 나오면 성공



pip 통해서 설치
1. C:\>pip install Django
2. 설치 확인하기: 
C:\>python --version
C:\>python -m django --version

3. 장고 프로젝트 시작하기:
C:\>django-admin startproject install_check_project

4. 생성된 폴더로 들어가서 실행
C:\>install_check_project\python manage.py runserver

5. 웹브아우저에서 주소창에 
http://127.0.1:8000/

cmd창에서 Ctrl+C 누르면 서버 종료됨


