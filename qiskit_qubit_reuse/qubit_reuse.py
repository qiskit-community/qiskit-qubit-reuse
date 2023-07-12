# This code is part of Qiskit.
#
# (C) Copyright IBM 2022.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

"""QubitReuse pass to reduce the number of qubits on an QuantumCircuit"""
import logging

from qiskit.transpiler.basepasses import TransformationPass
from .qubit_reuse_greedy import Greedy

logger = logging.getLogger(__name__)


class QubitReuse(TransformationPass):
    """A qubit reuse via midcircuit measurement transformation pass

    Cite paper here
    """

    def __init__(self, target, type="default"):
        """Initialize a ``QubitReuse`` pass instance

        Args:
            target (Target): A target representing the backend device to run ``QubitReuse`` on.
            type (str): A string specifying which method will be used. Defaults to "default".

        **References:**

        [1] Matthew DeCross et al. "Qubit-reuse compilation with mid-circuit measurement and reset"
        `arXiv:2210.0.08039v1 <https://arxiv.org/abs/2210.08039v1>`_
        """
        super().__init__()
        self.target = target
        self.type = type

    def run(self, dag):
        """run the qubit reuse pass method"""
        if self.type == "dual":
            result = Greedy(dag=dag, dual=True)
        elif self.type == "normal":
            result = Greedy(dag)
        else:
            regular = Greedy(dag=dag)
            dual = Greedy(dag=dag, dual=True)
            regular_qubits = regular.dag.num_qubits()
            dual_qubits = dual.dag.num_qubits()

            result = regular if regular_qubits <= dual_qubits else dual

        return result.dag
