#Retrived from http://stackoverflow.com/a/35753431

import tkinter as tk

class Activity(tk.Label):
    def __init__(self, master = None, delay = 1000, cnf = {}, **kw):
        self._taskID = None
        self.delay = delay
        return super().__init__(master, cnf, **kw)

    # starts the animation
    def start(self):
        self.after(0, self._loop)

    # calls its self after a specific <delay>
    def _loop(self):
        currentText = self["text"] + "."

        if currentText == "....":
            currentText = ""

        self["text"] = currentText

        self._taskID = self.after(self.delay, self._loop)

    # stopps the loop method calling its self
    def stop(self):
        self.after_cancel(self._taskID)
        # Depends if you want to destroy the widget after the loop has stopped
        self.destroy()


class AcitivityImage(Activity):
    def __init__(self, imagename, frames, filetype, master = None, delay = 1000, cnf = {}, **kw):
        self._frames = []
        self._index = 0
        for i in range(frames):
            self._frames.append(tk.PhotoImage(file = imagename+str(i)+'.'+str(filetype)))

        return super().__init__(master, delay, cnf, **kw)

    def _loop(self):
        self["image"] = self._frames[self._index]

        # add one to index if the index is less then the amount of frames
        self._index = (self._index + 1 )% len(self._frames)

        self._taskID = self.after(self.delay, self._loop)