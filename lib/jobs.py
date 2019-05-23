import requests, re, jenkins
from lib.helper import *

class Jobs():
    def __init__(self, jenkins, context):
        url = 'http://%s/job/TelematicsHub-%s' % (jenkins['domain'], context)
        self.server = jenkins.Jenkins(url, username=jenkins['user'], password=jenkins['token'])

    #create jenkins job base on existing job
    def create_job(self, job):
        xml = self.update_xml(job)
        self.server.create_job(job, xml)

    def build(self, job, params = {}):
        self.server.build_job(job, params)

    def get_jobs(self):
        return self.server.get_jobs(folder_depth=0)

    def update_xml(self, job):
        service = get_service(job)
        job = re.sub(r'telhub[-_]', '', job)
        heartbeat = self.server.get_job_config('telhub-ps-heartbeat-adapter')
        return heartbeat.replace('ps-heartbeat-adapter', job).replace('heartbeat-ps-adapter', service)

    def update_jobs(self):
        for job in self.get_jobs():
            if re.match(r'^hudson\.model', job['_class']) and job['name'] != 'telhub_devops':
                print(job['name'])
                xml = self.update_xml(job['name'])
                self.server.reconfig_job(job['name'], xml)

    # def select_job(self):
    #     choices = []
    #     for job in self.get_jobs():
    #         choices.update(job['name'])
    #
    #     jobs = [
    #         inquirer.List('job',
    #                       message="Which job",
    #                       choices=choices,
    #                   ),
    #     ]
    #
    #     return inquirer.prompt(jobs)
