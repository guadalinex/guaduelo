#!/usr/bin/python
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

__version__ = '0.2'


setup(name = "Guaduelo",
      version = __version__,
      description = "A Memory card game",
      long_description="Simple memory game that consists in make card pairs.",
      author = "Javier Hernandez",
      author_email = "jhernandez@emergya.es",
      url = "http://forja.guadalinex.org/projects/guaduelo",

      classifiers = [ 'Development Status :: 5 - Production/Stable',
                      'Intended Audience :: End Users/Desktop',
                      'License :: OSI Approved :: GNU General Public License (GPL)',
                      'Operating System :: POSIX :: Linux',
                      'Topic :: Games/Entertainment :: Board Games',
                      'Programming Language :: Python :: 2.6',
                      'Environment :: X11 Applications'],

      install_requires = ["pygame"],

      packages = ['lib'],
      package_dir = {'lib': 'lib'},

      scripts = ['guaduelo'],

      data_files = [('share/guaduelo/data/img', 
                        ['data/img/0_award.png', 'data/img/1_award.png', 'data/img/2_award.png',
                         'data/img/3_award.png', 'data/img/back.png', 'data/img/both_win.png',
                         'data/img/card.ico', 'data/img/card.png', 'data/img/cards1.png',
                         'data/img/cards2.png', 'data/img/img10.png', 'data/img/img11.png',
                         'data/img/img12.png', 'data/img/img13.png', 'data/img/img14.png',
                         'data/img/img15.png', 'data/img/img16.png', 'data/img/img17.png',
                         'data/img/img18.png', 'data/img/img1.png', 'data/img/img2.png',
                         'data/img/img3.png', 'data/img/img4.png', 'data/img/img5.png',
                         'data/img/img6.png', 'data/img/img7.png', 'data/img/img8.png',
                         'data/img/img9.png', 'data/img/known_known.png', 'data/img/known.png',
                         'data/img/mouse.png', 'data/img/player.png', 'data/img/robot.png',
                         'data/img/side.png', 'data/img/star1.png', 'data/img/star2.png',
                         'data/img/star3.png', 'data/img/star4.png', 'data/img/star5.png',
                         'data/img/unknown_known.png', 'data/img/unknown.png',
                         'data/img/unknown_unknown.png', 'data/img/win.png']),
                     ('share/guaduelo/data/snd', 
                         ['data/snd/applause.wav', 'data/snd/boom.wav', 'data/snd/card.wav',
                          'data/snd/pair.wav', 'data/snd/win.wav']),
                     ('share/guaduelo/data/fnt', ['data/fnt/KLEPTOMA.TTF','data/fnt/scribble.TTF']),
                     ('share/pixmaps', ['guaduelo.xpm']),
                     ('share/applications', ['guaduelo.desktop'])
                     
                   ]
      )
