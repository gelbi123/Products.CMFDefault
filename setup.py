import os
from setuptools import setup
from setuptools import find_packages

NAME = 'CMFDefault'

here = os.path.abspath(os.path.dirname(__file__))

def _package_doc(name):
    f = open(os.path.join(here, name))
    return f.read()

_boundary = '\n' + ('-' * 60) + '\n\n'
README = ( _package_doc('README.rst')
         + _boundary
         + _package_doc('CHANGES.rst')
         + _boundary
         + "Download\n========"
         )

setup(name='Products.%s' % NAME,
      version='2.3.0.dev0',
      description='Default product for the Zope Content Management Framework',
      long_description=README,
      classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Framework :: Plone",
        "Framework :: Zope2",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Zope Public License",
        "Programming Language :: Python",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
        ],
      keywords='web application server zope zope2 cmf',
      author="Zope Foundation and Contributors",
      author_email="zope-cmf@zope.org",
      url="http://pypi.python.org/pypi/Products.CMFDefault",
      license="ZPL 2.1 (http://www.zope.org/Resources/License/ZPL-2.1)",
      packages=find_packages(),
      include_package_data=True,
      namespace_packages=['Products'],
      zip_safe=False,
      setup_requires=['eggtestinfo',
                     ],
      install_requires=[
          'setuptools',
          'Zope2 >= 2.13.12',
          'Products.CMFCore < 2.4',
          'Products.GenericSetup < 1.9',
          'Products.MailHost',
          'Products.PythonScripts',
          'five.globalrequest < 99',
          'five.localsitemanager < 3',
          'zope.formlib',
          ],
      tests_require=[
          'zope.testing >= 3.7.0',
          'Products.DCWorkflow < 2.4',
          ],
      extras_require={ 'test': ['Products.DCWorkflow < 2.4'],
                       'docs': ['Sphinx', 
                                'repoze.sphinx.autointerface', 
                                'pkginfo'],
                       'locales': ['zope.app.locales'],},
      test_loader='zope.testing.testrunner.eggsupport:SkipLayers',
      test_suite='Products.%s' % NAME,
      entry_points="""
      [zope2.initialize]
      Products.%s = Products.%s:initialize
      [distutils.commands]
      ftest = zope.testing.testrunner.eggsupport:ftest
      """ % (NAME, NAME),
      )
