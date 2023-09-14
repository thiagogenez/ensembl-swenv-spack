# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class PyMypyBoto3S3(PythonPackage):
    """Type annotations for boto3.S3 service compatible with VSCode, PyCharm, Emacs, Sublime Text, mypy, pyright and other tools."""

    homepage = "https://github.com/youtype/mypy_boto3_builder"
    pypi = "mypy-boto3-s3/mypy-boto3-s3-1.28.36.tar.gz"

    maintainers("EbiArnie", "thiagogenez")

    version("1.28.36", sha256="44da375fd4d75b1c5ccc26dcd3be48294c7061445efd6d90ebfca43ffebbb3e4")
    version("1.28.27", sha256="f1094344f68d1ffe2b998404e2e4ff9aa4239438692187fa83ad7b734739991c")
    version("1.28.19", sha256="b8104b191924d8672068d21d748c0f8ae0b0e1950324cb315ec8a1ceed9d23ac")
    version("1.28.16", sha256="4e55fdad729b6e6f45211e354bd1a0a745a565fe9d1e462737f775c28849cfb5")
    version(
        "1.28.15.post1", sha256="65502be825789fd16e4cacf10aecd6408554b60ae5d261be60fd46bee69d8592"
    )

    depends_on("python@3.7:", type=("build", "run"))
    depends_on("py-setuptools", type="build")
    depends_on("py-typing-extensions@4.1.0:", when="python@:3.12", type=("build", "run"))
