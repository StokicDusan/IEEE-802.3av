# IEEE 802.3av simulation scripts

This simulation models observe the registration procedure in IEEE 802.3av networks. The aim is to review the performance of the network during the process of finding and registering newly connected optical network units (ONUs) to the optical line terminal (OLT) 

## `802-3av-cluster.py` :
Scripts draw a 3D plot of the dependence of registration efficiency (U) upon the number of ONUs (N) placed in a cluster and the maximal wait time (wmax).

## `802-3av-random.py` :
Scripts draw a 3D plot of the dependence of registration efficiency (U) upon the number of ONUs (N) randomly distanced and the maximal wait time (wmax).
## `802-3av-equidistant.py` :
Scripts draw a 3D plot of the dependence of registration efficiency (U) upon the number of ONUs (N) equidistant form each other and the maximal wait time (wmax).

## Installing the dependencies
This script require the mpl_toolkits, pylab, numpy and matplotlib package. To install the packages, execute:
```zsh
$> pip install -r requirements.txt
```

## How to use it
#### 1. Clone this repository:
```zsh
$> git clone https://github.com/StokicDusan/IEEE-802.3av.git
$> cd IEEE-802.3av
```
#### 2. Launch
In the command line simply invoke the scripts:
```zsh
$> python 802-3av-cluster.py
$ >python 802-3av-random.py
$ >python 802-3av-equidistant.py
```
## Results
Figures of invoked scripts with 10000 of replications are seen below

<span class="img_container center" style="display: block;">
    <img alt="test" src="https://github.com/StokicDusan/IEEE-802.3av/blob/master/assets/Figure_1.png" style="display:block; margin-left: auto; margin-right: auto;" title="caption" />
    <span class="img_caption" style="display: block; text-align: center;">equidistant ONU</span>
</span>

<span class="img_container center" style="display: block;">
    <img alt="test" src="https://github.com/StokicDusan/IEEE-802.3av/blob/master/assets/Figure_2.png" style="display:block; margin-left: auto; margin-right: auto;" title="caption" />
    <span class="img_caption" style="display: block; text-align: center;">cluster ONU</span>
</span>

<span class="img_container center" style="display: block;">
    <img alt="test" src="https://github.com/StokicDusan/IEEE-802.3av/blob/master/assets/Figure_3.png" style="display:block; margin-left: auto; margin-right: auto;" title="caption" />
    <span class="img_caption" style="display: block; text-align: center;">random ONU</span>
</span>

