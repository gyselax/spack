# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyGysmc(PythonPackage):
    """f90wrap is a tool to automatically generate Python extension
    modules which interface to Fortran code that makes use of derived types."""

    homepage = "https://github.com/gyselax/gysela_magnet_conf"
    git = "https://github.com/gyselax/gysela_magnet_conf.git"
    # pypi = ""

    license("MIT", checked_by="tpadioleau")

    version("main", branch="main")

    depends_on("py-setuptools@65:", type="build")
    depends_on("py-setuptools-scm@8: +toml", type="build")

    depends_on("python@3.9:", type=("build", "run"))
    depends_on("py-numpy@1.22:", type=("build", "run"))
    depends_on("py-scipy@1.3:", type=("build", "run"))
