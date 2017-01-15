#from distutils.core import setup  
from setuptools import setup, find_packages

setup(name='pydocbuild',  #打包后的包文件名  
    version='0.1.0',    
    description='automatizie my notebook creations',    
    author='irhawks',
    author_email='irahwks@163.com',    
    url='http://irhawks.github.io',    
    py_modules=['pydocbuild'],   #与前面的新建文件名一致  
    keywords=['etl', 'doit', 'task automation'],

    packages= find_packages(),
    requires=["doit","selenium"],
    install_requires=["doit", "selenium"],
    classifiers=(
        "Development Status :: 2 - Pre-Alpha",
        "Programming Language :: Python",
    ),
)
