from github import Github
import oyaml as yaml, json, io, os, subprocess, sys, re

def get_services():
    with open(os.path.join(sys.path[0],'lib','telhub.json')) as file:
        services = json.loads(file.read())
    return services

def get_repos(github_token):
    return Github(github_token).search_repositories(query='telematics hub user:schneidertech')

def build_yaml(args, github_token):
    services = get_services()
    yaml = {}
    for repo in get_repos(github_token):
        service = repo.name.replace('telematics-hub-','')
        if re.match(r'dev-ops|common', service):
            continue
        sep = '_' if re.match(r'devops|migrations', service) else '-'
        service = services[service] if service in services.keys() else service
        job = "telhub%s%s" % (sep, service)
        dict = {job: {'commit': repo.get_branch('master').commit.sha, 'branch': args.release}}
        if service == 'devops':
            devops = dict
            devops[job].update({'run_config': True, 'wait': 1})
        else:
            yaml.update(dict)
    yaml[job].update({'wait': 1})
    return {'jobs': {**devops, **yaml}}

def create_yaml(args, github_token):
    path = os.path.join(sys.path[0],'deployments','%s.yaml' % args.release)
    with open(path, 'w') as outfile:
        yaml.dump(build_yaml(args, github_token), outfile, default_flow_style=False)
