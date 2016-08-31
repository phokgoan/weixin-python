# -*- coding: utf-8 -*-


from distutils.core import setup


setup(
    name='weixin-python',
    py_modules=['weixin'],
    version='0.1.1',
    description='Weixin for python',
    author='zwczou',
    author_email='zwczou@gmail.com',
    url='https://github.com/zwczou/weixin-python',
    keywords=['weixin', 'weixin pay', 'weixin login'],
    zip_safe=False,
    platforms='any',
    install_requires=[
        'Flask',
    ],
    classifiers=[],
)