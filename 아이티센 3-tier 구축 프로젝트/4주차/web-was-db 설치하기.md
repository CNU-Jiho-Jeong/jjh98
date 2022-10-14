## 3티어 아키텍쳐

- 플랫폼을 3개의 계층으로 물리/논리적으로 나누어 운영하는 것.
- 웹 서버의 경우, 1대의 서버에 전부 구축하지 않고 각각 웹, WAS, DB의 3개로 나누어 운영한다.
- 각각 계층들은 서로 독립적이므로 서로간에 영향을 미치지 않기에 업무 분담 시 각 계층을 담당하도록 인원을 배치하거나, 서버의 부하를 줄여주거나 보안상의 이점을 얻을 수 있다.
- 2개의 가용영역으로 나누어 하나의 인스턴스에서 작동이 중단되어도 다른 인스턴스에서 작동할 수 있게끔 해주면 더 좋다.


## 구축 순서(AWS)

#### 1. VPC 생성
#### 2. IGW 생성
#### 3. 서브넷 생성 (Public 2대, private 6대)
#### 4. NAT 게이트웨이 생성
#### 5. 라우팅 테이블 생성(IGW, NAT, 서브넷 연결)
#### 6. 보안그룹 생성
#### 7. EC2 인스턴스 생성 (WEB, WAS)
#### 8. ELB 생성
#### 9. RDS 생성

---

#### 1. VPC 생성

![image](https://user-images.githubusercontent.com/108641325/195844995-c3c23fbd-ef87-4e5d-a64e-5625815ae5aa.png)

- VPC(Virtual Private Cloud)는 AWS에서 가상 네트워크를 제공해주는 서비스이다.
- 사용자 상황에 맞게 VPC를 생성하고, 서브넷, 라우팅 테이블, 게이트웨이 등 네트워크 자원들을 가상으로 생성, 사용할 수 있다.


#### 2. IGW 생성

- IGW(Internet GateWay)는 VPC가 외부 인터넷과 연결할 수 있게 해준다.
- VPC - IGW - 외부 인터넷


#### 3. 서브넷 형성

- 서브넷은 하나의 네트워크가 분할되어 나눠진 작은 네트워크.
- IP 주소를 효율적으로 사용하기 위해 적절한 단위로 네트워크를 분할하자.


#### 4. NAT 게이트웨이 생성

- NAT 게이트웨이는 프라이빗 서브넷에서 외부로 통신하기 위한 관문
- 프라이빗 서브넷이 외부와 통신하기 위해 NAT 게이트웨이에 EIP를 할당받아 연결한다.


#### 5. 라우팅 테이블 설정

- 네트워크 통신이 이루어질 때, 데이터는 라우터를 거쳐간다.
라우터는 해당 데이터들의 경로를 지정해주는 역할을 하고, 경로들을 라우팅 테이블에 저장시킨다.

- 데이터들은 라우팅 테이블의 저장되어 있는 경로를 따라 원하는 목적치를 찾아가게 된다.

- 5.1 퍼블릭 서브넷용 라우팅 테이블을 생성, 모든 트래픽은 인터넷 게이트를 통해 외부와 연결할 수 있게 한다.

- 5.2 2개의 퍼블릭 서브넷과 연결, 퍼블릭 서브넷의 경로를 지정해줌.

- 5.3 마찬가지로, 프라이빗 서브넷들의 모든 NAT 게이트웨이로 향하는 경로를 지정해줌.

- 5.4 6개의 프라이빗 서브넷과 연결, 프라이빗 서브넷들의 경로 지정.


#### 6. 보안그룹 생성

- 인스턴스에 접근하거나, 인스턴스가 접근하려고 하는 패킷을 포트번호로 제어하기 위한 설정.

- 인바운드, 아웃바운드 규칙을 통해 어느 포트를 허용/차단할지 정한다.

  - 인바운드 규칙 - 기본 규칙은 모든 트래픽에 대해 차단.
허용해 줄 포트만 열어주는 Whitelist 방식

  - 아웃바운드 규칙 - 기본 규칙은 모든 트래픽에 대해서 허용.
차단해 줄 포트만 닫아주는 BlackList 방식

![image](https://user-images.githubusercontent.com/108641325/195845518-f59413e0-abf9-414f-9478-eb8fe9b7f38e.png)


## 실제로 구축해보기

### 1. VPC 생성

![image](https://user-images.githubusercontent.com/108641325/195845709-57360c15-f393-4c7f-885e-afd5110f3bba.png)


### 2. vpc 내부에 서브넷 생성하기

![image](https://user-images.githubusercontent.com/108641325/195845748-cbf49d05-001d-4e5f-887d-72717ec4871e.png)


- 서브넷은 총 3개를 생성한다.
![image](https://user-images.githubusercontent.com/108641325/195845885-a7ffda9c-4486-494b-96f8-be933c85a12e.png)

![image](https://user-images.githubusercontent.com/108641325/195846034-2cd3598f-9c8e-4aa3-a3b2-a1b29aadebbc.png)

![image](https://user-images.githubusercontent.com/108641325/195846054-995accc6-06e3-4a58-aae3-e49d691f6e0a.png)

![image](https://user-images.githubusercontent.com/108641325/195846085-0cd6d9aa-7fbb-4f7d-891a-fbaf7b5c8777.png)


### 3. WAS 서버에서 Yum으로 프로그램 설치를 위해 NAT Gateway 생성해주고, Route Table을 설정해주기

![image](https://user-images.githubusercontent.com/108641325/195846138-52552e37-5d1e-4ce6-80c9-c08fd2d065ee.png)

![image](https://user-images.githubusercontent.com/108641325/195846156-2f70a653-cdda-4568-9234-eb6d2b409212.png)

![image](https://user-images.githubusercontent.com/108641325/195846624-2e27f923-1c62-43b9-abad-b84ed2b1947c.png)

![image](https://user-images.githubusercontent.com/108641325/195846642-f6b6e0b7-40f8-475a-99f7-55e14bc3bf18.png)


### 4. ACG 생성(우선 두 개)

![image](https://user-images.githubusercontent.com/108641325/195846693-333070ef-6d77-4ce2-97e3-f65aec9fc26e.png)

![image](https://user-images.githubusercontent.com/108641325/195846705-56d9492b-3d4e-4fee-b989-fdb4cbcdf9a3.png)

![image](https://user-images.githubusercontent.com/108641325/195846741-b655234f-b057-4c4c-b79d-5f056852ff59.png)


### 5. ACG 설정해주기

![image](https://user-images.githubusercontent.com/108641325/195846809-520732c3-d777-42af-a5bf-ff11f9845863.png)

![image](https://user-images.githubusercontent.com/108641325/195846832-4cd8211c-f590-4930-874d-63e12818fab0.png)

![image](https://user-images.githubusercontent.com/108641325/195846845-5fffbffa-592a-4f5a-9708-afbac4bdd727.png)

![image](https://user-images.githubusercontent.com/108641325/195846869-8ebc2f28-517c-477e-88a6-e21be0f4f0db.png)

- 공통 outbound 룰 설정(epel 로 설치하는 Package 설치를 위해)

![image](https://user-images.githubusercontent.com/108641325/195846925-22492a9c-4276-459a-a524-2ae3f05d5609.png)


### 6. 서버 3개 생성해주기

1. 웹서버 생성
![image](https://user-images.githubusercontent.com/108641325/195847118-05dd6f2b-942b-4737-9af5-78ded6e9aa79.png)

