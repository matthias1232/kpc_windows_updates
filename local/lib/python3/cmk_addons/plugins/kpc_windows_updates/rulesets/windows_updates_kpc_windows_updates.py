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
from cmk.rulesets.v1 import Help, Label, Title
from cmk.rulesets.v1.rule_specs import CheckParameters, HostCondition, Topic



 
def _parameter_valuespec_windows_updates_kpc() -> Dictionary:
    return Dictionary(
        elements={
            "levels_important1": DictElement[SimpleLevelsConfigModel[int]](
                parameter_form=SimpleLevels(
                    title=Title("Levels for pending important updates"),
                    level_direction=LevelDirection.UPPER,
                    form_spec_template=Integer(),
                    prefill_levels_type=DefaultValue(LevelsType.FIXED),
                    prefill_fixed_levels=InputHint((1, 1)),
                )
            ),
            "levels_optional": DictElement[SimpleLevelsConfigModel[int]](
                parameter_form=SimpleLevels(
                    title=Title("Levels for pending optional updates"),
                    level_direction=LevelDirection.UPPER,
                    form_spec_template=Integer(),
                    prefill_levels_type=DefaultValue(LevelsType.FIXED),
                    prefill_fixed_levels=InputHint((1, 99)),
                )
            ),
            "levels_mandatory": DictElement[SimpleLevelsConfigModel[int]](
                parameter_form=SimpleLevels(
                    title=Title("Levels for pending updates with critical severity"),
                    level_direction=LevelDirection.UPPER,
                    form_spec_template=Integer(),
                    prefill_levels_type=DefaultValue(LevelsType.FIXED),
                    prefill_fixed_levels=InputHint((1, 1)),
                )
            ),
            "levels_critical": DictElement[SimpleLevelsConfigModel[int]](
                parameter_form=SimpleLevels(
                    title=Title("Levels for pending updates with critical severity"),
                    level_direction=LevelDirection.UPPER,
                    form_spec_template=Integer(),
                    prefill_levels_type=DefaultValue(LevelsType.FIXED),
                    prefill_fixed_levels=InputHint((1, 1)),
                )
            ),
            "levels_important": DictElement[SimpleLevelsConfigModel[int]](
                parameter_form=SimpleLevels(
                    title=Title("Levels for pending updates with important severity"),
                    level_direction=LevelDirection.UPPER,
                    form_spec_template=Integer(),
                    prefill_levels_type=DefaultValue(LevelsType.FIXED),
                    prefill_fixed_levels=InputHint((1, 6)),
                )
            ),
            "levels_moderate": DictElement[SimpleLevelsConfigModel[int]](
                parameter_form=SimpleLevels(
                    title=Title("Levels for pending updates with moderate severity"),
                    level_direction=LevelDirection.UPPER,
                    form_spec_template=Integer(),
                    prefill_levels_type=DefaultValue(LevelsType.FIXED),
                    prefill_fixed_levels=InputHint((1, 10)),
                )
            ),
            "levels_low": DictElement[SimpleLevelsConfigModel[int]](
                parameter_form=SimpleLevels(
                    title=Title("Levels for pending updates with low severity"),
                    level_direction=LevelDirection.UPPER,
                    form_spec_template=Integer(),
                    prefill_levels_type=DefaultValue(LevelsType.FIXED),
                    prefill_fixed_levels=InputHint((1, 99)),
                )
            ),
            "levels_unspecified": DictElement[SimpleLevelsConfigModel[int]](
                parameter_form=SimpleLevels(
                    title=Title("Levels for pending updates with unspecified severity"),
                    level_direction=LevelDirection.UPPER,
                    form_spec_template=Integer(),
                    prefill_levels_type=DefaultValue(LevelsType.FIXED),
                    prefill_fixed_levels=InputHint((1, 99)),
                )
            ),
            "levels_pendingreboot": DictElement[SimpleLevelsConfigModel[int]](
                parameter_form=SimpleLevels(
                    title=Title("Levels for pending reboot after update installation (hours)"),
                    level_direction=LevelDirection.UPPER,
                    form_spec_template=Integer(),
                    prefill_levels_type=DefaultValue(LevelsType.FIXED),
                    prefill_fixed_levels=InputHint((48, 96)),
                )
            ),
        },
        title=Title("Windows Updates"),
        help_text=Help("Windows Updates"),  
    )


rule_spec_windows_updates_kpc_windows_lastupdateinstalldate = CheckParameters(
    name="windows_updates_kpc_windows_updates",
    topic=Topic.WINDOWS,
    parameter_form=_parameter_valuespec_windows_updates_kpc,
    title=Title("Windows Updates"),
    condition=HostCondition(),
)