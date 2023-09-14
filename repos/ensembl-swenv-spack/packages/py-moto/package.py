# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class PyMoto(PythonPackage):
    """Moto is a library that allows your tests to easily mock out AWS Services."""

    homepage = "https://github.com/getmoto/moto"
    pypi = "moto/moto-4.2.2.tar.gz"

    maintainers("EbiArnie", "thiagogenez")

    version("4.2.2", sha256="ee34c4c3f53900d953180946920c9dba127a483e2ed40e6dbf93d4ae2e760e7c")

    depends_on("python@3.7:", type=("build", "run"))
    depends_on("py-setuptools", type="build")
    depends_on("py-boto3@1.9.201:", type=("build", "run"))
    depends_on("py-botocore@1.12.201:", type=("build", "run"))
    depends_on("py-cryptography@3.3.1:", type=("build", "run"))
    depends_on("py-requests@2.5:", type=("build", "run"))
    depends_on("py-xmltodict", type=("build", "run"))
    depends_on("py-werkzeug@0.5:2.1.0,2.2.2:", type=("build", "run"))
    depends_on("py-python-dateutil@0:3.0.0,2.1:", type=("build", "run"))
    depends_on("py-responses@0.13.0:", type=("build", "run"))
    depends_on("py-jinja2@2.10.1:", type=("build", "run"))
    depends_on("py-importlib-metadata", when="python@:3.8", type=("build", "run"))
