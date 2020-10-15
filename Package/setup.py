from setuptools import setup

setup(
    name="Package", # Replace with your own username
    version="0.0.1",
    author="GabrielBlancoMora",
    author_email="gaboblanco256@gmail.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/GabrielBlancoM/Tarea3.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'playsound',
        'opencv-python',
        'matplotlib',
        ]
    python_requires='>=3.6',
     
) 