import yaml, io, os, requests, sys, time
from datetime import datetime

def run(args, jenkins_url):
    ## read in yaml
    with io.open(args.yaml, 'r') as stream:
        data_loaded = yaml.safe_load(stream)

    ## send jobs
    for job, params in data_loaded['jobs'].items():
        build = 'buildWithParameters' if job == 'telhub_devops' or args.context != 'Dev' else 'build'
        url = 'http://%s/job/TelematicsHub-%s/job/%s/%s' % (jenkins_url, args.context, job, build)
        params.update({'token' : job})
        if args.test :
            print(job, url, params, datetime.now(), '\n', sep='\n')
        else:
            response = requests.post(url, params)
            print(job, params, response, datetime.now(), '\n', sep='\n')
        time.sleep(params.get('wait') or args.seconds)
