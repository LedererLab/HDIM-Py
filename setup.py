from distutils.core import setup, Extension
from glob import glob

import os

source_files = glob( 'src/FOS/x_fos.cpp' )
source_files.append( 'src/Solvers/SubGradientDescent/ISTA/ista.cpp' )
source_files.append( 'src/Solvers/SubGradientDescent/FISTA/fista.cpp' )
source_files.append( 'src/Solvers/CoordinateDescent/coordinate_descent.cpp' )

source_files.append( 'hdim/hdim_wrap.cxx' )

source_files.append( 'src/Solvers/SubGradientDescent/ISTA/viennacl_ista.cpp' )
source_files.append( 'src/Solvers/SubGradientDescent/FISTA/viennacl_fista.cpp' )

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


setup(name='hdim',
      version='0.1.0',
      description='A toolkit for working with high-dimensional data.',
      url='https://github.com/LedererLab/FOS',
      author='Benjamin J Phillips',
      author_email='bejphil@uw.edu',
      license='MIT',
      packages=['hdim'],
      ext_modules=[extension],
      requires=['NumPy (>= 1.3)'],
      python_requires=['>=3'],
      zip_safe=False)
