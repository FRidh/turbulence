{ buildPythonPackage

, flit-core

, matplotlib
, numexpr
, numpy
, pandas
, scipy

, black
, pylint
, pytest
, pytestCheckHook
}:

buildPythonPackage rec {
  pname = "turbulence";
  version = "dev";
  format = "pyproject";

  src = ./.;

  nativeBuildInputs = [
    flit-core
  ];

  propagatedBuildInputs = [
    matplotlib
    numexpr
    numpy
    pandas
    scipy
  ];

  checkInputs = [
    black
    pylint
    pytest
    pytestCheckHook
  ];

  preCheck = ''
    echo "Checking formatting with black..."
    black --check turbulence tests
    # Lots of classes were not fully implemented
    # echo "Static analysis with pylint..."
    # pylint -E turbulence
  '';

  passthru.allInputs = nativeBuildInputs ++ propagatedBuildInputs ++ checkInputs;
}

