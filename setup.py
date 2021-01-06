"""
# Upload Package: https://pypi.org/project/yajwt/
python3 setup.py sdist bdist_wheel
twine upload dist/yajwt-0.0.10*
"""
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements.txt") as f:
    required = f.read().splitlines()

setuptools.setup(
    name="yajwt",
    version="0.0.10",
    author="Nuno Nelas",
    author_email="nuno.nelas@icloud.com",
    description="Yet Another JWT wrapper for Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Aptoide/yajwt",
    packages=setuptools.find_packages(),
    install_requires=required,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
