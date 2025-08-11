+++
title = 'Tetrahedral Projection using Vertex Shaders'
+++

{{% pubtitle %}}Tetrahedral Projection using Vertex Shaders{{% /pubtitle %}}.
Brian Wylie, Kenneth Moreland, Lee Ann Fisk, and Patricia Crossno.
In _Proceedings of IEEE Volume Visualization and Graphics Symposium_, pages 7–12, October 2002.
[doi:10.1109/SWG.2002.1226504](https://dx.doi.org/10.1109/SWG.2002.1226504).

## Abstract

Projective methods for volume rendering currently represent the best approach
for interactive visualization of unstructured data sets. We present a technique
for tetrahedral projection using the programmable vertex shaders on current
generation commodity graphics cards. The technique is based on Shirley and
Tuchman's Projected Tetrahedra (PT) algorithm and allows tetrahedral elements to
be volume scan converted within the graphics processing unit. Our technique
requires no pre-processing of the data and no additional data structures. Our
initial implementation allows interactive viewing of large unstructured datasets
on a desktop personal computer.

## Full Paper

{{% pubtitle %}}[Tetrahedral Projection using Vertex Shaders](volvis2002.pdf){{% /pubtitle %}}

## Supplemental Materials

* [Vertex program](tetra_linear.nvv) for the GL_NV_vertex_program OpenGL
  extension.
* [Vertex program](tetra_linear.arb) for the GL_ARB_vertex_program/shader
  extensions.
* List of [uniform parameters](tetra_linear.params) that need to be loaded.
* [Example OpenGL code](vertex_feedtxt.pdf) that loads the vertex program.
* [Cg vertex program](gator.cg) that also implements the tetrahedral projection.
