import cv2
from tensorflow.keras.models import load_model
import numpy as np
from math import atan2, degrees

img_size = 224

def resize_img(im):
    old_size = im.shape[:2] # old_size is in (height, width) format
    ratio = float(img_size) / max(old_size)
    new_size = tuple([int(x*ratio) for x in old_size])
    # new_size should be in (width, height) format
    im = cv2.resize(im, (new_size[1], new_size[0]))
    delta_w = img_size - new_size[1]
    delta_h = img_size - new_size[0]
    top, bottom = delta_h // 2, delta_h - (delta_h // 2)
    left, right = delta_w // 2, delta_w - (delta_w // 2)
    new_im = cv2.copyMakeBorder(im, top, bottom, left, right, cv2.BORDER_CONSTANT,
      value=[0, 0, 0])
    return new_im, ratio, top, left

# overlay function
def overlay_transparent(background_img, img_to_overlay_t, x, y, overlay_size=None):
    bg_img = background_img.copy()
    # convert 3 channels to 4 channels
    if bg_img.shape[2] == 3:
        bg_img = cv2.cvtColor(bg_img, cv2.COLOR_BGR2BGRA)

    if overlay_size is not None:
        img_to_overlay_t = cv2.resize(img_to_overlay_t.copy(), overlay_size)

    b, g, r, a = cv2.split(img_to_overlay_t)

    mask = cv2.medianBlur(a, 5)

    h, w, _ = img_to_overlay_t.shape
    roi = bg_img[int(y-h/2):int(y+h/2), int(x-w/2):int(x+w/2)]

    img1_bg = cv2.bitwise_and(roi.copy(), roi.copy(), mask=cv2.bitwise_not(mask))
    img2_fg = cv2.bitwise_and(img_to_overlay_t, img_to_overlay_t, mask=mask)

    bg_img[int(y-h/2):int(y+h/2), int(x-w/2):int(x+w/2)] = cv2.add(img1_bg, img2_fg)

    # convert 4 channels to 4 channels
    bg_img = cv2.cvtColor(bg_img, cv2.COLOR_BGRA2BGR)

    return bg_img

def angle_between(p1, p2):
    xDiff = p2[0] - p1[0]
    yDiff = p2[1] - p1[1]
    return degrees(atan2(yDiff, xDiff))

def run(image_glasses, image_cat):

    """
    1. Load trained models.
    """
    bbs_model_name = "trained_models/model"
    lmks_model_name = "trained_models/lmks_model"
    bbs_model = load_model(bbs_model_name)
    lmks_model = load_model(lmks_model_name)

    """
    2. Process inference input to valid model format.
    """
    image_glasses = cv2.cvtColor(np.array(image_glasses), cv2.COLOR_RGBA2BGRA)
    image_cat = cv2.cvtColor(np.array(image_cat), cv2.COLOR_RGB2BGR)

    ori_img = image_cat.copy()
    result_img = image_cat.copy()

    # predict bounding box
    img, ratio, top, left = resize_img(image_cat)
    inputs = (img.astype('float32') / 255).reshape((1, img_size, img_size, 3))

    """
    3. Run model.
    """
    pred_bb = bbs_model.predict(inputs)[0].reshape((-1, 2))

    """
    2. Process inference input to valid model format.
    """
    # compute bounding box of original image
    ori_bb = ((pred_bb - np.array([left, top])) / ratio).astype(np.int)

    # compute lazy bounding box for detecting landmarks
    center = np.mean(ori_bb, axis=0)
    face_size = max(np.abs(ori_bb[1] - ori_bb[0]))
    new_bb = np.array([
    center - face_size * 0.6,
    center + face_size * 0.6
    ]).astype(np.int)
    new_bb = np.clip(new_bb, 0, 99999)

    # predict landmarks
    face_img = ori_img[new_bb[0][1]:new_bb[1][1], new_bb[0][0]:new_bb[1][0]]
    face_img, face_ratio, face_top, face_left = resize_img(face_img)

    face_inputs = (face_img.astype('float32') / 255).reshape((1, img_size, img_size, 3))

    """
    3. Run model.
    """
    pred_lmks = lmks_model.predict(face_inputs)[0].reshape((-1, 2))

    """
    4. Process and return inference results.
    """
    # compute landmark of original image
    new_lmks = ((pred_lmks - np.array([face_left, face_top])) / face_ratio).astype(np.int)
    ori_lmks = new_lmks + new_bb[0]

    # wearing glasses
    glasses_center = np.mean([ori_lmks[0], ori_lmks[1]], axis=0)
    glasses_size = np.linalg.norm(ori_lmks[0] - ori_lmks[1]) * 2

    angle = -angle_between(ori_lmks[0], ori_lmks[1])
    M = cv2.getRotationMatrix2D((image_glasses.shape[1] / 2, image_glasses.shape[0] / 2), angle, 1)
    rotated_glasses = cv2.warpAffine(image_glasses, M, (image_glasses.shape[1],image_glasses.shape[0]))

    try:
        result_img = overlay_transparent(result_img, rotated_glasses, glasses_center[0], glasses_center[1], overlay_size=(int(glasses_size), int(image_glasses.shape[0] * glasses_size / image_glasses.shape[1])))
    except:
        print('failed overlay image')

    result_img = cv2.cvtColor(result_img, cv2.COLOR_BGR2RGB)

    return result_img
