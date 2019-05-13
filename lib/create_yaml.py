
import oyaml as yaml, json, io, os, subprocess, sys, re
from collections import OrderedDict

def get_services():
    with open(os.path.join(sys.path[0],'lib','telhub.json')) as file:
        services = json.loads(file.read())
    return services.items()

def build_yaml(args):
    yaml = {}
    for repo, service in get_services():
        url = "git@github.com:schneidertech/telematics-hub-%s" % repo
        cmd = "git ls-remote %s refs/heads/master | awk '{ print $1}'" % url
        commit = subprocess.run(cmd, stdout=subprocess.PIPE, shell=True).stdout.decode('utf-8')
        sep = '_' if re.match(r'devops|migrations', service) else '-'
        service = 'telhub%s%s' % (sep, service)
        yaml.update({service: {'commit': commit.strip()}})
        if service == 'telhub_devops':
            yaml[service].update({'run_config': True, 'wait': 1})
    return {'jobs': yaml}

def create_yaml(args):
    path = os.path.join(sys.path[0],'deployments','%s.yaml' % args.release)
    with open(path, 'w') as outfile:
        yaml.dump(build_yaml(args), outfile, default_flow_style=False)
