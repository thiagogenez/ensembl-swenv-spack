# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class PyTypesS3transfer(PythonPackage):
    """Type annotations and code completion for s3transfer package."""

    homepage = "https://youtype.github.io/mypy_boto3_builder/"
    pypi = "types_s3transfer/types_s3transfer-0.6.2.tar.gz"

    maintainers("EbiArnie", "thiagogenez")

    version("0.6.2", sha256="4ba9b483796fdcd026aa162ee03bdcedd2bf7d08e9387c820dcdd158b0102057")
    version("0.6.1", sha256="75ac1d7143d58c1e6af467cfd4a96c67ee058a3adf7c249d9309999e1f5f41e4")

    depends_on("python@3.7:", type=("build", "run"))
    depends_on("py-poetry-core", type="build")
