#!/usr/bin/python

import sys, getopt

from cluster import MininetCluster, SwitchBinPlacer
from cluster import RemoteSSHLink, RemoteGRELink
from clustercli import ClusterCLI as CLI

from mininet.topolib import TreeTopo
from mininet.log import setLogLevel

servers = ['localhost', 'mn1.local', 'mn2.local']

def main(argv):

    Link = RemoteGRELink
    topo = TreeTopo(depth=2, fanout=3)
    plot = False

    try:
        opts, args = getopt.getopt(argv, "hpt:", ["tunnel="])
    except getopt.GetoptError:
        print './clustertest.py -t <tunnel> -p'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print './clustertest.py -t <tunnel(ssh|gre)> -p'
            sys.exit()
        if opt in ("-t", "--tunnel"):
            if arg in ['ssh', 'SSH']:
                Link = RemoteSSHLink
            elif arg in ['gre', 'GRE']:
                Link = RemoteGRELink
        if opt == '-p':
            plot = True

    net = MininetCluster(topo=topo, servers=servers, link=Link,
                         placement=SwitchBinPlacer)
    net.start()
    net.pingAll()
    if plot:
        CLI(net).do_plot()
    else:
        CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    main(sys.argv[1:])
