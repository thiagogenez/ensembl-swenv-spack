# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class PyTypesAwscrt(PythonPackage):
    """Type annotations and code completion for awscrt package."""

    homepage = "https://github.com/youtype/types-awscrt"
    pypi = "types_awscrt/types_awscrt-0.19.1.tar.gz"

    maintainers("EbiArnie", "thiagogenez")

    version("0.19.1", sha256="61833aa140e724a9098025610f4b8cde3dcf65b842631d7447378f9f5db4e1fd")
    version("0.19.0", sha256="eaef60422cf716b4ae216f164b74d679c82b0d9c53db380a37deb29ae5579b1b")
    version("0.18.0", sha256="c0293b1d149df839930d37bd50e304e8fab29ff92a252a02ebea49cd6e300f99")
    version("0.17.0", sha256="4214783a747af900a5f98ec020d52ecae5910b470fd636813637a45b82a97516")
    version("0.16.26", sha256="011b0efc054cddb542416f4a38452a3cab3f2d6cef7af0cd124c03a89634f101")

    depends_on("python@3.7:", type=("build", "run"))
    depends_on("py-poetry-core", type="build")
