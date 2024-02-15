from tkinter import Tk, messagebox, BOTH, X, N, LEFT, Frame, Label, Entry, Button, Checkbutton, IntVar,RAISED, RIGHT, filedialog, END
from GroupMerger import multiSubMerger


class SubtitleMerger(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent = parent
        self.initUI()
        self.initialDir = "/"

    def initUI(self):
        self.parent.title("Group Subtitle Merger")
        self.pack(fill=BOTH, expand=True)

        frame1 = Frame(self, relief=RAISED, borderwidth=1)
        frame1.pack(fill=X)

        lbl1 = Label(frame1, text="Series Folder", width=15)
        lbl1.pack(side=LEFT, padx=5, pady=5)

        entry1 = Entry(frame1)
        entry1.pack(side=LEFT, fill=X, padx=5, expand=True)

        button1 = Button(frame1, text="Browse...", width=10, command=lambda: bt1Callback())
        button1.pack(fill=X, padx=5)

        frame2 = Frame(self, relief=RAISED, borderwidth=1)
        frame2.pack(fill=X)

        lbl2 = Label(frame2, text="Subtitles Folder", width=15)
        lbl2.pack(side=LEFT, padx=5, pady=5)

        entry2 = Entry(frame2)
        entry2.pack(side=LEFT, fill=X, padx=5, expand=True)

        button2 = Button(frame2, text="Browse...", width=10, command=lambda: bt2Callback())
        button2.pack(fill=X, padx=5)

        frame3 = Frame(self, relief=RAISED, borderwidth=1)
        frame3.pack(fill=X)

        lbl3 = Label(frame3, text="MKVmerge Folder", width=15)
        lbl3.pack(side=LEFT, anchor=N, padx=5, pady=5)

        entry3 = Entry(frame3)
        entry3.pack(side=LEFT, fill=X, padx=5, expand=True)
        entry3.insert(0, "C:\\Program Files\\MKVToolNix")

        button3 = Button(frame3, text="Browse...", width=10, command=lambda: bt3Callback())
        button3.pack(fill=X, padx=5)

        frame4 = Frame(self, relief=RAISED, borderwidth=1)
        frame4.pack(fill=X)

        lbl4 = Label(frame4, text="Output Folder", width=15)
        lbl4.pack(side=LEFT, padx=5, pady=5)

        entry4 = Entry(frame4)
        entry4.pack(side=LEFT, fill=X, padx=5, expand=True)

        button4 = Button(frame4, text="Browse...", width=10, command=lambda: bt4Callback())
        button4.pack(fill=X, padx=5)

        frame5 = Frame(self)
        frame5.pack(fill=X)

        checkBoxValue = IntVar()
        checkBox = Checkbutton(frame5, text=" Keep Previous Subtitles ", width=25, variable = checkBoxValue, onvalue = 1, offvalue = 0)
        checkBox.deselect()
        checkBox.pack(side=LEFT, padx=5, pady=5)

        closeButton = Button(frame5, text="GoodBye!", width=15, command=lambda: cbCallback())
        closeButton.pack(side=RIGHT, padx=5, pady=5)

        okButton = Button(frame5, text="Start Merging", width=15, command=lambda: okCallback())
        okButton.pack(side=RIGHT, padx=5, pady=5)

        def bt1Callback():
            if entry1.get() != "":
                self.initialDir = entry1.get()
            dirnameInputSeries = filedialog.askdirectory(initialdir=self.initialDir, title='Please select a directory')
            entry1.delete(0, END)
            entry1.insert(0, dirnameInputSeries)
            if entry4.get() == "" and entry1.get() != "":
                entry4.delete(0, END)
                entry4.insert(0, dirnameInputSeries + "\\MergedWithSubtitles")
                self.initialDir = dirnameInputSeries

        def bt2Callback():
            if entry2.get() != "":
                self.initialDir = entry2.get()
            dirnameSubtitles = filedialog.askdirectory(initialdir=self.initialDir, title='Please select a directory')
            entry2.delete(0, END)
            entry2.insert(0, dirnameSubtitles)
            checkBox.flash()
            if entry2.get() != "":
                self.initialDir = dirnameSubtitles

        def bt3Callback():
            if entry3.get() != "" and entry1.get() == "" and entry4.get() == "" and entry2.get() == "":
                self.initialDir = entry3.get()
            dirnameMKVmerge = filedialog.askdirectory(initialdir=self.initialDir, title='Please select a directory')
            entry2.delete(0, END)
            entry2.insert(0, dirnameMKVmerge)

        def bt4Callback():
            if entry4.get() != "":
                self.initialDir = entry4.get()
            dirnameOutputs = filedialog.askdirectory(initialdir=self.initialDir, title='Please select a directory')
            entry4.delete(0, END)
            entry4.insert(0, dirnameOutputs)
            if entry4.get() != "":
                self.initialDir = dirnameOutputs

        def cbCallback():
            self.parent.destroy()

        def okCallback():
            message = multiSubMerger(entry4.get(), entry1.get(), entry2.get(), entry3.get(), checkBoxValue)
            messagebox.showinfo("!", message)


def main():
    root = Tk()
    root.geometry("700x180+500+500")
    app = SubtitleMerger(root)
    root.mainloop()


if __name__ == '__main__':
    main()
