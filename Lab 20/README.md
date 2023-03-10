## Docker-compose

Docker-compose to narzędzie ułatwiające budowanie "instalatora" złożonej aplikacji, np. składającej się z Frontendu, Backendu i Bazy danych.
W pliku docker-compose.yaml definiujemy jakie obrazy zbudować, jakie kontenery uruchomić oraz ustalić zależności między kontenerami.
Następnie wystarczy jednym poleceniem uruchomić całą aplikację.

1. Przejdź do katalogu compose_flask i obejrzyj plik docker-compose.yaml
```
cd ~/docker-training/Lab\ 20/compose_flask
```

2. Uruchom aplikację Flask
```
sudo docker-compose up -d
```
![Docker compose](img/lab20_1.png)

3. Zatrzymaj bazę "redis" z aplikację Flask i sprawdź jej status na liscie kontenerów
```
sudo docker-compose stop redis
```
```
sudo docker ps -a | grep redis
```
![Docker compose](img/lab20_3.png)

4. Usuń aplikację Flask
```
sudo docker-compose down
```
![Docker compose](img/lab20_2.png)


5. Uruchom klaster Apache Kafka (opcjonalnie)
```
cd kafka_compose
docker-compose up -d
``` 
