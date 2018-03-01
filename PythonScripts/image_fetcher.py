import requests

# First we need to read in the image_links.txt file
filename = "image_links.txt"
with open(filename) as f:
    content = f.readlines()

content = [x.strip() for x in content]

# Now that we have an list of the links we need to 
# fetch each image at each link 
# and then save the returned image to a file

# This is where we will write the names of all of the image files
# If no image was found at the link, we can indicate that here.
directory = "image_index.txt"
file = open(directory, 'a')

# This will be the iterator that we will use for the filenames
d = 0
extension = "jpg"

# For each image link
for line in content:
	# Get the image data 
	img_data = requests.get(line).content

	# Create the filename 
	fn = "images/file_%d.jpg"%d
	d+=1

	# If an actual image was returned...
	if len(img_data) > 1000:
		# Save this image at the filename specified
		with open(fn, 'wb') as handler:
			handler.write(img_data)
		# Make an entry in our directory
		file.write(fn)
		file.write('\n')
	else:
		# If we didn't successfully get an image
		# then make a note in our directory
		file.write('/// No Picture ///')

file.close()



	

