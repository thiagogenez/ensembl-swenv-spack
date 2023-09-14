# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class PyMypyBoto3Sts(PythonPackage):
    """Type annotations for boto3.STS service compatible with VSCode, PyCharm, Emacs, Sublime Text, mypy, pyright and other tools."""

    homepage = "https://github.com/youtype/mypy_boto3_builder"
    pypi = "mypy-boto3-sts/mypy-boto3-sts-1.28.37.tar.gz"

    maintainers("EbiArnie", "thiagogenez")

    version("1.28.37", sha256="54d64ca695ab90a51c68ac1e67ff9eae7ec69f926649e320a3b90ed1ec841a95")
    version(
        "1.28.36.post1", sha256="f7403245aa5651b8690b5969329bfded18d6ebdd3d5849c602642274458626e6"
    )
    version("1.28.36", sha256="eea9dd108ff15bd97bbf20d0ea88ba73e3f054ae43ba4ef54d8a0f0de286120c")
    version("1.28.16", sha256="7cd388a7451611813730b83c78179759eb5701b849618d82c3ec7e95576bedb9")
    version(
        "1.28.15.post1", sha256="08d8b6095c41fe4a8e23d7a34d0897e0a102a4572262e237c2a76908c6e7f378"
    )

    depends_on("python@3.7:", type=("build", "run"))
    depends_on("py-setuptools", type="build")
    depends_on("py-typing-extensions@4.1.0:", when="python@:3.12", type=("build", "run"))
