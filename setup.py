from setuptools import setup

setup(
    name="rag-assistant",
    install_requires=[
        "torch>=2.2.0",
        "sentence-transformers>=2.2.0",
        "numpy>=1.26.0"
    ],
    python_requires=">=3.11",
)
