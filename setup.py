from setuptools import setup, find_packages
from os.path import join

name = 'plumi.skin'
version = '0.1'
readme = open("README.txt").read()
history = ""

setup(name = name,
      version = version,
      description = 'Plumi skin',
      long_description = readme[readme.find('\n\n'):] + '\n' + history,
      keywords = 'plone CMS zope',
      author = 'Souheil Chelfouh',
      author_email = 'trollfot@gmail.com',
      url = 'http://plumi.org/',
      download_url = 'https://svn.plone.org/svn/collective/plumi.skin/trunk',
      license = 'GPL',
      packages = find_packages(),
      namespace_packages = ['plumi.skin', 'plumi'],
      include_package_data = True,
      platforms = 'Any',
      zip_safe = False,
      install_requires=[
          'setuptools',
      ],
      classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Plone',
        'Intended Audience :: Other Audience',
	'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
      ],
)
