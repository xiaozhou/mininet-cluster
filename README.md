## Mininet Cluster Edition
This repository contains a library and demo scripts of Mininet cluster edition.
It modifies the implementation of Mininet cluster edition in the [official
Mininet repository]. The original prototype connects mininet nodes on different
servers with SSH tunnels, which are secure but relatively slow. We add a new
remote link type that uses GRE tunnel. It introduces less overhead thus can
achieve higher throughput than SSH.

[Mininet] is not included in this repository and needs to be separately
installed in all servers before using this library or running the demo scripts.
Please read the [official Mininet wiki page on cluster edition prototype] for
more details on the design overview and cluster setup.


[Mininet]: <https://github.com/mininet/mininet/>
[official Mininet repository]: <https://github.com/mininet/mininet/>
[official Mininet wiki page on cluster edition prototype]:<https://github.com/mininet/mininet/wiki/Cluster-Edition-Prototype>
