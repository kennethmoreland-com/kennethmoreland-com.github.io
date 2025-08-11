+++
title = 'Time Dependent Processing in a Parallel Pipeline Architecture'
+++

{{% pubtitle %}}Time Dependent Processing in a Parallel Pipeline Architecture{{% /pubtitle %}}.
John Biddiscombe, Berk Geveci, Ken Martin, Kenneth Moreland, and David Thompson.
_IEEE Transactions on Visualization and Computer Graphics_, 6, 13(6):1376–1383, November/December 2007.
[doi:10.1109/TVCG.2007.70600](https://dx.doi.org/10.1109/TVCG.2007.70600).

## Abstract

Pipeline architectures provide a versatile and efficient mechanism for
constructing visualizations, and they have been implemented in numerous
libraries and applications over the past two decades. In addition to allowing
developers and users to freely combine algorithms, visualization pipelines have
proven to work well when streaming data and scale well on parallel
distributed-memory computers. However, current pipeline visualization frameworks
have a critical flaw: they are unable to manage time varying data. As data flows
through the pipeline, each algorithm has access to only a single snapshot in
time of the data. This prevents the implementation of algorithms that do any
temporal processing such as particle tracing; plotting over time; or
interpolation, fitting, or smoothing of time series data. As data acquisition
technology improves, as simulation time-integration techniques become more
complex, and as simulations save less frequently and regularly, the ability to
analyze the time-behavior of data becomes more important.

This paper describes a modification to the traditional pipeline architecture
that allows it to accommodate temporal algorithms. Furthermore, the architecture
allows temporal algorithms to be used in conjunction with algorithms expecting a
single time snapshot, thus simplifying software design and allowing adoption
into existing pipeline frameworks. Our architecture also continues to work well
in parallel distributed-memory environments. We demonstrate our architecture by
modifying the popular VTK framework and exposing the functionality to the
ParaView application. We use this framework to apply time-dependent algorithms
on large data with a parallel cluster computer and thereby exercise a
functionality that previously did not exist.

## Full Paper

{{% pubtitle %}}[Time Dependent Processing in a Parallel Pipeline Architecture](TimeVis-IEEE2007.pdf){{% /pubtitle %}}

## Supplemental Materials

* [Example animations](TimeVis-IEEE2007.avi)
* This system is implemented in [VTK] and [ParaView]. Download your copy today!

[VTK]: https://vtk.org/
[ParaView]: https://www.paraview.org/
