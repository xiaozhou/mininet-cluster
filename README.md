## Mininet Cluster Edition
This repository contains a prototype and test scripts of Mininet cluster
edition. It modifies the implementation of Mininet cluster edition in the
[official Mininet repository]. The original implementation connects mininet
nodes on different servers with SSH tunnels, which is secure but relatively
slow. We add a new remote link type that uses GRE tunnel, which has much less
overhead and higher throughput than SSH.

Please first read the [official Mininet wiki page on cluster edition prototype].


[official Mininet repository]: <https://github.com/mininet/mininet/>
[official Mininet wiki page on cluster edition prototype]:<https://github.com/mininet/mininet/wiki/Cluster-Edition-Prototype>
