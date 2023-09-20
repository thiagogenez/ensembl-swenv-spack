# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class PyCigar(PythonPackage):
    """Cigar is a simple library for management of cigar strings."""

    homepage = "https://github.com/brentp/cigar"
    pypi = "cigar/cigar-0.1.3.tar.gz"

    maintainers("EbiArnie", "thiagogenez")

    version("0.1.3", sha256="5847f5e8968035b3a5b04dcfa879fb6c14dd3a42dce8994864806dcda8a4fcf2")

    depends_on("py-setuptools", type="build")
