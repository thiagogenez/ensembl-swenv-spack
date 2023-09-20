# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class PyPubsub(PythonPackage):
    """Provides a publish-subscribe API to facilitate event-based or message-based architecture in a single-process application."""

    url = "https://github.com/schollii/pypubsub/archive/refs/tags/v4.0.3.tar.gz"
    git = "https://github.com/schollii/pypubsub.git"

    maintainers("EbiArnie", "thiagogenez")

    version("4.0.3", sha256="0df83daa1cb0021bab858ff6812d836c9712dea59a5172be1888bb554c3a89a2")

    depends_on("py-setuptools", type="build")
