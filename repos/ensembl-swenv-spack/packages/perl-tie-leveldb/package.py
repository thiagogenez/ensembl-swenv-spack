# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
from spack.package import *


class PerlTieLeveldb(PerlPackage):
    """Tie::LevelDB - A Perl Interface to the Google LevelDB NoSQL database"""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://metacpan.org/pod/Tie::LevelDB"
    url = "https://cpan.metacpan.org/authors/id/S/SA/SARFY/Tie-LevelDB-0.07.tar.gz"

    maintainers("EbiArnie")

    version("0.07", sha256="6dbb24e260ad141e0c9baf932354cdbd41cb02b688faced190e017759c6df653")

    depends_on("snappy", type=("build", "link", "run"))
    depends_on("perl-extutils-makemaker", type=("build", "link"))

#    def configure_args(self):
#        args = []
#        return args
