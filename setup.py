#!/usr/bin/env python
import os
import sys

if sys.version_info < (3, 6):
    print('Error: dbt does not support this version of Python.')
    print('Please upgrade to Python 3.6 or higher.')
    sys.exit(1)


from setuptools import setup
try:
    from setuptools import find_namespace_packages
except ImportError:
    # the user has a downlevel version of setuptools.
    print('Error: dbt requires setuptools v40.1.0 or higher.')
    print('Please upgrade setuptools with "pip install --upgrade setuptools" '
          'and try again')
    sys.exit(1)

this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, 'README.md')) as f:
    long_description = f.read()


package_name = "dbt"
# package_version = "0.19.0b1"
# Otherwise dbt-utils seems not to work.
package_version = "0.18.1"
description = """With dbt, data analysts and engineers can build analytics \
the way engineers build applications."""


setup(
    name=package_name,
    version=package_version,

    description=description,
    long_description=long_description,
    long_description_content_type='text/markdown',

    author="Fishtown Analytics",
    author_email="info@fishtownanalytics.com",
    url="https://github.com/fishtown-analytics/dbt",
    # These two lines added so we can install dbt-bigquery from this repo,
    # rather than PyPI.
    packages=['dbt-bigquery'],
    package_dir={'dbt-bigquery': 'plugins/bigquery'},
    install_requires=[
        'dbt-core=={}'.format(package_version),
        'dbt-postgres=={}'.format(package_version),
        'dbt-redshift=={}'.format(package_version),
        'dbt-snowflake=={}'.format(package_version),
        # copied from dbt-bigquery, since setuptools doesn't seem to respect
        # sub-packages `install_requires`?
        'protobuf>=3.13.0,<4',
        'google-cloud-core>=1.3.0,<2',
        'google-cloud-bigquery>=1.25.0,<2',
        'google-api-core>=1.16.0,<2',
        'googleapis-common-protos>=1.6.0,<2',
        'six>=1.14.0',
    ],
    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',

        'License :: OSI Approved :: Apache Software License',

        'Operating System :: Microsoft :: Windows',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX :: Linux',

        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    python_requires=">=3.6.2",
)
