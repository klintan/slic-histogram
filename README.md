slic-histogram
==============

Constructs a color (RGB) histogram for each SLIC superpixel region in an image.


arguments:
- "im" the complete image (as a numpy array)
- "superpixels" SLIC extracted superpixel regions, same size as the image (all though 2D) and each pixel index value is the same for each region it belongs to (all 0 is region 0, all 1 is region 1 and so forth)
- "index", the super pixel region index, to be able to loop through all the regions in an image.
         
outputs:
- "histogram", the RGB histogram of the superpixel region



Small addition: It would be easy to replace the np.bincount() with np.histogram(x,bins=8) to get a less sparse histogram and also to perhaps get a better result.
