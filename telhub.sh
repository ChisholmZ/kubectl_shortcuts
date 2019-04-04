#!/bin/sh
# telehub repo list
#~zach

REPO[0]='common-package'
REPO[1]='inbound-api'
REPO[2]='migrations'
REPO[3]='rods-adapter'
REPO[4]='ps-heartbeat-adapter'
REPO[5]='pay-file-generator'
REPO[6]='ps-driver-adapter'
REPO[7]='ps-fuel-event-adapter'
REPO[8]='ps-critical-event-adapter'
REPO[9]='ps-performance-monitor-adapter'
REPO[10]='inbound-message-vehicle-maintenance-fault-adapter'
REPO[11]='hos-timers-api'
REPO[12]='ps-hos-events-adapter'
REPO[13]='ps-device-adapter'
REPO[14]='ps-driver-parameter-group-adapter'
REPO[15]='ps-equipment-adapter'
REPO[16]='ps-pay-adapter'
REPO[17]='rabbit'
REPO[18]='telhub-db'
REPO[19]='alpine-sqs'
REPO[20]='orion-equipment-adapter'
REPO[21]='orion-driver-adapter'
REPO[22]='orion-driver-parameter-group-adapter'
REPO[23]='router'

SERVICE[1]='inbound-messages-api'
SERVICE[2]='migrations'
SERVICE[3]='rods-ps-adapter'
SERVICE[4]='heartbeat-ps-adapter'
SERVICE[5]='pay-file-generator'
SERVICE[6]='driver-update-ps-adapter'
SERVICE[7]='fuel-event-ps-adapter'
SERVICE[8]='critical-event-ps-adapter'
SERVICE[9]='performance-monitor-ps-adapter'
SERVICE[10]='vehicle-fault-ps-adapter'
SERVICE[11]='hos-timer-api'
SERVICE[12]='hos-timer-ps-adapter'
SERVICE[13]='device-update-ps-adapter'
SERVICE[14]='driver-parm-update-ps-adapter'
SERVICE[15]='equipment-update-ps-adapter'
SERVICE[16]='pay-file-adapter'
SERVICE[17]='rabbit'
SERVICE[18]='telhub-db'
SERVICE[19]='alpine-sqs'
SERVICE[20]='orion-equipment-adapter'
SERVICE[21]='orion-driver-adapter'
SERVICE[22]='orion-driver-parameter-group-adapter'
SERVICE[23]='messages-router'
