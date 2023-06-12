# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class PyStarlette(PythonPackage):
    """The little ASGI library that shines."""

    homepage = "https://github.com/encode/starlette"
    pypi = "starlette/starlette-0.23.1.tar.gz"

    version("0.23.1", sha256="8510e5b3d670326326c5c1d4cb657cc66832193fe5d5b7015a51c7b1e1b1bf42")
    version("0.22.0", sha256="b092cbc365bea34dd6840b42861bdabb2f507f8671e642e8272d2442e08ea4ff")
    version("0.14.2", sha256="7d49f4a27f8742262ef1470608c59ddbc66baf37c148e938c7038e6bc7a998aa")

    depends_on("python@3.7:", type=("build", "run"))
    depends_on("py-setuptools", type=("build", "run"))
    depends_on("py-hatchling", type="build")

    depends_on("py-anyio@3.4:4", type=("build", "run"))
    depends_on("py-typing-extensions@3.10.0:", when="^python@:3.9", type=("build", "run"))
