# Multi-stage Dockerfile
Ćwiczenie pokaże w jaki sposób budować aplikację z wykorzystaniem Muli-stage Docker

1. Przejdź do katalogu multistage-app i obejrzyj pliki
- Aplikacja: server.js
- Plik package.json
- Dockerfile
```
cd ~/docker-training/Lab\ 14/multistage-app
```

2. Zbuduj obraz
```
sudo docker build --tag multi-app .
```

3. Uruchom aplikację Flask
```
sudo docker run -d --name multi -p 5100:80 multi:latest
```

4. Pokaż stronę
```
curl localhost:5100
```
