# Docker WebGUI
Środowiskiem Docker można zarządzać również z użyciem interfejsu graficznego. Jednym takich rozwiązań jest webowa aplikacja Portainer.

## Instalacja
```
sudo docker run -d -p 9000:9000 --name=portainer --restart=unless-stopped -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer-ce
```

