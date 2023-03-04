# Zarządzanie kontenerami

- zarządzanie uruchomionymi kontenerami tj start, stop, restart
- usuwaniem kontenerów
- wyświetlaniem logów kontenera
- update parametrów kontenera

Lab 4 jest kontynuuacją Lab3 !!!

1. Wyświetl wszystkie kontenery
```
sudo docker ps -a
```

2. Uruchom kontener o nazwie external-wordpress i sprawdź jego status na liście kontenerów
```
sudo docker container start external-wordpress
```

3. Wyświetl ponownie wszystkie kontenery i sprawdź status kontenera external-wordpress
```
sudo docker ps -a
```

4. Zatrzymaj kontener o nazwie external-wordpress
```
sudo docker container stop external-wordpress
```

5. Zrestartuj kontener o nazwie internal-wordpress i sprawdź jego status na liście kontenerów
```
sudo docker container stop internal-wordpress
```

6. Usuń kontener external-wordpress
```
sudo docker rm -f external-wordpress
```

7. Zaktualizuje parametr uruchomionego kontenera internal-wordpress
Istnieje możliwość zmiany parametrów zgodnie z listę na stronie https://docs.docker.com/engine/reference/commandline/update/
```
sudo docker update --memory 256M internal-wordpress
sudo docker update --restart always internal-wordpress
```
