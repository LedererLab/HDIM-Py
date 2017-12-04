HDIM
========================================

.. currentmodule:: hdim

Iterative Solvers
----------------------------------------

Iterative solve the following problem, :math:`\hat{\beta} = \underset{ \beta \in \mathbb{R}^p }{\mathrm{argmin}}  ||Y - X  \beta||_2^2 + \lambda || \beta ||_1`

For a given design matrix X, a vector of predictors Y and vector :math:`\beta`.

.. autofunction:: ISTA

.. autofunction:: FISTA

.. autofunction:: CoordinateDescent

Variable Selection & Support Estimation
----------------------------------------

Use the LASSO objective function to estimate signifigant, non-zero enteries in a L1 regularized regression.

.. autofunction:: FOS
