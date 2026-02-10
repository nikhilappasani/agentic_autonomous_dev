class Stakeholder:
    def __init__(self, name: str, role: str, expectations: str):
        """
        Initialize a Stakeholder object.

        :param name: Name of the stakeholder.
        :param role: Role of the stakeholder in the project.
        :param expectations: Expectations of the stakeholder from the project.
        """
        self.name = name
        self.role = role
        self.expectations = expectations

    def __repr__(self) -> str:
        return f"Stakeholder(name={self.name}, role={self.role}, expectations={self.expectations})"


class UseCase:
    def __init__(self, title: str, scenario: str, expected_outcome: str):
        """
        Initialize a UseCase object.

        :param title: Title of the use case.
        :param scenario: Detailed scenario of the use case.
        :param expected_outcome: Expected outcome of the use case.
        """
        self.title = title
        self.scenario = scenario
        self.expected_outcome = expected_outcome

    def __repr__(self) -> str:
        return f"UseCase(title={self.title}, scenario={self.scenario}, expected_outcome={self.expected_outcome})"


class Requirement:
    def __init__(self, description: str, priority: int, is_validated: bool = False):
        """
        Initialize a Requirement object.

        :param description: Description of the requirement.
        :param priority: Priority of the requirement (1-5, 1 being highest).
        :param is_validated: Whether the requirement is validated with stakeholders.
        """
        self.description = description
        self.priority = priority
        self.is_validated = is_validated

    def validate(self):
        """
        Validate the requirement with stakeholders.
        """
        self.is_validated = True

    def __repr__(self) -> str:
        return f"Requirement(description={self.description}, priority={self.priority}, is_validated={self.is_validated})"


class SystemComponent:
    def __init__(self, name: str, interactions: list[str]):
        """
        Initialize a SystemComponent object.

        :param name: Name of the system component.
        :param interactions: List of interactions with other components.
        """
        self.name = name
        self.interactions = interactions

    def __repr__(self) -> str:
        return f"SystemComponent(name={self.name}, interactions={self.interactions})"


class TechnologyStack:
    def __init__(self, languages: list[str], frameworks: list[str], tools: list[str]):
        """
        Initialize a TechnologyStack object.

        :param languages: List of programming languages.
        :param frameworks: List of frameworks.
        :param tools: List of development tools.
        """
        self.languages = languages
        self.frameworks = frameworks
        self.tools = tools

    def __repr__(self) -> str:
        return f"TechnologyStack(languages={self.languages}, frameworks={self.frameworks}, tools={self.tools})"


class DataEntity:
    def __init__(self, name: str, relationships: dict[str, str]):
        """
        Initialize a DataEntity object.

        :param name: Name of the data entity.
        :param relationships: Dictionary of relationships with other entities.
        """
        self.name = name
        self.relationships = relationships

    def __repr__(self) -> str:
        return f"DataEntity(name={self.name}, relationships={self.relationships})"


class EnvironmentSetup:
    def __init__(self, version_control: str, ci_cd_pipeline: str, infrastructure: str):
        """
        Initialize an EnvironmentSetup object.

        :param version_control: Version control system used.
        :param ci_cd_pipeline: CI/CD pipeline configuration.
        :param infrastructure: Development and testing infrastructure details.
        """
        self.version_control = version_control
        self.ci_cd_pipeline = ci_cd_pipeline
        self.infrastructure = infrastructure

    def __repr__(self) -> str:
        return f"EnvironmentSetup(version_control={self.version_control}, ci_cd_pipeline={self.ci_cd_pipeline}, infrastructure={self.infrastructure})"


class Component:
    def __init__(self, name: str, functionality: str):
        """
        Initialize a Component object.

        :param name: Name of the component.
        :param functionality: Core functionality of the component.
        """
        self.name = name
        self.functionality = functionality

    def __repr__(self) -> str:
        return f"Component(name={self.name}, functionality={self.functionality})"


class Deployment:
    def __init__(self, process: str, monitoring: str, training_support: str):
        """
        Initialize a Deployment object.

        :param process: Deployment process details.
        :param monitoring: Post-deployment monitoring strategy.
        :param training_support: Training and support provided to users.
        """
        self.process = process
        self.monitoring = monitoring
        self.training_support = training_support

    def __repr__(self) -> str:
        return f"Deployment(process={self.process}, monitoring={self.monitoring}, training_support={self.training_support})"


class Maintenance:
    def __init__(self, schedule: str, support_system: str, performance_monitoring: str):
        """
        Initialize a Maintenance object.

        :param schedule: Maintenance schedule for updates and patches.
        :param support_system: Support system for user queries and issues.
        :param performance_monitoring: Continuous performance monitoring strategy.
        """
        self.schedule = schedule
        self.support_system = support_system
        self.performance_monitoring = performance_monitoring

    def __repr__(self) -> str:
        return f"Maintenance(schedule={self.schedule}, support_system={self.support_system}, performance_monitoring={self.performance_monitoring})"
