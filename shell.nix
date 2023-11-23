{ pkgs ? import <nixpkgs> {} }:
pkgs.mkShell {
  name = "compiler";
  packages =[
        pkgs.python310
        pkgs.python310Packages.tkinter
  ];
}
