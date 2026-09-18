# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyScimba(PythonPackage):
    """This library implements some common tools for scientific machine learning."""

    homepage = "https://www.scimba.org"
    pypi = "scimba/scimba-1.3.4.tar.gz"

    # maintainers("")

    license("MIT", checked_by="tpadioleau")

    version("1.3.4", sha256="7b555633c577c043b73417f86a85ca2c71837e4310fc114de7ada31a1f60a755")

    variant("jax", default=False, description="Install the experimental JAX backend")

    depends_on("py-setuptools@61.2:", type="build")

    with default_args(type=("build", "run")):
        depends_on("python@3.10:", when="@1.0.0:")
        depends_on("py-matplotlib")
        depends_on("py-numpy")
        depends_on("py-scipy")
        depends_on("py-tqdm")
        depends_on("py-torch@2.9:")

        with when("+jax"):
            depends_on("py-jax@0.6.2:")
            depends_on("py-equinox@0.13:")
            depends_on("py-optax")
            depends_on("py-jax-tqdm")
