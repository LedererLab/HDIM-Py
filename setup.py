from setuptools import setup, Extension
import glob

import os

from shutil import copytree
import pathlib

def file_search( directory, extension ):

    found_headers = []

    for path, subdirs, files in os.walk( directory ):
        for name in files:
            if name.endswith( extension ):
                found_headers.append( os.path.join( path , name ) )

    return found_headers

source_files = glob.glob( 'hdim/hdim_wrap.cxx' )

source_files.extend( file_search( "src/FOS", '.cpp' ) )
source_files.extend( file_search( "src/Solvers", '.cpp' ) )

header_files = []

header_files.extend( file_search( "src/FOS/", '.hpp' ) )
header_files.extend( file_search( "src/Screening/", '.hpp' ) )
header_files.extend( file_search( "src/Solvers/", '.hpp' ) )
header_files.extend( file_search( "src/Generic/", '.hpp' ) )
header_files.extend( file_search( "src/OpenCL_Generics/", '.h' ) )

extension = Extension('_hdim',
	            define_macros = [('NDEBUG',None),('W_OPENCL',None),('VIENNACL_WITH_OPENCL',None),('VIENNACL_WITH_EIGEN',None)],
	            include_dirs = ['/usr/include/eigen3','/usr/include/viennacl','/usr/local/cuda/include'],
	            libraries = ['OpenCL'],
	            library_dirs = ['/usr/local/cuda/lib64'],
	            sources = source_files,
	            language='c++',
	            extra_compile_args=['--std=c++11','-O3','-mtune=native','-march=native'])

#extension = Extension('_hdim',
#	            define_macros = [('NDEBUG',None)],
#	            include_dirs = ['/usr/include/eigen3'],
#	            sources = source_files,
#	            language='c++',
#	            extra_compile_args=['--std=c++11','-O3','-mtune=native','-march=native'])

setup(name="hdim",
      version="0.1.0",
      description=("A toolkit for working with high-dimensional data."),
      url="https://github.com/LedererLab/FOS",
      author="Benjamin J Phillips",
      author_email="bejphil@uw.edu",
      license="MIT",
      packages=['hdim'],
      data_files = header_files, # Actually the header files needed to build from source
      ext_modules=[extension],
      requires=["NumPy (>= 1.3)"],
      zip_safe=False)
