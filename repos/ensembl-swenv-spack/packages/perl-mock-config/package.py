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
#     spack install perl-mock-config
#
# You can edit this file again by typing:
#
#     spack edit perl-mock-config
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class PerlMockConfig(PerlPackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url = "https://cpan.metacpan.org/authors/id/R/RU/RURBAN/Mock-Config-0.03.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers("github_user1", "github_user2")

    version("0.03", sha256="a5b8345757ca4f2b9335f5be14e93ebbb502865233a755bf53bc7156deec001b")

    # FIXME: Add dependencies if required:
    depends_on("perl-extutils-makemaker", type=("build"))
    depends_on("perl-test-more", type=("test"))

