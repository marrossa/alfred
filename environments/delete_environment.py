import sys
import os
import json
import configparser
from watson_developer_cloud import DiscoveryV1

# Loads the config file to read the configuration variables
config = configparser.ConfigParser()
config.read('../config.file')

discovery = DiscoveryV1(
  username = config['watson']['username'],
  password = config['watson']['password'],
  version = config['watson']['version']
)

del_env = discovery.delete_environment('386aca79-3773-4409-a3a6-303c8b8c9ed7')
print(json.dumps(del_env, indent=2))
