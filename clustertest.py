#!/usr/bin/python

import sys

from cluster import MininetCluster, SwitchBinPlacer
from cluster import RemoteLink, RemoteSSHLink, RemoteGRELink
from clustercli import ClusterCLI as CLI

from mininet.net import Mininet
from mininet.link import TCIntf
from mininet.node import CPULimitedHost
from mininet.topolib import TreeTopo, TreeNet
from mininet.topo import Topo
from mininet.util import custom, quietRun
from mininet.log import setLogLevel, info
from mininet.node import OVSSwitch, UserSwitch
from mininet.link import TCLink

class myTopo( Topo ):
    def __init__(self, **opts):
        Topo.__init__(self, **opts)
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')

        self.addLink(h1, s1)
        self.addLink(s1, s2)
        self.addLink(s2, h2)


# ./benchmark [mode] [topology] [duration]
if __name__ == '__main__':
    mode = 'cluster'
    topology = 'linear'
    duration = 10
    if len(sys.argv) > 1:
        mode = sys.argv[1]
    if len(sys.argv) > 2:
        topology = sys.argv[2]
    if len(sys.argv) > 3:
        duration = int(sys.argv[3])

    setLogLevel('info')
    if topology in ['linear', 'l']:
        topo = myTopo()
    else:
        topo = TreeTopo(2, 3)
    servers = [ 'localhost', 'mn1.local']
    localIP = '10.211.55.12'
    if mode in ['cluster', 'c']:
        net = MininetCluster(topo=topo, servers=servers, localIP = localIP,
                             link=RemoteGRELink, placement=SwitchBinPlacer)
    else:
        net = Mininet(topo=topo, switch=OVSSwitch)
    net.start()
    CLI(net)
    #net.iperf(seconds=duration)
    net.stop()
