from setuptools import setup
from setuptools import find_packages

VERSION = '1.0.0'
GITHUB_REPOSITORY_URL = "https://github.com/yixinNB/container-cli"

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="container-cli",
    version=VERSION,
    description="✨A non-antihuman way to modify docker's container port mapping✨",
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='yixinNB_github',
    url=GITHUB_REPOSITORY_URL,
    packages=find_packages(exclude=['test']),
    project_urls={
        "Documentation": GITHUB_REPOSITORY_URL,
        "Code": GITHUB_REPOSITORY_URL,
        "Issue tracker": GITHUB_REPOSITORY_URL + "/issues",
    },
    entry_points={
        'console_scripts': [
            'cc = container_cli:main',
            'container_cli = container_cli:main',
        ]
    },
    install_requires=[
        'loguru>=0.7',
        'checkopt>=1',
        'questionary>=2'
    ],
)
