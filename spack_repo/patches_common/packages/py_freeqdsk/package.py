# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyFreeqdsk(PythonPackage):
    """"""

    homepage = "https://freeqdsk.readthedocs.io/"
    git = "https://github.com/freegs-plasma/FreeQDSK.git"
    pypi = "freeqdsk/freeqdsk-0.5.2.tar.gz"

    license("MIT", checked_by="tpadioleau")

    version("main", branch="main")
    version("0.5.2", sha256="a43a0aadfc2d68a03523ecafd6c542f3ddef256b20b7b02fcb36eaace85026ab")

    depends_on("py-setuptools@65:", type="build")
    depends_on("py-setuptools-scm@8: +toml", type="build")

    depends_on("python@3.9:", type=("build", "run"))
    depends_on("py-numpy@1.22:", type=("build", "run"))
    depends_on("py-fortranformat@2", type=("build", "run"))
