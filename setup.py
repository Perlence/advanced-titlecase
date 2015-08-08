from setuptools import setup

with open('README.md') as fp:
    README = fp.read()

setup(
    name='advanced-titlecase',
    version='1.0',
    author='Sviatoslav Abakumov',
    author_email='dust.harvesting@gmail.com',
    description='Capitalize English titles.',
    long_description=README,
    url='https://github.com/Perlence/advanced-titlecase',
    download_url='https://github.com/Perlence/advanced-titlecase/archive/master.zip',
    py_modules=['advanced_titlecase'],
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'atc = advanced_titlecase:main',
        ],
    },
    tests_require=[
        'nose',
    ],
    test_suite='nose.collector',
    classifiers=[
        'Development Status :: 3 - Stable',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: BSD License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python',
        'Topic :: System :: Shells',
    ]
)
