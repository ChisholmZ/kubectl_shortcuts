import yaml, io, os, sys, time
from datetime import datetime

def run(args, jobs):
    if not os.path.isfile(args.yaml):
        return "file doesn't exist"

    ## read in yaml
    with io.open(args.yaml, 'r') as stream:
        data_loaded = yaml.safe_load(stream)

    ## send jobs
    for job, params in data_loaded['jobs'].items():
        params.update({'token' : job})
        if not args.test:
            jobs.build_job(job, params)
        print(job, params, datetime.now(), '\n', sep='\n')
        time.sleep(params.get('wait') or args.seconds)

    return 'done'
