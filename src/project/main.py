import sys
import warnings

from project.crew import Project

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def run():
    """
    Run the crew.
    """
    inputs = {
        'requirements': "A calculator with all available mathematical operations",
        'module_name': 'calculator',
        'class_name': 'Calculator'
    }

    try:
        Project().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")
