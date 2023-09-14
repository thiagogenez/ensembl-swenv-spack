# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class PyMypyBoto3Sdb(PythonPackage):
    """Type annotations for boto3.SimpleDB service compatible with VSCode, PyCharm, Emacs, Sublime Text, mypy, pyright and other tools."""

    homepage = "https://github.com/youtype/mypy_boto3_builder"
    pypi = "mypy-boto3-sdb/mypy-boto3-sdb-1.28.36.tar.gz"

    maintainers("EbiArnie", "thiagogenez")

    version("1.28.36", sha256="a5b1f9cbf6d2d794ba05e4cf219d1bc3c8747a57cb78775a6ff231245e033585")
    version("1.28.16", sha256="543025f1e8f5486d7064a60699dec9182dcc478ca8ec1609a6252e8f250c502f")
    version(
        "1.28.15.post1", sha256="49955f467e706ec0aa5f64559eb724093d355b77e635743870b0e383cd474d3c"
    )
    version("1.28.15", sha256="e91e802c8908cc99c43c79af1cfb322209c828b58126e3349292223d4013ce11")
    version("1.28.12", sha256="cbcfb63385d43ceba898301f503e85bc40362b8a26e994161d063f49e24d155f")

    depends_on("python@3.7:", type=("build", "run"))
    depends_on("py-setuptools", type="build")
    depends_on("py-typing-extensions@4.1.0:", when="python@:3.12", type=("build", "run"))
