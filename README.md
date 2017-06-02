## Segmenting the given image into three different regions

Firstly,  an initial look-up on the image made it clear that the Optic Disk class, the atrophy class and the background class are all touching each other and hence, the traditional thresholding and contour detection methods would be unable to treat them distinctly.

### A naive approach with the Watershed algorithm

A second thought was the marker-based image segmentation using Watershed algorithm ([naive_watershed.py](https://github.com/Saurav0074/Advenio/blob/master/naive_watershed.py)), which is considered to be very useful in such cases because of its implicit assumption of the image surface being composed of peaks and valleys where high intensity denotes peaks and hills while low intensity denotes valleys; we start by filling water (color) in the valleys and making barriers in order to prevent the merging of peaks with valleys; these barriers eventually form the border-line of segmentation. An additional benifit of this method is the identification of background, foreground as well as the unknown regions which can't be surely classified as either (this fits our case very closely).

The output of applying a naive watershed algorithm to the image:
 
 ![Naive Watershed result](output.png)
 
 The algorithm is okay with the optic disk (the sure foreground class) and background (the sure background) classes but fails to recognise the fainter atrophy class distinctly (which it should have recognised as an unknown region) and instead includes it in the sure background class.
 
 Next, I went on to see the contours plotted by the above naive watershed algorithm ([finding_Contours.py](https://github.com/Saurav0074/Advenio/blob/master/finding_Contours.py)) in order to find the regions which were being considered distinct by the algorithm. 
 
 ![Contours plotted by the naive watershed algorithm](finding_Contours.png)
 
 The output observed clarifies the above point as no single contour falls solely within the Atrophy Class region. This indicates that the algorithm somehow can't classify the Atrophy class's pixel intensities, i.e. it treats them similar to the values of the neighboring background class. This led me to my final approach.

### Final approach : Watershed along with color-space conversion

Now, the foremost task was to detect the Atrophy class region. For this purpose, I applied a color-space conversion of the orginial image from RGB to L*a*b*, and found out that the Atrophy region could be clearly recognised by varying the values of the a-channel. Following is the output with the color range set between `[10, 10, 0]` and `[185, 146, 255]` in order to discard the rest of the pixels of the image ( the range was obtained by manual tweaking of the values):

![Atrophy region](atrophy.png)


 
