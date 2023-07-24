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
from qiskit.transpiler.passes import UnitarySynthesis, Unroll3qOrMore
from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager
from qiskit.transpiler.preset_passmanagers.plugin import PassManagerStagePlugin

from .qubit_reuse import QubitReuse


def generate_optimization_manager(pass_manager_config, optimization_level=None, type="default"):
    # Build init state depending on the configs passed. Extract init
    preset_stage = generate_preset_pass_manager(
        optimization_level=optimization_level,
        target=pass_manager_config.target,
        basis_gates=pass_manager_config.basis_gates,
        inst_map=pass_manager_config.inst_map,
        backend_properties=pass_manager_config.backend_properties,
        instruction_durations=pass_manager_config.instruction_durations,
        timing_constraints=pass_manager_config.timing_constraints,
    )
    # Try and get init attribute, if nonexistent, create a regular pass
    plugin_stage = getattr(
        preset_stage,
        "init",
        PassManager(
            [
                UnitarySynthesis(
                    target=pass_manager_config.target,
                    basis_gates=pass_manager_config.basis_gates,
                    backend_props=pass_manager_config.backend_properties,
                ),
                Unroll3qOrMore(
                    target=pass_manager_config.target,
                    basis_gates=pass_manager_config.basis_gates,
                ),
            ]
        ),
    )
    # Append qubit reuse.
    plugin_stage.append(QubitReuse(target=pass_manager_config.target, type=type))
    return plugin_stage


class QubitReusePluginDefault(PassManagerStagePlugin):
    """Plugin for using Qubit Reset and Reuse in Default Mode."""

    def pass_manager(self, pass_manager_config, optimization_level=None):
        """build qubit reuse init plugin stage pass manager. Default Mode."""
        return generate_optimization_manager(
            pass_manager_config=pass_manager_config,
            optimization_level=optimization_level,
        )


class QubitReusePluginNormal(PassManagerStagePlugin):
    """Plugin for using Qubit Reset and Reuse."""

    def pass_manager(self, pass_manager_config, optimization_level=None):
        """build qubit reuse init plugin stage pass manager in Normal Mode."""
        return generate_optimization_manager(
            pass_manager_config=pass_manager_config,
            optimization_level=optimization_level,
            type="normal",
        )


class QubitReusePluginDual(PassManagerStagePlugin):
    """Plugin for using Qubit Reset and Reuse. Dual Mode."""

    def pass_manager(self, pass_manager_config, optimization_level=None):
        """build qubit reuse init plugin stage pass manager in Dual Mode."""
        return generate_optimization_manager(
            pass_manager_config=pass_manager_config,
            optimization_level=optimization_level,
            type="dual",
        )
