import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="scenariogeneration",
    version="0.13.1",
    license="MPL-2.0",
    author="Ankita",
    author_email="andmika@gmail.com",
    description="Generation of OpenSCENARIO and OpenDRIVE xml files",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Ankita6332/Ankita.git",
    packages=setuptools.find_packages(),
    keywords=["OpenDRIVE", "OpenSCENARIO", "xml"],
    install_requires=["numpy", "scipy", "pyclothoids", "xmlschema", "lxml"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
