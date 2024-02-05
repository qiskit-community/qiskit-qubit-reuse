# This code is part of Qiskit.
#
# (C) Copyright IBM 2017.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

"""The Qiskit Qubit Reuse setup file."""

import os
import re
from setuptools import setup, find_packages


with open("requirements.txt") as f:
    REQUIREMENTS = f.read().splitlines()

# Read long description from README.
README_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), "README.md")
with open(README_PATH) as readme_file:
    README = re.sub(
        "<!--- long-description-skip-begin -->.*<!--- long-description-skip-end -->",
        "",
        readme_file.read(),
        flags=re.S | re.M,
    )

setup(
    name="qiskit-qubit-reuse",
    version="0.0.2",
    description="A Qiskit's compiler plugin to reuse qubits using midcircuit measurement",
    long_description=README,
    long_description_content_type="text/markdown",
    author="Raynel Sanchez and Danielle Odigie",
    license="Apache 2.0",
    classifiers=[
        "Environment :: Console",
        "License :: OSI Approved :: Apache Software License",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering",
    ],
    keywords="qiskit sdk quantum",
    packages=find_packages(exclude=["test*"]),
    install_requires=REQUIREMENTS,
    include_package_data=True,
    python_requires=">=3.8",
    zip_safe=False,
    entry_points={
        "qiskit.transpiler.init": [
            "qubit_reuse = qiskit_qubit_reuse.plugin:QubitReusePluginDefault",
            "qubit_reuse_normal = qiskit_qubit_reuse.plugin:QubitReusePluginNormal",
            "qubit_reuse_dual = qiskit_qubit_reuse.plugin:QubitReusePluginDual",
        ],
    },
)
