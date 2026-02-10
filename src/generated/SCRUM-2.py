class Stakeholder:
    """
    Represents a stakeholder in the project.

    Attributes:
        name (str): The name of the stakeholder.
        role (str): The role of the stakeholder in the project.
        expectations (str): The expectations of the stakeholder.
    """
    def __init__(self, name: str, role: str, expectations: str):
        self.name = name
        self.role = role
        self.expectations = expectations


class Requirement:
    """
    Represents a requirement for the project.

    Attributes:
        description (str): The description of the requirement.
        priority (int): The priority of the requirement.
        type (str): The type of the requirement (functional or non-functional).
    """
    def __init__(self, description: str, priority: int, req_type: str):
        self.description = description
        self.priority = priority
        self.type = req_type


class SystemComponent:
    """
    Represents a system component in the architecture.

    Attributes:
        name (str): The name of the component.
        interactions (list): The list of interactions with other components.
    """
    def __init__(self, name: str, interactions: list):
        self.name = name
        self.interactions = interactions


class TechnologyStack:
    """
    Represents the technology stack for the system.

    Attributes:
        languages (list): The list of programming languages used.
        databases (list): The list of databases used.
        frameworks (list): The list of frameworks used.
    """
    def __init__(self, languages: list, databases: list, frameworks: list):
        self.languages = languages
        self.databases = databases
        self.frameworks = frameworks


class DataEntity:
    """
    Represents a data entity in the system.

    Attributes:
        name (str): The name of the data entity.
        relationships (list): The list of relationships with other entities.
    """
    def __init__(self, name: str, relationships: list):
        self.name = name
        self.relationships = relationships


class Environment:
    """
    Represents an environment setup for the project.

    Attributes:
        name (str): The name of the environment (development, testing, production).
        version_control (str): The version control system used.
        ci_cd_pipeline (str): The CI/CD pipeline configuration.
    """
    def __init__(self, name: str, version_control: str, ci_cd_pipeline: str):
        self.name = name
        self.version_control = version_control
        self.ci_cd_pipeline = ci_cd_pipeline


class TestCase:
    """
    Represents a test case for the system.

    Attributes:
        description (str): The description of the test case.
        test_type (str): The type of the test (unit, integration, system).
    """
    def __init__(self, description: str, test_type: str):
        self.description = description
        self.test_type = test_type


class Deployment:
    """
    Represents a deployment configuration for the system.

    Attributes:
        environment (Environment): The environment to deploy to.
        status (str): The status of the deployment.
    """
    def __init__(self, environment: Environment, status: str):
        self.environment = environment
        self.status = status


class MonitoringTool:
    """
    Represents a monitoring tool for the system.

    Attributes:
        name (str): The name of the monitoring tool.
        metrics (list): The list of metrics tracked by the tool.
    """
    def __init__(self, name: str, metrics: list):
        self.name = name
        self.metrics = metrics


class Documentation:
    """
    Represents documentation for the system.

    Attributes:
        content (str): The content of the documentation.
        doc_type (str): The type of documentation (architecture, user manual, etc.).
    """
    def __init__(self, content: str, doc_type: str):
        self.content = content
        self.doc_type = doc_type


class TrainingSession:
    """
    Represents a training session for stakeholders and users.

    Attributes:
        topic (str): The topic of the training session.
        audience (list): The list of participants in the training session.
    """
    def __init__(self, topic: str, audience: list):
        self.topic = topic
        self.audience = audience