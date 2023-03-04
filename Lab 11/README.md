# Budowa obrazu aplikacji Python
Ćwiczenie pokaże w jaki sposób zbudować własną aplikację Python z modułem Flask

1. Przejdź do katalogu python-app i obejrzyj pliki
- Aplikacja Pytgon: app.py
- Plik requirements.txt
- Dockerfile

2. Zbuduj obraz
```
sudo docker build --tag flask-app .
```

3. Uruchom aplikację Flask
```
sudo docker run -d --name flask -p 5000:5000 flask-app:latest
```

4. Pokaż stronę
```
curl localhost:5000
```

5. Poszukaj kontenera flask-app na podstawie nazwy
```
sudo docker ps -a --filter "name=flask-app"
```

6. Poszukaj kontenera flask-app na podstawie LABEL ustawionej w pliku Dockerfile
```
sudo docker ps -a --filter "label=engine=python"
```
