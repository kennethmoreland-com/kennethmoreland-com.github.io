+++
title = 'Optimizing Multi-Image Sort-Last Parallel Rendering'
+++

{{% pubtitle %}}Optimizing Multi-Image Sort-Last Parallel Rendering{{% /pubtitle %}}.
Matthew Larsen, Kenneth Moreland, Chris Johnson, and Hank Childs.
In _Proceedings of the IEEE Symposium on Large Data Analysis and Visualization (LDAV)_, October 2016.
[doi:10.1109/LDAV.2016.7874308](https://dx.doi.org/10.1109/LDAV.2016.7874308).

## Abstract

Sort-last parallel rendering can be improved by considering the rendering of
multiple images at a time. Most parallel rendering algorithms consider the
generation of only a single image. This makes sense when performing interactive
rendering where the parameters of each rendering are not known until the
previous rendering completes. However, in situ visualization often generates
multiple images that do not need to be created sequentially. In this paper we
present a simple and effective approach to improving parallel image generation
throughput by amortizing the load and overhead among multiple image renders.
Additionally, we validate our approach by conducting a performance study
exploring the achievable speed-ups in a variety of image-based in situ use cases
and rendering workloads. On average, our approach shows a 1.5 to 3.7 fold
improvement in performance, and in some cases, shows a 10 fold improvement.

## Full Paper

{{% pubtitle %}}[Optimizing Multi-Image Sort-Last Parallel Rendering](LDAV2016.pdf){{% /pubtitle %}}

## Results Data

Here you can find the data collected that were presented in numerous figures/tables.

* Average Speed-ups ([Figure 1](Average_Overall_SpeedUp.pdf))
  * [Raw data in csv format](Average_Overall_SpeedUp.csv)
  * [Python script for processing](https://github.com/kennethmoreland-com/kennethmoreland-com.github.io/blob/master/ldav2016/Average_Overall_SpeedUp.ipynb) ([download Jupyter Notebook](Average_Overall_SpeedUp.ipynb))
* Overall Speed-ups ([Figure 2](Overall_SpeedUp_Summary.pdf))
  * [Raw data in csv format](All_Overall_SpeedUp.csv)
  * [Python script for processing](https://github.com/kennethmoreland-com/kennethmoreland-com.github.io/blob/master/ldav2016/Overall_SpeedUp_Summary.ipynb) ([download Jupyter Notebook](Overall_SpeedUp_Summary.ipynb))
* Rendering Speed-ups ([Figure 4](Rendering_SpeedUp.pdf))
  * [Raw data in csv format](All_Rendering_SpeedUp.csv)
  * [Python script for processing](https://github.com/kennethmoreland-com/kennethmoreland-com.github.io/blob/master/ldav2016/Rendering_SpeedUp.ipynb) ([download Jupyter Notebook](Rendering_SpeedUp.ipynb))
* Compositing Speed-ups ([Figure 5](Compositing_SpeedUp_Cinema.pdf), [Figure 6](Compositing_SpeedUp_Inverse_Cinema.pdf), and [Figure 7](Compositing_SpeedUp_Surface_Reconstruct.pdf))
  * [Raw data in csv format](All_Compositing_SpeedUp.csv)
  * [Python script for processing Cinema](https://github.com/kennethmoreland-com/kennethmoreland-com.github.io/blob/master/ldav2016/Compositing_SpeedUp_Cinema.ipynb) ([download Jupyter Notebook](Compositing_SpeedUp_Cinema.ipynb))
  * [Python script for processing Inverse Cinema](https://github.com/kennethmoreland-com/kennethmoreland-com.github.io/blob/master/ldav2016/Compositing_SpeedUp_Inverse_Cinema.ipynb) ([download Jupyter Notebook](Compositing_SpeedUp_Inverse_Cinema.ipynb))
  * [Python script for processing Surface Reconstruction](https://github.com/kennethmoreland-com/kennethmoreland-com.github.io/blob/master/ldav2016/Compositing_SpeedUp_Surface_Reconstruct.ipynb) ([download Jupyter Notebook](Compositing_SpeedUp_Surface_Reconstruct.ipynb))
