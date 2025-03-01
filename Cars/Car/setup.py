from setuptools import setup, find_packages

setup(
    name="Cars",
    version="0.1",
    author="FatmaKchaou",
    description="Ce projet vise à développer des compétences en gestion de projet logiciel, en mettant l'accent sur la gestion de version, la compilation, la protection du code et le déploiement dans un environnement cible",
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
    python_requires='>=3.10.0',  # Version de Python requise
)
