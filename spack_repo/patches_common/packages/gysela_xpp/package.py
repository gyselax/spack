# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class GyselaXpp(CMakePackage):
    """Gysela-X++"""

    homepage = "https://gyselax.github.io"
    git = "git@gitlab.maisondelasimulation.fr:gysela-developpers/Gysela-X.git"

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

    depends_on("googletest@1.12:1 +gmock", type="test")
    depends_on("pdiplugin-decl-hdf5 +mpi", type="test")
    depends_on("pdiplugin-decl-netcdf +mpi", type="test")
    depends_on("pdiplugin-mpi", type="test")
    depends_on("pdiplugin-pycall", type="test")
    depends_on("python@3.11:3", type="test")
    depends_on("py-dask +distributed", type="test")
    depends_on("py-gysmc", type="test")
    depends_on("py-h5py", type="test")
    depends_on("py-imageio", type="test")
    depends_on("py-matplotlib", type="test")
    depends_on("py-numpy", type="test")
    depends_on("py-numexpr", type="test")
    depends_on("py-netcdf4 +mpi", type="test")
    depends_on("py-pip", type="test")
    depends_on("py-psutil", type="test")
    depends_on("py-xarray", type="test")
    depends_on("py-pyyaml", type="test")

    def cmake_args(self):
        args = [
            self.define("GYSELAX_BUILD_DOCUMENTATION", False),
            self.define("GYSELAX_BUILD_SIMULATIONS", True),
            self.define("GYSELAX_BUILD_TESTING", self.run_tests),
            self.define("GYSELAX_USE_EXTERNAL_GYSELALIBXX", True),
        ]

        if self.spec.satisfies("^kokkos+rocm"):
            args.append(self.define("CMAKE_CXX_COMPILER", self.spec["hip"].hipcc))
        else:
            args.append(self.define("CMAKE_CXX_COMPILER", self["kokkos"].kokkos_cxx))

        return args
