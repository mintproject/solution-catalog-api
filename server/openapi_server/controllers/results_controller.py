import asyncio

import connexion
import six

from mint_firebase.mint_results import fetch_mint_thread_not_download
from openapi_server import mint_fetch_config


def results_scenario_id_subgoal_id_thread_id_get(scenario_id, subgoal_id, thread_id):  # noqa: E501
    """Get the results of a thread

    Gets the details of a single instance of a results # noqa: E501

    :param scenario_id: The ID of the scenario
    :type scenario_id: str
    :param subgoal_id: The ID of the subgoal
    :type subgoal_id: str
    :param thread_id: The ID of the thread
    :type thread_id: str

    :rtype: object
    """
    outputs = asyncio.run(fetch_mint_thread_not_download(scenario_id, subgoal_id, thread_id, mint_fetch_config))

    return outputs
