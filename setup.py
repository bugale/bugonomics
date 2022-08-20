import os
import setuptools


def read(*parts: str) -> str:
    with open(os.path.join(os.path.dirname(__file__), *parts), encoding='utf-8') as file:
        return file.read()


setuptools.setup(
    name='bugonomics',
    version='1.0.0',
    url='https://github.com/bugale/bugonomics',
    license='MIT',
    author='Bugale',
    author_email='bugalit@gmail.com',
    description='A Pytohn library for calculating economics-related stuff.',
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    packages=['bugonomics'],
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=[
    ],
    extras_require={
        'tests': [
            'pytest',
        ],
        'dev': [
            'flake8',
            'mypy',
            'pylint',
            'types-setuptools',
        ],
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX',
        'Operating System :: MacOS',
        'Operating System :: Unix',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.10',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
