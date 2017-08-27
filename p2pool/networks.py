from p2pool.bitcoin import networks
from p2pool.util import math

# CHAIN_LENGTH = number of shares back client keeps
# REAL_CHAIN_LENGTH = maximum number of shares back client uses to compute payout
# REAL_CHAIN_LENGTH must always be <= CHAIN_LENGTH
# REAL_CHAIN_LENGTH must be changed in sync with all other clients
# changes can be done by changing one, then the other

nets = dict(

 DeepOnion=math.Object(
        PARENT=networks.nets['DeepOnion'],
        SHARE_PERIOD=40,
        NEW_SHARE_PERIOD=40,
        CHAIN_LENGTH=24*60*60//10,
        REAL_CHAIN_LENGTH=24*60*60//10,
        TARGET_LOOKBEHIND=200,
        SPREAD=30,
        NEW_SPREAD=30,
        IDENTIFIER='1bfe1e0a01f6844b'.decode('hex'),
        PREFIX='1bfe1e0a0327b14c'.decode('hex'),
        P2P_PORT=28743,
        MIN_TARGET=0,
        MAX_TARGET=2**256//2**20 - 1,
        PERSIST=False,
        WORKER_PORT=28744,
        BOOTSTRAP_ADDRS=' '.split(' '),
        ANNOUNCE_CHANNEL='#p2pool-onion',
        VERSION_CHECK=lambda v: True,
    ),
)
for net_name, net in nets.iteritems():
    net.NAME = net_name
