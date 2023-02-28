## Docker-compose

Docker-compose to narzędzie ułatwiające budowanie "instalatora" złożonej aplikacji, np. składającej się z Frontendu, Backendu i Bazy danych.
W pliku docker-compose.yaml definiujemy jakie obrazy zbudować, jakie kontenery uruchomić oraz ustalić zależności między kontenerami.
Następnie wystarczy jednym poleceniem uruchomić całą aplikację.

1. Przejdź do katalogu compose_flask
```
cd compose_flask
```

2. Uruchom aplikację 
```
docker-compose up -d
``` 
