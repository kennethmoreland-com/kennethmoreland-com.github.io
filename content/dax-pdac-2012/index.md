+++
title = 'Flexible Analysis Software for Emerging Architectures'
+++

{{% pubtitle %}}Flexible Analysis Software for Emerging Architectures{{% /pubtitle %}}.
Kenneth Moreland, Brad King, Robert Maynard, and Kwan-Liu Ma.
In _2012 SC Companion (Petascale Data Analytics: Challenges and Opportunities)_, pages 821–826, November 2012.
[doi:10.1109/SC.Companion.2012.115](https://dx.doi.org/10.1109/SC.Companion.2012.115).

## Abstract

We are on the threshold of a transformative change in the basic architecture of
high-performance computing. The use of accelerator processors, characterized by
large core counts, shared but asymmetrical memory, and heavy thread loading, is
quickly becoming the norm in high performance computing. These accelerators
represent significant challenges in updating our existing base of software. An
intrinsic problem with this transition is a fundamental programming shift from
message passing processes to much more fine thread scheduling with memory
sharing. Another problem is the lack of stability in accelerator implementation;
processor and compiler technology is currently changing rapidly. In this paper
we describe our approach to address these two immediate problems with respect to
scientific analysis and visualization algorithms. Our approach to accelerator
programming forms the basis of the Dax toolkit, a framework to build data
analysis and visualization algorithms applicable to exascale computing.

## Full Paper

{{% pubtitle %}}[Flexible Analysis Software for Emerging Architectures](DaxPDAC2012.pdf){{% /pubtitle %}}

## Example Programs

I built two simple programs to provide the empirical results from this paper.
The first is called thresholdexample that loads in a sample data set and runs
the [Dax] threshold algorithm using one of the many device adapters available in
Dax. The second is called pistoncompare that performs, as close as possible, a
comparison between identical threshold operations in Dax and [PISTON]. Below are
all the source you should need to replicate the results.

* The [thresholdexample] test program.
* The [pistoncompare] test program (also contains PISTON modifications).
* A [snapshot of Dax] used in the paper.
* A [snapshot of PISTON] used in the paper.

In addition, you will of course need the appropriate build tools and libraries:
[CMake], [CUDA], an OpenMP-compliant C++ compiler, and the [TBB] library.

The paper also features some timings from the VTK threshold algorithm. These
timings were performed using the [ParaView] 3.14 binary provided by Kitware. I
executed [this Python script](CycleThreshold.py) for ParaView to run the
threshold algorithm for the 20 trials.

<!--
Since the writing of the paper, changes to the Dax API mean the original examples no longer compile with the latest version of Dax. I will try to periodically update the code to work against the most recent versions of Dax and PISTON. If you find they no longer work, you can send me an email and hopefully I'll be able to get to in a reasonable amount of time. (Even better, you can help me fix the problem.)

Updated thresholdexample.
Updated pistoncompare.
-->

Unfortunately, I am unable to post the data set I used as, to the best of my knowledge, it has not been released openly. However, the data is a simple brick of floats, so it should be trivial to load a similar data set if you cannot get hold of this one.

[thresholdexample]: thresholdexample-snapshot.tar.gz
[pistoncompare]: pistoncompare-snapshot.tar.gz
[snapshot of Dax]: DaxToolkit-110fa7713e5b20837d13833bcd6c1c412afd5569-snapshot.tar.gz
[snapshot of PISTON]: PISTON-0.4-snapshot.tar.gz

## Results Data

Here you can find the detailed timing numbers for the experimental results.

* [Results from thresholdexample].
* [Results from pistoncompare].

[Results from thresholdexample]: thresholdexample.csv
[Results from pistoncompare]: pistoncompare.csv

To use these data to get plots like those in the paper, you will need to use something like a pivot table. (For what it's worth, I used Tableau, which is really a visual pivot table and plotter.)

[Dax]: https://daxtoolkit.org/
[PISTON]: https://viz.lanl.gov/projects/PISTON.html
[CMake]: https://cmake.org/
[CUDA]: https://developer.nvidia.com/cuda-zone
[TBB]: https://threadingbuildingblocks.org/
[ParaView]: https://www.paraview.org/
