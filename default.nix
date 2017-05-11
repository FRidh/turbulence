{ buildPythonPackage
, pytest
, numpy
, scipy
, matplotlib
, pandas
, numexpr
, traitlets
, numtraits
}:

buildPythonPackage rec {
  name = "turbulence-${version}";
  version = "0.1dev";

  src = ./.;

  buildInputs = [ pytest ];
  propagatedBuildInputs = [ numpy scipy matplotlib pandas numexpr traitlets numtraits ];

  meta = {
    description = "Acoustics module for Python";
  };

  doCheck = false;
}

