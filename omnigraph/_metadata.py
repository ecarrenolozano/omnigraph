#!/usr/bin/env python

#
# This file is part of the `omnigraph` Python module
#
# Copyright 2025
# Heidelberg University Hospital
#
# File author(s): Edwin (edwin@gmail.com)
#
# Distributed under the MIT license
# See the file `LICENSE` or read a copy at
# https://opensource.org/license/mit
#

"""Package metadata (version, authors, etc)."""

__all__ = ['get_metadata']

import os
import pathlib
import importlib.metadata

import toml

_VERSION = '0.0.1'


def get_metadata() -> dict:
    """Basic package metadata.

    Retrieves package metadata from the current project directory or from
    the installed package.
    """

    here = pathlib.Path(__file__).parent
    pyproj_toml = 'pyproject.toml'
    meta = {}

    for project_dir in (here, here.parent):
        toml_path = str(project_dir.joinpath(pyproj_toml).absolute())

        if os.path.exists(toml_path):
            pyproject = toml.load(toml_path)

            meta = {
                'name': pyproject['tool']['poetry']['name'],
                'version': pyproject['tool']['poetry']['version'],
                'author': pyproject['tool']['poetry']['authors'],
                'license': pyproject['tool']['poetry']['license'],
                'full_metadata': pyproject,
            }

            break

    if not meta:
        try:
            meta = {
                k.lower(): v
                for k, v in importlib.metadata.metadata(here.name).items()
            }

        except importlib.metadata.PackageNotFoundError:
            pass

    meta['version'] = meta.get('version', None) or _VERSION

    return meta


metadata = get_metadata()
__version__ = metadata.get('version', None)
__author__ = metadata.get('author', None)
__license__ = 'MIT'
