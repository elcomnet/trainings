# Multi-stage Dockerfile
Ćwiczenie pokaże w jaki sposób budować aplikację z wykorzystaniem Muli-stage Docker

1. Przejdź do katalogu multistage-app i pobierz przykładową aplikację
```
cd ~/docker-training/Lab\ 14/multistage-app
sudo git clone https://github.com/vigneshsweekaran/easyclaim-frontend.git
```

2. Obejrzyj plik Dockerfile

3. Zbuduj obraz
```
sudo docker build --no-cache=true --tag multi-app:latest .
```

4. Uruchom aplikację Flask
```
sudo docker run -d --name multi -p 5100:80 multi-app:latest
```

5. Pokaż stronę
```
curl localhost:5100
```

6. Przejdź do katalogu 'others' i obejrzyj inne przykłady plików Dockerfile Multistage
