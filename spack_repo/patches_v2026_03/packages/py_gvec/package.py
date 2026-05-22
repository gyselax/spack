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
#     spack install py-gvec
#
# You can edit this file again by typing:
#
#     spack edit py-gvec
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyGvec(PythonPackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"

    # FIXME: ensure the package is not available through PyPI. If it is,
    # re-run `spack create --force` with the PyPI URL.
    pypi = "gvec/gvec-1.3.1.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers("github_user1", "github_user2")

    # FIXME: Add the SPDX identifier of the project's license below.
    # See https://spdx.org/licenses/ for a list. Upon manually verifying
    # the license, set checked_by to your Github username.
    # license("UNKNOWN", checked_by="github_user1")

    version("1.3.1", sha256="40b60a565eda6838dde5084e26aa869d23fc0fb5f4295b87bb32d4dbb7bf6487")

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("fortran", type="build")

    depends_on("py-scikit-build-core", type="build")
    depends_on("py-setuptools-scm", type="build")
    depends_on("py-f90wrap", type=("build", "run"))
    depends_on("py-f90nml", type=("build", "run"))

    depends_on("pkg-config", type="build")

    depends_on("lapack")
    depends_on("python@3:")
    depends_on("py-numpy@2:")
    depends_on("netcdf-fortran")
    depends_on("netcdf-c")

    depends_on("py-matplotlib", type=("build", "run"))
    depends_on("py-requests", type=("build", "run"))
    depends_on("py-scipy", type=("build", "run"))
    depends_on("py-tqdm", type=("build", "run"))
    depends_on("py-xarray", type=("build", "run"))
    depends_on("py-pyevtk", type=("build", "run"))
