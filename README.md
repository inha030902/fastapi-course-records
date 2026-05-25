# FastAPI Course Records

## 프로젝트 소개

이 프로젝트는 오픈소스소프트웨어실습 실습 4 과제로 제작한 FastAPI 기반 REST API 서버입니다.

수강기록 데이터를 `courses.json` 파일로 관리하며, FastAPI를 통해 전체 수강기록 조회와 새로운 수강기록 추가 기능을 구현했습니다.

---

## 주요 기능

1. `GET /courses`를 통한 전체 수강기록 조회
2. `POST /courses`를 통한 새로운 수강기록 추가
3. `courses.json` 파일 기반 데이터 관리
4. POST 요청 후 변경된 데이터를 다시 JSON 파일에 저장
5. Postman을 이용한 GET / POST 요청 테스트

---

## 파일 구성

```text
fastapi-course-records/
├─ main.py
├─ courses.json
├─ requirements.txt
├─ .gitignore
└─ README.md