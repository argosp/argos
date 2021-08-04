A docker based local environment

## Setup

Clone repo with the submodules:

```bash
git clone --recursive git@github.com:argosp/argos.git
```

Go inside folder

```bash
cd argos
```

Copy configuration template and edit if needed

```bash
cp .env.example .env
```

Build the docker images

```bash
docker-compose build
```

Run the project

```bash
docker-compose up -d
```
Dev enviroment:  
https://argos.new-aks-stage.linnovate.net/


need add argos.new-aks-stage.linnovate.net to /etc/hosts 

127.0.0.1 argos.new-aks-stage.linnovate.net

web ports:
 - http://argos.new-aks-stage.linnovate.net:8080  
 - https://argos.new-aks-stage.linnovate.net:4433 
