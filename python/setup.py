from setuptools import setup, find_packages
import package as app


setup(
    name='pyleniumio',
    version=app.__version__,
    packages=find_packages(),
    include_package_data=True,
    url='https://github.com/map34/dev-starter-kits',
    license='MIT',
    author='Adrian Prananda',
    author_email='prananda0203@gmail.com',
    description='Starter kit for Python',
    long_description='Starter kit for Python',
    long_description_content_type='text/markdown',
    install_requires=[
        "mypy==0.910",
        "flake8==4.0.1",
        "pytest-cov==3.0.0",
        "pytest==6.2.5"
    ],
)
