Install DAOS from scratch
=========================

Use the guide from Github: https://github.com/daos-stack/daos/blob/master/docs/QSG/build_from_scratch.md.

This process is test and run successfully on `daosfs05`.
After installation, check `<daos_path>/install`:

::

    (venv) [xmei@daosfs05 daos]$ ls install/bin/
    acl_dump_test          daos_server_helper         nvme_control_ctests
    agent_tests            daos_storage_estimator.py  obj_ctl
    bio_ut                 daos_test                  pl_bench
    cart_ctl               dfs_test                   pool_scrubbing_tests
    common_test            dfuse                      rdbt
    crt_launch             dfuse_test                 ring_pl_map
    daos                   dmg                        rpc_tests
    daos_agent             drpc_engine_test           security_test
    daos_debug_set_params  drpc_test                  self_test
    daos_engine            eq_tests                   smd_ut
    daos_gen_io_conf       evt_ctl                    srv_checksum_tests
    daos_metrics           fault_status               vea_stress
    daos_perf              hello_drpc                 vea_ut
    daos_racer             jobtest                    vos_perf
    daos_run_io_conf       job_tests                  vos_tests
    daos_server            jump_pl_map