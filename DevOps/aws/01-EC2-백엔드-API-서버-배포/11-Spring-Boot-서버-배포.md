# 🍃Spring Boot 서버를 EC2에 배포하기

EC2의 Ubuntu 환경에 JDK를 설치하고, Spring Boot 프로젝트를 빌드해 실행하는 과정을 정리한다.

## 이 글에서 배우는 것

- Ubuntu에 JDK 17 설치하기
- GitHub 프로젝트를 EC2로 가져오기
- `application.yml` 파일을 서버에서 직접 만들기
- Gradle로 JAR 파일 빌드하기
- Spring Boot 서버를 백그라운드에서 실행하기

## 1. JDK 설치하기

강의에서는 Spring Boot 3.x와 JDK 17을 기준으로 진행한다.

```bash
sudo apt update
sudo apt install openjdk-17-jdk -y
```

설치가 완료되면 Java 버전을 확인한다.

```bash
java -version
```

출력 결과에 `17`이 포함되어 있으면 정상적으로 설치된 것이다.

## 2. Spring Boot 프로젝트 가져오기

GitHub에 있는 Spring Boot 프로젝트를 EC2로 가져온다.

```bash
git clone https://github.com/JSCODE-EDU/ec2-spring-boot-sample.git
cd ec2-spring-boot-sample
```

## 3. `application.yml` 파일 만들기

`application.yml`에는 서버 Port, 데이터베이스 정보, 비밀번호 등 민감한 설정이 들어갈 수 있다.

이 파일은 GitHub에 올리지 않고 EC2 서버에서 직접 작성한다.

파일 위치는 다음과 같다.

```text
src/main/resources/application.yml
```

예시:

```yaml
server:
  port: 80
```

프로젝트에 데이터베이스 연결 정보나 API 키가 필요하다면, 실제 프로젝트의 설정에 맞게 추가한다.

민감한 값은 GitHub에 커밋하지 않는다.

## 4. JAR 파일 빌드하기

Gradle을 사용해 Spring Boot 프로젝트를 빌드한다.

```bash
./gradlew clean build
```

빌드가 완료되면 실행 가능한 JAR 파일이 `build/libs` 폴더에 생성된다.

```bash
cd build/libs
```

## 5. Spring Boot 서버 실행하기

생성된 JAR 파일을 실행한다.

```bash
sudo java -jar ec2-spring-boot-sample-0.0.1-SNAPSHOT.jar
```

JAR 파일 이름은 프로젝트 버전에 따라 달라질 수 있으므로, `build/libs` 폴더에서 실제 파일 이름을 확인한다.

## 백그라운드에서 실행하기

터미널을 닫아도 서버가 계속 실행되도록 하려면 `nohup`을 사용할 수 있다.

```bash
sudo nohup java -jar ec2-spring-boot-sample-0.0.1-SNAPSHOT.jar &
```

실행 로그는 기본적으로 `nohup.out` 파일에 저장된다.

```bash
tail -f nohup.out
```

## 서버 동작 확인하기

Spring Boot 서버가 `80`번 Port에서 실행 중이라면 브라우저에서 탄력적 IP 주소로 접속한다.

```text
http://<탄력적-IP-주소>
```

접속이 되지 않는다면 다음을 확인한다.

- EC2 인스턴스가 실행 중인지 확인한다.
- 보안 그룹에서 `80`번 Port를 허용했는지 확인한다.
- JAR 파일이 정상적으로 빌드되었는지 확인한다.
- 서버 실행 로그에 오류가 없는지 확인한다.
