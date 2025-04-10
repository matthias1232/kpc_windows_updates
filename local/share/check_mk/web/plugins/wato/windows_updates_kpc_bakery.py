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
from cmk.gui.plugins.wato import (
   HostRulespec,
   rulespec_registry,
)
try:
    from cmk.gui.cee.plugins.wato.agent_bakery.rulespecs.utils import (
        RulespecGroupMonitoringAgentsAgentPlugins
    )
except Exception:
    RulespecGroupMonitoringAgentsAgentPlugins = None

from cmk.gui.valuespec import (
   Age,
   Dictionary,
   TextAscii,
   DropdownChoice,
)

def _valuespec_windows_updates_kpc():
    return DropdownChoice(
        title=_('Windows Updates (Agent Plugin)'),
        help=_('This will deploy the agent plugin <tt>windows_updates_kpc.ps1</tt> '
               'for checking for available Windows Updates'),
        choices=[
            (True, _('Deploy plugin for Windows Updates')),
            (None, _('Do not deploy plugin for Windows Updates')),
        ],
    )


if RulespecGroupMonitoringAgentsAgentPlugins is not None:
    rulespec_registry.register(
       HostRulespec(
          group=RulespecGroupMonitoringAgentsAgentPlugins,
          name="agent_config:windows_updates_kpc",
          valuespec=_valuespec_windows_updates_kpc,
       ))
