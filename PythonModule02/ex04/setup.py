from setuptools import setup, find_packages

setup(
    name='my-minipack',
    version='1.0.0',
    description='A small example package',
    url=None,
    author='armendes',
    author_email='armendes@student.42.fr',
    license='GPLv3',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Students',
        'Topic :: Education',
        'Topic :: HowTo',
        'Topic :: Package',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only'
    ],
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    python_requires='>=3.6'
)