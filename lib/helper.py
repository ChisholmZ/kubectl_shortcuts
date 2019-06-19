from github import Github
import oyaml as yaml, json, io, os, subprocess, sys, re, webbrowser

# get repos from github api
def git_repos(github_token):
    return Github(github_token).search_repositories(query='telematics hub user:schneidertech')

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

def get_jobs():
    return get_json()['jobs']

def get_job(service):
    job = re.sub(r'(telematics-hub|telhub)[-_]', '', service)
    jobs = get_jobs()
    return jobs[job] if job in jobs.keys() else job

def get_service(service):
    service = re.sub(r'(telematics-hub|telhub)[-_]', '', service)
    services = get_services()
    return services[service] if service in services.keys() else service

def get_service_from_job(job):
    job = re.sub(r'(telematics-hub|telhub)[-_]', '', job)
    service = [k for k,v in get_services().items() if v == job]
    return service[0] if len(service) else job

# github jobs
def git_jobs(github_token):
    services = get_services()
    for repo in git_repos(github_token):
        service = repo.name.replace('telematics-hub-','')
        if service not in services:
            services.update({service: service})
    return services

# loop through branchs to see if it exists
def get_branch(repo, release):
    for branch in repo.get_branches():
        if release == branch.name:
            return True
    return False

def pull_request(args, github_token):
    for repo in git_repos(github_token):
        if get_branch(repo, args.release):
            pull_to = args.pull if args.pull == 'master' else args.release
            pull_from = args.release if args.pull == 'master' else args.pull
            url = "%s/compare/%s...%s" % (repo.html_url, pull_to, pull_from)
            webbrowser.open_new_tab(url)
