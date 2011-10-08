# vim: ft=python

from os import environ

# path to config file
environ['WEBSSHKEY_HELPER_CONFIG'] = '/var/lib/web-sshkey-helper/config.py'


activate_py = '/var/lib/web-sshkey-helper/env/bin/activate_this.py'
execfile(activate_py, dict(__file__=activate_py))

# or

#import site
#site.addsitedir("/var/lib/web-sshkey-helper/env/lib/pythonX.X/site-packages")


from websshkey.app import app as application
