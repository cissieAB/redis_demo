"""
A demo to operate the DAOS pools/containers with Python APIs.

Author: xmei@jlab.org. Created at Mar/7/2024.
"""

# DAOS official instructions and examples:
#    - https://docs.daos.io/v2.4/user/python/
#    - https://github.com/daos-stack/daos/tree/release/2.4/src/client/pydaos/raw
#    - https://github.com/daos-stack/daos/blob/release/2.4/src/client/pydaos/raw/daos_api.py

# Make sure the pool "python-pool" exists.
# $ dmg system list-pools
# Pool        Size   State Used Imbalance Disabled
# ----        ----   ----- ---- --------- --------
# python-pool 3.9 TB Ready 0%   0%        0/96

# Create the container "py-testcont" in the above pool.
# $ daos cont create $pool_name $cont_name -t PYTHON
# Successfully created container 01571915-f3bc-472e-ac42-c63f02ed54fd
#   Container UUID : 01571915-f3bc-472e-ac42-c63f02ed54fd
#   Container Label: py-testcont
#   Container Type : PYTHON

# NOTE: UPDATE YOUR PATH HERE!!!
# Manually import the DAOS python module
# Find the pydaos module by: sudo find / -name "*pydaos*"
# Usually it is at /usr/lib64/python3.6/site-packages/pydaos
import sys
sys.path.append('/usr/lib64/python3.6/site-packages')  # depend on your path
from pydaos import pydaos_core

POOL_NAME="python-pool"
CONT_LABEL="py-testcont"

# Ref: https://github.com/daos-stack/daos/blob/release/2.4/src/client/pydaos/pydaos_core.py
dcont = pydaos_core.DCont(pool=POOL_NAME, cont=CONT_LABEL)
print(dcont)
