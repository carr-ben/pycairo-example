import cairo
import random

pointsize_inches = 1/72

chessboard_width = 200
chessboard_height = 100
square_size = 18

data = []

def draw_base(c: cairo.Context):
     c.set_source_rgb(1, 1, 1)
     c.paint()
     c.set_source_rgb(0,0,0)
     for row in range(square_size*2,(chessboard_height+2)*square_size,square_size*5):
          _, _, txt_width, txt_height, _, _ = c.text_extents(str(int(row/square_size)-2))
          # print(f"{txt_width=} {txt_height=}")    
          c.move_to(square_size*2 - txt_width - 2, row + txt_height + ((square_size - txt_height)/2))
          c.show_text(str(int(row/square_size)-2))
     for col in range(square_size*2,(chessboard_width+2)*square_size,square_size*5):
          _, _, txt_width, txt_height, _, _ = c.text_extents(str(int(col/square_size)-2))
          c.move_to(col + ((square_size-txt_width)/2), (chessboard_height+2)*square_size + 2 + txt_height)
          c.show_text(str(int(col/square_size)-2))

def draw_new_page(c: cairo.Context):
     for row in range(square_size*2,(chessboard_height+2)*square_size,square_size):
          for col in range(square_size*2,(chessboard_width+2)*square_size,square_size):
               if (row + col) % (square_size*2) == 0:
                    c.set_source_rgb(random.uniform(0,1),random.uniform(0,1),random.uniform(0,1))
                    c.rectangle(col,row,square_size,square_size)
                    c.fill()

def draw_square(c: cairo.Context):
     pass

if __name__ == "__main__":
     # for i in range(10):
          # data[i] = []
          # for j in range(chessboard_height):
          #      for k in range(chessboard_width):
          #           pass
                    # data[i] = (random.randint(0,99),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1))

     surface = cairo.PDFSurface("test-drawing.pdf", (chessboard_width+4)*square_size, (chessboard_height+4)*square_size)
     context = cairo.Context(surface)

     for i in range(10):
          draw_base(context)
          # for row_num, square_row in enumerate(data[i]):
          #      for col_num, square in enumerate(square_row):
          #           draw_square()
          #           # TODO: 
          draw_new_page(context)
          surface.show_page()
