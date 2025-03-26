import unittest
from unittest.mock import patch, MagicMock
import serial
from io import BytesIO
from Sensors.particulate_matter import PM7003Sensor
from Database.influxdb import InfluxDB

class TestPM7003Sensor(unittest.TestCase):

    @patch('serial.Serial')
    def test_init_success(self, MockSerial):
        mock_serial_instance = MagicMock()
        MockSerial.return_value = mock_serial_instance

        sensor = PM7003Sensor()
        self.assertEqual(sensor.serial_port, '/dev/ttyAMA2')
        self.assertEqual(sensor.baudrate, 9600)
        mock_serial_instance.open.assert_called_once()

    # @patch('serial.Serial')
    # def test_init_failure(self, MockSerial):
    #     MockSerial.side_effect = serial.SerialException("Failed to open serial port")
    #     with self.assertRaises(serial.SerialException):
    #         PM7003Sensor()

    # @patch('serial.Serial')
    # @patch.object(InfluxDB, 'write_pm_data')
    # def test_read_data_valid(self, MockWritePMData, MockSerial):
    #     mock_serial_instance = MagicMock()
    #     MockSerial.return_value = mock_serial_instance
    #     mock_serial_instance.readable.return_value = True
    #     mock_serial_instance.read.return_value = bytes([0x42, 0x4D, 0] * 10 + [0x00, 0x10, 0x00, 0x15, 0x00, 0x1A])  # Mock valid data

    #     influx_db_mock = MagicMock()
    #     MockWritePMData.return_value = None

    #     sensor = PM7003Sensor()
    #     sensor.read_data()
    #     MockWritePMData.assert_called_once_with(16, 21, 26)

    # @patch('serial.Serial')
    # def test_read_data_invalid_header(self, MockSerial):
    #     mock_serial_instance = MagicMock()
    #     MockSerial.return_value = mock_serial_instance
    #     mock_serial_instance.readable.return_value = True
    #     mock_serial_instance.read.return_value = bytes([0x42, 0x4D, 0] * 10 + [0x00, 0x10, 0x00, 0x15, 0x00, 0x1A])

    #     sensor = PM7003Sensor()
    #     sensor.read_data()
    #     mock_serial_instance.read.assert_called_once()
    
    # @patch('serial.Serial')
    # def test_read_data_no_data(self, MockSerial):
    #     mock_serial_instance = MagicMock()
    #     MockSerial.return_value = mock_serial_instance
    #     mock_serial_instance.readable.return_value = True
    #     mock_serial_instance.read.return_value = b'' 

    #     sensor = PM7003Sensor()
    #     sensor.read_data()
    #     influx_db_mock = MagicMock()
    #     influx_db_mock.write_pm_data.assert_not_called()

    # @patch('serial.Serial')
    # def test_read_data_error(self, MockSerial):
    #     mock_serial_instance = MagicMock()
    #     MockSerial.return_value = mock_serial_instance
    #     mock_serial_instance.readable.return_value = False

    #     sensor = PM7003Sensor()
    #     with self.assertRaises(Exception):
    #         sensor.read_data()

    # @patch('serial.Serial')
    # def test_is_connected_true(self, MockSerial):
    #     mock_serial_instance = MagicMock()
    #     MockSerial.return_value = mock_serial_instance
    #     mock_serial_instance.is_open = True

    #     sensor = PM7003Sensor()
    #     self.assertTrue(sensor.is_connected())

    # @patch('serial.Serial')
    # def test_is_connected_false(self, MockSerial):
    #     mock_serial_instance = MagicMock()
    #     MockSerial.return_value = mock_serial_instance
    #     mock_serial_instance.is_open = False

    #     sensor = PM7003Sensor()
    #     self.assertFalse(sensor.is_connected())


if __name__ == '__main__':
    unittest.main()
