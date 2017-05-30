# Copyright 2017, Erlang Solutions Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

#
# Distribution flags from http://erlang.org/doc/apps/erts/erl_dist_protocol.html
#
DFLAG_PUBLISHED = 0x01
DFLAG_ATOM_CACHE = 0x02
DFLAG_EXT_REFS = 0x04
""" The node supports encoding/decoding of external references. """
DFLAG_DIST_MONITOR = 0x08
""" The node supports remote monitoring for processes. """
DFLAG_FUN_TAGS = 0x10
DFLAG_DIST_MONITOR_NAME = 0x20
""" The node supports remote monitoring for named processes. """
DFLAG_HIDDEN_ATOM_CACHE = 0x40
DFLAG_NEW_FUN_TAGS = 0x80
DFLAG_EXT_PIDS_PORTS = 0x100
""" The node supports encoding/decoding of external pids and ports. """
DFLAG_EXPORT_PTR_TAG = 0x200
DFLAG_BIT_BINARIES = 0x400
""" The node supports incomplete trailing byte in binaries. """
DFLAG_NEW_FLOATS = 0x800
""" The node supports 8-byte double encoding as IEEE-double. """
DFLAG_UNICODE_IO = 0x1000
DFLAG_DIST_HDR_ATOM_CACHE = 0x2000
DFLAG_SMALL_ATOM_TAGS = 0x4000
# 0x8000
DFLAG_UTF8_ATOMS = 0x10000
DFLAG_MAP_TAG = 0x20000
""" The node can handle map encoding. """
DFLAG_BIG_CREATION = 0x40000

DEFAULT_DFLAGS = (DFLAG_EXT_REFS |
                  DFLAG_EXT_PIDS_PORTS |
                  DFLAG_FUN_TAGS | DFLAG_NEW_FUN_TAGS |
                  DFLAG_EXPORT_PTR_TAG |
                  DFLAG_BIT_BINARIES |
                  DFLAG_NEW_FLOATS |
                  DFLAG_MAP_TAG |
                  DFLAG_DIST_MONITOR_NAME | DFLAG_DIST_MONITOR)
""" Default flags value represents current Pyrlang library features
    as a combination of feature bits.
"""

class NodeOpts:
    """ A class holding an integer with features that are supported
        by this node, and the network cookie.
    """
    def __init__(self, cookie: str, dflags: int = DEFAULT_DFLAGS) -> None:
        self.dflags_ = dflags
        self.cookie_ = cookie
        self.network_tick_time_ = 60
