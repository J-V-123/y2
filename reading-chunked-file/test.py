import unittest
from io import StringIO

from chunkIO import ChunkIO
from broken_reader import BrokenReader
from corrupted_chess_file_error import CorruptedChessFileError
from piece import Piece


class Test(unittest.TestCase):

    def test_given_example(self):
        """
        IMPORTANT!

        The test method is allowed here to throw the CorruptedChessFileError.

        The reasons for this are
        1) we expect the code to work
        2) if the code throws this exception the test will self.fail

        This is therefore desired behavior for this test. It also removes the problem
        of untestable code in the catch section.
        """
        test_data = u"SHAKKI1205072001" \
                    + u"CMT54Laurin revanssipeli, hyvin huonosti on taas menossa..." \
                    + u"PLR17M5MarkoKa4Ta6b3c3" + u"PLR19V5LAURIKd3Dc4La5Rf1" + u"FOO101234567890" + u"END00"

        self.input_file = StringIO(test_data)

        chunk_IO = ChunkIO()
        # self.input_file = open('game.txt', 'r')
        game = None

        try:
            game = chunk_IO.load_game(self.input_file)
        except CorruptedChessFileError:
            self.fail("Loading a correctly structured file caused an exception")

        self.input_file.close()

        self.assertNotEqual(None, game.get_black(), "Loading data self.failed. Player missing.")
        self.assertEqual("Marko", game.get_black().get_name(), "Loading data self.failed. Wrong player name.")

        # Add your own tests, check that the players are ok and that the pieces were correctly placed.

    def testOSError(self):
        """
        This test was designed to test the catch code in method load_game.
        """
        test_data = u"SHAKKI1205072001" \
                    + u"CMT54Laurin revanssipeli, hyvin huonosti on taas menossa..." \
                    + u"PLR17M5MarkoKa4Ta6b3c3" + "PLR13V5LAURIKd3Rf1" + "END00"

        # original_file = open('game.txt', 'r')

        # Adding a brokenreader allows raising simulated exceptions
        self.input_file = BrokenReader(test_data, 26)

        check_this = None
        try:
            ChunkIO().load_game(self.input_file)
        except CorruptedChessFileError as e:
            check_this = e

        # Note that initially your code does not read past the file header
        # so this test will fail.

        self.assertNotEqual(None, check_this, "A CorruptedChessFileError was not raised.")

        try:
            self.input_file.close()
            self.fail("Closing a file did not cause an exception.")
        except OSError:
            """All ok"""

        self.input_file.close_really()

    def testIllegalPiece(self):

        test_data = u"SHAKKI1205072001" \
                    + u"CMT54Laurin revanssipeli, hyvin huonosti on taas menossa..." \
                    + u"PLR17M5MarkoKa4Ha6b3c3" + "PLR13V5LAURIKd3Rf1" + "END00"
        self.input_file = StringIO(test_data)
        try:
            ChunkIO().load_game(self.input_file)
        except CorruptedChessFileError as e:
            check = e
        self.input_file.close()
        self.assertRaises(CorruptedChessFileError)

    def testTooManyPlayers(self):

        test_data = u"SHAKKI1205072001" \
                    + u"CMT54Laurin revanssipeli, hyvin huonosti on taas menossa..." \
                    + u"PLR17M5MarkoKa4Ta6b3c3" + "PLR13V5LAURIKd3Rf1" + "PLR15V5SeppoKd4Rf2f6" + "END00"
        self.input_file = StringIO(test_data)
        try:
            ChunkIO().load_game(self.input_file)
        except CorruptedChessFileError as e:
            check = e
        self.input_file.close()
        self.assertRaises(CorruptedChessFileError)

    def testTooLittlePlayers(self):

        test_data = u"SHAKKI1205072001" \
                    + u"CMT54Laurin revanssipeli, hyvin huonosti on taas menossa..." \
                    + u"PLR17M5MarkoKa4Ta6b3c3" + "END00"
        self.input_file = StringIO(test_data)
        try:
            ChunkIO().load_game(self.input_file)
        except CorruptedChessFileError as e:
            check = e
        self.input_file.close()
        self.assertRaises(CorruptedChessFileError)

    def testWrongHeader(self):

        test_data = u"SHAKKO1205072001" \
                    + u"CMT54Laurin revanssipeli, hyvin huonosti on taas menossa..." \
                    + u"PLR17M5MarkoKa4Ta6b3c3" + "PLR13V5LAURIKd3Rf1" + "END00"
        self.input_file = StringIO(test_data)
        try:
            ChunkIO().load_game(self.input_file)
        except CorruptedChessFileError as e:
            check = e
        self.input_file.close()
        self.assertRaises(CorruptedChessFileError)

    def testSameSquare(self):

        test_data = u"SHAKKI1205072001" \
                    + u"CMT54Laurin revanssipeli, hyvin huonosti on taas menossa..." \
                    + u"PLR17M5MarkoKa4Ta4b3c3" + "PLR13V5LAURIKa4Rf1" + "END00"
        self.input_file = StringIO(test_data)
        try:
            ChunkIO().load_game(self.input_file)
        except CorruptedChessFileError as e:
            check = e
        self.input_file.close()
        self.assertRaises(CorruptedChessFileError)

    def testInvalidSquare(self):

        test_data = u"SHAKKI1205072001" \
                    + u"CMT54Laurin revanssipeli, hyvin huonosti on taas menossa..." \
                    + u"PLR17M5MarkoKa4Ty4b3c3" + "PLR13V5LAURIKa4Rf1" + "END00"
        self.input_file = StringIO(test_data)
        try:
            ChunkIO().load_game(self.input_file)
        except CorruptedChessFileError as e:
            check = e
        self.input_file.close()
        self.assertRaises(CorruptedChessFileError)

    def testUnexpectedEnd(self):

        test_data = u"SHAKKI1205072001" \
                    + u"CMT54Laurin revanssipeli, hyvin huonosti on taas menossa..." \
                    + u"PLR17M5MarkoKb4Td4b3c3" + "PLR13V5LAURIKa4Rf"
        self.input_file = StringIO(test_data)
        try:
            ChunkIO().load_game(self.input_file)
        except CorruptedChessFileError as e:
            check = e
        self.input_file.close()
        self.assertRaises(CorruptedChessFileError)

    def close_silently(self, r):
        try:
            r.close()
        except OSError:
            """ignore"""


if __name__ == "__main__":
    unittest.main()
