# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class PyBotocoreStubs(PythonPackage):
    """Type annotations and code completion for botocore package."""

    homepage = "https://youtype.github.io/mypy_boto3_builder/"
    pypi = "botocore_stubs/botocore_stubs-1.31.42.tar.gz"

    maintainers("EbiArnie", "thiagogenez")

    version("1.31.43", sha256="fe0ec981be961be6d35b0c5bae7aad1e650baa3e001d70ca9f971db0fbdeb223")
    version("1.31.42", sha256="215a55fe840fe621d7fe6406bbe369ea98443340b6ce233961b17f20ae61869f")
    version("1.31.41", sha256="8738438ba52a6d97b3f5491290b72f5165d8be10d2e8f50a473081bb1eb1447a")
    version("1.31.40", sha256="2001a253daf4ae2e171e6137b9982a00a7fbfc7a53449a16856dc049e7cd5214")
    version("1.31.39", sha256="a6aa469cf5d94f99439d3a5705fb09934fed06d528be06b301665ffd36497cd8")


    depends_on("python@3.7:", type=("build", "run"))
    depends_on("py-poetry-core", type="build")
    depends_on("py-types-awscrt", type=("build", "run"))
    depends_on("py-typing-extensions@4.1.0:", when="python@:3.9", type=("build", "run"))
