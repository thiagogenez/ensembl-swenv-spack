# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install perl-devel-checklib
#
# You can edit this file again by typing:
#
#     spack edit perl-devel-checklib
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class PerlDevelChecklib(PerlPackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url = "https://cpan.metacpan.org/authors/id/M/MA/MATTN/Devel-CheckLib-1.16.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers("github_user1", "github_user2")

    version("1.16", sha256="869d38c258e646dcef676609f0dd7ca90f085f56cf6fd7001b019a5d5b831fca")

    # FIXME: Add dependencies if required:
    depends_on("perl-extutils-makemaker", type=("build", "run"))
    depends_on("perl-text-parsewords", type=("run"))
    depends_on("perl-pathtools", type=("run"))
    depends_on("perl-file-temp", type=("run"))
    depends_on("perl-capture-tiny", type=("build","test"))
    depends_on("perl-mock-config", type=("build","test"))
