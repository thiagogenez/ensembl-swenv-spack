# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class PyMypyBoto3Iam(PythonPackage):
    """Type annotations for boto3.IAM service generated with mypy-boto3-builder"""

    homepage = "https://github.com/youtype/mypy_boto3_builder"
    pypi = "mypy-boto3-iam/mypy-boto3-iam-1.28.37.tar.gz"

    maintainers("EbiArnie", "thiagogenez")

    version("1.28.37", sha256="39bd5b8b9a48cb47d909d45c13c713c099c2f84719612a0a848d7a0497c6fcf4")
    version(
        "1.28.36.post1", sha256="6d31da063d1095bf5e5efedea3cce10f0682a809b5d561bae9420ffe230239a5"
    )
    version("1.28.36", sha256="a661a5e8eedec75d2c1171bcc16fba9a46a12dba83b5732d8777ec2f4f062dd7")
    version("1.28.16", sha256="8ef9ef9a9fabcc1058a46bbd6b1408960a70d72e45a024862676e5a896c446b3")
    version(
        "1.28.15.post1", sha256="7ff0ac23fd99cc44fefe975b09b06e8bd77cd300a6b91c55a92a46de21495dad"
    )

    depends_on("python@3.7:", type=("build", "run"))
    depends_on("py-setuptools", type="build")
    depends_on("py-typing-extensions@4.1.0:", when="python@:3.12", type=("build", "run"))
