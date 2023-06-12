# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlDbdMysql(PerlPackage):
    """MySQL driver for the Perl5 Database Interface (DBI)"""

    homepage = "https://metacpan.org/pod/DBD::mysql"
    url = "https://cpan.metacpan.org/authors/id/D/DV/DVEEDEN/DBD-mysql-4.050.tar.gz"

    version("4.050", sha256="4f48541ff15a0a7405f76adc10f81627c33996fbf56c95c26c094444c0928d78")
    version("4.043", sha256="629f865e8317f52602b2f2efd2b688002903d2e4bbcba5427cb6188b043d6f99")

    depends_on("perl-test-deep", type=("build", "run"))
    depends_on("perl-dbi", type=("build", "run"))
    # Avoid segfault with 8.0.33 and DBD::mysql 4.050
    # See https://github.com/perl5-dbi/DBD-mysql/issues/352
    depends_on("mysql@:8.0.32", type=("build", "run"))
    depends_on("perl-devel-checklib", type=("build"))
