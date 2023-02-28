## Docker-compose

Docker-compose to narzędzie ułatwiające budowanie "instalatora" złożonej aplikacji, np. składającej się z Frontendu, Backendu i Bazy danych.
W pliku docker-compose.yaml definiujemy jakie obrazy zbudować, jakie kontenery uruchomić oraz ustalić zależności między kontenerami.
Następnie wystarczy jednym poleceniem uruchomić całą aplikację.

1. Uruchom aplikację Flask
```
cd compose_flask
docker-compose up -d
```

2. Uruchom klaster Apache Kafka (opcjonalnie)
```
cd compose_kafka
docker-compose up -d
``` 
