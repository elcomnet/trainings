# Wolumeny
Ćwiczenie pokaże w jaki sposób zamontować do kontenera zewnętrzny katalog lub wolumen

1. 1. Utwórz katalog z zawartością strony www
```
sudo mkdir /strona
cp ~/docker-training/Lab\ 7/web/ /strona
```

2. Zamontuj katalog /strona do kontenera ubuntu
```
sudo docker run -v /strona/:/foo/ -w /foo -i -t --name ubuntu ubuntu bash
```

3. Sprawdź czy w kontenerze widać plik index.html
```
sudo docker exec ubuntu cat /foo/index.html'
```

4. Uruchom kontener httpd z zamontowaną zewnętrznym katalogiem zawierającym plik index.html
```
sudo docker run -dit --name web3 -v /strona:/usr/local/apache2/htdocs -p 8087:80 httpd:2.4
```

5. Wyświetl stronę w przeglądarce

6. Utwórz wolumen o nazwie training
```
sudo docker volume create training
```

7. Wyświetl listę wolumenów
```
sudo docker volume ls
```

8. Wyświetl właściwości wolumenu "training" a szczególnie znajdź punkt montowania
```
sudo docker volume inspect training
```

7. Zamontuj wolumen do kontenera ubuntu
```
sudo docker run -v training/:/foo/ -w /foo --name ubuntu2 -i -t ubuntu bash
```

8. Utwórz plik "test1" w konterze "foo"
```
sudo docker exec ubuntu2 echo "test1234" > /foo/test1'
```

9. Sprawdź co widać w katalogu z punktem montowania
```
cd /var/lib/docker/volumes/.....
```
