#!/usr/bin/env python3

import argparse
from kubernetes import client, config

parser = argparse.ArgumentParser()
parser.add_argument('-a', help='get pods all namespaces', action='store_true')
args = parser.parse_args()


contexts, active_context = config.list_kube_config_contexts()


config.load_kube_config()

v1 = client.CoreV1Api(api_client=config.new_client_from_config())

if args.a:
    ret = v1.list_pod_for_all_namespaces(watch=False)
    for i in ret.items:
        if active_context['name'] == i.metadata.namespace:
            print(i.status)
            exit()
            # print(f"{i.metadata.name} \t{i.status.phase}")