import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()

# read requirements.txt
#with open('requirements.txt', 'r') as f:
#    content = f.read()
#li_req = content.split('\n')
#install_requires = [e.strip() for e in li_req if len(e)]

setuptools.setup(
    name="endid",
    version="0.0.3",
    author="Dan Lester",
    author_email="support@endid.app",
    description="Command line utility to call the Endid.app Slack app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/endid-app/endid-python",
    packages=setuptools.find_packages(),
    install_requires=[],
    include_package_data=True,
    zip_safe=False,
    entry_points={"console_scripts": ["endid = endid.endid:cli"]},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=2.7',
)


