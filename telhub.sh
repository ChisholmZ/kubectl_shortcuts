#!/bin/sh
# telehub repo list
#~zach

declare -A SKIP
SKIP[common-package]='common-package'
SKIP[rabbit]='rabbit'
SKIP[telhub-db]='telhub-db'
SKIP[alpine-sqs]='alpine-sqs'
SKIP[elasticmq]='elasticmq'
SKIP[jenkins]='jenkins'
SKIP[messages-router]='router'
SKIP[orion]='orion'

declare -A REPO_SERVICE
REPO_SERVICE[common-package]='common-package'
REPO_SERVICE[inbound-api]='inbound-messages-api'
REPO_SERVICE[migrations]='migrations'
REPO_SERVICE[rods-adapter]='rods-ps-adapter'
REPO_SERVICE[ps-heartbeat-adapter]='heartbeat-ps-adapter'
REPO_SERVICE[pay-file-generator]='pay-file-generator'
REPO_SERVICE[ps-driver-adapter]='driver-update-ps-adapter'
REPO_SERVICE[ps-fuel-event-adapter]='fuel-event-ps-adapter'
REPO_SERVICE[ps-critical-event-adapter]='critical-event-ps-adapter'
REPO_SERVICE[ps-performance-monitor-adapter]='performance-monitor-ps-adapter'
REPO_SERVICE[inbound-message-vehicle-maintenance-fault-adapter]='vehicle-fault-ps-adapter'
REPO_SERVICE[hos-timers-api]='hos-timer-api'
REPO_SERVICE[ps-hos-events-adapter]='hos-timer-ps-adapter'
REPO_SERVICE[ps-device-adapter]='device-update-ps-adapter'
REPO_SERVICE[ps-driver-parameter-group-adapter]='driver-parm-update-ps-adapter'
REPO_SERVICE[ps-equipment-adapter]='equipment-update-ps-adapter'
REPO_SERVICE[ps-pay-adapter]='pay-file-adapter'
REPO_SERVICE[rabbitmq]='rabbitmq'
REPO_SERVICE[telhub-db]='telhub-db'
REPO_SERVICE[alpine-sqs]='alpine-sqs'
REPO_SERVICE[elasticmq]='elasticmq'
REPO_SERVICE[orion-equipment-adapter]='orion-equipment-adapter'
REPO_SERVICE[orion-driver-adapter]='orion-driver-adapter'
REPO_SERVICE[orion-driver-parameter-group-adapter]='orion-driver-parameter-group-adapter'
REPO_SERVICE[router]='messages-router'
REPO_SERVICE[purge-service]='purge-service'
REPO_SERVICE[heartbeat-xml-service]='heartbeat-xml-service'
REPO_SERVICE[fuel-event-xml-service]='fuel-event-xml-service'
REPO_SERVICE[critical-event-xml-service]='critical-event-xml-service'
REPO_SERVICE[vehicle-faults-xml-service]='vehicle-faults-xml-service'
REPO_SERVICE[performace-monitor-xml-service]='performace-monitor-xml-service'
REPO_SERVICE[geofence-api]='geofence-api'
REPO_SERVICE[jenkins]='jenkins'
REPO_SERVICE[geofence-migration-service]='geofence-migration-service'
REPO_SERVICE[orion]='orion'
REPO_SERVICE[schneider-forms-service-dev-ops]='schneider-forms-service'

getDir(){
    FULL=$(pwd)
    DIR=$(basename "$FULL")
    DIR=$(echo $DIR | sed "s/telematics-hub-//g")
    echo $DIR
}

getServiceName(){
    DIR=$(getDir)
    echo ${REPO_SERVICE[$DIR]}
}

getPod(){
    SERVICE_NAME=$(getServiceName)
    echo $(kubectl get pods | grep $SERVICE_NAME | awk '{print $1}')
}

getCon(){
    DIR=$(getDir)
    echo $(docker ps -aqf "ancestor=${DIR}")
}
