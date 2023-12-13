# read in data
import pandas as pd
import pydicom
import os
import matplotlib.pyplot as plt
import cv2
import numpy as np
from PIL import Image, ImageDraw
    
from collections import defaultdict

def realToPix(ds, real):
    F11, F21, F31 = ds.ImageOrientationPatient[3:]
    F12, F22, F32 = ds.ImageOrientationPatient[:3]

    dr, dc = ds.PixelSpacing
    Sx, Sy, Sz = ds.ImagePositionPatient
    
    img_aff = np.array(
        [
            [F11 * dr, F12 * dc, 0, Sx],
            [F21 * dr, F22 * dc, 0, Sy],
            [F31 * dr, F32 * dc, 0, Sz],
            [0, 0, 0, 1]
        ]
    )
    
    xyz = real[:-1]
    
    M = img_aff[:3, :3]
    b = img_aff[:3, 3]
    xyz = np.array(xyz)
    xyz = np.array(xyz)-b
    
    matr_inv = np.linalg.pinv(M).dot(xyz)
    
    return matr_inv

def poly_to_mask(polygon, width, height):    
    img = Image.new(mode='L', size=(width, height), color=0)
    ImageDraw.Draw(img).polygon(xy=polygon, outline=0, fill=1)
    mask = np.array(img).astype(bool)
    return mask

def make_sslice_mask(contour_data, img_UID, path_test_case, show_figure=False):
    
    xs = []
    ys = []
    zs = []
    
    ds = pydicom.dcmread(os.path.join(path_test_case, f'CT{img_UID}.dcm'))

    for i in range(0, len(contour_data), 3):
        list_real = contour_data[i:i+3]
        list_real.append(1)
        xyz = realToPix(ds, list_real)
        xs.append(xyz[0])
        ys.append(xyz[1])
        zs.append(list_real[2])
        
    xys = [(xs[i], ys[i]) for i in range(len(xs))]
    mask = poly_to_mask(xys, 512, 512)
    
    if show_figure:
        plt.figure()
        plt.title(img_UID)
        plt.imshow(mask)
        plt.show()
    
    return mask, zs[0]

def get_3D_img_mask_for_one_case(paths_train_case):
    path_train = 'Training/'#'Test/'
    # for test, need to change path
    path_test_case = os.path.join(path_train, paths_train_case)
    path_imgs = []
    for p_temp in list(os.listdir(path_test_case)):
        if not p_temp.lower().endswith('.dcm'):
            continue
        if p_temp.lower().startswith('ct'):
            path_imgs.append(p_temp)
        elif 'str.dcm' in p_temp.lower():
            str_dcm = p_temp
    
    path_imgs = [os.path.join(path_test_case, p) for p in path_imgs]
    path_contour = os.path.join(path_test_case, str_dcm)
    
    ds_contour = pydicom.dcmread(path_contour)
    ## segmentation_types is the segmentation color
    segmentation_types = []
    # segmentation_realspace_ds
    segmentation_realspace_ds = []
    for ds_segmentation in list(ds_contour[0x30060039]):
        segmentation_types.append(ds_segmentation[0x3006002a].value)
        segmentation_realspace_ds.append(list(ds_segmentation[0x30060040]))
        
    ## gather all masks and corresponding zs
    volumes = []
    masks_all = []
    zs_all = []
    ## iterate through different colors
    for segmentation_realspace_contours in segmentation_realspace_ds:
        ## segmentation_realspace_contours is the list of multiple slices for one color instance
        segmentation_realspace_contours = list(segmentation_realspace_contours)
        ## iterate through all the slices for one color segmentation
        masks = []
        zs = [] # in descending order
        for segmentation_realspace_contour in segmentation_realspace_contours:
            contour_data = segmentation_realspace_contour[0x30060050].value
            img_UID = list(segmentation_realspace_contour[0x30060016])[0][0x00081155].value
            mask, z = make_sslice_mask(contour_data, img_UID, path_test_case, show_figure=False)
            masks.append(mask)
            zs.append(z)
        volumes.append(np.sum(masks)) # multiply by slice thickness 
        masks_all += masks
        zs_all += zs
        
    ## gather all images and corresponding zs
    imgs_all = []
    zs_imgs_all = []
    for p in path_imgs:
        ds = pydicom.dcmread(p)
        if ds.Modality != 'CT':
            continue
        z_pos = float(ds.ImagePositionPatient[2])
        pix = ds.pixel_array
        imgs_all.append(pix)
        zs_imgs_all.append(z_pos)
    dz = ds.SliceThickness
    dr, dc = ds.PixelSpacing
    mm_3 = dz*dr*dc
    
    # 3D mask -- stack masks and imgs based on z value order
    mask_3D = np.zeros((imgs_all[0].shape[0], imgs_all[0].shape[1], len(imgs_all)))
    ## sort imgs using z order
    order = np.argsort(zs_imgs_all)
    imgs_all = np.array(imgs_all)[order]
    zs_imgs_all.sort()
    zs_all = [round(z, 3) for z in zs_all]
    zs_imgs_all = [round(z, 3) for z in zs_imgs_all]
    for i, z in enumerate(zs_all):
        indx = zs_imgs_all.index(z)
        mask_3D[:,:,indx] = masks_all[i]
    imgs_all = np.transpose(imgs_all, (1, 2, 0))
    
    return imgs_all, mask_3D, volumes, mm_3