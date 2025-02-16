from setuptools import setup, find_packages

setup(
    name='assignment2_rl',
    version='0.1',
    description='Reinforcement Learning Assignment 2 for UoT EE569 Deep Learning Course',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'opencv-python',
        'torch',
        'gym',
        'imageio',
        'tensorboard',
    ],
)