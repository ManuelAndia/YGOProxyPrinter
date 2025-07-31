from PyQt5.QtCore import QThread, pyqtSignal
from YGOCardTools import NameMatchesFromYGOProDeck
from fpdf import FPDF
from Utilities_Qt import ThreadStopped

# =============================================================================
# Default parameters
# =============================================================================

# =============================================================================
# Definitions - functions
# =============================================================================

# =============================================================================
# Definitions - worker thread classes
# =============================================================================

class WorkerThreadCardSearch(QThread):
    
    signal = pyqtSignal('PyQt_PyObject')

    def __init__(self):
        QThread.__init__(self)
        
    # run method gets called when we start the thread
    def run(self):
        self.signal.emit(0)
        
        all_params = self.all_params # other parameters
        n = self.n # frame number
        search_string = all_params.frame_contents[n]["card_search_text"] # search string
        language = all_params.language
        
        try:
            self.signal.emit(10) # update progress bar
            
            res = NameMatchesFromYGOProDeck(search_string, language=language) # includes language code
            
            self.signal.emit(80)
            
            elm = {"name_matches":  res,
                   "n":             n}
            
            self.signal.emit(elm) # send dictionary with all the results
            
        except Exception as err:
            self.signal.emit(err)
            return
    
    def stop(self):
        self.requestInterruption()

class WorkerThreadCardImagePull(QThread):
    
    signal = pyqtSignal('PyQt_PyObject')

    def __init__(self):
        QThread.__init__(self)
        
    # run method gets called when we start the thread
    def run(self):
        self.signal.emit(0)
        
        all_params = self.all_params
        N = len(all_params.frame_contents)
        
        try:
            self.signal.emit(10) # update progress bar
            
            res = {}
            res_images = {}
            
            for i, (n, frame_contents) in enumerate(all_params.frame_contents.items()):
                if self.isInterruptionRequested():
                    raise ThreadStopped("Thread was interrupted by user.")
                search_results = frame_contents["search_results"]
                if len(search_results) > 0:
                    ind = frame_contents["current_index"] # current index of the combo box
                    _card = search_results[ind] # Card instance corresponding to the currently-selected search result
                    res[n] = _card.get_image_raw()
                    res_images[n] = _card.get_image()
                self.signal.emit(int(10 + (i/(N-1))*(80-10)))
            
            self.signal.emit(80)
            
            elm = {"images_raw": res, "images": res_images}
            
            self.signal.emit(elm) # send dictionary with all the results
            
        except Exception as err:
            self.signal.emit(err)
            return
    
    def stop(self):
        self.requestInterruption()

class WorkerThreadPDFExport(QThread):
    
    signal = pyqtSignal('PyQt_PyObject')

    def __init__(self):
        QThread.__init__(self)
    
    # run method gets called when we start the thread
    def run(self):
        self.signal.emit(0)
        all_params = self.all_params
        save_file = self.save_file
        
        NN = len(all_params.frame_contents)
        
        try:
            self.signal.emit(10) # update progress bar
            
            pdf = FPDF()
            
            pdf.add_page(format="A4", orientation="portrait")
            
            l = 210 # page width in mm
            card_w = 59 # card width in mm
            x = (l - 3*card_w)/2 # abscissae of left side of leftmost card
            
            L = 297 # page height in mm
            card_h = 86 # card height in mm
            y = (L - 3*card_h)/2 # ordinates of top side of top card
            
            for i, (n, frame_contents) in enumerate(all_params.frame_contents.items()):
                if self.isInterruptionRequested():
                    raise ThreadStopped("Thread was interrupted by user.")
                _image = frame_contents["image"]
                if _image is not None:
                    N = n%3 # index of card horizontally
                    _x = x+N*card_w # horizontal position of current card
                    M = n//3 # index of card vertically
                    _y = y+M*card_h # vertical position of current card
                    pdf.image(_image, _x, _y, card_w, card_h)
                self.signal.emit(int(10 + (i/(NN-1))*(80-10)))
            
            pdf.output(save_file, "F")
            
            self.signal.emit(100)
            
            elm = {"file_saved": save_file}
            
            self.signal.emit(elm) # send dictionary with all the results
            
        except Exception as err:
            self.signal.emit(err)
            return

    def stop(self):
        self.requestInterruption()