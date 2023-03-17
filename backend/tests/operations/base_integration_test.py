import tempfile
import unittest


class BaseIntegrationTest(unittest.TestCase):
    def setUp(self) -> None:
        self.tempdir = tempfile.TemporaryDirectory()

    def tearDown(self) -> None:
        self.tempdir.cleanup()

    def mock_sqlite_file(self, mock_file):
        """
        This method replaces `config.SQLITE_FILE` with the mock object `mock_file`.
        It should be used in a test method decorator, for example:

        @patch('config.SQLITE_FILE', new_callable=str)
        def test_something(self, mock_file):
            self.mock_sqlite_file(mock_file)
            # Continue with the actual test here
        """
        mock_file.return_value = 'mocked_file.sqlite'
        self.addCleanup(mock_file.stopall)