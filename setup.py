from distutils.core import setup

setup(
    name='nav_tts_sr',
    packages=['nav_tts_v1'],
    version='0.4',
    license='MIT',
    description='A module which simplifies stuff related to voice',
    author='Navaneeth K',
    author_email='snmlogic111@gmail.com',
    url='https://github.com/SnmLogic/nav',
    download_url='https://github.com/SnmLogic/nav/archive/refs/tags/version_0.1.tar.gz',
    keywords=['Voice', 'Nav', 'TTS'],
    install_requires=[
        'pyttsx3',
        'pyaudio'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
