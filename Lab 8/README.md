# Backup and Restore
W tym ćwiczeniu zostaną pokazane mechanizmy wykonywania kopi zapasowowej obrazów i kontenerów oraz ich przywracanie z plików do instancji Docker.

1. Zbuduj obraz www3 w oparciu o pliki z katalogu www3
```
sudo docker build -t www3:v1 www3\
```

2. Uruchom kontener app-www z obrazu www3
```
sudo docker run -dit --name app-www -p 8081:80 www3:latest
```

3. Zapisz obraz do pliku
```
sudo docker save --output www3.tar www3:latest
```

4. Wykonaj export działającego kontenera app-www do pliku
```
sudo docker export --output="app-www.tar" app-www
```

5. Usuń kontener
```
sudo docker rm -f app-www
```

6. Usuń obraz www3
```
sudo docker image rm -f www3
```

7. Przywróć obraz www3 z pliku
```
sudo docker load --input www3.tar
```

8. Wyświetl listę obrazów i sprawdź czy znajduje się na niej wczytany obraz
```
???
```

9. Importuj kontener z pliku
```
sudo docker import app-www.tar
```

10. Wyświetl listę kontenerów i sprawdź czy znajduje się na niej zaimportowany kontener
```
???
```


