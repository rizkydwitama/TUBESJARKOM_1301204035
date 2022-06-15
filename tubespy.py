from mininet.net import Mininet
from mininet.cli import CLI
from mininet.link import Link, TCLink, Intf
from subprocess import Popen, PIPE
from mininet.log import setLogLevel
import time
import os

if '__main__' == __name__:
	os.system('mn -c')
	setLogLevel('info')
	net = Mininet(link=TCLink)
	key = "net.mptcp.mptcp_enabled"
	value = 0
	p = Popen("sysctl -w %s=%s" %(key,value), shell=True, stdout=PIPE, stderr=PIPE)
	stdout, stderr = p.communicate()
	print("stdout=",stdout,"stderr=",stderr)

    #BUILD TOPOLOGY
    #ADD HOST
    HostA = net.addHost('HostA')
    HostB = net.addHost('HostB')

    #ADD ROUTER
    R1 = net.addHost('R1')
    R2 = net.addHost('R2')
    R3 = net.addHost('R3')
    R4 = net.addHost('R4')

    #MENDEFINISIKAN BANDWIDTH
    bwA = {'bw':1}
    bwB = {'bw':0.5}

    
    #MENGHUBUNGKAN ANTAR DEVICE
    #Add link 
	net.addLink(HostA, R1, intfName1='HostA-eth0', intfName2='R1-eth0', cls=TCLink, **bwA)
    net.addLink(HostA, R2, intfName1='HostA-eth1', intfName2='R2-eth1', cls=TCLink, **bwA)

    net.addLink(R1, R3, intfName1='R1-eth1', intfName2='R3-eth1', cls=TCLink, **bwB)
    net.addLink(R1, R4, intfName1='R1-eth2', intfName2='R4-eth2', cls=TCLink, **bwA)

    net.addLink(R3, HostB, intfName1='R3-eth0', intfName2='HostB-eth0', cls=TCLink, **bwA)
    net.addLink(R3, R2, intfName1='R3-eth2', intfName2='R2-eth2', cls=TCLink, **bwA)

    net.addLink(HostB, R4, intfName1='HostB-eth1', intfName2='R4-eth1', cls=TCLink, **bwA)
    net.addLink(R4, R2, intfName1='R4-eth0', intfName2='R2-eth0', cls=TCLink, **bwB)

    net.build()
    net.start
    CLI(net)