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
#     spack install py-tes
#
# You can edit this file again by typing:
#
#     spack edit py-tes
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class PyTes(PythonPackage):
    """FIXME: Put a proper description of your package here."""

    homepage = "https://github.com/deeshugupta/tes"
    pypi = "py-tes/py-tes-0.4.2.tar.gz"

    maintainers("EbiArnie", "thiagogenez")

    version("0.4.2", sha256="f6926cd59b7dfc8e37840955bf1cc7c43ad4d99ba5eae100b6156c918617472c")

    depends_on("py-setuptools", type="build")
    depends_on("py-attrs@17.4.0:", type=("build", "run"))
    depends_on("py-future@0.16.0:", type=("build", "run"))
    depends_on("py-python-dateutil@2.6.1:", type=("build", "run"))
    depends_on("py-requests@2.18.2:", type=("build", "run"))
