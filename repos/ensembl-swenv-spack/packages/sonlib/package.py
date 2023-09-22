# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


import os, shutil

from spack.package import *


class Sonlib(MakefilePackage):
    """SonLib is a compact C/Python library for sequence analysis in bioinformatics."""

    homepage = "https://github.com/ComparativeGenomicsToolkit/sonLib"
    git = "https://github.com/ComparativeGenomicsToolkit/sonLib.git"

    maintainers("EbiArnie", "thiagogenez")

    version("9734083", commit="9734083dffb180e3d76c323609c082b401336c0a")

    variant("hiredis", default=True, description="Enable hiredis database support")

    depends_on("pkg-config", type=("build"))
    depends_on("hiredis", when="+hiredis", type=("build", "link"))

    def edit(self, spec, prefix):
        makefiles = ["Makefile", "externalTools/cutest/Makefile", "externalTools/Makefile"]
        for i in makefiles:
            makefile = FileFilter(i)
            makefile.filter(r"BINDIR =", "BINDIR ?=")
            makefile.filter(r"LIBDIR =", "LIBDIR ?=")

    def setup_build_environment(self, env):
        build = {
            "BINDIR": join_path(self.stage.path, "bin"),
            "LIBDIR": join_path(self.stage.path, "lib"),
        }
        for k, v in build.items():
            mkdirp(v)
            env.set(k, v)

    def install(self, spec, prefix):
        # Manually libs, headers, binaries by moving it from stage to prefix
        mkdirp(prefix.include)
        mkdirp(prefix.lib)
        mkdirp(prefix.bin)

        for header in find(env["LIBDIR"], "*.h"):
            install(header, prefix.include)

        for lib in find(env["LIBDIR"], "*.a"):
            install(lib, prefix.lib)

        for bin in find(env["BINDIR"], "*"):
            install(bin, prefix.bin)

    @run_before("install")
    def cleanup(self):
        for rubbish in find(env["BINDIR"], "*.dSYM"):
            shutil.rmtree("{0}".format(rubbish))
