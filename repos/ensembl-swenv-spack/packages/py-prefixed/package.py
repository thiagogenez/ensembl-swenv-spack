# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class PyPrefixed(PythonPackage):
    """Prefixed provides an alternative implementation of the built-in float which supports formatted output with SI (decimal) and IEC (binary) prefixes."""

    homepage = "https://github.com/Rockhopper-Technologies/prefixed"
    pypi = "prefixed/prefixed-0.7.0.tar.gz"

    maintainers("EbiArnie", "thiagogenez")

    version("0.7.0", sha256="0b54d15e602eb8af4ac31b1db21a37ea95ce5890e0741bb0dd9ded493cefbbe9")

    depends_on("py-setuptools", type="build")
