# -*- coding: utf-8 -*-

"""
Populates a provided Cloudbreak Instance with resources for Demos

Warnings:
    Experimental
"""

from __future__ import absolute_import
import logging
from datetime import datetime
import whoville

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)


# 'horton' is a shared state function to make deployment more readable
# to non-python users
horton = whoville.deploy.Horton()


def step_1_init_service():
    log.info("------------- Initialising Whoville Deployment Service")
    log.info("------------- Validating Profile")
    if not whoville.config.profile['deploy']:
        raise ValueError("whoville Config Profile is not populated with"
                         "deployment controls, cannot proceed")
    log.info("------------- Fetching Resources from Profile Definitions")
    if whoville.config.profile['deploy']['resources']:
        for res_def in whoville.config.profile['deploy']['resources']:
            if res_def['loc'] == 'local':
                log.info("Loading resources from Local path [%s]",
                         res_def['uri'])
                horton.resources.update(whoville.utils.load_resources_from_files(
                    res_def['uri']
                ))
            elif res_def['loc'] == 'github':
                log.info("Loading resources from Github Repo [%s]",
                         res_def['repo'])
                horton.resources.update(whoville.utils.load_resources_from_github(
                    repo_name=res_def['repo'],
                    username=whoville.config.profile['deploy']['githubuser'],
                    token=whoville.config.profile['deploy']['githubtoken'],
                    tgt_dir=res_def['subdir']
                ))
            else:
                raise ValueError("Resource Location [%s] Unsupported",
                                 res_def['loc'])
        for k, v in horton.resources.items():
            horton.defs[k] = v[k + '.yaml']


def step_2_init_infra():
    log.info("------------- Getting Cloudbreak Environment")
    horton.cbd = whoville.infra.get_cloudbreak(
        purge=horton.global_purge
    )
    log.info("------------- Connecting to Cloudbreak")
    url = 'https://' + horton.find('cbd:extra:dns_name') + '/cb/api'
    log.info("Setting endpoint to %s", url)
    whoville.utils.set_endpoint(url)
    log.info("------------- Authenticating to Cloudbreak")
    auth_success = whoville.security.service_login(
            service='cloudbreak',
            username=whoville.config.profile['deploy']['email'],
            password=whoville.config.profile['deploy']['password'],
            bool_response=False
        )
    if not auth_success:
        raise ConnectionError("Couldn't login to Cloudbreak")
    else:
        log.info('Logged into Cloudbreak at [%s]', url)
    # Cloudbreak may have just booted and not be ready for queries yet
    # Waiting up to an additional minute for query success
    log.info("Waiting for Cloudbreak API Calls to be available")
    whoville.utils.wait_to_complete(
        whoville.deploy.list_blueprints,
        bool_response=True,
        whoville_delay=5,
        whoville_max_wait=60
    )
    log.info("------------- Setting Deployment Credential")
    horton.cred = whoville.deploy.get_credential(
        whoville.config.profile['deploy']['namespace'] + 'credential',
        create=True,
        purge=horton.global_purge
    )


def step_3_sequencing():
    log.info("------------- Establishing Deployment Sequence")
    for def_key in horton.defs.keys():
        log.info("Checking Definition [%s]", def_key)
        priority = horton.find('defs:' + def_key + ':control:priority')
        if priority is not None:
            log.info("Registering [%s] as Priority [%s]",
                     def_key, str(priority))
            horton.seq[priority] = horton.find('defs:' + def_key + ':control:seq')
        else:
            log.info("Priority not set for [%s], skipping...", def_key)


def step_4_build():
    for seq_key in sorted(horton.seq.keys()):
        log.info("Running Deployment Priority [%s]", str(seq_key))
        start_ts = datetime.utcnow()
        log.info("Started Priority [%s] at [%s]", str(seq_key), start_ts)
        steps = horton.seq[seq_key]
        for step in steps:
            for action, args in step.items():
                log.info("Executing Action [%s] with Args [%s] at [%s]",
                         action, str(args), datetime.utcnow())
                if action == 'prepdeps':
                    def_key = args[0]
                    shortname = args[1]
                    whoville.deploy.prep_dependencies(def_key, shortname)
                if action == 'prepspec':
                    def_key = args[0]
                    shortname = args[1]
                    whoville.deploy.prep_stack_specs(def_key, shortname)
                if action == 'deploy':
                    for spec_key in args:
                        fullname = horton.namespace + spec_key
                        whoville.deploy.create_stack(
                            fullname,
                            purge=False
                        )
                if action == 'wait':
                    def_key = args[0]
                    spec_key = args[1]
                    fullname = horton.namespace + spec_key
                    event = args[2]
                    whoville.deploy.wait_for_event(
                        fullname,
                        event,
                        start_ts,
                        horton.defs[def_key]['control']['deploywait']
                    )
                if action == 'openport':
                    protocol = args[0]
                    start_port = args[1]
                    end_port = args[2]
                    cidr = args[3]
                    whoville.deploy.add_security_rule(
                        protocol=protocol,
                        start=start_port,
                        end=end_port,
                        cidr=cidr
                    )
                if action == 'writecache':
                    spec_key = args[0]
                    fullname = horton.namespace + spec_key
                    target = args[1]
                    cache_key = args[2]
                    whoville.deploy.write_cache(fullname, target, cache_key)
                if action == 'replace':
                    def_key = args[0]
                    res_name = args[1]
                    cache_key = args[2]
                    log.info("Replacing string [%s] with [%s] in Resource [%s]"
                             " in def [%s]",
                             cache_key, horton.cache[cache_key], res_name, def_key)
                    horton.resources[def_key][res_name].replace(
                        cache_key, horton.cache[cache_key]
                    )
                log.info("Completed Action [%s] with Args [%s] at [%s]",
                         action, str(args), datetime.utcnow())
        finish_ts = datetime.utcnow()
        diff_ts = finish_ts - start_ts
        log.info("Completed Deployment [%s] at [%s] after [%d]",
                 seq_key, finish_ts, diff_ts.seconds)


def autorun():
    step_1_init_service()
    step_2_init_infra()
    step_3_sequencing()
    step_4_build()


if __name__ == '__main__':
    autorun()
    exit(0)
