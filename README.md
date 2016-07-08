## Mininet Cluster Edition
This repository contains a library and demo script of Mininet cluster edition.
It modifies the implementation of Mininet cluster edition in the [official
Mininet repository]. The original prototype connects mininet nodes on different
servers with SSH tunnels, which are secure but relatively slow. We add a new
remote link type that uses GRE tunnel. It has much less overhead and higher
throughput than SSH.

[Mininet] needs to be installed in all servers before using this library or
running the demo. Please read the [official Mininet wiki page on cluster
edition prototype] for more details on cluster setup and design overview.


[Mininet]: <https://github.com/mininet/mininet/>
[official Mininet repository]: <https://github.com/mininet/mininet/>
[official Mininet wiki page on cluster edition prototype]:<https://github.com/mininet/mininet/wiki/Cluster-Edition-Prototype>
