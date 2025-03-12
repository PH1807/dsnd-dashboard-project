from pathlib import Path
from setuptools import setup, find_packages

cwd = Path(__file__).resolve().parent
requirements = (cwd / 'employee_events' / 'requirements.txt').read_text().splitlines()  # Use splitlines() for better handling

setup_args = dict(
    name='employee_events',
    version='0.0',
    description='SQL Query API',
    packages=find_packages(),
    package_data={'employee_events': ['employee_events.db', 'requirements.txt']},  # Specify the package
    install_requires=requirements,  # Corrected from install_requirements to install_requires
)

if __name__ == "__main__":
    setup(**setup_args)
