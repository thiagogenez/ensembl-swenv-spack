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
#     spack install py-liftofftools
#
# You can edit this file again by typing:
#
#     spack edit py-liftofftools
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class PyLiftofftools(PythonPackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"

    # FIXME: ensure the package is not available through PyPI. If it is,
    # re-run `spack create --force` with the PyPI URL.
    url = "https://github.com/agshumate/LiftoffTools/archive/refs/tags/v0.4.4.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ["github_user1", "github_user2"]

    version("0.4.4", sha256="dacd8120debf5eb3190cae2ee87bf88d13a903e1eefebbad6a9ea847ea5dcba3")

    # FIXME: Only add the python/pip/wheel dependencies if you need specific versions
    # or need to change the dependency type. Generic python/pip/wheel dependencies are
    # added implicity by the PythonPackage base class.
    depends_on("python@3.6:", type=("build", "run"))
    # depends_on("py-pip@X.Y:", type="build")
    # depends_on("py-wheel@X.Y:", type="build")

    # FIXME: Add a build backend, usually defined in pyproject.toml. If no such file
    # exists, use setuptools.
    depends_on("py-setuptools", type="build")
    # depends_on("py-flit-core", type="build")
    # depends_on("py-poetry-core", type="build")

    # FIXME: Add additional dependencies if required.
    # depends_on("py-foo", type=("build", "run"))

    depends_on("py-matplotlib@3.5.2:")
    depends_on("py-nltk@3.6.7:")
    depends_on("mmseqs2@14:")
    depends_on("py-liftoff@1.6.3.2:")

    depends_on("py-numpy@1.21.1:")
    depends_on("py-biopython@1.76:")
    depends_on("py-gffutils@0.10.1:")
    depends_on("py-pyfaidx@0.5.8:")
    depends_on("py-parasail@1.2.4:")

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
