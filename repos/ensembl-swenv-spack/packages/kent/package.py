# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Kent(MakefilePackage):
    """UCSC Genome Browser: Kent libs and htslib"""

    homepage = "https://github.com/ucscGenomeBrowser/kent"
    url = "https://github.com/ucscGenomeBrowser/kent/archive/refs/tags/v415_branch.1.tar.gz"
    license = 'This package mainly includes the MIT licensed parts of the Kent distribution. Parts may be under a non-commercial use licens by Kent Informatics. See original LICENSE file for details.'
    maintainers = ["EbiArnie"]

    version("415.1", sha256="85cea727a76b3c37ec22760e5bf17dc84e3794a5e3c1f55039aa4e684ecf9419")
    version("335.1", sha256="a661b6004b83e9a70bd1d17cd1c8599e5c6892f25868c797a5ac20f45c7a28c6")

    # The docs say it needs gcc to build.
    requires("%gcc")

    depends_on("gmake", type='build')
    depends_on("libiconv")
    depends_on("libpng")
    depends_on("mysql-client")
    depends_on("ncurses")
    depends_on("openssl")
    depends_on("rsync")
    depends_on("zlib+pic")

    # TODO - upstream htslib does not work, we need the "ucsc" htslib which
    # includes a specific member field in one of the structs
    #depends_on("ucsc_htslib", when="@335.1")

    cflags = ["-fPIC", "-z muldefs"]

    def url_for_version(self, version):
        url = "https://github.com/ucscGenomeBrowser/kent/archive/refs/tags/v{0}_branch.{1}.tar.gz"
        return url.format(version[0], version[1])

    def edit(self, spec, prefix):
        env['PREFIX'] = prefix
        env["DESTDIR"] = prefix
        env["BINDIR"] = '/bin'
        env["SCRIPTS"] = prefix + '/bin'
        env["CFLAGS"] = " ".join(self.cflags)
        env["MACHTYPE"] = str(spec.target.family)
        env["USE_SSL"] = '1'
        makefile = FileFilter("src/inc/common.mk")
        makefile.filter("ICONVLIB=.*", "ICONVLIB={0}".format(spec["libiconv"].libs.ld_flags))

    # Version 335.1
    @when("@335.1")
    def build(self, spec, prefix):
        env["HTSDIR"] = spec["htslib"].home + '/lib'
        env['USE_HTS'] = '1'
        mkdirp(prefix.bin)
        make("-C", "src/lib")
        make("-C", "src/hg/lib")
        env["DESTDIR"] = ''
        env['PREFIX'] = ''
        env["BINDIR"] = prefix + '/bin'
        make("-C", "src/utils")
        make("-C", "src/hg/mouseStuff/axtBest")
        env["DESTDIR"] = prefix
        env['PREFIX'] = ''
        env["BINDIR"] = '/bin'
        make("-C", "src/", "userApps")

    # Starting with 415.1
    @when("@415.1:")
    def build(self, spec, prefix):
        mkdirp(prefix.bin)
        make("-C", "src/lib")
        make("-C", "src/htslib")
        make("-C", "src/hg/lib")
        env["DESTDIR"] = ''
        env['PREFIX'] = ''
        env["BINDIR"] = prefix + '/bin'
        make("-C", "src/utils")
        make("-C", "src/hg/mouseStuff/axtBest")
        env["DESTDIR"] = prefix
        env['PREFIX'] = ''
        env["BINDIR"] = '/bin'
        make("-C", "src/", "userApps")

    def install(self, spec, prefix):
        machine_lib = 'src/lib/' + str(spec.target.family)
        mkdirp(prefix.inc)
        mkdirp(prefix.lib)
        install_tree('src/inc', prefix.inc)
        install_tree(f'{machine_lib}', prefix.lib)
