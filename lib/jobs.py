import requests, re

def create_job(args, jenkins_url):

    xml = requests.get("http://%s/job/TelematicsHub-%s/job/telhub-ps-heartbeat-adapter/config.xml" % (jenkins_url, args.context))

    data = re.sub(r'(ps-)?heartbeat-(ps-)?adapter', args.job, xml.content.decode('utf-8')).encode('utf-8')

    response = requests.post("http://%s/job/TelematicsHub-%s/createItem?name=%s" % (jenkins_url, args.context, args.job), data=data, headers={"Content-Type":"application/xml"})
    print(response)