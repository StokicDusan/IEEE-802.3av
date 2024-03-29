[![Commit-activity][commit-activity-shield]][commit-activity-url]
[![Issues][issues-shield]][issues-url]
[![Repo-size][repo-size-shield]][repo-size-url]
[![License][license-shield]][license-url]  
[![Forks][forks-shield]][forks-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

# IEEE 802.3av simulation scripts

This simulation models observe the registration procedure in IEEE 802.3av networks. The aim is to review the performance of the network during the process of finding and registering newly connected optical network units (ONUs) to the optical line terminal (OLT).

Simulations based on article [Allocation of optimal discovery slots in IEEE 802.3av networks][article-bjelica-peric].

## `802-3av-cluster.py` :
Scripts draw a 3D plot of the dependence of registration efficiency (U) upon the number of ONUs (N) placed in a cluster and the maximal wait time (wmax).

## `802-3av-random.py` :
Scripts draw a 3D plot of the dependence of registration efficiency (U) upon the number of ONUs (N) randomly distanced and the maximal wait time (wmax).
## `802-3av-equidistant.py` :
Scripts draw a 3D plot of the dependence of registration efficiency (U) upon the number of ONUs (N) equidistant form each other and the maximal wait time (wmax).

## Installing the dependencies
This script require the mpl_toolkits, pylab, numpy and matplotlib package. To install the packages, execute:
```bash
$ pip install -r requirements.txt
```

## How to use it
#### 1. Clone this repository:
```bash
$ git clone https://github.com/StokicDusan/IEEE-802.3av.git
$ cd IEEE-802.3av/
```
#### 2. Launch
In the command line simply invoke the scripts:
```bash
$ python3 802-3av-cluster.py
$ python3 802-3av-random.py
$ python3 802-3av-equidistant.py
```
## Results
Figures of invoked scripts with 10000 replications are seen below

- Equidistant ONU: <span class="img_container center" style="display: block;">
    <br />
    <img alt="test" src="https://github.com/StokicDusan/IEEE-802.3av/blob/master/assets/Figure_1.png" style="display:block; margin-left: auto; margin-right: auto;" title="caption" />
</span>

- Cluster ONU: <span class="img_container center" style="display: block;">
    <br />
    <img alt="test" src="https://github.com/StokicDusan/IEEE-802.3av/blob/master/assets/Figure_2.png" style="display:block; margin-left: auto; margin-right: auto;" title="caption" /> 
</span>

- Random ONU: <span class="img_container center" style="display: block;">
    <br />
    <img alt="test" src="https://github.com/StokicDusan/IEEE-802.3av/blob/master/assets/Figure_3.png" style="display:block; margin-left: auto; margin-right: auto;" title="caption" />
</span>

Provide Feedback
================

If you encounter any bugs or have suggestions, please file an issue in the [Issues][issues-url] section of the project.

[article-bjelica-peric]: https://www.sciencedirect.com/science/article/abs/pii/S1434841111001981?via%3Dihub
[contributors-shield]: https://img.shields.io/github/contributors/StokicDusan/IEEE-802.3av
[contributors-url]: https://github.com/StokicDusan/IEEE-802.3av/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/StokicDusan/IEEE-802.3av?style=social
[forks-url]: https://github.com/StokicDusan/IEEE-802.3av/network/members
[issues-shield]: https://img.shields.io/github/issues/StokicDusan/IEEE-802.3av
[issues-url]: https://github.com/StokicDusan/IEEE-802.3av/issues
[commit-activity-shield]: https://img.shields.io/github/last-commit/StokicDusan/IEEE-802.3av
[commit-activity-url]: https://github.com/StokicDusan/IEEE-802.3av/graphs/commit-activity
[license-url]: https://github.com/StokicDusan/IEEE-802.3av/blob/master/LICENSE
[license-shield]: https://img.shields.io/github/license/StokicDusan/IEEE-802.3av
[repo-size-shield]: https://img.shields.io/github/repo-size/StokicDusan/IEEE-802.3av
[repo-size-url]: https://img.shields.io/github/repo-size/StokicDusan/IEEE-802.3av
[linkedin-shield]: https://img.shields.io/badge/LinkedIn-0077B5?style=plastice&logo=linkedin&logoColor=white
[linkedin-url]: https://linkedin.com/in/stokicdusan
