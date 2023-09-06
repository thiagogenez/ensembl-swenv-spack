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
#     spack install py-enlighten
#
# You can edit this file again by typing:
#
#     spack edit py-enlighten
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class PyEnlighten(PythonPackage):
    """Enlighten Progress Bar is a console progress bar library for Python."""

    homepage = "https://github.com/Rockhopper-Technologies/enlighten"
    pypi = "enlighten/enlighten-1.11.2.tar.gz"

    maintainers("EbiArnie", "thiagogenez")

    version("1.11.2", sha256="9284861dee5a272e0e1a3758cd3f3b7180b1bd1754875da76876f2a7f46ccb61")

    depends_on("py-setuptools", type="build")
    depends_on("py-blessed", type=("build", "run"))
    depends_on("py-prefixed", type=("build", "run"))

