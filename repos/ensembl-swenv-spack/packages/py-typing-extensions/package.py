# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class PyTypingExtensions(PythonPackage):
    """typing_extensions complements the standard-library typing module, providing runtime support for type hints as specified by PEP 484 and subsequent PEPs."""

    homepage = "https://github.com/python/typing_extensions"
    pypi = "typing_extensions/typing_extensions-4.7.1.tar.gz"

    maintainers("EbiArnie", "thiagogenez")

    version("4.8.0rc1", sha256="86b48a88e428cbd88382fb599b8101363c3d92799f965f6b634183367cca1526")
    version("4.7.1", sha256="b75ddc264f0ba5615db7ba217daeb99701ad295353c45f9e95963337ceeeffb2")
    version("4.7.0rc1", sha256="3c2c2cd887648efa0ea8f8ba4260a1213058e8e4a25a6a6f4e084740b2c858e2")
    version("4.7.0", sha256="935ccf31549830cda708b42289d44b6f74084d616a00be651601a4f968e77c82")
    version("4.6.3", sha256="d91d5919357fe7f681a9f2b5b4cb2a5f1ef0a1e9f59c4d8ff0d3491e05c0ffd5")

    depends_on("python@3.7:", type=("build", "run"))
    depends_on("py-flit-core", type="build")
    


