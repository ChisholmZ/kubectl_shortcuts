import requests, re, jenkins
from lib.helper import *

class Jobs():
    def __init__(self, config, context):
        url = 'http://%s/job/TelematicsHub-%s' % (config['domain'], context)
        self.server = jenkins.Jenkins(url, username=config['user'], password=config['token'])
        path = os.path.join(sys.path[0],'files','job_%s.xml' % context.lower())
        if os.path.isfile(path):
            self.xml = open(path, 'r').read()
        self.context = context

    # create jenkins job base on existing job
    def create_job(self, job):
        xml = self.update_xml(job)
        self.server.create_job(job, xml)

    # build jenkins job
    def build_job(self, job, params = {}):
        self.server.build_job(job, params)

    # get jenkins jobs
    def get_jobs(self):
        return self.server.get_jobs(folder_depth=0)

    # update the jenkins xml
    def update_xml(self, job):
        job = re.sub(r'telhub[-_]', '', job)
        service = get_service(job)
        repo = get_repo(job)
        return self.xml.replace('#JOB#', job).replace('#SERVICE#', service).replace('#REPO#', repo)

    # update job
    def update_job(self, job):
        xml = self.update_xml(job)
        self.server.reconfig_job(job, xml)

    # update all the jobs
    def update_jobs(self):
        for job in self.get_jobs():
            if re.match(r'^hudson\.model', job['_class']) and job['name'] != 'telhub_devops':
                update_job(job['name'])

    def save_config(self):
        xml = self.server.get_job_config('telhub-heartbeat-ps-adapter')
        xml = xml.replace('ps-heartbeat-adapter<','#JOB#<')
        xml = xml.replace('=heartbeat-ps-adapter', '=#SERVICE#')
        xml = xml.replace('ps-heartbeat-adapter.git','#REPO#.git')
        path = os.path.join(sys.path[0],'files','job_%s.xml' % self.context.lower())
        open(path, 'w').write(xml)

    def select_job(self):
        print('TODO:')
        # choices = {}
        # for job in self.get_jobs():
        #     choices.update(job['name'])
        #
        # answers = whaaaaat.prompt(questions)
        # whaaaaat.print_json(answers)
