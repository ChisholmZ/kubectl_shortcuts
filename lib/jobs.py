import requests, re, jenkins

class Jobs():
    def __init__(self, jenkins_user, jenkins_token, jenkins_domain):
        self.server = jenkins.Jenkins(jenkins_domain, username=jenkins_user, password=jenkins_token)

    #create jenkins job base on existing job
    def create_job(args, jenkins_url):
        xml = requests.get("http://%s/job/TelematicsHub-%s/job/telhub-ps-heartbeat-adapter/config.xml" % (jenkins_url, args.context))
        data = re.sub(r'(ps-)?heartbeat-(ps-)?adapter', args.job, xml.content.decode('utf-8')).encode('utf-8')
        response = requests.post("http://%s/job/TelematicsHub-%s/createItem?name=telhub-%s" % (jenkins_url, args.context, args.job), data=data, headers={"Content-Type":"application/xml"})
        print(response)

    def get_jobs():
        return self.server.get_jobs()
