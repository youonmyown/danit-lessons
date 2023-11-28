## ELK Stack local machine logging

This repository was used as a basis:
https://github.com/deviantony/docker-elk/

First we need to clone the repository:
```
git clone https://github.com/deviantony/docker-elk.git

cd docker-elk/
```

Then, initialize the Elasticsearch users and groups required by docker-elk by executing the command:
```
docker-compose up setup
```
If everything went well and the setup completed without error, start the other stack components:
```
docker compose up
```
If everything starts without errors, we can execute `docker compose down` and go to the settings:
