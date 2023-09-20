# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


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
