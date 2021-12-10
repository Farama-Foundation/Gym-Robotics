import os.path
import sys

from setuptools import find_packages, setup

# Don't import gym_robotics module here, since deps may not be installed
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "gym_robotics"))
from version import VERSION

setup(
    name="gym-robotics",
    version=VERSION,
    description="Gym: A universal API for reinforcement learning environments.",
    url="https://github.com/Farama-Foundation/gym-robotics",
    author="Seungjae Ryan Lee",
    author_email="seungjaeryanlee@gmail.com",
    license="",
    packages=[package for package in find_packages() if package.startswith("gym_robotics")],
    zip_safe=False,
    install_requires=[
        "numpy>=1.18.0",
        "cloudpickle>=1.2.0",
        "importlib_metadata>=4.8.1; python_version < '3.8'",
        "mujoco_py>=1.50, <2.0",
    ],
    package_data={
        "gym_robotics": [
            "envs/assets/LICENSE.md",
            "envs/assets/fetch/*.xml",
            "envs/assets/hand/*.xml",
            "envs/assets/stls/fetch/*.stl",
            "envs/assets/stls/hand/*.stl",
            "envs/assets/textures/*.png",
        ]
    },
    tests_require=["pytest", "mock"],
    python_requires=">=3.7",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)