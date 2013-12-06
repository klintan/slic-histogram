def get_color_histogram(image,superpixels,index):
	indices = np.where(grid.ravel() == index)[0]
	r = np.bincount(im[:,:,0].ravel()[indices],minlength=256)
	g = np.bincount(im[:,:,1].ravel()[indices],minlength=256)
	b = np.bincount(im[:,:,2].ravel()[indices],minlength=256)
	
	histogram = (rhist0+bhist0+ghist0)/3
	return histogram
