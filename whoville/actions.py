# -*- coding: utf-8 -*-

"""
Action Primitives for Deployment Orchestration.
Used by Mayor to resolve deployment sequences

Warnings:
    Experimental
"""

from __future__ import absolute_import as _absolute_import
import logging as _logging
from datetime import datetime as _datetime
from whoville import deploy
from whoville.utils import get_val as _get_val
from whoville.utils import set_val as _set_val

_horton = deploy.Horton()

log = _logging.getLogger(__name__)


def prep_deps(args):
    def_key = args[0]
    shortname = args[1]
    deploy.prep_dependencies(def_key, shortname)


def prep_spec(args):
    def_key = args[0]
    shortname = args[1]
    deploy.prep_stack_specs(def_key, shortname)


def do_builds(args):
    for spec_key in args:
        fullname = _horton.namespace + spec_key
        deploy.create_stack(
            fullname,
            purge=False
        )


def wait_event(args):
    def_key = args[0]
    spec_key = args[1]
    fullname = _horton.namespace + spec_key
    field = args[2]
    state = args[3]
    deploy.wait_for_event(
        fullname,
        field,
        state,
        _datetime.utcnow(),
        _horton.defs[def_key]['deploywait']
    )


def open_port(args):
    protocol = args[0]
    start_port = args[1]
    end_port = args[2]
    cidr = args[3]
    deploy.add_security_rule(
        protocol=protocol,
        start=start_port,
        end=end_port,
        cidr=cidr
    )


def write_cache(args):
    spec_key = args[0]
    fullname = _horton.namespace + spec_key
    target = args[1]
    cache_key = args[2]
    deploy.write_cache(fullname, target, cache_key)


def replace_str(args):
    def_key = args[0]
    res_name = args[1]
    cache_key = args[2]
    log.info("Replacing string [%s] with [%s] in Resource [%s] in def [%s]",
             cache_key, _horton.cache[cache_key], res_name, def_key)
    s = _horton.resources[def_key][res_name].replace(
        cache_key, _horton.cache[cache_key]
    )
    _horton.resources[def_key][res_name] = s


def copy_def(args):
    sep = args[2] if len(args) > 2 else ':'
    s = args[0]
    t = args[1]
    for d in ['defs', 'resources']:
        log.info("-- Running copy_def on [%s] component", d)
        _horton._setr(
            sep.join([d, t]),
            _horton._getr(sep.join([d, s]), sep=sep),
            sep=sep,
            merge=False
        )
    s_def = args[0] + '.yaml'
    t_def = args[1] + '.yaml'
    log.debug("source [%s] target [%s]", s_def, t_def)
    _horton.resources[t][t_def] = _horton.resources[s].pop(s_def)


def merge_def(args):
    sep = args[2] if len(args) > 2 else ':'
    s = args[0]
    t = args[1]
    source = sep.join(['defs', s])
    target = sep.join(['defs', t])
    log.info("-- Running merge_def on defs")
    _horton._setr(
        target,
        _horton._getr(source, sep=sep),
        sep=sep,
        merge=True,
        squash_keys=['seq']
    )
    source = sep.join(['resources', s])
    target = sep.join(['resources', t])
    log.info("-- Running merge_def on resources")
    _horton._setr(
        target,
        _horton._getr(source, sep=sep),
        sep=sep,
        merge=True,
        max_depth=1
    )


def call_seq(args):
    from whoville.mayor import step_4_build
    def_key_to_build = args[0]
    step_4_build(def_key_to_build)