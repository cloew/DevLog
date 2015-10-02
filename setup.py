from distutils.core import setup

setup(name='devlog',
      version='0.1.0',
      description="",
      author='Chris Loew',
      author_email='cloew123@gmail.com',
      packages=['devlog',
                'devlog.commands',
                'devlog.config',
                'devlog.dates',
                'devlog.files'],
      scripts=['devlog/scripts/devlog']
     )