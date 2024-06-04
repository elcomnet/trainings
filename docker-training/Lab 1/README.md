# Konfiguracja serwera
Ćwiczenia będa wykonywane na maszynie wirtualnej z systemem Ubuntu.

### Instalacja Docker
```
sudo apt-get update
sudo apt-get install docker docker-compose -y
sudo apt-get install npm -y
```
Sprawdź czy Docker działa
```
sudo docker version
```
![Docker Version](img/lab1_1.png)

### Pobranie Lab-ów na maszynę wirtualną

```
sudo git clone https://github.com/elcomnet/docker-training.git
```

### Alternatywna Instalacja Docker
```
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --batch --yes --dearmor -o /etc/apt/keyrings/docker.gpg
sudo echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
sudo apt-get install docker docker-compose -y
sudo apt-get install npm -y
```
