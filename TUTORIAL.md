# YGO Proxy Printer tutorial
> [!NOTE]
> You can change the language of the search by clicking one of the flags at the top of the window. The current choices are:
> * English (default) <img src="img/united-kingdom.png" width="20px" />
> * French (Français) <img src="img/france.png" width="20px" />
> * German (Deutsch) <img src="img/germany.png" width="20px" />
> * Italian (Italiano) <img src="img/italy.png" width="20px" />
> * Portuguese (Português) <img src="img/portugal.png" width="20px" />

> [!WARNING]
> Note that changing the language of the search **will not affect the display language of the final card picture (only available in English for now)**.

* The interface consists of 9 boxes (3 rows and 3 columns):

<img src="tutorial/1.png" width="500px" alt="The graphical user interface, at startup." />

* Each box contains two groups: The first group allows searching for a card name (from the https://www.ygoprodeck.com/ database). You may type a few letters and hit the Return button or click the <img src="img/magnifier.png" width="15px" /> "search" button to run the search. The search result(s), if any, will be displayed in the dropdown list below the search bar, in the same box.

<img src="tutorial/2.png" width="500px" alt="Selecting a search result." />

* In the second group, one can choose between deleting the current search results for the current box (using the central <img src="img/delete.png" width="15px" /> "delete" button) and copying the search result(s) of the current box towards a neighbouring box (using one of the four <img src="img/up-arrow.png" width="15px" /><img src="img/down-arrow.png" width="15px" /><img src="img/left-arrow.png" width="15px" /><img src="img/right-arrow.png" width="15px" /> arrow buttons).

<img src="tutorial/3_1.png" width="500px" alt='Using the "Copy down" option on box number 2.' />
<img src="tutorial/3_2.png" width="500px" alt='After using the "Copy down" option on box number 2, box number 5 (just underneath box number 2) now has the same search results as box number 2.' />
<img src="tutorial/3_3.png" width="500px" alt='Using the "delete" option on box number 5.' />
<img src="tutorial/3_4.png" width="500px" alt='After using the "delete" option on box number 5, the box is now reset to an empty box.' />

> [!NOTE]
> From version 0.3.5, it is now possible to select the desired artwork variant from any card that has two or more possible artworks from which to choose, using the dropdown menu which will be automatically available in that case. See the following example with "Dark Magician" which has 9 available artworks:
> 
> <img src="tutorial/4.png" width="500px" alt='Selecting desired artwork among several choices, when available.' />

* Click <img src="img/picture.png" width="15px" /> "Get images" to pull each card's image from the server (ignores any box with no search results). The progress bar will start filling and you may stop the process using the "<span style="color: red">STOP</span>" button:

<img src="tutorial/5_1.png" width="500px" alt='Before clicking "Get images".' />
<img src="tutorial/5_2.png" width="500px" alt='After clicking "Get images", the progress bar will start filling and a "STOP" button replaces the previous "Get images" button until operation is complete or cancelled by user.' />

* If successful, the boxes will now display their respective card's image in the background (at this point, you may still change any of the boxes' contents, but you'll have to click <img src="img/picture.png" width="15px" /> "Get images" again to update the pictures):

<img src="tutorial/6.png" width="500px" alt="The images of the chosen card(s) now appear in the background of each box where a card was chosen." />

* You can export the result to a `.pdf` file using the <img src="img/floppy-disk.png" width="15px" /> "Export to PDF" button. If successful, the operation will show a prompt with two buttons, one of which allows the user to reveal the exported PDF in their OS's file browser:

<img src="tutorial/7.png" width="500px" alt='After a successful export to PDF, the user is presented with two options: either confirming by clicking "OK", or revealing the exported file in their storage.' />

* The resulting PDF will have all cards with the correct size on an A4 page, with no spacing between the cards to facilitate the cutout process, and the document is ready to print (do not forget to check the "Actual size" check box of your PDF reader's printer interface):

<img src="tutorial/8.png" width="500px" alt="Screenshot of the resulting PDF file for the example above." />