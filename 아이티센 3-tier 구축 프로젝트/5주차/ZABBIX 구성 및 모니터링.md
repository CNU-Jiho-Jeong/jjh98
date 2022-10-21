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




