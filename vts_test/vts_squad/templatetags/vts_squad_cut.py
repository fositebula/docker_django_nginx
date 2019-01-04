from django import template
# import re

register = template.Library()

@register.filter(name='my_cut')
def my_cut(v):
    #http://10.0.1.99:8080/jenkins/job/sprdroid9.0_trunk/lastBuild/artifact/GMS/Images/sp9832e_1h10_gofu-userdebug-gms/sp9832e_1h10_gofu-userdebug-gms_SHARKLE_9_LL_SIN.pac.gz
    url_s = v.split('/')
    project = url_s[-1]
    branch = url_s[5]
    if 'sprdroid' not in branch:
        branch = url_s[7]

    # s = v.\
    #     replace('lastBuild/artifact/GMS/Images', '...').\
    #     replace('jenkins/job', '...').\
    #     replace('http://', '')

    return "{} : {}".format(branch, project)

@register.filter
def branch_project(v):
    #http://cmverify.spreadtrum.com:8080/jenkins/job/gerrit_do_verify_sprdroidp/26643//artifact/sps.image/sprdroid9.0_trunk/sp7731e_1h20_native-userdebug-gms.tar.gz
    l = v.split('/')
    try:
        branch = l[9]
        project = l[10].replace('.tar.gz', '')
        return "{}:{}".format(branch, project)
    except:
        return v