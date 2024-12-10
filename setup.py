from setuptools import setup, find_packages
import pathlib

# Read README.md for the long description
here = pathlib.Path(__file__).parent.resolve()
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="hf_transformers_custom_model_ced",
    version="0.0.1",
    description="", # Description will be read from README.md
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Heinrich Dinkel, Junbo Zhang",
    author_email="dinkelheinrich@xiaomi.com, zhangjunbo1@xiaomi.com",
    maintainer="Junbo Zhang, Heinrich Dinkel",
    maintainer_email="zhangjunbo1@xiaomi.com, dinkelheinrich@xiaomi.com",
    python_requires=">=3.9",
    packages=find_packages(where="."),
    install_requires=[
        "torch==2.2.0",
        "torchaudio==2.2.0",
        "transformers",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
)
