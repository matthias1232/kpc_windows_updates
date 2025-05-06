#!/usr/bin/env python3
#
#This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the #License, or (at your option) any later version.
#
#This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU #General Public License for more details.
#
#You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>.
#
# Written by Matthias Binder m.binder@kpc.de, July 2023
#
################################################################################################################
#
# Author: K&P Computer Service- und Vertriebs-GmbH
# Author: Matthias Binder
# License: GNU General Public License
# License Changed to GPL: 11/2024
#
# 
# For Support and Sales Please Contact K&P Computer!
#
# E-Mail: hds@kpc.de
#
# 24/7 Helpdesk-Support:
# International: +800 4479 3300
# Germany: +49 6122 7071 330
# Austria: +43 1 525 1833
#
# Web Germany: https://www.kpc.de
# Web Austria: https://www.kpc.at
# Web International: https://www.kpc.de/en
#
################################################################################################################

from cmk.rulesets.v1 import Title
from cmk.rulesets.v1.form_specs import (
    DefaultValue,
    DictElement,
    Dictionary,
    InputHint,
    Integer,
    Float,
    LevelDirection,
    LevelsType,
    SimpleLevels,
    SimpleLevelsConfigModel,
)
from cmk.rulesets.v1.rule_specs import CheckParameters, HostCondition, Topic



 
def _parameter_form_windows_updates_kpc_windows_lastupdateinstalldate() -> Dictionary:
    return Dictionary(
        elements={
            "warning_lower": DictElement[SimpleLevelsConfigModel[int]](
                required=False,
                parameter_form=SimpleLevels(
                    title=Title("Levels on Windows Last Updates installed days ago"),
                    level_direction=LevelDirection.UPPER,
                    form_spec_template=Integer(),
                    prefill_fixed_levels=InputHint(value=(30, 50)),
                ),
            ),
        }
    )
        
rule_spec_windows_updates_kpc_windows_lastupdateinstalldate = CheckParameters(
    name="windows_updates_kpc_windows_lastupdateinstalldate",
    topic=Topic.WINDOWS,
    parameter_form=_parameter_form_windows_updates_kpc_windows_lastupdateinstalldate,
    title=Title("Windows Updates Last Updates installed days ago"),
    condition=HostCondition(),
)
