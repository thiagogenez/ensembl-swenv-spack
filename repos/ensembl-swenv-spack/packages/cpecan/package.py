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
#     spack install cpecan
#
# You can edit this file again by typing:
#
#     spack edit cpecan
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

import os,shutil

from spack.package import *


class Cpecan(MakefilePackage):
    """FIXME: Put a proper description of your package here."""

    homepage = "https://github.com/ComparativeGenomicsToolkit/cPecan"
    git = "https://github.com/ComparativeGenomicsToolkit/cPecan.git"

    maintainers("EbiArnie", "thiagogenez")

    version("af9c597", commit="af9c59789e997d7a38723e567cc4c62394679cdd")

    variant("hiredis", default=True, description="Enable hiredis database support")

    depends_on("sonlib", type=("build", "link"))
    depends_on("llvm-openmp", type=("build","link"),  when="platform=darwin")
    depends_on("hiredis", when="+hiredis", type=("build", "link"))


    def edit(self, spec, prefix):

        include_mk = FileFilter("include.mk")
        include_mk.filter("include","#include")
        include_mk.filter("CPPFLAGS","#CPPFLAGS")

        pairwiseAlignerTest = FileFilter('tests/pairwiseAlignerTest.c')
        pairwiseAlignerTest.filter(r'#include "../../sonLib/lib/multipleAligner.h"',  '')
        
        make_include = FileFilter("externalTools/lastz-distrib-1.03.54/make-include.mak")
        make_include.filter("installDir.*","installDir = {0}".format(os.environ.get("BINDIR")))        

        

    def setup_build_environment(self, env):
        build = {
            "BINDIR": join_path(self.stage.path, "bin"),
            "LIBDIR": join_path(self.stage.path, "lib"),
        }
        for k, v in build.items():
            mkdirp(v)
            env.set(k, v)

        # pointer to sonlib dependency
        env.set("sonLibRootDir", "{0}".format(self.spec['sonlib'].prefix))

        # from include.mk of sonlib
        env.set("RANLIB", "ranlib")
        env.set("dblibs", "-lz -lm")
        env.append_flags("CXXFLAGS","-fPIC -O3 -g -Wall --pedantic -funroll-loops -DNDEBUG")
        env.append_flags("CFLAGS", "-fPIC -std=c99 -O3 -g -Wall -funroll-loops -DNDEBUG")
        env.append_flags("CPPFLAGS", "-Iinc -Iimpl -fsigned-char")
        

    def build(self, spec, prefix):
        make(parallel=True)

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
