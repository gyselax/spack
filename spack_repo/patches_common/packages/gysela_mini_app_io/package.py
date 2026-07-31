# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class GyselaMiniAppIo(CMakePackage):
    """Mini-application for IO testing and performance benchmarking"""

    homepage = "https://gyselax.github.io/gyselalibxx/"
    git = "https://github.com/tpadioleau/gysela-mini-app_io.git"

    maintainers("tpadioleau")

    license("MIT", checked_by="tpadioleau")

    version("develop", branch="external-gyselalibxx", no_cache=True)

    depends_on("cxx", type="build")
    depends_on("cmake@3.25:4", type="build")

    depends_on("ddc +pdi")
    depends_on("gyselalibxx")
    depends_on("mpi")
    depends_on("paraconf")
    depends_on("pdi")

    def cmake_args(self):
        args = [
            self.define("GYSELA_MINI_APP_BUILD_SIMULATIONS", True),
        ]

        if self.spec.satisfies("^kokkos+rocm"):
            args.append(self.define("CMAKE_CXX_COMPILER", self.spec["hip"].hipcc))
        else:
            args.append(self.define("CMAKE_CXX_COMPILER", self["kokkos"].kokkos_cxx))

        return args
