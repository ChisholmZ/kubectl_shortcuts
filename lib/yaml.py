# from github import Github
import oyaml as yaml, json, io, os, subprocess, sys, re
from lib.helper import *

# create dictionary for yaml
def build_yaml(args, github_token):
    services = get_services()
    yaml = {}
    devops = {}
    migrations = {}
    router = {}
    inbound = {}

    for repo in git_repos(github_token):
        if not get_branch(repo, args.release):
            continue

        service = repo.name.replace('telematics-hub-','')
        if re.match(r'dev-ops|common', service):
            continue

        sep = '_' if re.match(r'devops|migrations', service) else '-'
        service = services[service] if service in services.keys() else service
        job = "telhub%s%s" % (sep, get_job(service))
        dict = {job: {'commit': repo.get_branch('master').commit.sha, 'branch': args.release}}

        if service == 'devops':
            devops = dict
            devops[job].update({'run_config': True, 'wait': 1})
        elif service == 'migrations':
            migrations = dict
        elif service == 'messages-router':
            router = dict
        elif service == 'inbound-messages-api':
            inbound = dict
        else:
            yaml.update(dict)

    if job:
        yaml[job].update({'wait': 1})

    return {'jobs': {**devops, **migrations, **router, **inbound, **yaml}}

# build the yaml for jenkins to deploy from
def create_yaml(args, github_token):
    path = os.path.join(sys.path[0],'deployments','%s.yaml' % args.release)
    with open(path, 'w') as outfile:
        yaml.dump(build_yaml(args, github_token), outfile, default_flow_style=False)
