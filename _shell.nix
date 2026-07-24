{ pkgs ? import <nixpkgs> {} }:

with pkgs;

mkShell {
buildInputs = [
    pre-commit ruff #security
    python313 uv #python
    go-task # alternative to make
    nodejs_24 #for the doc
    opam curl git ninja #for catala

];
shellHook = ''
        export SENTRY_DSN="variable value"
        export DN_PILOTAGE_TOKEN="token fourni par DN"
        export GRIST_API_KEY="api key"
        export GRIST_DOC_ID="doc id"
        eval $(opam env)
    '';

}
