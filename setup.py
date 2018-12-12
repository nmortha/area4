import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="area4",
    version="1.2.7-dev",
    author="RDIL",
    author_email="contactspaceboom@gmail.com",
    description="Dividers in Python, the easy way! Many different divider looks.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/RDIL/area4",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2 :: Only",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: Implementation :: PyPy',
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft",
        "Operating System :: MacOS",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX :: Linux",
        "Operating System :: Other OS",
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
        'Topic :: System',
        'Topic :: Terminals',
        "Topic :: Text Processing",
        'Development Status :: 5 - Production/Stable',
        'Framework :: IDLE',
        'Natural Language :: English',
    ],
    project_urls={
        # "Bug Tracker": "https://github.com/RDIL/area4/issues", (we don't keep track of bugs for this branch)
        # "Documentation": "https://area4.readthedocs.io/en/stable/", (we don't have docs for this branch)
        "Source Code": "https://github.com/RDIL/area4",
    },
    keywords=["area4", "dividers", "python", "utilities", "enhancements"],
    include_package_data=True
)
