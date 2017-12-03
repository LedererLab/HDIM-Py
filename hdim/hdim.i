%module hdim

%{
#include "../src/Solvers/base_solver.hpp"
#include "../src/Solvers/abstractsolver.hpp"
#include "../src/Solvers/solver.hpp"
#include "../src/Solvers/screeningsolver.hpp"
#include "../src/Solvers/SubGradientDescent/subgradient_descent.hpp"
#include "../src/Solvers/SubGradientDescent/ISTA/ista.hpp"
#include "../src/Solvers/SubGradientDescent/FISTA/fista.hpp"
#include "../src/Solvers/CoordinateDescent/coordinate_descent.hpp"
#include "../src/Solvers/CoordinateDescent/coordinatedescentwithscreen.hpp"
#include "../src/FOS/x_fos.hpp"
%}

%include <typemaps.i>
%include <eigen.i>

%eigen_typemaps(Eigen::Matrix<double,Eigen::Dynamic,Eigen::Dynamic>)
%eigen_typemaps(Eigen::Matrix<double,1,Eigen::Dynamic>)
%eigen_typemaps(Eigen::Matrix<double, Eigen::Dynamic,1>)

%eigen_typemaps(Eigen::Matrix<float,Eigen::Dynamic,Eigen::Dynamic>)
%eigen_typemaps(Eigen::Matrix<float,1,Eigen::Dynamic>)
%eigen_typemaps(Eigen::Matrix<float,Eigen::Dynamic,1>)

%eigen_typemaps(Eigen::Matrix<int,Eigen::Dynamic,1>)

%include "../src/Solvers/base_solver.hpp"
%include "../src/Solvers/abstractsolver.hpp"
%include "../src/Solvers/solver.hpp"
%include "../src/Solvers/screeningsolver.hpp"

%include "../src/Solvers/SubGradientDescent/subgradient_descent.hpp"
%include "../src/Solvers/SubGradientDescent/ISTA/ista.hpp"
%include "../src/Solvers/SubGradientDescent/FISTA/fista.hpp"

%include "../src/Solvers/CoordinateDescent/coordinate_descent.hpp"
%include "../src/Solvers/CoordinateDescent/coordinatedescentwithscreen.hpp"

%include "../src/FOS/x_fos.hpp"

template < typename T >
class BaseSolver {

  public:

    virtual ~BaseSolver() = 0;

    virtual Eigen::Matrix< T, Eigen::Dynamic, 1 > operator()(
        const Eigen::Matrix< T, Eigen::Dynamic, Eigen::Dynamic >& X,
        const Eigen::Matrix< T, Eigen::Dynamic, 1 >& Y,
        const Eigen::Matrix< T, Eigen::Dynamic, 1 >& Beta_0,
        T lambda,
        unsigned int num_iterations ) = 0;

    virtual Eigen::Matrix< T, Eigen::Dynamic, 1 > operator()(
        const Eigen::Matrix< T, Eigen::Dynamic, Eigen::Dynamic >& X,
        const Eigen::Matrix< T, Eigen::Dynamic, 1 >& Y,
        const Eigen::Matrix< T, Eigen::Dynamic, 1 >& Beta_0,
        T lambda,
        T duality_gap_target ) = 0;

};

template < typename T >
class AbstractSolver : public BaseSolver < T > {
};

template < typename T >
class Solver : public AbstractSolver < T > {

  public:

    Solver();
    virtual ~Solver() = 0;

    virtual Eigen::Matrix< T, Eigen::Dynamic, 1 > operator()(
        const Eigen::Matrix< T, Eigen::Dynamic, Eigen::Dynamic >& X,
        const Eigen::Matrix< T, Eigen::Dynamic, 1 >& Y,
        const Eigen::Matrix< T, Eigen::Dynamic, 1 >& Beta_0,
        T lambda,
        unsigned int num_iterations );

    virtual Eigen::Matrix< T, Eigen::Dynamic, 1 > operator()(
        const Eigen::Matrix< T, Eigen::Dynamic, Eigen::Dynamic >& X,
        const Eigen::Matrix< T, Eigen::Dynamic, 1 >& Y,
        const Eigen::Matrix< T, Eigen::Dynamic, 1 >& Beta_0,
        T lambda,
        T duality_gap_target );
};

template < typename T >
class ScreeningSolver : public AbstractSolver < T >  {

  public:

    ScreeningSolver();
    virtual ~ScreeningSolver() = 0;

    virtual Eigen::Matrix< T, Eigen::Dynamic, 1 > operator()(
        const Eigen::Matrix< T, Eigen::Dynamic, Eigen::Dynamic >& X,
        const Eigen::Matrix< T, Eigen::Dynamic, 1 >& Y,
        const Eigen::Matrix< T, Eigen::Dynamic, 1 >& Beta_0,
        T lambda,
        unsigned int num_iterations );

    virtual Eigen::Matrix< T, Eigen::Dynamic, 1 > operator()(
        const Eigen::Matrix< T, Eigen::Dynamic, Eigen::Dynamic >& X,
        const Eigen::Matrix< T, Eigen::Dynamic, 1 >& Y,
        const Eigen::Matrix< T, Eigen::Dynamic, 1 >& Beta_0,
        T lambda,
        T duality_gap_target );

};

template < typename T, typename Base = hdim::internal::Solver<T> >
class SubGradientSolver : public Base {

  public:
    SubGradientSolver( T L = 0.1 );
    ~SubGradientSolver();

};

template < typename T >
class X_FOS {

public:
	X_FOS();
	~X_FOS();

	void operator()( const Eigen::Matrix< T, Eigen::Dynamic, Eigen::Dynamic >& x,
									 const Eigen::Matrix< T, Eigen::Dynamic, 1 >& y,
									 SolverType s_type = SolverType::ista );

	T ReturnLambda();
	T ReturnIntercept();
	Eigen::Matrix< T, Eigen::Dynamic, Eigen::Dynamic > ReturnBetas();
	unsigned int ReturnOptimIndex();
	Eigen::Matrix< T, Eigen::Dynamic, 1 > ReturnCoefficients();
	Eigen::Matrix< int, Eigen::Dynamic, 1 > ReturnSupport();

};


template < typename T, typename Base = hdim::internal::Solver< T > >
class ISTA : public hdim::internal::SubGradientSolver<T,Base> {

  public:
    ISTA( T L_0 = 0.1 );

};

template < typename T, typename Base = hdim::internal::Solver< T > >
class FISTA : public hdim::internal::SubGradientSolver<T,Base> {

  public:
    FISTA( const Eigen::Matrix< T, Eigen::Dynamic, 1 >& Beta, T L_0 = 0.1 );

};

template < typename T, typename Base = hdim::internal::Solver<T> >
class LazyCoordinateDescent : public Base {

  public:
    LazyCoordinateDescent( const Eigen::Matrix< T, Eigen::Dynamic, Eigen::Dynamic >& X,
                           const Eigen::Matrix< T, Eigen::Dynamic, 1 >& Y,
                           const Eigen::Matrix< T, Eigen::Dynamic, 1 >& Beta_0 );
    ~LazyCoordinateDescent();

};

%template(baseSolver) hdim::internal::BaseSolver<double>;
%template(abstractSolver) hdim::internal::AbstractSolver<double>;
%template(solver) hdim::internal::Solver<double>;
%template(SR_solver) hdim::internal::ScreeningSolver<double>;

%template(SGD) hdim::internal::SubGradientSolver<double,hdim::internal::Solver<double>>;
%template(SGD_SR) hdim::internal::SubGradientSolver<double,hdim::internal::ScreeningSolver<double>>;

%template(ista) hdim::ISTA<double,hdim::internal::Solver<double>>;
%template(screened_ista) hdim::ISTA<double,hdim::internal::ScreeningSolver<double>>;

%template(fista) hdim::FISTA<double,hdim::internal::Solver<double>>;
%template(screened_fista) hdim::FISTA<double,hdim::internal::ScreeningSolver<double>>;

%template(CD) hdim::LazyCoordinateDescent<double,hdim::internal::Solver<double>>;
%template(CD_SR) hdim::LazyCoordinateDescent<double,hdim::internal::ScreeningSolver<double>>;

%template(fos) hdim::X_FOS<double>;
