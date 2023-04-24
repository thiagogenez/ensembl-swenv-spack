# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
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
#     spack install py-liftoff
#
# You can edit this file again by typing:
#
#     spack edit py-liftoff
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class PyLiftoff(PythonPackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    pypi = "Liftoff/Liftoff-1.6.3.2.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ["github_user1", "github_user2"]

    version("1.6.3.2", sha256="7070a861144d0f043533893d39f95589a64d63f0365a99d06d71f1700b7fb758")

    # FIXME: Only add the python/pip/wheel dependencies if you need specific versions
    # or need to change the dependency type. Generic python/pip/wheel dependencies are
    # added implicity by the PythonPackage base class.
    # depends_on("python@2.X:2.Y,3.Z:", type=("build", "run"))
    # depends_on("py-pip@X.Y:", type="build")
    # depends_on("py-wheel@X.Y:", type="build")

    # FIXME: Add a build backend, usually defined in pyproject.toml. If no such file
    # exists, use setuptools.
    depends_on("py-setuptools", type="build")
    # depends_on("py-flit-core", type="build")
    # depends_on("py-poetry-core", type="build")

    # FIXME: Add additional dependencies if required.
    # depends_on("py-foo", type=("build", "run"))

    depends_on("py-numpy@1.22.0:")
    depends_on("py-biopython@1.76:")
    depends_on("py-gffutils@0.10.1:")
    depends_on("py-networkx@2.4:")
    depends_on("py-pysam@0.19.1:")
    depends_on("py-pyfaidx@0.5.8:")
    depends_on("py-interlap@0.2.6:")
    depends_on("py-ujson@3.2.0:")
    depends_on("py-parasail@1.2.1:")

    # Tested with 2.17 and 2.24
    depends_on("minimap2@2.17:2.24")

    #def global_options(self, spec, prefix):
    #    # FIXME: Add options to pass to setup.py
    #    # FIXME: If not needed, delete this function
    #    options = []
    #    return options

    #def install_options(self, spec, prefix):
    #    # FIXME: Add options to pass to setup.py install
    #    # FIXME: If not needed, delete this function
    #    options = []
    #    return options
