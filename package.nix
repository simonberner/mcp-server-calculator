{pkgs, ...}:
with pkgs;
  python313Packages.buildPythonPackage {
    name = "mcp-server-calculator";
    format = "pyproject";
    src = ./.;
    propagatedBuildInputs = with python313Packages; [
      mcp
      uv
      hatchling
    ] ++ mcp.optional-dependencies.cli;
  }
