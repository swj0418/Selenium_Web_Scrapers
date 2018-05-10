import io
from setuptools import find_packages, setup

def description():
    with io.open('README.rst', 'r', encoding='utf-8') as file:
        readme = file.read()
    return readme

setup(name='TextSearch',
      version='0.0.1',
      description='Practice Engine for NLP',
      long_description=description(),
      url='',
      author='Sangwon Jeong',
      author_email='swj0418@hotmail.com',
      license='MIT',
      packages=find_packages(),
      classifiers=[
          'Programming Language ::: Python 3.6'
      ],
      zip_safe=False)

"""
setup() Function의 Arguments는 프로젝트의 자세한 정보를 어떻게 정의할 것인지를 결정한다.

name
패키지의 이름
version
패키지의 배포 버전
description
패키지에 대한 설명
url
패키지를 대표하는 웹페이지
author
패키지의 작성자
license
패키지의 라이센스
packages
프로젝트에 포함되는 패키지 리스트
install_requires
실행 환경에 필요한 최소한의 패키지 리스트
python_requires
실행 환경에 필요한 파이썬 버전
"""