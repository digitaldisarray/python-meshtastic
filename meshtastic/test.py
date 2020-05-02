import logging
from . import util
from . import StreamInterface
from pubsub import pub
import time
import threading

"""The interfaces we are using for our tests"""
interfaces = None

"""A list of all packets we received while the current test was running"""
receivedPackets = None

testsRunning = False

testNumber = 0


def onReceive(packet):
    """Callback invoked when a packet arrives"""
    print(f"Received: {packet}")
    if packet.payload.data.typ == "CLEAR_TEXT":
        # We only care a about clear text packets
        receivedPackets.extend(packet)


def onNode(node):
    """Callback invoked when the node DB changes"""
    print(f"Node changed: {node}")


def subscribe():
    """Subscribe to the topics the user probably wants to see, prints output to stdout"""

    pub.subscribe(onNode, "meshtastic.node")


def testSend(fromInterface, toInterface):
    """
    Sends one test packet between two nodes and then returns success or failure

    Arguments:
        fromInterface {[type]} -- [description]
        toInterface {[type]} -- [description]

    Returns:
        boolean -- True for success
    """
    global receivedPackets
    receivedPackets = []
    fromNode = fromInterface.myInfo.my_node_num
    toNode = toInterface.myInfo.my_node_num
    logging.info(f"Sending test packet from {fromNode} to {toNode}")
    fromInterface.sendText(f"Test {testNumber}", toNode)
    time.sleep(10)
    if (len(receivedPackets) < 1):
        logging.error("Test failed, expected packet not received")
        return True
    else:
        logging.info("Test succeeded")
        return False


def testThread():
    logging.info("Found devices, starting tests...")
    while True:
        global testNumber
        testNumber = testNumber + 1
        testSend(interfaces[0], interfaces[1])
        time.sleep(10)


def onConnection(topic=pub.AUTO_TOPIC):
    """Callback invoked when we connect/disconnect from a radio"""
    print(f"Connection changed: {topic.getName()}")

    global testsRunning
    if (all(iface.isConnected for iface in interfaces) and not testsRunning):
        testsRunning = True
        t = threading.Thread(target=testThread, args=())
        t.start()


def openDebugLog(portName):
    debugname = "log" + portName.replace("/", "_")
    logging.info(f"Writing serial debugging to {debugname}")
    return open(debugname, 'w+', buffering=1)


def testAll():
    """
    Run a series of tests using devices we can find.

    Raises:
        Exception: If not enough devices are found
    """
    ports = util.findPorts()
    if (len(ports) != 2):
        raise Exception("Must have at least two devices connected to USB")

    pub.subscribe(onConnection, "meshtastic.connection")
    pub.subscribe(onReceive, "meshtastic.receive")
    global interfaces
    interfaces = list(map(lambda port: StreamInterface(
        port, debugOut=openDebugLog(port)), ports))
    logging.info("Ports opened, waiting for device to complete connection")
