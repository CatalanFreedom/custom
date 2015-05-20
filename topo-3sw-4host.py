"""Custom topology example

Two directly connected switches plus a host for each switch:

   host --- switch --- switch --- host

Adding the 'topos' dict with a key/value pair to generate our newly defined
topology enables one to pass in '--topo=mytopo' from the command line.
"""

from mininet.topo import Topo

class MyTopo( Topo ):
    "Simple topology example."

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

        # Add hosts and switches
        leftHosts1 = self.addHost( 'h1' )
        rightHosts1 = self.addHost( 'h2' )
	leftHosts2 = self.addHost( 'h3' )
	rightHosts2 = self.addHost( 'h4' )
        leftSwitch = self.addSwitch( 's1' )
        rightSwitch = self.addSwitch( 's2' )
	filterSwitch = self.addSwitch( 's3' )

        # Add links
        self.addLink( leftHosts1, leftSwitch )
	self.addLink( rightHosts1, leftSwitch )
	self.addLink( leftHosts2, rightSwitch )
	self.addLink( rightHosts2, rightSwitch )

        self.addLink( leftSwitch, rightSwitch )
	self.addLink( leftSwitch, filterSwitch )
	self.addLink( filterSwitch, rightSwitch )


topos = { 'mytopo': ( lambda: MyTopo() ) }
