{
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixpkgs-unstable";
    flake-parts = {
      url = "github:hercules-ci/flake-parts";
    };
  };

  outputs = inputs @ {flake-parts, ...}:
    flake-parts.lib.mkFlake {inherit inputs;} {
      systems = [
        "aarch64-darwin"
        "aarch64-linux"
        "x86_64-darwin"
        "x86_64-linux"
      ];
      perSystem = {pkgs, ...}: let
        mcp-server-calculator = pkgs.callPackage ./package.nix {};
      in {
        devShells = rec {
          default = dev;
          dev = let
            python = pkgs.python313.withPackages (ps:
              with ps; [
                mcp-server-calculator
                pytest
              ]);
          in
            pkgs.mkShell {
              packages = with pkgs; [
                python
              ];
            };
        };
        packages.default = mcp-server-calculator;
      };
    };
}
