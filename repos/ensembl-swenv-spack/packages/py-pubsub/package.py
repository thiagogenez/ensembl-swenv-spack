# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install py-pypubsub
#
# You can edit this file again by typing:
#
#     spack edit py-pypubsub
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class PyPubsub(PythonPackage):
    """Provides a publish-subscribe API to facilitate event-based or message-based architecture in a single-process application."""

    url = "https://github.com/schollii/pypubsub/archive/refs/tags/v4.0.3.tar.gz"
    git = "https://github.com/schollii/pypubsub.git"

    maintainers("EbiArnie", "thiagogenez")

    version("4.0.3", sha256="0df83daa1cb0021bab858ff6812d836c9712dea59a5172be1888bb554c3a89a2")

    depends_on("py-setuptools", type="build")

    def global_options(self, spec, prefix):
        # FIXME: Add options to pass to setup.py
        # FIXME: If not needed, delete this function
        options = []
        return options

    def install_options(self, spec, prefix):
        # FIXME: Add options to pass to setup.py install
        # FIXME: If not needed, delete this function
        options = []
        return options
