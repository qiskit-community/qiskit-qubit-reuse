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

"""Qubit Reuse Init plugin."""

from qiskit.transpiler import PassManager
from qiskit.transpiler.preset_passmanagers import common
from qiskit.transpiler.preset_passmanagers.plugin import PassManagerStagePlugin

from .qubit_reuse import QubitReuse


class QubitReusePlugin(PassManagerStagePlugin):
    """Plugin for using vf2 partial layout."""

    def pass_manager(self, pass_manager_config, optimization_level=None):
        """build qubit reuse init plugin stage pass manager."""
        # TODO: Build plugin
        plugin_stage = PassManager()
        return plugin_stage
