from .hdim import *

def ISTA( X, Y, Beta_0, convergence_criteria, Lambda, L_0 = 0.1, use_screening_rules = True ):
    """
    Use the Iterative Shrinkage Thresholding Algorithm ( ISTA ) to iteratively solve the LASSO.

    Solves the problem: arg min Beta { || X*Y - Beta ||_2^2 + Lambda*|| Beta ||_1 }

    Args:
        X: An n x p 2D array representing the design matrix.
        Y: A 1 x p 1D array representing the predictors
        Beta_0: A 1 x p 1D array describing initial condition for Beta.
        convergence_criteria: Can be either an positive integer descrbing the number
        if iterations that the solve should be run for, or a positive float describing
        the smallest allowable Duality Gap.
        Lambda: Regularization hyper-parameter for the LASSO ( e.g. Lambda x || Beta ||_1 )
        L_0: Learning rate used by the backtracking line search.
        use_screening_rules: Enable or disable GAPSAFE screening rules. Enabling
        these rules MAY speed up the algorithm.

    Returns:
        numpy array containing the coefficients of Beta after the specified convergence
        criteria has been meet.

    Raises:
        ValueError: Raised if convergence_criteria is neither a positive integer
        or a positive float.

    """

    if( convergence_criteria <= 0 ):
        raise ValueError( "Convergence criteria must be positive int or float.")

    if use_screening_rules:
        solver = hdim.ista( L_0 )
    else:
        solver = hdim.screened_ista( L_0 )

    return solver( X, Y, Beta_0, Lambda, convergence_criteria )


def FISTA( X, Y, Beta_0, convergence_criteria, Lambda, L_0 = 0.1, use_screening_rules = True ):
    """
    Use the Fast Iterative Shrinkage Thresholding Algorithm ( FISTA ) to iteratively solve the LASSO.

    Solves the problem: arg min Beta { || X*Y - Beta ||_2^2 + Lambda*|| Beta ||_1 }
    Using an accelerated version of ISTA.

    Args:
        X: An n x p 2D array representing the design matrix.
        Y: A 1 x p 1D array representing the predictors
        Beta_0: A 1 x p 1D array describing initial condition for Beta.
        convergence_criteria: Can be either an positive integer descrbing the number
        if iterations that the solve should be run for, or a positive float describing
        the smallest allowable Duality Gap.
        Lambda: Regularization hyper-parameter for the LASSO ( e.g. Lambda x || Beta ||_1 )
        L_0: Learning rate used by the backtracking line search.
        use_screening_rules: Enable or disable GAPSAFE screening rules. Enabling
        these rules MAY speed up the algorithm.

    Returns:
        numpy array containing the coefficients of Beta after the specified convergence
        criteria has been meet.

    Raises:
        ValueError: Raised if convergence_criteria is neither a positive integer
        or a positive float.

    """

    if( convergence_criteria <= 0 ):
        raise ValueError( "Convergence criteria must be positive int or float.")

    if use_screening_rules:
        solver = hdim.fista( Beta_0, L_0 )
    else:
        solver = hdim.screened_fista( Beta_0, L_0 )

    return solver( X, Y, Beta_0, Lambda, convergence_criteria )

def CoordinateDescent( X, Y, Beta_0, Lambda, convergence_criteria, use_screening_rules = True ):
    """
    Use Coordinate Descent to iteratively solve the LASSO.

    Solves the problem: arg min Beta { || X*Y - Beta ||_2^2 + Lambda*|| Beta ||_1 }

    Generally performs better than sub-gradient descent methods such as ISTA or FISTA.

    Args:
        X: An n x p 2D array representing the design matrix.
        Y: A 1 x p 1D array representing the predictors
        Beta_0: A 1 x p 1D array describing initial condition for Beta.
        convergence_criteria: Can be either an positive integer descrbing the number
        if iterations that the solve should be run for, or a positive float describing
        the smallest allowable Duality Gap.
        Lambda: Regularization hyper-parameter for the LASSO ( e.g. Lambda x || Beta ||_1 )
        use_screening_rules: Enable or disable GAPSAFE screening rules. Enabling
        these rules MAY speed up the algorithm.

    Returns:
        numpy array containing the coefficients of Beta after the specified convergence
        criteria has been meet.

    Raises:
        ValueError: Raised if convergence_criteria is neither a positive integer
        or a positive float.

    """
    if use_screening_rules:
        solver = hdim.CD( X, Y, Beta_0 )
    else:
        solver = hdim.CD_SR( X, Y, Beta_0 )

    return solver( X, Y, Beta_0, Lambda, convergence_criteria )

def FOS( X, Y, Beta_0, solver = hdim.SolverType_cd, screening_rules = True ):
    """
    Use the Fast and Optimal Support ( FOS ) method to estimate the support for
    a given LASSO problem.

    Args:
        X: An n x p 2D array representing the design matrix.
        Y: A 1 x p 1D array representing the predictors
        Beta_0: A 1 x p 1D array describing initial condition for Beta.
        solver: The type of iterative solver used internally. Can used
        sub-gradient descent methods or coordinate descent, both of which
        can use GAPSAFE screening rules or not.

    Returns:
        numpy array containing the estimated support and intercept term.
    """

    fos_object = hdim.fos()
    fos_object( X, Y, solver )

    return fos_object.ReturnCoefficients()
