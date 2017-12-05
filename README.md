# HDIM-Py

HDIM is a toolkit for working with high-dimensional data that emphasizes
speed and statistical guarantees. Specifically, it provides tools for working
with the LASSO objective function.

HDIM provides iterative solvers for the LASSO objective function
 including ISTA, FISTA and Coordinate Descent. HDIM also provides FOS,
  the Fast and Optimal Selection algorithm, a novel new method
for performing variable selection via the LASSO.

This package is a Python wrapper over the original [C++ implementation of HDIM](https://github.com/LedererLab/FOS).

## Dependencies

This package requires that the [Eigen 3](http://eigen.tuxfamily.org/index.php)
C++ linear algebra package be installed on the target system. Note that the root
directory for Eigen 3, labeled `eigen3`, should be located under `/usr/include/`.

## Supported Platforms

This package is currently tested and officially supported only on **Linux** platforms.

## Installation

This package can be installed from source, or from the Python Package Index ( PyPi ).

### From source

- Clone the HDIM package into a convenient location via `git clone https://github.com/LedererLab/HDIM-Py.git`
- Navigate to the root directory of the newly cloned repo ( e.g. `HDIM-Py` ).
This directory will contain a file called `setup.py`.
- Run the following command `pip3 install --user .` to install the package for only the
current user, or run `sudo pip3 install .` to install the package system wide.
- Either command will build the package and install it.

### From PyPi

This package is hosted on the Python Package Index and can be installed without
cloning this repository.

- Run the following command `pip3 install --user hdim` to install the package for only the
current user, or run `sudo pip3 install hdim` to install the package system wide.

## Licensing

The HDIM package is licensed under the MIT license. To view the MIT license please consult
the `LICENSE.txt` file included with this package.

## Authors

Based on research conducted by the Lederer and Hauser HDIM group including work
 by Johannes Lederer, Alain Hauser, Néhémy Lim, and others.

The original C++ implementation of the HDIM package was constructed by Saba Noorassa
 and Benjamin J Phillips.

This package was constructed by Benjamin J Phillips.

## References

* [FOS](https://arxiv.org/abs/1609.07195)
* [GAP SAFE Screening Rules](https://arxiv.org/abs/1505.03410)
