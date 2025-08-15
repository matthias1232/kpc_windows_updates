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

from cmk.rulesets.v1 import Title, Label, Help
from cmk.rulesets.v1.form_specs import (
    BooleanChoice,
    DefaultValue,
    DictElement,
    Dictionary,
    Integer,
    MatchingScope,
    RegularExpression,
    List,
)
from cmk.rulesets.v1.rule_specs import AgentConfig, Topic


def _valuespec_windows_updates_kpc():
    return Dictionary(
        title=Title("Windows Updates (Agent Plugin)"),
        help_text=Help(
            "This will deploy the agent plugin <tt>windows_updates_kpc.ps1</tt> for checking for available Windows Updates"
        ),
        elements={
            "deploy": DictElement(
                parameter_form=BooleanChoice(
                    label=Label("Deploy plugin for Windows Updates"),
                ),
                required=True,
            ),
        },
    )




rule_spec_agent_config_windows_updates_kpc = AgentConfig(
    title=Title("Windows Updates (Agent Plugin)"),
    topic=Topic.WINDOWS,
    name="windows_updates_kpc",
    parameter_form=_valuespec_windows_updates_kpc,
)