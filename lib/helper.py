from github import Github
import oyaml as yaml, json, io, os, subprocess, sys, re

def choose_jobs(jobs):
    for job in jobs:
        print(job)

# get json
def get_json():
    with open(os.path.join(sys.path[0],'files','telhub.json')) as file:
        data = json.loads(file.read())
    return data

# get services from json to fix names
def get_services():
    return get_json()['services']

# get repo from json
def get_repos():
    return get_json()['repos']

def get_repo(job):
    job = re.sub(r'(telematics-hub|telhub)[-_]', '', job)
    repos = get_repos()
    return repos[job] if job in repos.keys() else get_service_from_job(job)

def get_service(service):
    service = re.sub(r'(telematics-hub|telhub)[-_]', '', service)
    services = get_services()
    return services[service] if service in services.keys() else service

def get_service_from_job(job):
    job = re.sub(r'(telematics-hub|telhub)[-_]', '', job)
    service = [k for k,v in get_services().items() if v == job]
    return service[0] if len(service) else job
