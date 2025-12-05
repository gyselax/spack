# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack.package import *


class Koliop(CMakePackage):
    """FIXME: Put a proper description of your package here."""

    homepage = "https://gitlab.com/cines/code.gysela/libkoliop"
    git = "https://gitlab.com/cines/code.gysela/libkoliop.git"
    url = "https://gitlab.com/cines/code.gysela/libkoliop/-/archive/0.0.21/libkoliop-0.0.21.tar.gz"

    maintainers("etiennemlb", "tpadioleau")

    license("MIT", checked_by="tpadioleau")

    version("0.0.21")

    depends_on("kokkos")
    depends_on("kokkos-kernels")

    def cmake_args(self):
        args = [
            self.define("koliop_ASSERT_ENABLED", False),
            self.define("koliop_ASSUME_INPUT_BUFFERS_ARE_DEVICE_COMPATIBLE", True),
            self.define("koliop_BUILD_FORTRAN_INTERFACE", False),
            self.define("koliop_BUILD_TESTING", False),
            self.define("koliop_ENABLE_Kokkos", "SYSTEM"),
            self.define("koliop_ENABLE_KokkosKernels", "SYSTEM"),
            self.define("koliop_ENABLE_LTO", False),
            self.define("koliop_FENCE_ON_OPERATOR_EXIT", True),
            self.define("koliop_RUN_DEMONSTRATION_AS_TEST", False),
        ]
        return args
