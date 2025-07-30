# Tutorial for YGO Proxy Printer v0.2
1. The interface consists of 9 boxes (3 rows and 3 columns):
```{image} tutorial/1.png
:alt: The interface at startup
:width: 400px
:align: center
```
2. Each box contains two groups: a first group which allows searching for a card name (from the https://www.ygoprodeck.com/ database), in which you may type a few letters and hit the Return button to run the search, and a dropdown list, which displays the search result(s) – if any;
```{image} tutorial/2.png
:alt: Picking a card from the search results
:width: 400px
:align: center
```
3. And a second group which allows deleting the current search results for a given box (using the central <img src="img/delete.png" width="20px" /> "delete" button), or copying the search result(s) of a neighbouring box (using one of the four ↑↓←→ arrow buttons):
```{image} tutorial/3.png
:alt: Using the "Copy from / delete" group
:width: 400px
:align: center
```
4. Click "Get images" to pull each card's image from the server (ignores any box with no search results). The progress bar will start filling and you may stop the process using the "STOP" button:
```{image} tutorial/4.png
:alt: Pulling images from database
:width: 400px
:align: center
```
5. If successful, the boxes will now display their respective card's image in the background (at this point, you may still change any of the boxes' contents, but you'll have to click "Get images" again to update the pictures):
```{image} tutorial/5.png
:alt: Card images successfully pulled
:width: 400px
:align: center
```
6. You may export the result to a `.pdf` file using the "Export to PDF" button. If successful, the operation will show a prompt with two buttons, one of which allows the user to reveal the exported PDF in their OS's file browser:
```{image} tutorial/6.png
:alt: PDF export successful
:width: 400px
:align: center
```
7. The resulting PDF will have all cards with the correct size on an A4 page, with no spacing between the cards to facilitate the cutout process, and the document is ready to print (do not forget to check the "Actual size" check box of your PDF reader's printer interface):
```{image} tutorial/7.png
:alt: Preview of the exported PDF file
:width: 400px
:align: center
```