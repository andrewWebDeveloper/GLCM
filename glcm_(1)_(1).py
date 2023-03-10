# -*- coding: utf-8 -*-
"""GLCM_(1)_(1).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1DX100WPdMRJeBdOZaefWGKxYqs2cwcD-
"""

import numpy as np
from skimage import io
from skimage.feature import greycomatrix, greycoprops
import matplotlib.pyplot as plt

import cv2
# Load the image
#image = io.imread('/content/N3.jpg')
# Load the image
file_paths = ["/content/Z1067.jpg", "/content/Z452.jpg", "/content/Z555.jpg","/content/Z979.jpg","/content/Z941.jpg"]
images = []
for file_path in file_paths:
    img = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
    images.append(img)




glcm_features = []
for img in images:
  img = img.astype('uint8')
# Convert the image to grayscale
gray_image = np.dot(img[...,:3], [0.250, 0.587, 0.114])
gray_image = gray_image.astype(np.uint8) # Place this line of code here

# Calculate the GLCM for the image
glcm_matrix = greycomatrix(img, [1, 2], [0, np.pi/4], 256, symmetric=True, normed=True)
glcm = greycomatrix(img, [1], [0, np.pi/4, np.pi/2, 3*np.pi/4], levels=256, symmetric=False, normed=True)

# Extract features from the GLCM
contrast = greycoprops(glcm, 'contrast')
correlation = greycoprops(glcm, 'correlation')
energy = greycoprops(glcm, 'energy')
homogeneity = greycoprops(glcm, 'homogeneity')

# Print the results
print("Contrast:", contrast)
print("Correlation:", correlation)
print("Energy:", energy)
print("Homogeneity:", homogeneity)
for angle in range(4):
    plt.matshow(glcm[:, :, 0, angle], cmap='gray')
    plt.colorbar()
    plt.title("Angle: {}".format(angle*90))
    plt.show()
plt.imshow(glcm[:, :, 0, 0], cmap='gray')
plt.show()





import cv2
import numpy as np
from skimage.feature import greycomatrix, greycoprops

# Load the image
file_paths = ["/content/Z1067.jpg", "/content/Z452.jpg", "/content/Z555.jpg","/content/Z941.jpg","/content/Z979.jpg"]
images = []
for file_path in file_paths:
    img = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
    images.append(img)

# Initialize an empty list to store GLCM features
glcm_features = []

# Loop through the images
for i, img in enumerate(images):
    # Convert the image to an unsigned 8-bit integer
    img = img.astype('uint8')

    # Create the GLCM matrix
    glcm_matrix = greycomatrix(img, [1, 2], [0, np.pi/4], 256, symmetric=True, normed=True)

    # Extract texture features from the GLCM matrix
    contrast = greycoprops(glcm_matrix, 'contrast')
    correlation = greycoprops(glcm_matrix, 'correlation')
    energy = greycoprops(glcm_matrix, 'energy')
    homogeneity = greycoprops(glcm_matrix, 'homogeneity')

    # Append the features to the list
    glcm_features.append([contrast, correlation, energy, homogeneity])

    # Print the values of the features for each image
    print("For image {}:".format(i+1))
    print("Contrast: ", contrast)
    print("Correlation: ", correlation)
    print("Energy: ", energy)
    print("Homogeneity: ", homogeneity)



from skimage.feature import greycomatrix, greycoprops

# ----------------- calculate greycomatrix() & greycoprops() for angle 0, 45, 90, 135 ----------------------------------
def calc_glcm_all_agls(img, label, props, dists=[5], agls=[0, np.pi/4, np.pi/2, 3*np.pi/4], lvl=256, sym=True, norm=True):
    
    glcm_matrix = greycomatrix(images, 
                        distances=dists, 
                        angles=agls, 
                        levels=lvl,
                        symmetric=sym, 
                        normed=norm)
    feature = []
    glcm_props = [propery for name in props for propery in greycoprops(glcm, name)[0]]
    for item in glcm_props:
            feature.append(item)
    feature.append(label) 
    
    return feature


# ----------------- call calc_glcm_all_agls() for all properties ----------------------------------
properties = ['dissimilarity', 'correlation', 'homogeneity', 'contrast', 'ASM', 'energy']

glcm_all_agls = []
for img, label in zip(img, "label"): 
    glcm_all_agls.append 
calc_glcm_all_agls(img, 
                                label, 
                                props=properties)
                            )
 
columns = []
angles = ['0', '45', '90','135']
for name in properties :
    for ang in angles:
        columns.append(name + "_" + ang)
        
columns.append("label")

import cv2
import numpy as np
from skimage.feature import greycomatrix, greycoprops

# Load the image
file_paths = ["/content/Z1067.jpg", "/content/Z452.jpg", "/content/Z555.jpg","/content/Z941.jpg","/content/Z979.jpg"]
images = []
for file_path in file_paths:
    img = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
    images.append(img)

# Initialize an empty list to store GLCM features
glcm_features = []

# Loop through the images
for i, img in enumerate(images):
    # Convert the image to an unsigned 8-bit integer
    img = img.astype('uint8')

    # Create the GLCM matrix
    glcm_matrix = greycomatrix(img, [1, 2], [0, np.pi/4], 256, symmetric=True, normed=True)

    # Extract texture features from the GLCM matrix
    contrast = greycoprops(glcm_matrix, 'contrast')
    correlation = greycoprops(glcm_matrix, 'correlation')
    energy = greycoprops(glcm_matrix, 'energy')
    homogeneity = greycoprops(glcm_matrix, 'homogeneity')

    # Append the features to the list
    glcm_features.append([contrast, correlation, energy, homogeneity])

    # Print the values of the features for each image
    print("For image {}:".format(i+1))
    print("Contrast: ", contrast)
    print("Correlation: ", correlation)
    print("Energy: ", energy)
    print("Homogeneity: ", homogeneity)


from skimage.feature import greycomatrix, greycoprops

# ----------------- calculate greycomatrix() & greycoprops() for angle 0, 45, 90, 135 ----------------------------------
def calc_glcm_all_agls(img, label, props, dists=[5], agls=[0, np.pi/4, np.pi/2, 3*np.pi/4], lvl=256, sym=True, norm=True):
    
    glcm_matrix = greycomatrix(img, 
                        distances=dists, 
                        angles=agls, 
                        levels=lvl,
                        symmetric=sym, 
                        normed=norm)
    feature = []
    glcm_props = [propery for name in props for propery in greycoprops(glcm_matrix, name)[0]]
    for item in glcm_props:
            feature.append(item)
    feature.append(label) 
    
    return feature


# ----------------- call calc_glcm_all_agls() for all properties ----------------------------------
properties = ['dissimilarity', 'correlation', 'homogeneity', 'contrast', 'ASM', 'energy']

glcm_all_agls = []
for img, label in zip(images, ["label"]*len(images)): 
    glcm_all_agls



    import pandas as pd
    import numpy as np
 

# Create the pandas DataFrame for GLCM features data
# Create the pandas DataFrame for GLCM features data
glcm_all_agls = []
for img, label in zip(images, ["label"]*len(images)): 
    glcm_all_agls.append(calc_glcm_all_agls(img, label, properties))
columns = ["dissimilarity_0", "correlation_0", "homogeneity_0", "contrast_0", "ASM_0", "energy_0","dissimilarity_45", "correlation_45", "homogeneity_45", "contrast_45", "ASM_45", "energy_45",            "dissimilarity_90", "correlation_90", "homogeneity_90", "contrast_90", "ASM_90", "energy_90",            "dissimilarity_135", "correlation_135", "homogeneity_135", "contrast_135", "ASM_135", "energy_135", "label"]

glcm_df = pd.DataFrame(glcm_all_agls, 
                      columns = columns)

glcm_df.head(15)