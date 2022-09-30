# NFS 서버 구축하여 클라이언트에서 NAS 연결해보기

1. 서버 생성

![image](https://user-images.githubusercontent.com/108641325/193247649-11624fc2-d223-4952-8c67-fc97d381c8ec.png)

---

2. Services - NAS - NAS 볼륨 - NAS 생성

![image](https://user-images.githubusercontent.com/108641325/193247680-16ac42c9-8263-4d70-9541-41a98d5edcf5.png)

---

3. NAS 볼륨을 마운트 할 서버를 선택 (생성한 서버 선택)

![image](https://user-images.githubusercontent.com/108641325/193247733-55a4766a-83ea-4ecd-9951-c894175a2db1.png)

---

4. Putty 로그인 후, yum install nfs-utils -y 명령어로 NFS 관련 패키지 설치

![image](https://user-images.githubusercontent.com/108641325/193247751-661f89c5-c87f-49c1-8274-82a6c25c3bb3.png)

![image](https://user-images.githubusercontent.com/108641325/193247771-e548eb80-0e4e-4e6d-b8dc-702cefa149da.png)

---

5. RPC 데몬 기동(systemctl start rpcbind / systemctl enable rpcbind 사용)

![image](https://user-images.githubusercontent.com/108641325/193247795-754cd5f9-c1e1-41f6-8064-6b374d3adda8.png)

---

6. mkdir /nas 명령어로 마운트 포인트 생성

![image](https://user-images.githubusercontent.com/108641325/193247835-dcb12d70-ee20-4ae9-a18f-20bfc2f837b7.png)

---

7. mount -t nfs 10.250.116.32:/n009149_user08 /nas 명령어로 NAS 볼륨 마운트
 
 - 10.250.116.32:/n009149_user08: 마운트 정보
 
 ![image](https://user-images.githubusercontent.com/108641325/193247875-da4556a2-2b9b-467e-b096-1d48468a3a9d.png)

---

8. vim /etc/fstab 명령어로 마운트 정보 유지 설정

![image](https://user-images.githubusercontent.com/108641325/193247955-45576bcb-b306-4568-9f0f-1379fe9c70ba.png)

