FROM maven:3.8.3-openjdk-17-slim
WORKDIR /usr/app
COPY . /usr/app
RUN mvn clean package -DskipTests && rm -rf /usr/app