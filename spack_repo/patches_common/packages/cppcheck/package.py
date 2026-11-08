# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Cppcheck(CMakePackage):
    """A tool for static C/C++ code analysis."""

    homepage = "https://cppcheck.sourceforge.net/"
    git = "https://github.com/cppcheck-opensource/cppcheck.git"
    url = "https://github.com/cppcheck-opensource/cppcheck/archive/refs/tags/2.22.0.tar.gz"

    maintainers("white238")

    license("GPL-3.0-or-later")

    version("2.22.0", sha256="d74945deb2d50393430e07596b766f8a779512c7f60dac2a30ea64e059ece57b")

    variant("rules", default=False, description="Enable rules (requires PCRE)")

    depends_on("cxx", type="build")

    depends_on("pcre", when="+rules", type="build")
    depends_on("py-pygments", type="run")
    extends("python")

    def cmake_args(self):
        return [
            self.define("BUILD_TESTS", self.run_tests),
            self.define_from_variant("HAVE_RULES", "rules"),
            self.define("USE_MATCHCOMPILER", True),
        ]
