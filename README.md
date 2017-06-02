## Segmenting the given image into three different regions

Firstly,  an initial look-up on the image makes it clear that the Optic Disk class, the atrophy class and the background class are all touching each other and hence, the traditional thresholding and contour detection methods would be unable to treat them distinctly.

### A naive approach with the Watershed algorithm

A second thought is the marker-based image segmentation using Watershed algorithm ([naive_watershed.py](https://github.com/Saurav0074/Advenio/blob/master/naive_watershed.py)), which is considered to be very useful in such cases because of its implicit assumption of the image surface being composed of peaks and valleys where high intensity denotes peaks and hills while low intensity denotes valleys; we start by filling water (color) in the valleys and making barriers in order to prevent the merging of peaks with valleys; these barriers eventually form the border-line of segmentation. An additional benifit of this method is the identification of background, foreground as well as the unknown regions which can't be surely classified as either (this fits our case very closely).

The output of applying a naive watershed algorithm to the image:
 
 ![Naive Watershed result](output.png)
 
 The algorithm is okay with the optic disk (the sure foreground class) and background (the sure background) classes but fails to recognise the fainter atrophy class distinctly (which it should have recognised as an unknown region) and instead includes it in the sure-background class.
 
 Next, I went on to see the contours plotted by the above naive watershed algorithm ([finding_Contours.py](https://github.com/Saurav0074/Advenio/blob/master/finding_Contours.py)) in order to find the regions which were being considered distinct by the algorithm. 
 
 ![Contours plotted by the naive watershed algorithm](finding_Contours.png)
 
 The output observed clarifies the above point as no single contour falls solely within the Atrophy Class region. This indicates that the algorithm somehow can't classify the Atrophy class's pixel intensities, i.e. it treats them similar to the values of the neighboring background class. This led me to my final approach.

### Final approach : Watershed along with color-space conversion 
[colorSpace_with_watershed.py](https://github.com/Saurav0074/Advenio/blob/master/colorSpace_with_watershed.py)

Now, the foremost task is to detect the Atrophy class region. For this purpose, a color-space conversion of the orginial image from RGB to L*a*b* is applied, which shows the Atrophy region being clearly recognised by varying the values of the a-channel. Following is the output with the color range set as `[10, 10, 0] - [185, 146, 255]` (in order to discard the rest of the color regions of the image by bitwise-AND; the range is obtained by manual tweaking of the values):

![Atrophy region](atrophy.png)

The last thing I need now is the optic disc class separated from the rest of the image. For this, a color-space conversion from RGB to HLS is made with the color range `[0, 115, 0] - [255, 255, 255]` follwed by a bitwise_AND, giving the following output:

![Optic region](optic.png)

The next step is to mask the above obtained results with the original image to achieve the overall effect. But before that, one more thing to notice in the image is the reddish colored cross-shaped mark extending through the height of the image. In order to extract the mark, I used a RGB to HSV color conversion with the value range `[0,0,0]- [12, 240, 255]`:

![Crossed mark](cross_mark.png)

To remove the effect of the crossing on the final output, I performed a bitwise-XOR of the above image with that of the original one.
Finally, masking above three results with the original image gives the output:

![Final Masked Image](masking_result.png)
 


This image can now be passed as input to the watershed algorithm producing the result shown below:
 
 ![Final Output](final_output.png)
 
 ### Observation
 
 The final output shows much better results than that of the Naive approach but still has some cons:
 - Some regions of the Atrophy class have been misclassified for the Optic Disk Class.
 - The entire Atrophy class region has been classified into four distinct regions, however, the desired output should have only one.
 - Few gaps between the Optic Disk and Atrophy region still have been misclassified as the Background region.

 
