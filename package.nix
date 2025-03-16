{pkgs, ...}:
with pkgs;
  python3Packages.buildPythonPackage {
    name = "mcp-server-calculator";
    format = "pyproject";
    src = ./.;
    propagatedBuildInputs = with python3Packages; [
      mcp
      hatchling
    ] ++ mcp.optional-dependencies.cli;
  }
