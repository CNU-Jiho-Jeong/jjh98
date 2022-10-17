# Web-WAS-DB 설치해보기

## 1. nginx 설치하기
- putty로 webserver 접속

![image](https://user-images.githubusercontent.com/108641325/195853834-54fc141d-61be-43cf-ae3e-91f506dafc51.png)

![image](https://user-images.githubusercontent.com/108641325/195853851-755f4181-4087-452d-93c9-c217f3e35260.png)

(로그인 성공)

---

- nginx 서버를 설치하기 위해서는 다음과 같은 과정을 거쳐야한다.

**1. yum 외부 저장소 추가**

**2. yum install**

**3. 방화벽 포트 개방**

**4. nginx 포트 설정**

**5. nginx 데몬 실행**

**6. nginx 실행**

---

**1. yum 외부 저장소 추가**

- yum 저장소에는 nginx가 없기 때문에 외부저장소를 추가해야한다.
- /etc/yum.repos.d 디렉토리에 nginx.repo 파일을 추가해준다.

![image](https://user-images.githubusercontent.com/108641325/196190802-9e137c70-ed28-4ff0-a464-fb400c5e7017.png)

- 안에 넣어줄 내용은 다음과 같다.

![image](https://user-images.githubusercontent.com/108641325/196193023-adc54d21-3131-4107-9371-ca8f861cf201.png)

![image](https://user-images.githubusercontent.com/108641325/196193268-bf862e4a-2033-4991-a048-bc9e35115f30.png)

(OS 버전이 다를 시 수정한다.)

---

**2. yum install**

- yum install -y nginx 명령어를 사용하여 nginx를 설치한다.

![image](https://user-images.githubusercontent.com/108641325/196193535-e338d668-b004-4965-882a-a10a4d8b5b80.png)

---

**3. 방화벽 포트 개방**

![image](https://user-images.githubusercontent.com/108641325/196193731-3cd4a0fa-9848-4cb0-8b63-e4714550b685.png)

---

**4. nginx 포트 설정 및 환경설정**

- 설정한 포트에 맞춰 listen의 포트를 변경해주어야 한다.
- vi /etc/nginx/conf.d/default.conf

![image](https://user-images.githubusercontent.com/108641325/196193921-c04804cb-df90-4e93-ba23-87c614c725ce.png)

![image](https://user-images.githubusercontent.com/108641325/196194195-abe6efd4-397c-49cb-a130-c388591942b6.png)

(listen 포트와 server_name 설정. 80이 아닌 다른 포트를 사용하거나 도메인을 설정하게 될 경우 이 항목들을 수정하면 된다.)

---

- **참고**

![image](https://user-images.githubusercontent.com/108641325/196194598-39b03740-c100-4998-8742-0c28ff51efef.png)

(홈 디렉토리와 기본 문서 설정. 홈 디렉토리 경로를 설정하고 기본 문서를 지정한다.)

---

![image](https://user-images.githubusercontent.com/108641325/196194698-583acdaf-5cae-41d3-8580-c062aff9b5d8.png)

(에러 페이지 설정. 404, 500 등의 error 페이지를 설정할 경우 아래 내용들을 수정하면 된다.)

---

![image](https://user-images.githubusercontent.com/108641325/196195230-fc392846-b19f-4375-8798-e2aeb3345ab8.png)

(.htaccess 파일 접근 금지 설정. .htaccess 파일에 대한 접근 금지를 설정할 경우 아래 내용을 주석 해제하면 된다.)

---

**5. nginx 데몬 실행**

- 설정이 끝났으면 nignx를 실행해보자.

![image](https://user-images.githubusercontent.com/108641325/196195750-207a1216-6999-42a6-b8bf-9b6a8c7cc78e.png)

![image](https://user-images.githubusercontent.com/108641325/196195780-543fdf4a-f8de-446a-a0d0-2460d992791d.png)

(start는 시작, enable은 재부팅시에도 동작 유지, status로 작동 상태를 확인한다. 잘 동작하고 있다.)

---

**6. 실행확인**

- 발급 받은 공인 IP을 사용해서 nginx를 띄울 수 있다.

![image](https://user-images.githubusercontent.com/108641325/196196020-4ee6b2cd-3c29-4d88-a32a-00164f4a6224.png)



## 2. JBoss(wildfly) 설치하기

- 먼저 WAS용으로 생성한 서버로 이동한다.

![image](https://user-images.githubusercontent.com/108641325/196188369-ba3776a1-1845-47b4-8b29-e4871c6f6a53.png)

(ssh 아이디@ip주소)

---

- **JBoss를 설치하기 위한 과정은 다음과 같다.**

**1. Java Open JDK 설치**

**2. 사용자 생성**

**3. WildFly 설치**

**4. 소유권 변경**

**5. Systemd 구성**

**6. 방화벽 조정**

**7. WildFly 설치 테스트**

**8. WildFly 관리 콘솔에 액세스**



