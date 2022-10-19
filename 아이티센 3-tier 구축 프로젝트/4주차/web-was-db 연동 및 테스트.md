## 1. Web(Nginx)-WAS(JBoss) 도킹

![image](https://user-images.githubusercontent.com/108641325/196676144-55c6ed2f-e956-46ef-95e5-53a07145bf26.png)

- Curl http://10.0.1.6:8080 명령어를 사용해서 nginx 서버에서 JBoss에게 요청을 주고, HTML 파일을 받을 수 있다.

- 잘 도킹된 것을 확인할 수 있다.

---

### Nginx 서버에서 웹 띄워 보기

- 준비: git, node, npm, react 

**1. node.js 설치**

- epel 저장소 확인
  
  > yum repolist

- 없을 경우 설치진행
  
  > yum install epel-release


![image](https://user-images.githubusercontent.com/108641325/196677899-168df34c-aef0-47b9-9b53-83e83303dd54.png)

![image](https://user-images.githubusercontent.com/108641325/196677932-5ba12359-730d-47a4-8b67-d7e860512c1b.png)

---

- node.js 설치

  > yum install -y nodejs
  
  ![image](https://user-images.githubusercontent.com/108641325/196678275-fa3aba87-2c20-4ca4-8030-e949e121a3c1.png)

---

- node.js 버전 확인

  > node -v 혹은 node --version

  ![image](https://user-images.githubusercontent.com/108641325/196678519-9ce9a26a-ca7f-4901-b7cb-c7b3412cc501.png)

---

**2. npm 설치**

- npm 설치

  > yum install -y npm
  
  ![image](https://user-images.githubusercontent.com/108641325/196678660-bb2153a7-3806-4615-9d9b-4313d5488dd5.png)
  
---

- 버전 확인

  > npm --version 혹은 npm -v

---

**3. react 설치**

- yarn 설치

  > npm install yarn

![image](https://user-images.githubusercontent.com/108641325/196680482-9a87727d-f5b1-4bb9-8fd0-03b884566a8f.png)


![image](https://user-images.githubusercontent.com/108641325/196680981-b2f28dbb-4f5a-4e40-922a-073c24e8fc91.png)

(위와 같은 에러가 발생하였다.)

=> 패키지를 업데이트하고, NPM 캐쉬 삭제 및 업데이트를 진행한다.

![image](https://user-images.githubusercontent.com/108641325/196682795-ebc94d36-e077-439f-929f-2ae5b89580ce.png)

![image](https://user-images.githubusercontent.com/108641325/196682834-1cb25f68-d0b8-4b2c-b588-226ef535050e.png)

---

**4. git에서 파일 내려받기**

- git에서 이전에 작성해놓은 프로그램을 다운받는다.

출처: https://github.com/jaestury/react-springboot-rest-api (제 깃허브가 아닌 팀원분 깃허브 링크입니다.)

  > git clone (git URL)

![image](https://user-images.githubusercontent.com/108641325/196687145-29bab7fa-61a5-46bb-be87-e9cbaf27e075.png)

---

- git에서 내려받은 폴더

![image](https://user-images.githubusercontent.com/108641325/196687279-b04c2ad7-8dfa-4fcf-9348-0a9c381e9782.png)

![image](https://user-images.githubusercontent.com/108641325/196687297-8be14913-ac2e-484a-a1e4-8ec930331d5c.png)

---

- gc-coffee는 스프링, kdt-react-order-ui가 리액트다.

![image](https://user-images.githubusercontent.com/108641325/196687701-42c3ce33-7abb-4ded-a278-ce0ece369c4a.png)

---

- npm start로 리액트를 시작해준다.

![image](https://user-images.githubusercontent.com/108641325/196687839-d479a405-9989-40a9-b2ab-274d3f16ddb9.png)

  - 컴파일 오류가 발생한다.

  => App.js 라는 파일에 문제가 있는 것 같다. 수정해서 실행해보자.

---

![image](https://user-images.githubusercontent.com/108641325/196689083-2e804594-8d12-4e08-b909-54de924c0ca3.png)

- 리액트 컴파일 성공!
- 이제 접속해보자. 공인IP:3000으로 창을 띄워보자.
- 접속이 안된다. 당연한 일이다. 3000번 포트를 뚫어놓지 않았기 때문이다.
- ACG 설정으로 가서 포트 설정을 해주자.

![image](https://user-images.githubusercontent.com/108641325/196689558-a6f8e2fe-20f7-40dc-a513-43589298514b.png)

![image](https://user-images.githubusercontent.com/108641325/196689595-639c8f89-99bc-492e-bf3d-0aad19c4455a.png)

- 공인IP:3000로 nginx 서버에서 잘 출력된다. 

---

- nginx를 proxy로 사용해서 리액트를 출력해보도록 하자.

![image](https://user-images.githubusercontent.com/108641325/196689981-d83b6b17-2de7-412c-91e4-4328ac855171.png)
  - vi /etc/nginx/conf.d/default.conf을 조금 만져주자.
  - location을 바꾼다.
  - proxy_pass를 localhost:3000으로 바꿔서 nginx에 리액트 프로그램을 얹어 실행할 수 있다.

---

![image](https://user-images.githubusercontent.com/108641325/196690423-759ceb1e-8db6-4b42-8926-232b66adc48a.png)

- 3000번 포트를 삭제해도 공인IP:80로 리액트를 띄울 수 있다.

---
---


## 2. WAS(JBoss)-DB(CDB for MySQL) 도킹

- WAS 서버에 접속해서 MySQL을 설치하자.

![image](https://user-images.githubusercontent.com/108641325/196690778-ce296558-2af6-4d8e-b0c7-22ee379b06b8.png)

![image](https://user-images.githubusercontent.com/108641325/196690826-6b52b7ee-9c10-46f5-a778-d28bb4368f71.png)

![image](https://user-images.githubusercontent.com/108641325/196690849-dfacaac0-7fba-44e8-a484-b5e9491f4f55.png)

![image](https://user-images.githubusercontent.com/108641325/196690895-5cbb8ff6-3563-4f1d-bca3-2c95977631e4.png)

---

- 명령어 예시를 입력하여 DB 서버에 접속해주자.

![image](https://user-images.githubusercontent.com/108641325/196691101-e35a0e51-99f7-4bbe-8e32-25d5ff731006.png)

![image](https://user-images.githubusercontent.com/108641325/196691128-de3f25c0-6e52-4f2a-9a27-82294e17d9c3.png)

![image](https://user-images.githubusercontent.com/108641325/196691147-8d5491ba-5650-496d-8204-5096201b6176.png)

- WAS서버에서 DB서버에 접속한 후 테이블을 생성해봤다.

---

### WAS에서 서비스 띄워보기

- 준비: maven, spring boot

---

**1. Maven 설치**

- yum install maven

![image](https://user-images.githubusercontent.com/108641325/196691680-37af06ce-61de-4db5-a3e0-a2e31a6e661a.png)

mvn -version으로 설치 확인이 가능하다.

![image](https://user-images.githubusercontent.com/108641325/196691734-ae7b2316-4ec4-4fc0-9dac-2baf674cf2e7.png)

---

- git clone으로 WAS 서버에도 폴더를 내려 받는다.

![image](https://user-images.githubusercontent.com/108641325/196692801-585eadb7-3927-41ec-9ff6-6e9615be3d76.png)

- 여기서는 pom.xml 파일에서 Java 버전을 맞춰줘야 한다.
- mvn package로 target 폴더를 생성한다.

---

![image](https://user-images.githubusercontent.com/108641325/196693074-832f3cb3-5119-468e-b13a-23a4860e60ec.png)

- 빌드가 성공하면 gc-coffee-0.0.1-SNAPSHOT.jar 가 생성된다.
- java -jar gc-coffee-0.0.1-SNAPSHOT.jar 명령어를 통해 실행해준다.

---

![image](https://user-images.githubusercontent.com/108641325/196693276-b21fb85a-f948-4998-9585-bceca5007ccf.png)

- MySQL 서버에 접속할 수 있는 권한이 없다는 메시지가 나온다.
- MySQL 사용자를 추가해서 해결할 수 있다.

---

![image](https://user-images.githubusercontent.com/108641325/196693360-e6bb993d-a50c-4da6-bac7-e1e7ac388381.png)

- Root 사용자를 추가하였고, 외부에서도 MySQL 접속이 가능하게 되었다.

---

![image](https://user-images.githubusercontent.com/108641325/196693447-23d54bfb-a170-4ba8-8a2d-eefc2f88e1f4.png)

- 빌드가 성공한 모습이다.

---

능력부족으로 실패했습니다.
WAS와 Web서버를 연결해서 웹에서 보내는 데이터를 WAS가 DB에게 전달해 저장하는 모습을 보고 싶었는데, 거기까지는 하지 못했습니다.




