# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyGyselaXpp(PythonPackage):
    """Gysela-X++ tools"""

    homepage = "https://gyselax.github.io"
    git = "git@gitlab.maisondelasimulation.fr:gysela-developpers/Gysela-X.git"
    # pypi = ""

    maintainers("tpadioleau")

    license("MIT", checked_by="tpadioleau")

    version("develop", branch="external-gyselalibxx", no_cache=True)

    build_directory = "processing"

    depends_on("py-setuptools@61:", type="build")

    depends_on("python@3.11:3", type=("build", "run"))
    depends_on("py-dask +distributed", type=("build", "run"))
    depends_on("py-gysmc", type=("build", "run"))
    depends_on("py-h5py", type=("build", "run"))
    depends_on("py-imageio", type=("build", "run"))
    depends_on("py-matplotlib", type=("build", "run"))
    depends_on("py-numexpr", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-psutil", type=("build", "run"))
    depends_on("py-pyyaml", type=("build", "run"))
    depends_on("py-xarray +io +parallel", type=("build", "run"))
