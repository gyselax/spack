# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Gyselalibxx(CMakePackage):
    """Gyselalib++ is a collection of C++ components for writing
    gyrokinetic semi-Lagrangian codes and similar."""

    homepage = "https://gyselax.github.io/gyselalibxx/"
    git = "https://github.com/gyselax/gyselalibxx.git"
    url = "https://github.com/gyselax/gyselalibxx/archive/refs/tags/v0.7.0.tar.gz"

    maintainers("EmilyBourne", "tpadioleau")

    license("MIT", checked_by="tpadioleau")

    version("devel", branch="devel", no_cache=True)
    version("0.7.0", sha256="5ceefeaa6c47e8e6fa373d3b1ca6089c6e0639c9ce1dfb696157e9f0536a356a")

    # variant("tests", default=False, description="Build the tests")

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("cmake@3.25:4", type="build")

    depends_on("ddc +fft +pdi +splines")
    depends_on("ddc@0.14", when="@0.8:")
    depends_on("ddc@0.11", when="@0.7")
    depends_on("ginkgo@1.8:1")
    depends_on("gmgpolar@2.3.1:2")
    depends_on("kokkos@4.4.1:4")
    depends_on("kokkos-kernels@4.5.1:4")
    depends_on("koliop@0.1.2:0.1")
    depends_on("lapack")
    depends_on("mpi")
    depends_on("paraconf@1")
    depends_on("pdi@1.10.1:1")

    requires(
        "^kokkos +cuda_constexpr",
        when="^kokkos +cuda",
        msg="Gyselalib++ relies on the constexpr support of nvcc",
    )

    # with when("+tests"):
    #     depends_on("googletest@1.12:1 +gmock")
    #     depends_on("pdiplugin-decl-hdf5")
    #     depends_on("pdiplugin-mpi")
    #     depends_on("pdiplugin-set-value")
    #     depends_on("python@3")
    #     depends_on("py-dask")
    #     depends_on("py-h5py")
    #     depends_on("py-matplotlib")
    #     depends_on("py-numpy")
    #     depends_on("py-pyyaml")
    #     depends_on("py-xarray")

    def cmake_args(self):
        args = [
            self.define("GYSELALIBXX_BUILD_SIMULATIONS", True),
            self.define_from_variant("GYSELALIBXX_BUILD_TESTING", "tests"),
            self.define("GYSELALIBXX_ENABLE_DEPRECATED", False),
            self.define("GYSELALIBXX_ACTIVATE_RESTART_TESTS", False),
            self.define("GYSELALIBXX_COMPILE_SOURCE", True),
        ]

        if self.spec.satisfies("^kokkos+cuda"):
            args.append(self.define("CMAKE_CXX_FLAGS", "-fno-ipa-sra"))

        if self.spec.satisfies("^kokkos+rocm"):
            args.append(self.define("CMAKE_CXX_COMPILER", self.spec["hip"].hipcc))
        else:
            args.append(self.define("CMAKE_CXX_COMPILER", self["kokkos"].kokkos_cxx))

        return args
