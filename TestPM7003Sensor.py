import unittest
from unittest.mock import patch, MagicMock
import serial
from Sensors.particulate_matter import PM7003Sensor
from Database.influxdb import InfluxDB

class TestPM7003Sensor(unittest.TestCase):

    @patch('serial.Serial')
    def test_init_success(self, MockSerial):
        mock_serial_instance = MagicMock()
        mock_serial_instance.is_open = True
        MockSerial.return_value = mock_serial_instance
        sensor = PM7003Sensor()

        # Check if the serial port is open
        MockSerial.assert_called_once()
        self.assertTrue(sensor.ser.is_open)


    @patch('serial.Serial')
    def test_init_failure(self, MockSerial):
        MockSerial.side_effect = serial.SerialException("Failed to open serial port")
        with self.assertRaises(serial.SerialException):
            PM7003Sensor()


    @patch('serial.Serial')
    def test_is_connected_false(self, MockSerial):
        mock_serial_instance = MagicMock()
        MockSerial.return_value = mock_serial_instance
        mock_serial_instance.is_open = False
        sensor = PM7003Sensor()
        self.assertFalse(sensor.is_connected())


if __name__ == '__main__':
    unittest.main()
