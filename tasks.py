"""
SAM celery instance
"""

from __future__ import absolute_import
import os
from os.path import dirname, abspath
import sys
from celery import Celery
import logging
import redis
import json


logging.getLogger('celery.task.default').setLevel(logging.DEBUG)
logging.getLogger().setLevel(logging.DEBUG)

# This is where the above should be removed, and instead
# the set_environment.py module could be ran to set env vars
# from the config/ env vars files.
# BUT, can the module be accessed from the parent dir???
# from qed_cts.set_environment import DeployEnv
from temp_config.set_environment import DeployEnv
runtime_env = DeployEnv()
runtime_env.load_deployment_environment()

from models.sam import sam_exe as sam
from tools.sam import rest_validation, rest_model_caller

# from django.conf import settings
# settings.configure()
if not os.environ.get('DJANGO_SETTINGS_FILE'):
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'qed_ubertool.settings_outside')
else:
    # os.environ.setdefault('DJANGO_SETTINGS_MODULE', '.' + os.environ.get('DJANGO_SETTINGS_FILE'))
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')

REDIS_HOSTNAME = os.environ.get('REDIS_HOSTNAME')

if not os.environ.get('REDIS_HOSTNAME'):
    os.environ.setdefault('REDIS_HOSTNAME', 'localhost')
    REDIS_HOSTNAME = os.environ.get('REDIS_HOSTNAME')

logging.info("REDIS HOSTNAME: {}".format(REDIS_HOSTNAME))

app = Celery('tasks',
             broker='redis://{}:6379/0'.format(REDIS_HOSTNAME),
             backend='redis://{}:6379/0'.format(REDIS_HOSTNAME)
             )

app.conf.update(
    CELERY_ACCEPT_CONTENT=['json'],
    CELERY_TASK_SERIALIZER='json',
    CELERY_RESULT_SERIALIZE='json',
)


@app.task
def samTask(request_post):
    logging.info("celery worker consuming sam task")
    request_json = json.dumps(request_post)
    inputs = rest_validation.parse_inputs(request_json)
    jobID = request_post["token"]       # TODO: Change to appropriate ID key
    if inputs:
        return rest_model_caller.model_run("sam", jobID, inputs, module=sam)
    else:
        return rest_model_caller.error("sam", jobID, inputs)
