# Qubit Reuse By Reset Plugin

[![License](https://img.shields.io/github/license/qiskit-community/qiskit-qubit-reuse.svg?)](https://opensource.org/licenses/Apache-2.0) <!--- long-description-skip-begin -->
[![Current Release](https://img.shields.io/github/release/qiskit-community/qiskit-qubit-reuse.svg?logo=Qiskit)](https://github.com/qiskit-community/qiskit-qubit-reuse/releases)
[![Downloads](https://img.shields.io/pypi/dm/qiskit-qubit-reuse.svg)](https://pypi.org/project/qiskit-qubit-reuse/)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/qiskit-qubit-reuse)

This repository contains an experimental transpiler pass called `qubit_reuse` which is executed at the end of the `init` stage of transpilation. This pass is based on: Matthew DeCross et al. "Qubit-reuse compilation with mid-circuit measurement and reset" [arXiv:2210.0.08039v1](https://arxiv.org/abs/2210.08039v1)

### Background

Certain circuits can reduce the number of qubits required to produce results by resetting and re-using existent measured qubits. The order in which certain qubits are chosen is based on their **causal cones** and the order in which they are measured.

#### Causal Cones

Let's say we have qubit a x in a `DAGCircuit`. We can traverse the `DAGCircuit` from the output node of x by checking all its predecessor nodes. When checking every operation node found, if at any point x interacts with other qubits, via a multi-qubit gate, the qubits in that operation are added to a set. From that point we continue evaluating recursively all the predecessor nodes in that multi-qubit interaction and adding all qubits found into the set, until no more predecessor nodes are left. 

When the traversal ends, the set will contain **all the qubits whose interactions affect qubit x**. That is what we call the causal cone of x.

#### Order of Measurement

Qubits are re-arranged based on the length of their causal cones in ascending order, i.e. the first to be re-arranged are those with smaller causal cones. 

Before re-arranging a qubit, we need to check if there are any qubit that have been measured and is available to re-use. If so, we reset it and apply all operations onto its wire. Otherwise, a new qubit is added and the operations are passed on to that wire.

## Installation

This package is available through [PyPI](https://pypi.org/project/qiskit-qubit-reuse/), and can be installed using the command:

```zsh
pip install qiskit-qubit-reuse
```

It can also be installed by cloning this repository:

```zsh
git clone https://github.com/qiskit-community/qiskit-qubit-reuse
```
And then installing locally:

```zsh
pip install ./qiskit-qubit-reuse
```
If you have the proper authentication keys, you can install it remotely by using:

```zsh
pip install git+https://github.com/qiskit-community/qiskit-qubit-reuse
```

## Usage

Once installed, Qiskit is able to detect the `qubit_reuse` plugin via an entry point. All that needs to be done is to specify the init method in your `transpile` call by using `init_method="qubit_reuse"`. Use the following example:

```py3
from qiskit.circuit.random import random_circuit
from qiskit import transpile
from qiskit.providers.fake_provider import GenericBackendV2

qc = random_circuit(16, 4, measure=True)

transpiled_qc = transpile(qc, backend=GenericBackendV2(16), init_method="qubit_reuse")
```

This entry point provides the option with the least amount of qubits. If you want to specifically use the normal or dual circuit, you can specifcy that by using the `qubit_reuse_normal` or the `qubit_reuse_dual` endpoints.

**Warning: This plugin should only be used with circuits that contain measurements.**
