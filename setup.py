"""Setup for concept XBlock."""

from __future__ import absolute_import

import os

from setuptools import setup


def package_data(pkg, root):
    """Generic function to find package_data for `pkg` under `root`."""
    data = []
    for dirname, _, files in os.walk(os.path.join(pkg, root)):
        for fname in files:
            data.append(os.path.relpath(os.path.join(dirname, fname), pkg))

    return {pkg: data}


setup(
    name='concept-xblock',
    version='0.1',
    description='concept XBlock',   # TODO: write a better description.
    packages=[
        'concept',
    ],
    install_requires=[
        'XBlock',
    ],
    entry_points={
        'xblock.v1': [
            'concept = concept:ConceptXBlock',
        ]
    },
    package_data=package_data("concept", "static"),
)
