from setuptools import setup, Extension
from pathlib import Path
import glob, os, sys
import numpy
from distutils.sysconfig import get_python_inc

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

def maybe_find_eigen():

    eigen_path = os.path.dirname( [ filename for filename in glob.iglob('../**/eigen3/Eigen', recursive=True) ][0] )

    if( eigen_path == None ):
        raise ValueError( "Eigen3 include directory not found.")

    return eigen_path

if sys.platform == 'darwin':
    # Apple OS X
    inc_dirs = ['/usr/include/eigen3']
    inc_dirs.append( numpy.get_include() ) # Numpy header files
    inc_dirs.append( get_python_inc() ) # Python header files
elif sys.platform == 'linux':
    # Linux
    inc_dirs = ['/usr/include/eigen3']
elif sys.platform == 'win32':
    # Windows
    inc_dirs = [ maybe_find_eigen() ]
else:
    # We don't support other Operating Systems. Do people want to use our package on Haiku ...?
    raise OSError( "Can't install on this system -- unsupported OS." )

source_files = glob.glob( 'hdim/hdim_wrap.cxx' )
source_files.extend( file_search( "src", '.cpp' ) )

header_files = []
header_files.extend( file_search( "src", '.hpp' ) )

extension = Extension('_hdim',
	            define_macros = [('NDEBUG',None)],
	            include_dirs = inc_dirs,
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
