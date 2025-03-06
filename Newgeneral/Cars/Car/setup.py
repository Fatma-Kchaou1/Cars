from setuptools import setup, find_packages

with open("C:/Users/User/OneDrive/Bureau/Pycharm/Newgeneral/README.md", "r") as f:
    long_description = f.read()

setup(
    name="cars_fatma_kchaou",
    version="0.2.10",
    author="FatmaKchaou",
    description="Ce projet vise à développer des compétences en gestion de projet logiciel, en mettant l'accent sur la gestion de version, la compilation, la protection du code et le déploiement dans un environnement cible.",
    packages=find_packages(),  # Trouve automatiquement les packages
    install_requires=[
        "numpy",  # Liste des dépendances
        "requests",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],

    extras_require={
        "dev": [ "twine>=6.1.0"],
    },
    python_requires=">=3.10",
)
