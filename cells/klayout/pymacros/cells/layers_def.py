# Copyright 2022 GlobalFoundries PDK Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

########################################################################################################################
## layers definition for Klayout of GF180MCU
########################################################################################################################

from gdsfactory.types import LayerSpec

comp_layer: LayerSpec = (22, 0)
poly2_layer: LayerSpec = (30, 0)
nplus_layer: LayerSpec = (32, 0)
pplus_layer: LayerSpec = (31, 0)
contact_layer: LayerSpec = (33, 0)
metal1_layer: LayerSpec = (34, 0)
dnwell_layer: LayerSpec = (12, 0)
lvpwell_layer: LayerSpec = (204, 0)
dualgate_layer: LayerSpec = (55, 0)
v5_xtor_layer: LayerSpec = (112, 1)
m1_layer: LayerSpec = (34, 0)
m2_layer: LayerSpec = (36, 0)
m1_lbl: LayerSpec = (34, 10)
via1_layer: LayerSpec = (35, 0)
nwell_layer: LayerSpec = (21, 0)
nat_layer: LayerSpec = (5, 0)
