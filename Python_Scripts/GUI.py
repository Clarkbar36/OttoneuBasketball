import  tkinter as tk
import CR_Model_Build_Test as cr

root = tk.Tk()
root.title("NBA Lineup Builder")
root.grid_rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

frame_main = tk.Frame(root, bg="gray")
frame_main.grid(sticky='news')


# Create a frame for the canvas with non-zero row&column weights
frame_canvas = tk.Frame(frame_main)
frame_canvas.grid(row=2, column=0, pady=(5, 0), sticky='nw')
frame_canvas.grid_rowconfigure(0, weight=1)
frame_canvas.grid_columnconfigure(0, weight=1)
# Set grid_propagate to False to allow 5-by-5 buttons resizing later
frame_canvas.grid_propagate(False)

# Add a canvas in that frame
canvas = tk.Canvas(frame_canvas, bg="yellow")
canvas.grid(row=0, column=0, sticky="news")

# Link a scrollbar to the canvas
vsb = tk.Scrollbar(frame_canvas, orient="vertical", command=canvas.yview)
vsb.grid(row=0, column=7, sticky='ns')
canvas.configure(yscrollcommand=vsb.set)

# Create a frame to contain the buttons
frame_buttons = tk.Frame(canvas, bg="blue")
canvas.create_window((0, 0), window=frame_buttons, anchor='nw')

pcount = 0
colCount = 0
rowCount = 0
prevName = cr.player_deck[pcount][0]
for players in cr.player_deck:

    pName = cr.player_deck[pcount][0]
    pPos = cr.player_deck[pcount][1]
    pTeam = cr.player_deck[pcount][2]
    pInjured = cr.player_deck[pcount][3]
    pMin = cr.player_deck[pcount][4]
    pFppg = cr.player_deck[pcount][5]
    pGmDate = cr.player_deck[pcount][6]
    gm_date2 = pGmDate.strftime("%m/%d/%y")

    button_1 = tk.Button(frame_buttons, text=f"{pName}\n{pPos}\n{pTeam}\n{pInjured}\n{pMin}\n{pFppg}\n{gm_date2}\n")

    if pName == prevName:
        colCount += 1
    else:
        rowCount += 1
        colCount = 0

    button_1.grid(row=rowCount, column=colCount)
    pcount += 1
    prevName = pName

frame_buttons.update_idletasks()
frame_canvas.config(width=1080,height=1080)

canvas.config(scrollregion=canvas.bbox("all"))

root.mainloop()
