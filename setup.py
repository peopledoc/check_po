# -*- coding: utf-8 -*-
"""Python packaging."""
from os.path import abspath, dirname, join
from setuptools import setup


def read_relative_file(filename):
    """Returns contents of the given file, which path is supposed relative
    to this module."""
    with open(join(dirname(abspath(__file__)), filename)) as f:
        return f.read()


name = 'check_po'

version = read_relative_file('VERSION').strip()
readme = read_relative_file('README')
requirements = [
    'setuptools',
    'polib',
]

entry_points = {
    'console_scripts': [
        'check_po = check_po.pochecker:main',
        'podiff = check_po.podiff:main',
        'check_urls = check_po.check_urls:main',
    ]
}

if __name__ == '__main__':  # ``import setup`` doesn't trigger setup().
    setup(
        name=name,
        version=version,
        description="""Check_po to verify if everything is translated
                       and that no fuzzy are still here.""",
        long_description=readme,
        classifiers=[
            "License :: Other/Proprietary License",
            "Programming Language :: Python",
            "Programming Language :: Python :: 2.6",
            "Programming Language :: Python :: 2.7",
            "Programming Language :: Python :: 3",
        ],
        keywords='',
        author='Rémy Hubscher',
        author_email='hubscher.remy@gmail.com',
        url='https://github.com/novagile/%s' % name,
        license='WTFPL',
        packages=['check_po'],
        include_package_data=True,
        zip_safe=False,
        install_requires=requirements,
        entry_points=entry_points,
        test_suite='nose.collector',
        setup_requires=['nose'],
        tests_require=['nose', 'coverage']
    )
