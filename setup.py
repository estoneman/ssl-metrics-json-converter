from setuptools import setup

from ssl_metrics_json_converter import version

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="ssl-metrics-json-converter",
    packages=["ssl_metrics_json_converter"],
    version=version.version(),
    description="SSL Metrics - JSON Converter",
    author="Software and Systems Laboratory - Loyola University Chicago",
    author_email="ssl-metrics@ssl.luc.edu",
    license="BSD",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://ssl.cs.luc.edu/projects/metricsDashboard",
    project_urls={
        "Bug Tracker": "https://github.com/SoftwareSystemsLaboratory/ssl-metrics-json-converter/issues",
        "GitHub Repository": "https://github.com/SoftwareSystemsLaboratory/ssl-metrics-json-converter",
    },
    keywords=[
        "bus factor",
        "commits",
        "engineering",
        "git",
        "github",
        "issue density",
        "issues",
        "kloc",
        "loyola",
        "loyola university chicago",
        "luc",
        "mining",
        "metrics",
        "repository",
        "repository mining",
        "simple",
        "software",
        "software engineering",
        "software metrics",
        "software systems laboratory",
        "ssl",
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Software Development",
        "Topic :: Scientific/Engineering",
        "Operating System :: POSIX",
        "Operating System :: Unix",
        "Operating System :: MacOS",
    ],
    python_requires=">=3.9",
    install_requires=["pandas", "progress"],
    entry_points={
        "console_scripts": [
            "ssl-metrics-json-converter = ssl_metrics_json_converter.main:main",
        ]
    },
)
