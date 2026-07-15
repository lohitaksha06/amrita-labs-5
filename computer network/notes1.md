acces netowkr: DSL (digital subscriber line)
 1.uses existing telephone line to central
 2.data over dsl phone goes to internet
 3.voice over dsl phone goes to telephone net

acces networks: home networks
 can have wifi or lan also

FTTH - fiber to the home
    run optical fiber directly from the co to the home - simple in principle but delivers much highs peedz

ethernet (lan access)
     common settings: used on corporate campuses, universities and increasingly in home.

physical media
    host sending function:
bit: propagates between
transmitter/reciever pairs

physical link: what lies
between transmitter and reciever 

guided media:
    signal propagte in solid media: copper, fiber, coax

unguided media:
    signals progpagate freely, eg radio
    
coaxial cable:
    two concentric copper conductors
    bidirectional
    broadband:
        multiply fequency channels on cable

fiber optic cable:
    high speed operation:
        high speed point to point transmission.
    low error rate:
        repeaters spaced far apart 
        immune to electromagnetic noise

2 types 
    geostationary satellites:
        fixed above the same point on earth 
        introfuce a significant propagation delay of 280 milliseconds due to the huge distance.
        can oeprate at speeds of hundreds of mbps
        useful in areas lacking dsl/cable access.

2 fundamental approaches
    circuit switching:resources are reserved in advance for duration of the communication session
    packet switching: resources are not reserved used on demand, meaning messages may have to queu for access to a link

store and forward mechanism

2 key network core functions:
forward: aka switching, local action move arriving packets from router's input link to appropriate router output link
routing: global action,determine source destination paths taken by packets, routing algorithms

question: host a wants to transmit a packet which has 10 kb of information. the transmission range of the link is given to be 100 megabytes per second. calculate one hope transmission delay

ans: 1 hope = L/R = 10240/100 000 000 = 0.0001024

convert to miliseconds:
0.0001024 * 1000 = 0.1024 ms

if there are 3 hopes = 3 * L/R
for hopes 3*0.1024 = 0.3072

2 types of multiplexing:
FDM and TDM

FDM: each circuitcontinuously gets a fraction of bandwith.
TDM: each circuit gets all of the bandwidth periodically during brief intervals of line

transmission rate formula = framte rate * bits per slot

question: a transmission rate of a link is 1gb per sec (gbps), each user uses 100 mb per second when active. how many users can use this network under circuit switching and packet switching

circuit switching: number of users supported..

number of user = link capacity/bandwith per user

1000mbps/100mbps = 10

100mbps when active, active 10% of time
since the link capacity is 1000 mbps
1000/10 = 100 so about 100 users can b esupported on average3