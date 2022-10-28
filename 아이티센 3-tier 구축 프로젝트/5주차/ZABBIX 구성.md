## 1. 단일 구성

- version : zabbix 5.0
- OS : CentOS 7
- zabbix component : Server, Frontend, Agent
- Database : MySQL
- Web Server : Apache

![image](https://user-images.githubusercontent.com/108641325/197166845-800fc7d0-3e2b-470a-897e-cb5b7e36241b.png)

- zabbix 공식 홈페이지에 접속하여, 다운로드 탭에서 설치 형태/버전 등의
옵션을 선택할 수 있다.
- 이 방식 외에도 Cloud Images Docker Containers 등의 방식으로 다운받을
수 있다.

![image](https://user-images.githubusercontent.com/108641325/197166969-393f99d5-4053-41b0-8728-1db0abc97d27.png)

---

**- Zabbix 대쉬보드 띄워보기**


- 서버 생성 및 접속

  - ncloud 에서 서버를 생성하고, 공인 IP 를 발급받아서 접속한다.
단일 구성해보는 것이 목표임으로 classic 환경에서 진행했다.

![image](https://user-images.githubusercontent.com/108641325/197167408-b36af313-ecf4-4c03-963f-8224f97ff448.png)

1) Zabbix 레포지토리 생성

![image](https://user-images.githubusercontent.com/108641325/197167787-c023c1c2-15bb-4351-8af7-dc8c9935bdd1.png)

- zabbix 파일이 들어있는 레포지토리를 연결한다.
- rpm -Uvh https://repo.zabbix.com/zabbix/5.0/rhel/7/x86_64/zabbixrelease-5.0-1.el7.noarch.rpm

![image](https://user-images.githubusercontent.com/108641325/197178849-22aa077c-20fc-46fb-ada2-9afdcddc7975.png)

- 그리고 yum 캐시 데이터로 인해 잘못된 동작이 일어날 수 있으므
로 패키지를 설치하기 전에 # yum clean all 명령어로 yum 캐시를
정리해준다.

---

2) zabbix 다운로드

- serverm frontendm, agent를 패키지로 다운 받는다.
- yum install zabbix-server-mysql zabbix-agent

![image](https://user-images.githubusercontent.com/108641325/197179551-53165245-32eb-43a2-92ed-8d5bf65e0b99.png)

![image](https://user-images.githubusercontent.com/108641325/197179582-27d667b4-2fb6-4919-bef0-9fa0d572d053.png)

---

3) zabbix frontend 설치

- zabbix frontend를 설치한다.
- yum install centos-release-scl

![image](https://user-images.githubusercontent.com/108641325/198570557-afa96367-5cfc-4592-b8e9-52f98f894832.png)

![image](https://user-images.githubusercontent.com/108641325/198570578-5969b976-4bb8-4c1b-b887-4feb6f03c458.png)

---

4) frontend 활성화

- 다음 repo 파일을 수정해줘서 frontend를 활성화해준다(enabled=0으로 초기설정되어 있는 것을 =1로 바꿔주기)
- vi  /etc/yum.repos.d/zabbix.repo

![image](https://user-images.githubusercontent.com/108641325/198576365-e7410cfa-2bd6-4ec8-9a47-36424a758bc8.png)

---

5) frontend 패키지
 
- Zabbix frontend 패키지를 설치해준다.
- yum install zabbix-web-mysql-scl zabbix-apache-conf-scl

![image](https://user-images.githubusercontent.com/108641325/198576866-d9f6fb47-1e56-4354-984f-9d2bc1b43f7d.png)

![image](https://user-images.githubusercontent.com/108641325/198576875-c83ea0f3-5ead-40f9-b525-401d81bc4b95.png)

---

6) Database 설치(MySQL)

---

7) Database 생성 및 설정

- 다시 zabbix로 돌아와서 Database를 생성/계정 생성한 뒤 권한 설정을 한다.

![image](https://user-images.githubusercontent.com/108641325/198577126-ce79cfb8-7af1-435d-bd8c-e2e71a08a572.png)

![image](https://user-images.githubusercontent.com/108641325/198577145-a65a181d-75ed-437b-9fb9-08aa72947530.png)

![image](https://user-images.githubusercontent.com/108641325/198577150-8ae5af88-069b-4a5e-9d13-f80505963e0b.png)

---

8) schema 적용

- zabbix 서버 호스트에서 초기 스키마 및 데이터를 가져와 방금 생성한 Database에 적용.
- 데이터 베이스를 생성했을 때 설정한 패스워드를 입력하라는 메시지가 표시된다. root 사용자의 계정을 입력하면 된다.
- zcat /usr/share/doc/zabbix-server-mysql*/create.sql.gz | mysql -uzabbix -p zabbix

![image](https://user-images.githubusercontent.com/108641325/198577245-4ef12615-75e4-4603-8a55-73f62427a48e.png)

- 이후 데이터베이스의 테이블을 확인해 정상적으로 적용됐는지 확인하자.

![image](https://user-images.githubusercontent.com/108641325/198577273-913eaa53-bdd4-4e08-bbe7-ef2fc30566c8.png)

---

9) 데이터베이스 설정

- zabbix 서버에 대한 Database를 설정
- vi /etc/zabbix/zabbix_server.conf

![image](https://user-images.githubusercontent.com/108641325/198577334-fa772b9d-784b-46d1-b718-9ed4dddd8e2f.png)

![image](https://user-images.githubusercontent.com/108641325/198577361-dc3f26a6-214f-45e7-9719-724d8739ad84.png)

![image](https://user-images.githubusercontent.com/108641325/198577392-9044b1fb-d257-4129-9506-17f9681c6984.png)

- 주석 해제하고 패스워드를 입력해주자

![image](https://user-images.githubusercontent.com/108641325/198577464-998b474a-b0ff-4e5c-86b3-1e9576ddba76.png)

---

10) Timezone 설정 후 실행

- vi /etc/opt/rh/rh-php72/php-fpm.d/zabbix.conf 파일을 수정해서 Timezone을 수정해준다.

![image](https://user-images.githubusercontent.com/108641325/198577700-9e661236-5dd1-4886-93e9-1d3942165887.png)

![image](https://user-images.githubusercontent.com/108641325/198577616-0ea1d18d-3cda-4cc9-a02a-a1d92729da17.png)

- 설정이 완료되었다면 시작해보자.

![image](https://user-images.githubusercontent.com/108641325/198577821-ba4a9523-a1f9-48c0-9d67-f5e680405071.png)

---

11) 오류 발생 -> 해결해주자

![image](https://user-images.githubusercontent.com/108641325/198577998-3ab5d22b-153e-4bea-939a-3213ac6b5931.png)

- DB Password도 바꿔주자

https://velog.velcdn.com/images/rlawogus73/post/19f7c3ea-28fa-4367-b4d5-ad08e6da82d7/image.png

---

12) 방화벽 설정

![image](https://user-images.githubusercontent.com/108641325/198578100-3ba76e91-06c7-428e-a831-8767b7cd0479.png)

---

13) Frontend 설정

- http://{공인IP}/zabbix 접속

![image](https://user-images.githubusercontent.com/108641325/198578211-cb266d09-6b3d-443d-ab95-9bb14b015d53.png)

![image](https://user-images.githubusercontent.com/108641325/198578235-91165a7d-6e4b-4425-8418-ca342d328d46.png)


- 변경한 DB Password 입력

![image](https://user-images.githubusercontent.com/108641325/198578254-5cd2bc9a-37c8-41fb-8304-ab21ae347224.png)

![image](https://user-images.githubusercontent.com/108641325/198578420-bceef0e2-5ec2-4443-90e5-a6623e5de582.png)

![image](https://user-images.githubusercontent.com/108641325/198578454-338debd3-96c7-407f-9971-2c085590d2d9.png)

![image](https://user-images.githubusercontent.com/108641325/198578459-2892cfe6-240a-4d76-b030-4a230151828d.png)

![image](https://user-images.githubusercontent.com/108641325/198578461-afd838d5-257e-44b4-82cd-2c83bcede6d0.png)

- 설치 완료!
![image](https://user-images.githubusercontent.com/108641325/198578491-6cd4f059-418f-4f50-bef3-b6ed0ac8cb9a.png)

---



