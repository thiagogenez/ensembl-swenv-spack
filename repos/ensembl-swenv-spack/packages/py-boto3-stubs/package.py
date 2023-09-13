# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class PyBoto3Stubs(PythonPackage):
    """Type annotations for boto3 compatible with VSCode, PyCharm, Emacs, Sublime Text, mypy, pyright and other tools."""

    homepage = "https://github.com/youtype/mypy_boto3_builder"
    pypi = "boto3-stubs/boto3-stubs-1.28.42.tar.gz"

    maintainers("EbiArnie", "thiagogenez")

    version("1.28.43", sha256="9f41d92906629752f36d91c6c18e54c8d00a0b5df9f1bfe96d9cd3b159bfab95")
    version("1.28.42", sha256="496075f1de47e3984d9a367798d2c46ae7405fa0142b2668ba3ff2f2c2982b3f")
    version("1.28.41", sha256="c2023e441cd4017f914d0e6531536bff0869a72b0d83eceeae830534731dd932")
    version("1.28.40", sha256="76079a82f199087319762c931f13506e02129132e80257dab0888d3da7dc11c7")
    version("1.28.39", sha256="5821845cbda06c26745f0515c8f8b2bb85fef1d1a537892b4b57f8a1d68dc01b")

    variant("s3", default=False, description="enable mypy-boto3-s3 support")
    variant("sdb", default=False, description="enable mypy-boto3-sdb support")
    variant("sts", default=False, description="enable mypy-boto3-sts support")
    variant("iam", default=False, description="enable mypy-boto3-sts support")
    variant("boto3", default=False, description="enable boto3 support")

    depends_on("python@3.7:", type=("build", "run"))
    depends_on("py-setuptools", type="build")
    depends_on("py-botocore-stubs", type=("build", "run"))
    depends_on("py-types-s3transfer", type=("build", "run"))
    depends_on("py-typing-extensions@4.1.0:", when="python@:3.12", type=("build", "run"))

    # extra dependencies
    depends_on("py-mypy-boto3-s3@1.28.0:", when="+s3", type=("build", "run"))
    depends_on("py-mypy-boto3-sdb@1.28.0:", when="+sdb", type=("build", "run"))
    depends_on("py-mypy-boto3-sts@1.28.0:", when="+sts", type=("build", "run"))
    depends_on("py-mypy-boto3-iam@1.28.0:", when="+iam", type=("build", "run"))
    depends_on("py-boto3@1.28.42", when="+boto3", type=("build", "run"))
    depends_on("py-botocore@1.31.42", when="+boto3", type=("build", "run"))
