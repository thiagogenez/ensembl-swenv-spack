# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class PyToil(PythonPackage):
    """Pipeline management software for clusters."""

    homepage = "https://github.com/DataBiosphere/toil"
    pypi = "toil/toil-5.12.0.tar.gz"

    maintainers("EbiArnie", "thiagogenez")

    version("5.12.0", sha256="fb21c85b8654b0e628087ebd403fa5f53644d86a33a4c1e039ba5769dcaf6654")
    version("5.11.0", sha256="b5565ab9251f58c06c4ae5617e4484961e6923974d0e1bc4356a61f71ec8ea19")
    version("5.9.2", sha256="15018c0215448890c4a6ea4e4a122791bab7ab200424831c0a4eacaa57df0120")

    variant("aws", default=False, description="enable AWS support")

    depends_on("py-setuptools", type="build")
    depends_on("py-dill@0.3.2:0.4", type=("build", "run"))
    depends_on("py-requests@2:3", type=("build", "run"))
    depends_on("py-urllib3@1.26.0:2.0.0", type=("build", "run"))
    depends_on("py-python-dateutil", type=("build", "run"))
    depends_on("py-psutil@3.0.1:6", type=("build", "run"))
    depends_on("py-tes@0.4.2:1", type=("build", "run"))
    depends_on("py-pubsub@4.0.3:", type=("build", "run"))
    depends_on("py-addict@2.2.1:2.5", type=("build", "run"))
    depends_on("py-pytz@2012:", type=("build", "run"))
    depends_on("py-enlighten@1.5.2:2", type=("build", "run"))
    depends_on("py-typing-extensions@4.6.2:5", type=("build", "run"))

    # aws variant
    depends_on("py-boto@2.48:3", when="+aws", type=("build", "run"))
    depends_on(
        "py-boto3-stubs@1.28.3.post2:2+s3+sdb+sts+iam+boto3", when="+aws", type=("build", "run")
    )
    depends_on("py-mypy-boto3-iam@1.28.3.post2:2", when="+aws", type=("build", "run"))
    depends_on("py-moto@4.1.11:5", when="+aws", type=("build", "run"))
