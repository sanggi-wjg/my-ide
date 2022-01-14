### Concept

<details>
<summary>Docker build 와 Container 처리 (완료)</summary>
<div markdown="1">
<pre>
0. dockerfieles / language-version / Dockerfile 작성
1. 사용할 dockers.json 작성
2. commands / build_dockerfiles Dockerfile 빌드 시도, 성공이면 DockerImage 업데이트 
3. commands / run_docker_images Docker image container 생성 및 실행, 성공이면 DockerImage 업데이트
</pre>
</div>
</details>

<details>
<summary>Docker build 와 container 는 개발을 통해서  (완료)</summary>
<div markdown="1">
<pre>
python docker api 사용
https://docs.docker.com/language/python/build-images/

dockers / module / service 구현
</pre>
</div>
</details>

### Docker Container 안에 코드 실행 방법

<details>
<summary>Python 3.8 (완료)</summary>
<div markdown="1">
<pre>
Flask 로 개발된 소스를 Dockerfile 로 빌드
native 로 개발해도 상관 없으나 구현 해 봄

이후 사용자 요청시에 Django 에서 Flask Container 로 HTTP POST Request localhost:5000/run Response 를 view 로 retreive
</pre>
</div>
</details>

<details>
<summary>Python 2.7  (완료)</summary>
<div markdown="1">
<pre>
프레임 워크 없이 native 로 작성
docker container로 docker exec 실행하며 실행할때 arguements 로 코드를 전달 native 소스에서 실행
Response 를 view 로 retreive
</pre>
</div>
</details>

### 구현 TODO

#### Docker 관련
* [ ] Load Dockerfiles
  * dockerfiles 이하 폴더 리스트, (파일 내용까지?) 읽어 오기 
* [ ] Docker Image Build 
  * Docker build API 개발 하기
* [ ] Run Container
  * Build 가 완료된 Image 를 Docker container 로 run 하기 

#### 사용자 Source code 관련
* [ ] Code Snippets
  * 사용자 소스 저장(DB로 언어별 Depth 저장?)
* [ ] Elasticsearch 검색
  * source code filename 과 code content 검색
* [ ] Redis cache
  * 검색에 대해서 cache 작업

<details>
<summary></summary>
<div markdown="1">
<pre>

</pre>
</div>
</details>