#Inspekcja kontenerów  
Ćwiczenie pokaże w jaki sposób uzyskać informacje o konfiguracji kontenerów i parametrach jego pracy.

1. Pokaż pełną informację o kontenerze "web"
```
sudo docker inspect web
```

2. Pokaż zajętość dysku przez kontener "web"
```
sudo docker inspect --size web -f '{{ .SizeRootFs }}'
```

3. Pokaż zajętość dysku przez kontener "web" ale tylko dopisanych od czasu uruchomienia. 
```
sudo docker inspect --size web -f '{{ .SizeRw }}'
```

4. Pokaż konfigurację sieciową kontener "web"
```
sudo docker inspect --format='{{range .NetworkSettings.Networks}}{{.MacAddress}}{{end}}' web
```

5. Pokaż Nazwę kontnera oraz status dla wszystkich kontenerów
```
sudo docker ps -a --format '{{.Names}}\t{{.Status}}'
```

6. Pokaż nazwę kontenera oraz ścieżkę do LogPath dla wszystkich kontnerów
```
sudo docker inspect --format='{{.Name}} {{.LogPath}}' $(sudo docker ps -qa)
```

7. Sprawdź ile zajmuja wszystkie logi kontnerów
```
sudo su
du -sh /var/lib/docker/containers/*/*-json.log
```
