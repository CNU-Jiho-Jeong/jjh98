# 1. 타임 서버

- 타임 서버는 시계에서 실제 시간(원자시계 등을 기반)을 읽고, 컴퓨터 네트워크를 사용하여 이 시간 정보를 클라이언트에 배포하는 서버 컴퓨터이다.

- 인터넷을 통해 시간 정보를 배포하는데 있어 널리 사용되는 프로토콜이 NTP(Network Time Protocol)이다.

- 국내 공개 타임서버 리스트 (2021년 12월 13일 기준)

![image](https://user-images.githubusercontent.com/108641325/193717444-0ce0cb87-0ae1-4319-905e-10ab0105f363.png)

![image](https://user-images.githubusercontent.com/108641325/193717450-5af8138e-710a-4cd2-97df-bcf7d46befc0.png)

![image](https://user-images.githubusercontent.com/108641325/193717464-da19d9e3-f87d-4f60-9a6d-0a24965e40ab.png)


- 최대 256계급까지 존재. 현재 16계급까지 사용한다고 한다. 계급 순위가 낮을수록 타임 서버의 우선순위가 높아진다고 한다.

---

# 2. NTP 서버 구축해보기

1. 타임서버 ip 주소 파악하기 (ip addr 명령어 사용)

![image](https://user-images.githubusercontent.com/108641325/193717491-2f97f8a9-b879-4f74-9afe-8ffae8547a99.png)

(10.37.39.78)

---

2. ntp 패키지 설치 (yum install -y ntp 명령어 사용) -> 서버/클라이언트 모두 설치

![image](https://user-images.githubusercontent.com/108641325/193717603-abc3c693-c5f1-45d5-bb6d-13b8df2d4403.png)

![image](https://user-images.githubusercontent.com/108641325/193717611-2da683bb-7c6f-4db1-96ec-ce39df9a4054.png)

---

3. ntp 서버 설정

  1) ntp.conf 파일 들어가기(vi /etc/ntp.conf 명령어 사용)

![image](https://user-images.githubusercontent.com/108641325/193717626-cbf79282-7b5e-4454-8635-400e0aa74fc4.png)

  2) restrict 192.168.1.0 mask 255.255.255.0 nomodify notrap 부분 주석 해제

![image](https://user-images.githubusercontent.com/108641325/193717729-1e6d69f4-c513-4c47-a787-a0c4c6ceea11.png)

(현재 클라이언트가 존재하는 네트워크의 서버들이 ntp 서버에 시간을 요청할 수 있도록 함)

  3) 우선 순위가 높은 타임서버들을 주석처리해버린다. 그리고 편집기에서 나간다.
 
![image](https://user-images.githubusercontent.com/108641325/193717753-936c2f1b-1ee8-4bd9-b360-e7522ce9e584.png)

---

4. 방화벽ID 실행 후 포트를 추가한다.

![image](https://user-images.githubusercontent.com/108641325/193717788-bfc97683-90f1-4139-892e-4222d835d6a2.png)

(영구적으로 포트아이디123 - udp프로토콜 을 add해줌)

---

5. 포트 추가/변경은 --reload 옵션을 실행해야 반영된다.

![image](https://user-images.githubusercontent.com/108641325/193717809-c95d5418-4304-4367-add4-69f5a629e035.png)

---

6. ctl(control)을 통하여 스타트 (systemctl start ntpd)

![image](https://user-images.githubusercontent.com/108641325/193717833-addae9ca-28b0-4610-b749-0e282ff69a26.png)

---

7. ctl(control)을 통하여 enable (systemctl enable ntpd

![image](https://user-images.githubusercontent.com/108641325/193717849-179e0562-e77b-469b-9883-953c947adf2f.png)

---

8. 다시 ntp.conf 파일 들어가서(vi /etc/ntp.conf 명령어 사용) 타임 서버 IP 주소 기입. 그 후 편집기에서 나감.

![image](https://user-images.githubusercontent.com/108641325/193717868-c58ad2f5-1939-4fc2-a7e0-5d30db45ce23.png)

---

9. 현재 클라이언트에서 어떤 타임서버를 쓰는지 파악(ntpq -p 명령어 사용)

![image](https://user-images.githubusercontent.com/108641325/193717884-a2454e00-3978-4843-a655-960d8937149b.png)

(localhost를 사용)
