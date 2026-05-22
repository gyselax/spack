# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Gmgpolar(CMakePackage):
    """GMGPolar is a performant geometric multigrid solver using implicit extrapolation to raise the convergence order."""

    homepage = "https://github.com/SciCompMod/GMGPolar"
    git = "https://github.com/SciCompMod/GMGPolar.git"
    url = "https://github.com/SciCompMod/GMGPolar/archive/refs/tags/v2.2.0.tar.gz"

    maintainers("tpadioleau")

    license("Apache-2.0", checked_by="tpadioleau")

    version("main", branch="main", no_cache=True)
    # version("2.2.0", sha256="")

    depends_on("cxx", type="build")
    depends_on("cmake@3.12:", type="build")

    depends_on("kokkos@4.4.1:")
    depends_on("kokkos@:5")

    def cmake_args(self):
        args = [
            self.define("GMGPOLAR_BUILD_TESTS", False),
            self.define("GMGPOLAR_USE_LIKWID", False),
            self.define("GMGPOLAR_USE_MUMPS", False),
            self.define("GMGPOLAR_ENABLE_COVERAGE", False),
        ]

        if self.spec.satisfies("^kokkos+rocm"):
            args.append(self.define("CMAKE_CXX_COMPILER", self.spec["hip"].hipcc))
        else:
            args.append(self.define("CMAKE_CXX_COMPILER", self["kokkos"].kokkos_cxx))

        return args
