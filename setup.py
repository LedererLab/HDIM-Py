from setuptools import setup, Extension
from pathlib import Path
import glob, os

def file_search( directory, extension = None ):

    found_headers = []

    if( extension == None ):
        for path, subdirs, files in os.walk( directory ):
            for name in files:
                found_headers.append( os.path.join( path , name ) )

    else:
        for path, subdirs, files in os.walk( directory ):
            for name in files:
                if name.endswith( extension ):
                    found_headers.append( os.path.join( path , name ) )

    return found_headers

source_files = glob.glob( 'hdim/hdim_wrap.cxx' )
source_files.extend( file_search( "src", '.cpp' ) )

header_files = []
header_files.extend( file_search( "src", '.hpp' ) )

extension = Extension('_hdim',
	            define_macros = [('NDEBUG',None)],
	            include_dirs = ['/usr/include/eigen3'],
	            sources = source_files,
	            language='c++',
	            extra_compile_args=['--std=c++11','-O3','-mtune=native','-march=native'])

setup(name="hdim",
      version="0.1.4",
      description=("A toolkit for working with high-dimensional data."),
      url="https://github.com/LedererLab/FOS",
      author="Benjamin J Phillips",
      author_email="bejphil@uw.edu",
      license="MIT",
      packages=['hdim'],
      data_files = header_files, # Actually the header files needed to build from source
      ext_modules=[extension],
      requires=["NumPy (>= 1.3)"],
      platforms = ["Linux"],
    classifiers=[
    'Programming Language :: Python :: 3',
    'Programming Language :: C++',
    'Topic :: Scientific/Engineering :: Mathematics',
    'Intended Audience :: Science/Research',
    ],
      zip_safe=False)
