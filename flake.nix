{
  description = "Atmospheric turbulence models for sound propagation";

  inputs.nixpkgs.url = "nixpkgs/nixpkgs-unstable";
  inputs.utils.url = "github:numtide/flake-utils";

  outputs = { self, nixpkgs, utils }: {
    overlay = final: prev: {
      pythonPackagesOverrides = (prev.pythonPackagesOverrides or []) ++ [
        (self: super: {
          turbulence = self.callPackage ./. {};
        })
      ];
      # Remove when https://github.com/NixOS/nixpkgs/pull/91850 is fixed.
      python3 = let
        composeOverlays = nixpkgs.lib.foldl' nixpkgs.lib.composeExtensions (self: super: {});
        self = prev.python3.override {
          inherit self;
          packageOverrides = composeOverlays final.pythonPackagesOverrides;
        };
      in self;
    };
  } // (utils.lib.eachSystem [ "x86_64-linux" ] (system: let
    pkgs = (import nixpkgs {
      inherit system;
      overlays = [ self.overlay ];
    });
    python = pkgs.python3;
    turbulence = python.pkgs.turbulence;
    devEnv = python.withPackages(ps: with ps; with ps.turbulence; allInputs ++ [ notebook ]);
  in {
    # Our own overlay does not get applied to nixpkgs because that would lead to
    # an infinite recursion. Therefore, we need to import nixpkgs and apply it ourselves.
    defaultPackage = turbulence;

    devShell = pkgs.mkShell {
      nativeBuildInputs = [
        devEnv
      ];
      shellHook = ''
        export PYTHONPATH=$(readlink -f $(find . -maxdepth 1  -type d ) | tr '\n' ':'):$PYTHONPATH
      '';
    };
  }));
}
