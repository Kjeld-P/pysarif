import setuptools

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name='pysarif',
    version="0.1.0",
    author='Kjeld Perquin',
    author_email='kjeld.perquin96@gmail.com',
    description='Package to work with SARIF files as Python objects.',
    keywords='sarif, pysarif, package',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Kjeld-P/pysarif',
    project_urls={
        'Documentation': 'https://github.com/Kjeld-P/pysarif',
        'Bug Reports':
        'https://github.com/Kjeld-P/pysarif/issues',
        'Source Code': 'https://github.com/Kjeld-P/pysarif',
    },
    package_dir={'': 'src'},
    packages=setuptools.find_packages(where='src'),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Security',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
    install_requires=[
        'dataclasses-json'
    ],
)