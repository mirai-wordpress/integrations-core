# (C) Datadog, Inc. 2020-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)
import os

from datadog_checks.utils.common import get_docker_hostname

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))

CHECK_NAME = 'rethinkdb'

IMAGE = 'rethinkdb:2.4.0'
CONTAINER_NAME = 'rethinkdb'
SERVER_NAME = 'server0'

HOST = get_docker_hostname()
PORT = 28015