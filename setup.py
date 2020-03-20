from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup (
    name="http-config-api-sanjeev.pandey",
    version="1.0.1",
    author="Sanjeev Pandey",
    author_email="sanjeevkumarpandey@live.in",
    description="LLNW Config API HTTP Module",
    long_description=open('README.md').read().strip(),
    long_description_content_type="text/markdown",
    url="https://github.com/SanjeevKumarPandey/requests_llnw_config_api",
    license='Apache License 2.0',
    py_modules=['requests_http_config_api'],
    install_requires=['requests>=2.22.0', 'requests_llnw_auth>=1.0.0'],
    python_requires='>=3.7',
)