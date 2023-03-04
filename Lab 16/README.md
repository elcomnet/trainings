# Uruchomienie własnego repozytorium obrazów
Poberane z Docker Hub obrazy czy też buddowane własne obrazy domyślnie zapisywane są w lokalnym repozytorium instancji Docker.
Istnieje możliwość uruchomienia jako kontener własnego centralnego repozytorium obrazów, który będzie mógł służyć do "wystawiania" naszych obrazów klientom.

W tym celu uruchomimy obraz Registry

```
docker run -d -p 5000:5000 --restart always --name registry registry:2
```
