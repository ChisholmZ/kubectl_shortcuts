# kubectl and docker shortcuts

A few shortcuts for kubectl based on our environment.

To use clone repo and add to your path.

### pod
will give a list of pods to select based on your context.

`pod` will bring up the bash for the pod that you select.

`pod logs` will bring up the logs for the pod that you select.

`pod laravel-logs` will bring up the laravel logs for the pod that you select.

`pod describe` will describe the pod that you select.

`pod k` will ask to change context before selecting pods.

### kontext
will give a list of context to select and set the context base on your choice.


### kg

`kg` shortcut for `kubectl get pods`

`kg a` shortcut for `kubectl get pods --all-namespaces`

`kg s` shortcut for `kubectl get services`

`kg k` will ask to change context, then shortcut for `kubectl get pods`

### hs_config.sh.sample

Copy this to `hs_config.sh` and set the varibles to reflect your local environment.

### config_context

`config_context create` will create a context and namespace based on the `$NAMESPACE` and `$CONTEXT` values in `hs_config.sh`

`config_context` will update the context and namespace based on the `$NAMESPACE` and `$CONTEXT` values in `hs_config.sh`

### thr_clone

`thr_clone` clone all the repos into the current directory

### build_pod

`build_pod` will build a pod from the repo current directory and push to local kubernetes cluster

### build_all

`build_all` will build all of the pods from the repo current directory and push to local kubernetes cluster

## dk
shortcut for docker based on current directory

#### Build the Docker container
`dk build` shortcut for `docker build --tag=CURRENT_DIR`

#### Run Docker container
`dk r` shortcut for `docker run -d -p 4000:80 CURRENT_DIR`

#### Bash into the Docker container
`dk b` shortcut for `docker exec -it CURRENT_CONTAINER //bin/bash`

#### Bash into the Docker container as root
`dk root` shortcut for `docker exec -it --user root CURRENT_CONTAINER //bin/bash`

#### Prune unused docker container
`dk p` shortcut for `docker system prune -f -a`

#### list all docker containers
`dk ls` shortcut for `docker container ls -a`

#### kill docker container based on current directory
`dk kill` shortcut for `docker kill $(docker ps -aqf "ancestor=${DIR}")`

#### kill all docker containers
`dk killall` shortcut for `docker kill $(docker ps -q)`
