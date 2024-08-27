from setuptools import find_packages
from setuptools import setup

with open("requirements.txt") as f:
    content = f.readlines()
requirements = [x.strip() for x in content if "git+" not in x]

setup(name='treasurebot',
      version="0.0.1",
      description="This model helps you identify the correct waste category for your items",
      #url="https://github.com/msessini/TreasureBot3000",
      install_requires=requirements,
      packages=find_packages(),
      # include_package_data: to install data from MANIFEST.in
      include_package_data=True,
      zip_safe=False)
