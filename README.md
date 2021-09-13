## Respecting low-level components of content with skip connections and semantic information in image style transfer (CVMP'19)

[Man M. Ho](https://minhmanho.github.io/), [Jinjia Zhou](https://www.zhou-lab.info/jinjia-zhou), Yibo Fan.

[\[ DEMO Video\]](https://www.youtube.com/watch?v=u0S-3AFA1Ro), [\[Comparison Video\]](https://www.youtube.com/watch?v=Q3iGoJzBTwk)

This repository is to support our Paper/DOI: [https://doi.org/10.1145/3359998.3369403](https://doi.org/10.1145/3359998.3369403).

## News

| Date        | News                                                      |
| ----------- | --------------------------------------------------------- |
| 2020/04/04  | Code and trained models now available. |
| 2019/12/15  | Add additional results. |

## Environment Setup
We run our DEMO on Anaconda Environment with following packages:

- OpenCV
- [PyTorch](https://pytorch.org/) >= 1.1.0
- Qdarkstyle
- PyQt5
- Numpy
- gdown


## Get started

Clone this repo:
```bash
git clone https://github.com/minhmanho/respecting_content_ist.git
cd respecting_content_ist
```

Download models
```
bash ./models/fetch_models.sh
```

Stylize a folder of images:

```
python run.py --img_folder <folder_dir> --model <model_dir>
```

Run GUI DEMO:

<img src='images/others/demo.png' width='640'/>

```
python run.py --img <img_dir> --model <model_dir> --auto_update
```

If you have a powerful GPU, let's add *--auto_update* for the better experience.
The application will update every change you make automatically if *auto_update* is activated; otherwise, you have to click the button \[*Update*\].

## Addtional comparison results

### Content

Most of the content images are collected from [Unsplash](https://unsplash.com/)

<p align='center'>
  <img src='images/content/o1.png' width='200'/>
  <img src='images/content/o2.png' width='200'/>
  <img src='images/content/o3.png' width='200'/>
  <img src='images/content/o4.png' width='200'/>
</p>

<p align='center'>
  <img src='images/content/o5.png' width='200'/>
  <img src='images/content/o6.png' width='200'/>
  <img src='images/content/o7.png' width='200'/>
  <img src='images/content/o8.png' width='200'/>
</p>

<p align='center'>
  <img src='images/content/o9.png' width='200'/>
  <img src='images/content/o10.png' width='200'/>
  <img src='images/content/o11.png' width='200'/>
  <img src='images/content/o12.png' width='200'/>
</p>

<p align='center'>
  <img src='images/content/o13.png' width='200'/>
  <img src='images/content/o14.png' width='200'/>
  <img src='images/content/o15.png' width='200'/>
  <img src='images/content/o16.png' width='200'/>
</p>

<p align='center'>
  <img src='images/content/o17.png' width='200'/>
  <img src='images/content/o18.png' width='200'/>
  <img src='images/content/o19.png' width='200'/>
  <img src='images/content/o20.png' width='200'/>
</p>

<p align='center'>
  <img src='images/content/o21.png' width='200'/>
  <img src='images/content/o22.png' width='200'/>
  <img src='images/content/o23.png' width='200'/>
</p>

### Compare to Johnson's work + Instance Normalization

[Source code](https://github.com/pytorch/examples/tree/master/fast_neural_style)

\[Their work\] \[Ours\] \[Their work\] \[Ours\]

  <img src='images/style/candy.jpg' width='200'/> : Candy

<p align='center'>
  <img src='images/compare_to_john/candy/1.png' width='200'/>
  <img src='images/compare_to_john/candy/2.png' width='200'/>
  <img src='images/compare_to_john/candy/3.png' width='200'/>
  <img src='images/compare_to_john/candy/4.png' width='200'/>
</p>

<p align='center'>
  <img src='images/compare_to_john/candy/5.png' width='200'/>
  <img src='images/compare_to_john/candy/6.png' width='200'/>
  <img src='images/compare_to_john/candy/7.png' width='200'/>
  <img src='images/compare_to_john/candy/8.png' width='200'/>
</p>

<p align='center'>
  <img src='images/compare_to_john/candy/9.png' width='200'/>
  <img src='images/compare_to_john/candy/10.png' width='200'/>
  <img src='images/compare_to_john/candy/11.png' width='200'/>
  <img src='images/compare_to_john/candy/12.png' width='200'/>
</p>

  <img src='images/style/udnie.jpg' width='200'/> : Udnie

<p align='center'>
  <img src='images/compare_to_john/udnie/1.png' width='200'/>
  <img src='images/compare_to_john/udnie/2.png' width='200'/>
  <img src='images/compare_to_john/udnie/3.png' width='200'/>
  <img src='images/compare_to_john/udnie/4.png' width='200'/>
</p>


<p align='center'>
  <img src='images/compare_to_john/udnie/5.png' width='200'/>
  <img src='images/compare_to_john/udnie/6.png' width='200'/>
  <img src='images/compare_to_john/udnie/7.png' width='200'/>
  <img src='images/compare_to_john/udnie/8.png' width='200'/>
</p>

<p align='center'>
  <img src='images/compare_to_john/udnie/9.png' width='200'/>
  <img src='images/compare_to_john/udnie/10.png' width='200'/>
  <img src='images/compare_to_john/udnie/11.png' width='200'/>
  <img src='images/compare_to_john/udnie/12.png' width='200'/>
</p>

### Compare to recent works

\[[AdaIn](https://github.com/naoto0804/pytorch-AdaIN)\] \[[WCT](https://github.com/sunshineatnoon/PytorchWCT)\] \[[AvatarNet](https://github.com/LucasSheng/avatar-net)\] \[Ours\]

  <img src='images/style/candy.jpg' width='200'/> : Candy

<p align='center'>
  <img src='images/compare_to_recent/1.jpg' width='200'>
  <img src='images/compare_to_recent/2.png' width='200'>
  <img src='images/compare_to_recent/3.png' width='200'>
  <img src='images/compare_to_recent/4.png' width='200'>
</p>

<p align='center'>
  <img src='images/compare_to_recent/5.jpg' width='200'>
  <img src='images/compare_to_recent/6.png' width='200'>
  <img src='images/compare_to_recent/7.png' width='200'>
  <img src='images/compare_to_recent/8.png' width='200'>
</p>

<p align='center'>
  <img src='images/compare_to_recent/9.jpg' width='200'>
  <img src='images/compare_to_recent/10.png' width='200'>
  <img src='images/compare_to_recent/11.png' width='200'>
  <img src='images/compare_to_recent/12.png' width='200'>
</p>

<p align='center'>
  <img src='images/compare_to_recent/13.jpg' width='200'>
  <img src='images/compare_to_recent/14.png' width='200'>
  <img src='images/compare_to_recent/15.png' width='200'>
  <img src='images/compare_to_recent/16.png' width='200'>
</p>

  <img src='images/style/abstract_girl.jpg' width='200'/> : Watercolor painting portrait of a woman

<p align='center'>
  <img src='images/compare_to_recent/17.jpg' width='200'>
  <img src='images/compare_to_recent/18.png' width='200'>
  <img src='images/compare_to_recent/19.png' width='200'>
  <img src='images/compare_to_recent/20.png' width='200'>
</p>

<p align='center'>
  <img src='images/compare_to_recent/21.jpg' width='200'>
  <img src='images/compare_to_recent/22.png' width='200'>
  <img src='images/compare_to_recent/23.png' width='200'>
  <img src='images/compare_to_recent/24.png' width='200'>
</p>

<p align='center'>
  <img src='images/compare_to_recent/25.jpg' width='200'>
  <img src='images/compare_to_recent/26.png' width='200'>
  <img src='images/compare_to_recent/27.png' width='200'>
  <img src='images/compare_to_recent/28.png' width='200'>
</p>

<p align='center'>
  <img src='images/compare_to_recent/29.jpg' width='200'>
  <img src='images/compare_to_recent/30.png' width='200'>
  <img src='images/compare_to_recent/31.png' width='200'>
  <img src='images/compare_to_recent/32.png' width='200'>
</p>

<p align='center'>
  <img src='images/compare_to_recent/33.jpg' width='200'>
  <img src='images/compare_to_recent/34.png' width='200'>
  <img src='images/compare_to_recent/35.png' width='200'>
  <img src='images/compare_to_recent/36.png' width='200'>
</p>

<p align='center'>
  <img src='images/compare_to_recent/37.jpg' width='200'>
  <img src='images/compare_to_recent/38.png' width='200'>
  <img src='images/compare_to_recent/39.png' width='200'>
  <img src='images/compare_to_recent/40.png' width='200'>
</p>

  <img src='images/style/seated_nude.jpg' width='200'/> : Seated Nude by Pablo Picasso

<p align='center'>
  <img src='images/compare_to_recent/41.jpg' width='200'>
  <img src='images/compare_to_recent/42.png' width='200'>
  <img src='images/compare_to_recent/43.png' width='200'>
  <img src='images/compare_to_recent/44.png' width='200'>
</p>

<p align='center'>
  <img src='images/compare_to_recent/45.jpg' width='200'>
  <img src='images/compare_to_recent/46.png' width='200'>
  <img src='images/compare_to_recent/47.png' width='200'>
  <img src='images/compare_to_recent/48.png' width='200'>
</p>

<p align='center'>
  <img src='images/compare_to_recent/49.jpg' width='200'>
  <img src='images/compare_to_recent/50.png' width='200'>
  <img src='images/compare_to_recent/51.png' width='200'>
  <img src='images/compare_to_recent/52.png' width='200'>
</p>

<p align='center'>
  <img src='images/compare_to_recent/53.jpg' width='200'>
  <img src='images/compare_to_recent/54.png' width='200'>
  <img src='images/compare_to_recent/55.png' width='200'>
  <img src='images/compare_to_recent/56.png' width='200'>
</p>

<p align='center'>
  <img src='images/compare_to_recent/57.jpg' width='200'>
  <img src='images/compare_to_recent/58.png' width='200'>
  <img src='images/compare_to_recent/59.png' width='200'>
  <img src='images/compare_to_recent/60.png' width='200'>
</p>

<p align='center'>
  <img src='images/compare_to_recent/61.jpg' width='200'>
  <img src='images/compare_to_recent/62.png' width='200'>
  <img src='images/compare_to_recent/63.png' width='200'>
  <img src='images/compare_to_recent/64.png' width='200'>
</p>

  <img src='images/style/rabbit_watercolor.jpg' width='200'/> : Watercolor painting of rabbit

<p align='center'>
  <img src='images/compare_to_recent/65.jpg' width='200'>
  <img src='images/compare_to_recent/66.png' width='200'>
  <img src='images/compare_to_recent/67.png' width='200'>
  <img src='images/compare_to_recent/68.png' width='200'>
</p>

<p align='center'>
  <img src='images/compare_to_recent/69.jpg' width='200'>
  <img src='images/compare_to_recent/70.png' width='200'>
  <img src='images/compare_to_recent/71.png' width='200'>
  <img src='images/compare_to_recent/72.png' width='200'>
</p>

  <img src='images/style/sketch.png' width='200'/> : A sketch

<p align='center'>
  <img src='images/compare_to_recent/73.jpg' width='200'>
  <img src='images/compare_to_recent/74.png' width='200'>
  <img src='images/compare_to_recent/75.png' width='200'>
  <img src='images/compare_to_recent/76.png' width='200'>
</p>

<p align='center'>
  <img src='images/compare_to_recent/77.jpg' width='200'>
  <img src='images/compare_to_recent/78.png' width='200'>
  <img src='images/compare_to_recent/79.png' width='200'>
  <img src='images/compare_to_recent/80.png' width='200'>
</p>

<p align='center'>
  <img src='images/compare_to_recent/81.jpg' width='200'>
  <img src='images/compare_to_recent/82.png' width='200'>
  <img src='images/compare_to_recent/83.png' width='200'>
  <img src='images/compare_to_recent/84.png' width='200'>
</p>

<p align='center'>
  <img src='images/compare_to_recent/85.jpg' width='200'>
  <img src='images/compare_to_recent/86.png' width='200'>
  <img src='images/compare_to_recent/87.png' width='200'>
  <img src='images/compare_to_recent/88.png' width='200'>
</p>

<p align='center'>
  <img src='images/compare_to_recent/89.jpg' width='200'>
  <img src='images/compare_to_recent/90.png' width='200'>
  <img src='images/compare_to_recent/91.png' width='200'>
  <img src='images/compare_to_recent/92.png' width='200'>
</p>

<p align='center'>
  <img src='images/compare_to_recent/93.jpg' width='200'>
  <img src='images/compare_to_recent/94.png' width='200'>
  <img src='images/compare_to_recent/95.png' width='200'>
  <img src='images/compare_to_recent/96.png' width='200'>
</p>

<p align='center'>
  <img src='images/compare_to_recent/97.jpg' width='200'>
  <img src='images/compare_to_recent/98.png' width='200'>
  <img src='images/compare_to_recent/99.png' width='200'>
  <img src='images/compare_to_recent/100.png' width='200'>
</p>

<p align='center'>
  <img src='images/compare_to_recent/101.jpg' width='200'>
  <img src='images/compare_to_recent/102.png' width='200'>
  <img src='images/compare_to_recent/103.png' width='200'>
  <img src='images/compare_to_recent/104.png' width='200'>
</p>

<p align='center'>
  <img src='images/compare_to_recent/105.jpg' width='200'>
  <img src='images/compare_to_recent/106.png' width='200'>
  <img src='images/compare_to_recent/107.png' width='200'>
  <img src='images/compare_to_recent/108.png' width='200'>
</p>

  <img src='images/style/udnie.jpg' width='200'/> : Udnie

<p align='center'>
  <img src='images/compare_to_recent/109.jpg' width='200'>
  <img src='images/compare_to_recent/110.png' width='200'>
  <img src='images/compare_to_recent/111.png' width='200'>
  <img src='images/compare_to_recent/112.png' width='200'>
</p>

<p align='center'>
  <img src='images/compare_to_recent/113.jpg' width='200'>
  <img src='images/compare_to_recent/114.png' width='200'>
  <img src='images/compare_to_recent/115.png' width='200'>
  <img src='images/compare_to_recent/116.png' width='200'>
</p>

<p align='center'>
  <img src='images/compare_to_recent/117.jpg' width='200'>
  <img src='images/compare_to_recent/118.png' width='200'>
  <img src='images/compare_to_recent/119.png' width='200'>
  <img src='images/compare_to_recent/120.png' width='200'>
</p>

<p align='center'>
  <img src='images/compare_to_recent/121.jpg' width='200'>
  <img src='images/compare_to_recent/122.png' width='200'>
  <img src='images/compare_to_recent/123.png' width='200'>
  <img src='images/compare_to_recent/124.png' width='200'>
</p>

<p align='center'>
  <img src='images/compare_to_recent/125.jpg' width='200'>
  <img src='images/compare_to_recent/126.png' width='200'>
  <img src='images/compare_to_recent/127.png' width='200'>
  <img src='images/compare_to_recent/128.png' width='200'>
</p>

<p align='center'>
  <img src='images/compare_to_recent/129.jpg' width='200'>
  <img src='images/compare_to_recent/130.png' width='200'>
  <img src='images/compare_to_recent/131.png' width='200'>
  <img src='images/compare_to_recent/132.png' width='200'>
</p>

<p align='center'>
  <img src='images/compare_to_recent/133.jpg' width='200'>
  <img src='images/compare_to_recent/134.png' width='200'>
  <img src='images/compare_to_recent/135.png' width='200'>
  <img src='images/compare_to_recent/136.png' width='200'>
</p>

<p align='center'>
  <img src='images/compare_to_recent/137.jpg' width='200'>
  <img src='images/compare_to_recent/138.png' width='200'>
  <img src='images/compare_to_recent/139.png' width='200'>
  <img src='images/compare_to_recent/140.png' width='200'>
</p>

<p align='center'>
  <img src='images/compare_to_recent/141.jpg' width='200'>
  <img src='images/compare_to_recent/142.png' width='200'>
  <img src='images/compare_to_recent/143.png' width='200'>
  <img src='images/compare_to_recent/144.png' width='200'>
</p>

## License

This repository (as well as its materials) is for non-commercial uses and research purposes only.

## Cite

```
@inproceedings{ho2019respecting,
  title={Respecting low-level components of content with skip connections and semantic information in image style transfer},
  author={Ho, Minh-Man and Zhou, Jinjia and Fan, Yibo},
  booktitle={European Conference on Visual Media Production},
  pages={1--9},
  year={2019}
}
```

## Contact

If you have any suggestions, questions, or the use of these images infringe your copyrights/license, please contact me <man.hominh.6m@stu.hosei.ac.jp>. I will take action ASAP.

## Acknowledgements

We refer the [Interactive Colorization](https://github.com/junyanz/interactive-deep-colorization) to build our demonstration. This work is supported by the State Key Laboratory of ASIC & System, Fudan University, China. 
