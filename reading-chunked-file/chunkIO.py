from game import Game
from corrupted_chess_file_error import *
from player import Player
from piece import Piece
from board import Board


class ChunkIO(object):
    def load_game(self, input):
        """
        @note:This is the game object this method will fill with data. The object
               is returned when the END chunk is reached.
        """
        self.game = Game()

        try:

            # Read the file header and the save date

            header = self.read_fully(8, input)
            date = self.read_fully(8, input)

            # Process the data we just read.
            # NOTE: To test the line below you must test the class once with a broken header

            header = ''.join(header)
            date = ''.join(date)
            if not str(header).startswith("SHAKKI"):
                raise CorruptedChessFileError("Unknown file type")

            # The version information and the date are not used in this
            # exercise

            self.board = Board()
            self.game.set_board(self.board)

            chunk_header = self.read_fully(5, input)
            chunk_name = self.extract_chunk_name(chunk_header)
            chunk_size = self.extract_chunk_size(chunk_header)
            player_count = 0
            valid_names = ['PLR', 'CMT', 'END']

            while chunk_name != 'END':
                if chunk_name == 'CMT':
                    cmt = ''.join(self.read_fully(chunk_size, input))
                if chunk_name == 'PLR':
                    player = self.create_player(chunk_size, input)
                    player_count += 1
                if player_count > 2:
                    raise CorruptedChessFileError("Too many players!")
                if chunk_name not in valid_names:
                    self.read_fully(chunk_size, input)

                chunk_header = self.read_fully(5, input)
                chunk_name = self.extract_chunk_name(chunk_header)
                chunk_size = self.extract_chunk_size(chunk_header)

            # If we reach this point the Game-object should now have the proper players and
            # a fully set up chess board. Therefore we might as well return it.
            if not player_count == 2:
                raise CorruptedChessFileError("Wrong number of players!")
            return self.game

        except OSError:
            # To test this part the stream would have to cause an
            # OSError. That's a bit complicated to test. Therefore we have
            # given you a "secret tool", class BrokenReader, which will throw
            # an OSError at a requested position in the stream.
            # Throw the exception inside any chunk, but not in the chunk header.
            raise CorruptedChessFileError("Reading the chess data failed 1.")

    # HELPER METHODS -------------------------------------------------------

    def create_player(self, chunk_size, input):

        player_info = self.read_fully(chunk_size, input)
        player_name = ''.join(player_info[2:2 + int(player_info[1])])
        player_color = Player.BLACK if player_info[0] == 'M' else Player.WHITE
        player = Player(player_name, player_color)
        self.game.add_player(player)
        player_pieces = player_info[2 + int(player_info[1]):]
        while player_pieces:
            symbol = player_pieces.pop(0)
            if symbol.isupper():
                if symbol == 'K':
                    piece_type = Piece.KING
                elif symbol == 'D':
                    piece_type = Piece.QUEEN
                elif symbol == 'T':
                    piece_type = Piece.ROOK
                elif symbol == 'L':
                    piece_type = Piece.BISHOP
                elif symbol == 'R':
                    piece_type = Piece.KNIGHT
                else:
                    raise CorruptedChessFileError("invalid piece type")
                col = Board.column_char_to_integer(player_pieces.pop(0))
            elif symbol.isalpha():
                piece_type = Piece.PAWN
                col = Board.column_char_to_integer(symbol)
            row = Board.row_char_to_integer(player_pieces.pop(0))
            piece = Piece(player, piece_type)
            try:
                self.board.set_piece(piece, col, row)
            except ValueError:
                raise CorruptedChessFileError("Square already occupied!")
            except IndexError:
                raise CorruptedChessFileError("invalid square")

        return player

    def extract_chunk_size(self, chunk_header):
        """
        Given a chunk header (an array of 5 chars) will return the size of this
        chunk's data.

        @param chunk_header:
                   a chunk header to process (str)
        @return: the size (int) of this chunks data
        """

        # subtracting the ascii value of the character 0 from
        # a character containing a number will return the
        # number itself

        return int(''.join(chunk_header[3:5]))

    def extract_chunk_name(self, chunk_header):
        """
        Given a chunk header (an array of 5 chars) will return the name of this
        chunk as a 3-letter String.

        @param chunk_header:
                   a chunk header to process
        @return: the name of this chunk
        """
        return ''.join(chunk_header[0:3])

    def read_fully(self, count, input):
        """
        The read-method of the Reader class will occasionally read only part of
        the characters that were requested. This method will repeatedly call read
        to completely fill the given buffer. The size of the buffer tells the
        algorithm how many bytes should be read.

        @param count:
                   How many characters are read
        @param input:
                   The character stream to read from
        @raises: OSError
        @raises: CorruptedChessFileError
        """
        read_chars = input.read(count)

        # If the file end is reached before the buffer is filled
        # an exception is thrown.
        if len(read_chars) != count:
            raise CorruptedChessFileError("Unexpected end of file.")

        return list(read_chars)
