# Uruchamianie kontenerów

1. Pierwszy kontener
```
sudo docker run hello-world
```

2. Wyświetl listę działających kontenerów. Czy kontener busybox jest na liscie? Jaką ma nazwę?
```
sudo docker ps
```

3.  Drugi kontener
```
sudo docker run -it busybox
```

4. Wyświetl listę działających kontenerów. Czy kontener busybox jest na liscie? Jaką ma nazwę?
```
sudo docker ps
```

5. Wyświetl wszystkie kontenery 
```
sudo docker ps -a
```

6. Trzeci kontener
```
sudo docker run -it --name ubuntu ubuntu:20.04
```

7. Wejdź do kontenera
```
sudo docker exec -it ubuntu /bin/bas
```
Wykonaj kilka poleceń Linuxowych:
- ls
- ps -ef
- df -h
- cat

8. Uruchom poleceń "la -ls " w kontenerze bez wchodzenia do niego
```
sudo docker exec ubuntu ls -la
```

9. Czwarty kontener
```
sudo docker run --name some-wordpress -d wordpress
```

10. Piąty kontener - wystaw na świat :)
```
sudo docker run --name some-wordpress -d -p 8080:80 wordpress
```

11. 5. Wyświetl wszystkie kontenery 
```
sudo docker ps -a
```

12. Zrestartuj maszynę wirtualną
```
sudo reboot
```

