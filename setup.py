from setuptools import setup, find_packages

setup(name='slic-histogram',
      version='0.1.0',
      description='SLIC region histogram',
      url='https://github.com/klintan/slic-histogram',
      author='Andreas Klintberg',
      license='MIT',
      packages=find_packages(),
      package_dir={'': 'src'},
      install_requires=["numpy==1.16.3"],
      zip_safe=False)