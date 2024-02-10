# coding: utf-8

"""
    Agent Protocol

    Specification of the API protocol for communication with an agent.

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from agent_protocol_client.api.agent_api import AgentApi


class TestAgentApi(unittest.TestCase):
    """AgentApi unit test stubs"""

    def setUp(self) -> None:
        self.api = AgentApi()

    def tearDown(self) -> None:
        pass

    def test_create_agent_task(self) -> None:
        """Test case for create_agent_task

        Creates a task for the agent.
        """
        pass

    def test_download_agent_task_artifact(self) -> None:
        """Test case for download_agent_task_artifact

        Download a specified artifact.
        """
        pass

    def test_execute_agent_task_step(self) -> None:
        """Test case for execute_agent_task_step

        Execute a step in the specified agent task.
        """
        pass

    def test_get_agent_task(self) -> None:
        """Test case for get_agent_task

        Get details about a specified agent task.
        """
        pass

    def test_get_agent_task_step(self) -> None:
        """Test case for get_agent_task_step

        Get details about a specified task step.
        """
        pass

    def test_list_agent_task_artifacts(self) -> None:
        """Test case for list_agent_task_artifacts

        List all artifacts that have been created for the given task.
        """
        pass

    def test_list_agent_task_steps(self) -> None:
        """Test case for list_agent_task_steps

        List all steps for the specified task.
        """
        pass

    def test_list_agent_tasks(self) -> None:
        """Test case for list_agent_tasks

        List all tasks that have been created for the agent.
        """
        pass

    def test_upload_agent_task_artifacts(self) -> None:
        """Test case for upload_agent_task_artifacts

        Upload an artifact for the specified task.
        """
        pass


if __name__ == "__main__":
    unittest.main()
