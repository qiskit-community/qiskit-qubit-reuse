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

"""VF2Layout pass to find a layout using subgraph isomorphism"""
import logging

from qiskit.transpiler.basepasses import TransformationPass

logger = logging.getLogger(__name__)


class QubitReuse(TransformationPass)
    """A qubit reuse via midcircuit measurement transformation pass

    Cite paper here
    """

    def __init__(self, target):
        """Initialize a ``QubitReuse`` pass instance

        Args:
            target (Target): A target representing the backend device to run ``QubitReuse`` on.
        """
        super().__init__()
        self.target = target

    def run(self, dag):
        """run the qubit reuse pass method"""
        # todo add me
        return dag
