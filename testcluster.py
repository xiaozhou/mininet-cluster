#!/usr/bin/python

import sys, getopt

from cluster import MininetCluster, SwitchBinPlacer
from cluster import RemoteLink, RemoteSSHLink, RemoteGRELink
from clustercli import ClusterCLI as CLI

from mininet.net import Mininet
from mininet.topolib import TreeTopo, TreeNet
from mininet.topo import Topo
from mininet.util import custom, quietRun
from mininet.log import setLogLevel, info

def main(argv):

    Link = RemoteGRELink
    servers = ['localhost', 'mn1.local', 'mn2.local']
    localIP = '10.211.55.12'
    topo = TreeTopo(depth=2, fanout=3)

    try:
        opts, args = getopt.getopt(argv, "l:", ["link="])
    except getopt.GetoptError:
        print './clustertest.py [-l | --link] <link>'
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-l", "--link"):
            if arg in ['ssh', 'SSH']:
                Link = RemoteSSHLink
            elif arg in ['gre', 'GRE']:
                Link = RemoteGRELink

    net = MininetCluster(topo=topo, servers=servers, localIP=localIP,
                         link=Link, placement=SwitchBinPlacer)
    net.start()
    net.pingAll()
    CLI(net).do_plot()
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    main(sys.argv[1:])
