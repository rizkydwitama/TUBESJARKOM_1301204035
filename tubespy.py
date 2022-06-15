from mininet.net import Mininet
from mininet.cli import CLI
from mininet.link import Link, TCLink, Intf
from subprocess import Popen, PIPE
from mininet.log import setLogLevel
import time
import os

#BUILD TOPOLOGY
HostA = net.addHost('HostA')
HostB = net.addHost('HostB')
R1 = net.addHost('R1')
R2 = net.addHost('R2')
R3 = net.addHost('R3')
R4 = net.addHost('R4')

#MENDEFINISIKAN BANDWIDTH
bandwidth1 = {'bw':1}
bandwidth2 = {'bw':0.5}

#MENGHUBUNGKAN ANTAR DEVICE
net.addLink(HostA, R1, cls=TCLink, **bandwidth1) #HostA-eth0 R1-eth0
net.addLink(HostA, R2, cls=TCLink, **bandwidth1) #HostA-eth1 R3-eth1
