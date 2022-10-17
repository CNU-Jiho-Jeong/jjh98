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

---
---

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

---

**1. Java Open JDK 설치**

- WildFly는 Java 버전 8 이상을 설치해야한다. CentOS 7 의 기본 Java 개발 및 런타임인 Java 플랫폼의 오픈소스 구현인 OpenJDK를 설치하자.

  ![image](https://user-images.githubusercontent.com/108641325/196200417-4fa8b531-a092-4ea3-b3cf-2282433984ac.png)


- 이후 실행하게 될 스프링의 빌드 버전이 java 11이니, 11으로 설치하는 것도 좋다.
  
  ![image](https://user-images.githubusercontent.com/108641325/196200586-63bfefe4-4ab2-4a85-acbb-3cf7fd743bc0.png)  


- 두 버전이 이미 설치되어있다면 버전설정을 할 수도 있다.

![image](https://user-images.githubusercontent.com/108641325/196200859-a49913f2-5479-4e4c-a0d2-0d66d70a5e53.png)

![image](https://user-images.githubusercontent.com/108641325/196200902-8eff1023-4ac7-4d2a-8789-ae09acd2d4ce.png)

(중간에 y를 입력해줘야한다.)

---

**2. 사용자 생성**

- WildFly를 루트 사용자로 실행하는 것은 보안상 위험하다. **'home directory /opt/wildfly'** 를 사용해 wildfly라는 새 시스템 사용자 및 그룹을 만들도록 하자.

![image](https://user-images.githubusercontent.com/108641325/196201630-99f2fc49-c747-49ee-8bbc-ef6ac143f8af.png)


- groupadd
  - 리눅스 시스템 내에 새 그룹을 추가하기 위한 명령어.
  - 여러 사용자들을 하나의 그룹으로 구분하기 위해 사용한다.
  - **'groupadd -r ( ~~ )'** 는 시스템용 그룹(GID 499 이하)을 생성하는 명령어이다. 0~499 까지 할당되어 있지 않은 GID 중 가장 높은 번호를 할당해준다.


- useradd 
  - 신규 사용자를 추가하는 명령어.
  - -g는 그룹을 지정할 때 사용. -d는 홈 디렉터리 지정. -s는 사용자 생성 시 사용자가 사용할 셀을 지정한다.
  
 ![image](https://user-images.githubusercontent.com/108641325/196202216-611da255-c21d-4a71-878d-43397d005434.png)

---

**3. WildFly 설치**

![image](https://user-images.githubusercontent.com/108641325/196202329-666ee680-76a4-44f1-b25c-5fad8de1e0fe.png)

![image](https://user-images.githubusercontent.com/108641325/196202347-bb6a35fa-2777-4882-b26f-37e7ba818973.png)


- 설치파일을 다운받은 후 압축을 풀어주자.

![image](https://user-images.githubusercontent.com/108641325/196206536-bfef9020-2fa5-4103-bba7-df7398e4ce20.png)


- 그 다음에는 링크파일 생성

![image](https://user-images.githubusercontent.com/108641325/196206909-bb4d18ec-513c-454b-948b-f739c0e67ab3.png)

---

**4. 소유권 변경**

- WildFly는 WildFly 설치 디렉토리에 댛나 액세스 권한이 필요한 WildFly 사용자 아래에서 실행된다.
- 디렉터리 소유권을 사용자 및 그룹 wildfly로 변경.

  ![image](https://user-images.githubusercontent.com/108641325/196207178-bfa6ed14-35ef-4059-b25f-ed1127834f52.png)
 
 ![image](https://user-images.githubusercontent.com/108641325/196207306-135730cd-5e7b-4be7-881a-394406b2273a.png)
 
- chown명령어는 Change와 Owner를 조합한 명령어로 파일 소유권과 그룹을 변경하는 명령어.
- chown (OPTION) (OWNER) (:GROUP) FILE 순으로 사용할 수 있다.
- -RH는 지정한 파일 하위까지 변경(R)과 심볼릭링크의 참조파일만 변경(H)이다.

---

**5. Systemd 구성**

- WildFly 패키지에는 WildFly를 서비스로 실행하는데 필요한 파일이 포함되어 있다. 구성 파일을 저장할 디렉토리를 생성하자.

![image](https://user-images.githubusercontent.com/108641325/196207712-4d88af19-7e39-4135-85b3-f62a3bef1adf.png)

- wildfly.conf 파일을 사용하면 WildFly 모드와 바인드 주소를 지정할 수 있다. 기본적으로 WildFly는 독립 실행형 모드에서 실행되며, 모든 인터페이스에서 수신대기한다고 한다. 필요에 따라 파일 편집이 가능하다.

  ![image](https://user-images.githubusercontent.com/108641325/196208103-0ddad858-83bf-4928-97f5-f353a650158f.png)

  ![image](https://user-images.githubusercontent.com/108641325/196210100-fcc59142-9370-4c30-931a-b83509e2885b.png)
  
---

- 다음은 WildFly launch.sh 스크립트를 /opt/wildfly/bin/디렉토리에 복사한다.

  ![image](https://user-images.githubusercontent.com/108641325/196210426-420e52e7-9a33-4074-87e8-f1d2ac3f7781.png)

  ![image](https://user-images.githubusercontent.com/108641325/196210560-e390d6d7-3175-453f-b458-6e96cedd4d9a.png)

  ![image](https://user-images.githubusercontent.com/108641325/196210579-8a9eb562-c21e-4d28-975c-1b3d2abeafde.png)

---

- bin 디렉토리의 ![image](https://user-images.githubusercontent.com/108641325/196210889-0e22e6f3-74a9-4745-8821-0e1633a37d55.png)
 실행권한을 추가한다. (sh -c 옵션은 문자열에 대한 명령을 읽는다.)

  ![image](https://user-images.githubusercontent.com/108641325/196211080-40de32a5-7081-4c0e-aba2-a3b9f048ced3.png)


- 이름이 지정된 systemd 유닛파일을 /etc/systemd/ 디렉토리에 복사한다.

  ![image](https://user-images.githubusercontent.com/108641325/196211343-18dd21b9-68e6-4447-b5db-ae140cf317fc.png)

  ![image](https://user-images.githubusercontent.com/108641325/196211508-150e4e04-bfbf-47b4-a9d7-15a358b68ef0.png)

---

- 시스템이 새 장치 파일이 생성되었음을 알린다.

  ![image](https://user-images.githubusercontent.com/108641325/196211577-78574a1a-3297-4375-ba4d-77e6c1f11e48.png)

- WildFly 서비스를 시작하고 다음 부팅 시에도 자동으로 실행되게 설정한다. 서비스 실행중인지도 확인하자.

  ![image](https://user-images.githubusercontent.com/108641325/196211754-15a3ebc6-bf79-41e9-a669-60359b3f8bce.png)

  ![image](https://user-images.githubusercontent.com/108641325/196211892-101caa78-f138-45dc-bdec-3590f2e15636.png)

---

**6. 방화벽 조정**

- 와일드 플라이 인스턴스에 액세스 하기 위해 8080 포트를 열어주자

![image](https://user-images.githubusercontent.com/108641325/196212884-ba5f698e-b3fb-4b9d-9e5c-f27b5fe6928e.png)

---

**7. WildFly 설치 테스트**

- 새 사용자를 추가한다.

![image](https://user-images.githubusercontent.com/108641325/196213374-613362f8-942b-43a2-9037-5594cc44e5e4.png)

---

- 사용자 세부 정보를 입력해준다.

![image](https://user-images.githubusercontent.com/108641325/196213532-5f0a6331-1b49-417f-a0c5-ad93893021a2.png)

---

- 설치됐는지 보자(curl 명령어 활용)

![image](https://user-images.githubusercontent.com/108641325/196213630-612a65b8-1620-4a39-8fbe-022278f4582a.png)

(잘 설치되었다.)

---

**8. WildFly 관리 콘솔에 액세스**

![image](https://user-images.githubusercontent.com/108641325/196213882-3f78064d-b645-4d46-8399-49f587c85282.png)

(와일드플라이 빈 디렉토리로 이동하고 --connect 옵션을 사용하여 스크립트를 실행)

-> 콘솔 프롬프트가 [standalone@localhost:9990 /] 로 바뀐걸 볼수 있다.

---
---

## 3. MySQL 설치

- DB 서버에 접속해주자.

![image](https://user-images.githubusercontent.com/108641325/196214316-176cf35b-e2c7-4ef4-afa0-84e92a155250.png)

---

단계는

**1. MySQL 설치다운로드 링크 확인**

**2. MySQL Repository 설치**

**3. MySQL 설치**

**4. MySQL 서버 시작 및 접속**

**5. Root 계정 비밀번호 변경**

---

**1. MySQL 설치다운로드 링크 확인**

![image](https://user-images.githubusercontent.com/108641325/196214670-93cb7f7a-9bcb-4e6d-9cc9-0747d1b9d192.png)

![image](https://user-images.githubusercontent.com/108641325/196215184-35dedd51-a8ac-449e-bd5e-92bf6b4c20ac.png)

- CentOS에서는 Yum을 사용가능하니, Yum을 사용하자.

![image](https://user-images.githubusercontent.com/108641325/196215260-ee594f6e-4017-402d-aef5-313da721c092.png)

![image](https://user-images.githubusercontent.com/108641325/196215306-6520a274-de37-44e8-b9bb-44c855c0d2ab.png)

- No thanks, just start my download를 오른쪽 클릭해서 링크 주소를 복사해주자.

---

**2. MySQL Repository 설치**

- PuTTY에서 다음 명령어를 실행해준다.

![image](https://user-images.githubusercontent.com/108641325/196216944-febd9cd9-84f1-4f7a-bd8e-116546a6f397.png)

![image](https://user-images.githubusercontent.com/108641325/196216990-93bd9013-45bb-40db-bc76-4c04023d0960.png)

---

- MySQL을 설치할 수 있는 레포지토리가 설치되었다. yum repolist 명령어로 방금 설치된 mysql 레포지토리 목록을 확인할 수 있다.

  ![image](https://user-images.githubusercontent.com/108641325/196217265-7c7648bd-50aa-49fa-bce6-e7d29d93a102.png)

---

- yum search mysql을 사용해서 설치 가능한 mysql 패키지 목록도 확인할 수 있다.

  ![image](https://user-images.githubusercontent.com/108641325/196217477-4ad1ba3d-f987-4a8a-81e3-5449c53a6449.png)

---

**3. MySQL 설치**

- yum install -y mysql-server

![image](https://user-images.githubusercontent.com/108641325/196217899-b9cf708b-4591-43fc-8f74-80ab7bac7ea8.png)

![image](https://user-images.githubusercontent.com/108641325/196217923-ca6e978a-e404-4e32-98dd-ab795ddd9f4e.png)

---

- mysqld -V mysql -version으로 잘 설치되었는지 확인하자.

![image](https://user-images.githubusercontent.com/108641325/196217982-26a03887-cd72-4ab6-b290-28247ca51838.png)

---

**4. MySQL 서버 시작 및 접속**

- 서버를 시작해보자

![image](https://user-images.githubusercontent.com/108641325/196218230-10c801ba-81f4-4d4c-a22a-8e44e4ae61dd.png)

![image](https://user-images.githubusercontent.com/108641325/196218321-4f6177f7-9b8a-447b-9272-bdc62f0c6c54.png)

---

- 서버 설치과정에서 임시 비밀번호가 생성되며, 이 비밀번호로 접속이 가능하다.

- grep 'temporary password' /var/log/mysqld.log로 확인해보자.

![image](https://user-images.githubusercontent.com/108641325/196218492-f2988d56-54e4-4cea-9764-b77ccbd22f59.png)

(접속을 위해선 저 비밀번호가 필요하다.)

---

- mysql -u root -p 로 접속

![image](https://user-images.githubusercontent.com/108641325/196218716-2a17a875-ba6b-4a3e-8e4a-963948f4c91e.png)

---

**5. Root 계정 비밀번호 변경**

![image](https://user-images.githubusercontent.com/108641325/196218875-bb22c89a-d13b-41c8-9b2b-dd55d1db7645.png)

(database 조회를 좀 하려니까 오류가 생겨버린다.)

- 비밀번호를 바꾸라고 했으므로, root 유저의 비밀번호를 변경해주자.

---

![image](https://user-images.githubusercontent.com/108641325/196219167-6cc24e15-07c9-482e-bf05-a83737897925.png)

![image](https://user-images.githubusercontent.com/108641325/196219071-a93a1fe4-b5b4-4f26-b358-5606ad461fbb.png)

---

- 비밀번호를 바꾸어주면 database 조회가 잘 된다.

![image](https://user-images.githubusercontent.com/108641325/196219591-59e05bd0-04ee-4ece-95fc-f25337a0eff2.png)

---
---

## 4. ncloud의 CDB for MySQL 사용해보기

![image](https://user-images.githubusercontent.com/108641325/196220966-0de4bf5f-25e0-4b69-9a2e-1c719cccce8e.png)

---

- DB 서버를 생성하자
![image](https://user-images.githubusercontent.com/108641325/196221017-55c50b70-4c98-4a65-b83f-10e30a1a838b.png)

(VPC는 앞에 만들어놓았던 user07로, Subnet도 user07의 DB용 서버에 연결해준다.)

(서버 이름과 서비스 이름은 적당히 해준다.)

---

![image](https://user-images.githubusercontent.com/108641325/196221235-83237ea6-ec50-4186-8ba0-8cc74faf3dc8.png)

- 실제로 DB접속 정보와 DB를 구성하는 정보를 입력하는 페이지.
- User_ID는 DB에 접속할때 사용하는 ID,
- HOST(IP)는 DB에 접속 허용할 IP를 정하는 옵션이다. 여기서는 모든 IP를 허용하기 위해 '%' 를 입력했다.(좋은 방법은 아니다. 실제에서는 최소한의 권한을 주기위해 WAS IP대역을 주는 것을 권장하지만, 연습이니까..)
- USER 암호는 접속 암호다. 적당히 만들고 반드시 기억해주자.
- 기본 DB명은 최초에 생성할 DB명이다.

---

![image](https://user-images.githubusercontent.com/108641325/196221418-38c5436c-c7f1-40f1-a2ab-cc1aea719581.png)

- Master와 Standby Master으로 구성된 것을 볼 수 있는데, 마스터로 기존 운영하다, 장애 발생 시 자동으로 Standby Master로 교체된다고 한다. 서비스 자체에서 이중화와 fail over 기능을 제공하는 셈.

---
---
