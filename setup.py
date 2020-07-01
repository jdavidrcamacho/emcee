#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from setuptools import setup

setup(name='emcee3',
      version='0.3camacho',
      description='mine emcee',
      author='João Camacho',
      author_email='joao.camacho@astro.up.pt',
      license='MIT',
      url='https://github.com/jdavidrcamacho/emcee',
      packages=['emcee3'],
      install_requires=[
        'numpy',
        'scipy'
      ],
     )

