# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.test import BaseTestCase


class TestResultsController(BaseTestCase):
    """ResultsController integration test stubs"""

    def test_results_scenario_id_subgoal_id_thread_id_get(self):
        """Test case for results_scenario_id_subgoal_id_thread_id_get

        Get the results of a thread
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1.3.0/results/{scenario_id}/{subgoal_id}/{thread_id}'.format(scenario_id='scenario_id_example', subgoal_id='subgoal_id_example', thread_id='thread_id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
