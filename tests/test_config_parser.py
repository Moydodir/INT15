import unittest
from main import config_parser, param_finder


class TestConfigParser(unittest.TestCase):

    def setUp(self):
        """
        Prepare test data before each test case.
        Creates sample blocks and expected results for parsing.
        """
        self.blocks = [
            ' 0 RS ;;; LAN\n' +
            '      name="LAN" default-name="ether2" mtu=1500 mac-address=50:00:00:31:00:01 orig-mac-address=50:00:00:31:00:01 ' +
            'arp=enabled arp-timeout=auto loop-protect=on loop-protect-status=on\n' +
            '      loop-protect-send-interval=5s loop-protect-disable-time=5m disable-running-check=yes ' +
            'auto-negotiation=yes advertise=10M-half,10M-full,100M-half,100M-full,1000M-full full-duplex=yes\n' +
            '      tx-flow-control=off rx-flow-control=off cable-settings=default speed=1Gbps bandwidth=unlimited/unlimited\n \n',

            ' 1 R  name="ether1" default-name="ether1" mtu=1500 mac-address=50:00:00:31:00:00 orig-mac-address=50:00:00:31:00:00 ' +
            'arp=enabled arp-timeout=auto loop-protect=default loop-protect-status=off\n' +
            '      loop-protect-send-interval=5s loop-protect-disable-time=5m disable-running-check=yes ' +
            'auto-negotiation=yes advertise=10M-half,10M-full,100M-half,100M-full,1000M-full full-duplex=yes\n' +
            '      tx-flow-control=off rx-flow-control=off cable-settings=default speed=1Gbps bandwidth=unlimited/unlimited\n \n',

            ' 2 RS name="ether3" default-name="ether3" mtu=1500 mac-address=50:00:00:31:00:02 orig-mac-address=50:00:00:31:00:02 ' +
            'arp=proxy-arp arp-timeout=auto loop-protect=default loop-protect-status=off\n' +
            '      loop-protect-send-interval=5s loop-protect-disable-time=5m disable-running-check=yes ' +
            'auto-negotiation=yes advertise=10M-half,10M-full,100M-half,100M-full,1000M-full full-duplex=yes\n' +
            '      tx-flow-control=off rx-flow-control=off cable-settings=default speed=1Gbps bandwidth=unlimited/unlimited\n \n'
        ]

    def test_param_finder(self):
        """
        Test that param_finder correctly extracts parameters from blocks.
        """
        block = self.blocks[1]  # Using the second block for this test
        expected_params = {
            "Id": "ether1",
            "Name": "ether1",
            "Description": None,
            "MacAddress": "50:00:00:31:00:00",
            "Status": "up"
        }

        params = param_finder(block)

        self.assertEqual(params["Id"], expected_params["Id"])
        self.assertEqual(params["Name"], expected_params["Name"])
        self.assertEqual(params["Description"], expected_params["Description"])
        self.assertEqual(params["MacAddress"], expected_params["MacAddress"])
        self.assertEqual(params["Status"], expected_params["Status"])

    def test_config_parser(self):
        """
        Test that config_parser correctly processes the blocks and returns instances of SettingModel.
        """
        interfaces = config_parser(self.blocks)

        # Check the number of interfaces created
        self.assertEqual(len(interfaces), 3, "Should parse 3 interfaces")

        # Check that the first interface is created correctly
        self.assertEqual(interfaces[0].Id, "LAN")
        self.assertEqual(interfaces[0].Name, "ether2")
        self.assertEqual(interfaces[0].MacAddress, "50:00:00:31:00:01")
        self.assertEqual(interfaces[0].Status, "up")

        # Check that the second interface is created correctly
        self.assertEqual(interfaces[1].Id, "ether1")
        self.assertEqual(interfaces[1].Name, "ether1")
        self.assertEqual(interfaces[1].MacAddress, "50:00:00:31:00:00")
        self.assertEqual(interfaces[1].Status, "up")

        # Check that the third interface is created correctly
        self.assertEqual(interfaces[2].Id, "ether3")
        self.assertEqual(interfaces[2].Name, "ether3")
        self.assertEqual(interfaces[2].MacAddress, "50:00:00:31:00:02")
        self.assertEqual(interfaces[2].Status, "up")

if __name__ == "__main__":
    unittest.main()





