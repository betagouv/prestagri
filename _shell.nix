{ pkgs ? import <nixpkgs> {} }:

with pkgs;

mkShell {
buildInputs = [
    python313 poetry #python
    go-task # alternative to make
    nodejs_24 #for the doc
];
shellHook = ''
        export SENTRY_DSN="variable value"
    '';

}
