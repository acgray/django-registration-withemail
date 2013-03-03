# Copyright 2012 django-registration-withemail authors. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from setuptools import setup, find_packages

README = open('README.md').read()

setup(
		name='django-registration-withemail',
		version='0.1.3',
		description='This is a simple user-registration application for Django, designed to make allowing user signups as painless as possible.',
		packages=find_packages(),
		include_package_data=True,
		license='BSD License',
		long_description=README,
		author='Kamagatos',
		author_email='kamagatos@gmail.com',
	)