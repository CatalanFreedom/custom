#!/usr/bin/python
from mininet.net import Mininet
from mininet.node import Controller, RemoteController
from mininet.cli import CLI
from mininet.link import Intf
from mininet.log import setLogLevel, info
from mininet.link import TCLink
#Definisco la rete
def myNetwork():
	net = Mininet(topo=None,
	build=False, link=TCLink)
	#Aggiungo il Controller Remoto
	info('*** Adding controller\n') #con il comando info si stampano a video alcune scritte
	net.addController(name='c0',
	controller=RemoteController,
#	ip='192.168.224.133',
	port=6633)

	# aggiungo 3 SWITCH
	info( '*** Add switches\n')
	s1 = net.addSwitch('s1')
	s2 = net.addSwitch('s2')
	s3 = net.addSwitch('s3')

#	Intf('eth2',node = s1)
	#aggiungo 6 HOST
	info('*** Add hosts\n')
	h1 = net.addHost('h1', ip='10.0.0.1')
	h2 = net.addHost('h2', ip='10.0.0.2')
	h3 = net.addHost('h3', ip='10.0.0.3')
	h4 = net.addHost('h4', ip='10.0.0.4')

	# 3 host collegati a s1 3 host collegati a s2
	# switch tutti collegati tra loro eccetto 3 a 4
	info('*** Add links\n')
	net.addLink(h1, s1)
	net.addLink(h2, s1)
	net.addLink(h3, s2)
	net.addLink(h4, s2)
	net.addLink(s1, s2)
	net.addLink(s1, s3)
	net.addLink(s3, s2)

	Intf('eth2',node = s1)

	info('*** Starting network\n')
	#avvio la rete
	net.start()
	#Collego lo switch s1 alla porta eth1 della VM
	s1.cmd('ovs-vsctl add-port s1 eth2')
	# s1.cmd('ifconfig s1 10.0.0.5')
	#Avvio la CLI per la rete
	CLI(net)
	net.stop()
if __name__ == '__main__':
	setLogLevel('info')
	myNetwork()