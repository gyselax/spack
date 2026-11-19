# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyScimba(PythonPackage):
    """This library implements some common tools for scientific machine learning."""

    homepage = "https://www.scimba.org"
    pypi = "scimba/scimba-1.4.2.tar.gz"

    maintainers("tpadioleau")

    license("MIT", checked_by="tpadioleau")

    version("1.4.2", sha256="b689fc75074aa6ffbb483d6296e0490eac1c06ff160c4888c450136d14c513b3")

    variant("jax", default=False, description="Install the JAX backend")
    variant("torch", default=False, description="Install the PyTorch backend")

    depends_on("py-setuptools@61.2:", type="build")

    depends_on("python@3.11:", type=("build", "run"))
    depends_on("py-matplotlib", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-scipy", type=("build", "run"))
    depends_on("py-tqdm", type=("build", "run"))

    with when("+torch"):
        depends_on("py-torch@2.9:", type=("build", "run"))

    with when("+jax"):
        depends_on("py-jax@0.6.2:", type=("build", "run"))
        depends_on("py-orbax-checkpoint", type=("build", "run"))
        depends_on("py-jax-tqdm", type=("build", "run"))
