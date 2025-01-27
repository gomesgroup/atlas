""" Atlas: A Brain for Self-driving Laboratories
"""

from setuptools import find_packages, setup

import versioneer


def readme():
    with open("README.md") as f:
        return f.read()


# -----
# Setup
# -----
setup(
    name="matter-atlas",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description="some description",
    long_description=readme(),
    classifiers=[
        "Programming Language :: Python",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering",
    ],
    url="https://github.com/rileyhickman/atlas",
    author="Riley Hickman",
    author_email="riley.hickman@mail.utoronto.ca",
    license="MIT",
    packages=find_packages(where="src", include=["atlas*"]),
    package_dir={"": "src"},
    zip_safe=False,
    tests_require=["pytest"],
    install_requires=[
        "numpy",
        "pandas",
        "rich",
        "deap",
        "pymoo",
        "sobol-seq",
        "pyDOE",
        "botorch==0.8.5",
        "matter-chimera",
        # "matter-golem @ git+https://github.com/gomesgroup/golem",
    ],
    python_requires=">=3.6",
)
