{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  buildInputs = [
    pkgs.hello
    pkgs.uv
    pkgs.git
    pkgs.python313
    pkgs.just
    pkgs.ruff

    # keep this line if you use bash
    pkgs.bashInteractive
  ];
}
