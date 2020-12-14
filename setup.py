"""
# Upload Package: https://pypi.org/project/yajwt/
python3 setup.py sdist bdist_wheel
twine upload dist/yajwt-0.0.3*
"""
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="yajwt",
    version="0.0.3",
    author="Nuno Nelas",
    author_email="nuno.nelas@icloud.com",
    description="Yet Another JWT wrapper for Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nnelas/yajwt",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
