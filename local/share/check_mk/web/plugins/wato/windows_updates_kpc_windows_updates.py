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

from cmk.gui.i18n import _

# import required to register agent
from cmk.gui.plugins.wato import (
    rulespec_registry,
    HostRulespec,
    CheckParameterRulespecWithoutItem,
    RulespecGroupCheckParametersApplications
)

from cmk.gui.valuespec import (
    FixedValue,
    TextInput,
    Age,
    ListOfStrings,
    DropdownChoice,
    Tuple,
    Integer,
)

# import structure where special agent will be registered
from cmk.gui.plugins.wato.datasource_programs import RulespecGroupDatasourcePrograms



 
def _parameter_valuespec_windows_updates_kpc_windows_updates():
    return Dictionary(
        elements=[
            ("levels_important1", Tuple(
                title=_("Levels for pending important updates"),
                elements=[
                    Integer(title=_("Warning at"), default_value=1),
                    Integer(title=_("Critical at"), default_value=1),
                    DropdownChoice(
                        title = _("Check Enabled"),
                        help = _('default is Check Enabled'),
                        choices = [
                            ( "Enabled",  _("Check enabled") ),
                            ( "Disabled", _("Check disabled (always be OK)") ),                           
                        ],
                        default_value = "Enabled",
                    ),
                ],
            )),
            ("levels_optional", Tuple(
                title=_("Levels for pending optional updates"),
                elements=[
                    Integer(title=_("Warning at"), default_value=1),
                    Integer(title=_("Critical at"), default_value=99),
                    DropdownChoice(
                        title = _("Check Enabled"),
                        help = _('default is Check Enabled'),
                        choices = [
                            ( "Enabled",  _("Check enabled") ),
                            ( "Disabled", _("Check disabled (always be OK)") ),                           
                        ],
                        default_value = "Enabled",
                    ),
                ],
            )),
            ("levels_mandatory", Tuple(
                title=_("Levels for pending updates with mandatory severity"),
                elements=[
                    Integer(title=_("Warning at"), default_value=1),
                    Integer(title=_("Critical at"), default_value=1),
                    DropdownChoice(
                        title = _("Check Enabled"),
                        help = _('default is Check Enabled'),
                        choices = [
                            ( "Enabled",  _("Check enabled") ),
                            ( "Disabled", _("Check disabled (always be OK)") ),                           
                        ],
                        default_value = "Disabled",
                    ),
                ],
            )),
            ("levels_critical", Tuple(
                title=_("Levels for pending updates with critical severity"),
                elements=[
                    Integer(title=_("Warning at"), default_value=1),
                    Integer(title=_("Critical at"), default_value=1),
                    DropdownChoice(
                        title = _("Check Enabled"),
                        help = _('default is Check Enabled'),
                        choices = [
                            ( "Enabled",  _("Check enabled") ),
                            ( "Disabled", _("Check disabled (always be OK)") ),                           
                        ],
                        default_value = "Disabled",
                    ),
                ],
            )),  
            ("levels_important", Tuple(
                title=_("Levels for pending updates with important severity"),
                elements=[
                    Integer(title=_("Warning at"), default_value=1),
                    Integer(title=_("Critical at"), default_value=6),
                    DropdownChoice(
                        title = _("Check Enabled"),
                        help = _('default is Check Enabled'),
                        choices = [
                            ( "Enabled",  _("Check enabled") ),
                            ( "Disabled", _("Check disabled (always be OK)") ),                           
                        ],
                        default_value = "Disabled",
                    ),
                ],
            )),
            ("levels_moderate", Tuple(
                title=_("Levels for pending updates with moderate severity"),
                elements=[
                    Integer(title=_("Warning at"), default_value=1),
                    Integer(title=_("Critical at"), default_value=10),
                    DropdownChoice(
                        title = _("Check Enabled"),
                        help = _('default is Check Enabled'),
                        choices = [
                            ( "Enabled",  _("Check enabled") ),
                            ( "Disabled", _("Check disabled (always be OK)") ),                           
                        ],
                        default_value = "Disabled",
                    ),
                ],
            )),
            ("levels_low", Tuple(
                title=_("Levels for pending updates with low severity"),
                elements=[
                    Integer(title=_("Warning at"), default_value=1),
                    Integer(title=_("Critical at"), default_value=99),
                    DropdownChoice(
                        title = _("Check Enabled"),
                        help = _('default is Check Enabled'),
                        choices = [
                            ( "Enabled",  _("Check enabled") ),
                            ( "Disabled", _("Check disabled (always be OK)") ),                           
                        ],
                        default_value = "Disabled",
                    ),
                ],
            )),
            ("levels_unspecified", Tuple(
                title=_("Levels for pending updates with unspecified severity"),
                elements=[
                    Integer(title=_("Warning at"), default_value=1),
                    Integer(title=_("Critical at"), default_value=99),
                    DropdownChoice(
                        title = _("Check Enabled"),
                        help = _('default is Check Enabled'),
                        choices = [
                            ( "Enabled",  _("Check enabled") ),
                            ( "Disabled", _("Check disabled (always be OK)") ),                           
                        ],
                        default_value = "Disabled",
                    ),
                ],
            )),
            ("levels_pendingreboot", Tuple(
                title=_("Levels for pending reboot after update installation"),
                elements=[
                    Integer(title=_("Warning after (hours)"), default_value=48),
                    Integer(title=_("Critical after (hours)"), default_value=96),
                    DropdownChoice(
                        title = _("Check Enabled"),
                        help = _('default is Check Enabled'),
                        choices = [
                            ( "Enabled",  _("Check enabled") ),
                            ( "Disabled", _("Check disabled (always be OK)") ),                           
                        ],
                        default_value = "Enabled",
                    ),
                ],
            )),
        ],
    )
   
        
rulespec_registry.register(
CheckParameterRulespecWithoutItem(
check_group_name="windows_updates_kpc_windows_updates",
group=RulespecGroupCheckParametersApplications,
parameter_valuespec=_parameter_valuespec_windows_updates_kpc_windows_updates,
title=lambda: _("Windows Updates"),
))
