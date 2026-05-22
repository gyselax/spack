# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install py-pyevtk
#
# You can edit this file again by typing:
#
#     spack edit py-pyevtk
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPyevtk(PythonPackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"

    pypi = "pyevtk/pyevtk-1.6.0.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers("github_user1", "github_user2")

    # # FIXME: Add the SPDX identifier of the project's license below.
    # # See https://spdx.org/licenses/ for a list. Upon manually verifying
    # # the license, set checked_by to your Github username.
    # license("UNKNOWN", checked_by="github_user1")

    # FIXME: Add proper versions here.
    version("1.6.0", sha256="1f6be7876a3a005c8258861551da4fe7e44ff1a2e7ff2a93d6dc51deedfda5f4")

    # FIXME: Only add the python/pip/wheel dependencies if you need specific versions
    # or need to change the dependency type. Generic python/pip/wheel dependencies are
    # added implicity by the PythonPackage base class.
    # depends_on("python@2.X:2.Y,3.Z:", type=("build", "run"))
    # depends_on("py-pip@X.Y:", type="build")
    # depends_on("py-wheel@X.Y:", type="build")

    depends_on("py-setuptools", type="build")

    # FIXME: Add additional dependencies if required.
    depends_on("py-numpy@1.8:", type=("build", "run"))
