A docker based local environment

## Setup

Clone repo with the submodules:

```bash
git clone --recursive https://github.com/argosp/argos.git
```

Go inside folder

```bash
cd argos
```

Unlike large projects, this one has only one environment. The ci/cd is triggered only by merging to master branch.
That's why you need always get the latest code for each submodule from *master* branch

```bash
cd trialdash && git checkout master && git pull origin master && cd -
cd trialgraph && git checkout master && git pull origin master && cd -
```

Create an `.env` file this contents:
```
PROJECT_NAME=argos
GRAPH_PORT=8888
GRAPH_DEBUG_PORT=9229
ROOT_URI=https://root.new-aks-stage.linnovate.net
DASHBOARD_PORT=3000
```

Note: REACT_APP_PORT on trialdash/.env need to sync with DASHBOARD_PORT on argos/.env

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
