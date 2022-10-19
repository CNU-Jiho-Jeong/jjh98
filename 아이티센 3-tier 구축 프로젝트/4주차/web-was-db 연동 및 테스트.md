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

---

- 컴파일 오류가 발생한다.

=> App.js 라는 파일에 문제가 있는 것 같다. 수정해서 실행해보자.





## 2. 
