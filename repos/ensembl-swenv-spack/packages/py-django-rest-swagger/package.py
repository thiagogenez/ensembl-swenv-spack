# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
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
#     spack install py-django-rest-swagger
#
# You can edit this file again by typing:
#
#     spack edit py-django-rest-swagger
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class PyDjangoRestSwagger(PythonPackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    pypi = "django-rest-swagger/django-rest-swagger-2.2.0.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers("github_user1", "github_user2")

    version("2.2.0", sha256="48f6aded9937e90ae7cbe9e6c932b9744b8af80cc4e010088b3278c700e0685b")

    # FIXME: Only add the python/pip/wheel dependencies if you need specific versions
    # or need to change the dependency type. Generic python/pip/wheel dependencies are
    # added implicity by the PythonPackage base class.
    depends_on("python@3:", type=("build", "run"))
    # depends_on("py-pip@X.Y:", type="build")
    # depends_on("py-wheel@X.Y:", type="build")

    # FIXME: Add a build backend, usually defined in pyproject.toml. If no such file
    # exists, use setuptools.
    depends_on("py-setuptools", type="build")
    # depends_on("py-flit-core", type="build")
    # depends_on("py-poetry-core", type="build")

    # FIXME: Add additional dependencies if required.
    # depends_on("py-foo", type=("build", "run"))
    depends_on("py-django@2.1.3", type=("run"))
    depends_on("py-djangorestframework@3.9.0", type=("run"))
    depends_on("py-coreapi@2.3.3", type=("run"))
    depends_on("py-openapi-codec@1.3.2", type=("run"))
    depends_on("py-simplejson@3.9.0", type=("run"))
    depends_on("py-tox@2.4.1", type=("run"))
    depends_on("py-pylint@1.8.4", type=("run"))
    depends_on("py-coverage@4.5.1", type=("run"))
    depends_on("py-ipdb@0.10.1", type=("run"))
    depends_on("py-mkdocs@0.15.3", type=("run"))
    depends_on("py-dj_database_url@0.5.0", type=("run"))
    depends_on("py-psycopg2@2.7.4", type=("run"))
    depends_on("py-gunicorn@19.8.0", type=("run"))
    depends_on("py-whitenoise@3.3.1", type=("run"))

    def global_options(self, spec, prefix):
        # FIXME: Add options to pass to setup.py
        # FIXME: If not needed, delete this function
        options = []
        return options

    def install_options(self, spec, prefix):
        # FIXME: Add options to pass to setup.py install
        # FIXME: If not needed, delete this function
        options = []
        return options
