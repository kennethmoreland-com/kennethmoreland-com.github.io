+++
title = 'Rasterization with Data-Parallel Primitives'
+++

{{% pubtitle %}}Rasterization with Data-Parallel Primitives{{% /pubtitle %}}.
Makani Buckley, Kenneth Moreland, and Hank Childs.
In _Eurographics Symposium on Parallel Graphics and Visualization (EGPGV)_, 2026.
(To appear in).

## Abstract

Parallel rasterization can suffer from race conditions during fragment
generation, which is traditionally addressed by using specialized hardware
accessible via vendor graphics APIs. Unfortunately, graphics APIs are
increasingly problematic on high-performance computers, either because they are
not provided or because of concerns about dependencies with in situ
visualization. In response, we present a hardware-agnostic rasterization
algorithm that handles race conditions using only data-parallel primitives
(DPPs), enabling efficient rendering on HPC systems without graphics API
dependencies and aligning with recent efforts to deliver visualization software
with DPPs. Our evaluation consists of three phases: (1) evaluating portability
across different CPU and GPU architectures, (2) evaluating competitiveness with
a community standard, and (3) evaluating performance across varying workloads
and available parallelism. The supporting experiments run on both AMD and Nvidia
GPUs, considering data sets as large as 460 million triangles and 160 million
pixels. While the program performs worse in general when compared to community
standards for rasterization, we conclude that the program is portably performant
across different architectures without the need for specialized vendor support,
and therefore useful for rasterization on high-performance computers.

## Full Paper

{{% pubtitle %}}[Rasterization with Data-Parallel Primitives](https://1drv.ms/b/c/afd0e9b2332ffee6/IQAJvG49uQG5Rb8BeKEJudpWARg_LZI1pQhVnX2Eod2z240?e=qkWiSP){{% /pubtitle %}}

## Supplemental Materials

The following tarball contains the source code used for the experiments in the
paper. This code has been compiled against [CUDA Toolkit 11.5] and [Viskores
1.1.0].

[dpp-rasterizer-src.tar.gz](dpp-rasterizer-src.tar.gz)

The following archive contains the models tested in the paper.

[datasets-dpp-rasterizer.tar.gz](https://1drv.ms/u/c/afd0e9b2332ffee6/IQCBN6B4noj4RqiJYmXqb-wYAZ82QTRdB9YpmPbzl9NQG2c?e=zr4iQz)

[CUDA Toolkit 11.5]: https://developer.nvidia.com/cuda-11-5-0-download-archive
[Viskores 1.1.0]: https://github.com/Viskores/viskores/releases/tag/v1.1.0
