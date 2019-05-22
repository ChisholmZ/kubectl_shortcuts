from github import Github
import oyaml as yaml, json, io, os, subprocess, sys, re

def choose_jobs(jobs):
    for job in jobs:
        print(job)

# get services from json to fix names of repos
def get_services():
    with open(os.path.join(sys.path[0],'lib','telhub.json')) as file:
        services = json.loads(file.read())
    return services

def get_service(service):
    service = re.sub(r'(telematics-hub|telhub)[-_]', '', service)
    services = get_services()
    return services[service] if service in services.keys() else service
