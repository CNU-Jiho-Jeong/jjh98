# NFS 서버 구축하여 클라이언트에서 NAS 연결해보기

1. 서버 생성

2. Services - NAS - NAS 볼륨 - NAS 생성

3. NAS 볼륨을 마운트 할 서버를 선택 (생성한 서버 선택)

4. Putty 로그인 후, yum install nfs-utils -y 명령어로 NFS 관련 패키지 설치

5. RPC 데몬 기동(systemctl start rpcbind / systemctl enable rpcbind 사용)

6. mkdir /nas 명령어로 마운트 포인트 생성

7. mount -t nfs 10.250.116.32:/n009149_user08 /nas 명령어로 NAS 볼륨 마운트
 
 - 10.250.116.32:/n009149_user08: 마운트 정보

8. vim /etc/fstab 명령어로 마운트 정보 유지 설정