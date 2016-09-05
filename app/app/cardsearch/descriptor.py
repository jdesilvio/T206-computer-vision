import numpy as np
import cv2
from imutils import resize


class CardDescriptor:
    """Extract the keypoints and descriptors from an image."""
    def __init__(self, kpMethod="SIFT", descMethod="SIFT"):
        self.kpMethod = kpMethod
        self.descMethod = descMethod

    def describe(self, image):
        # -- This is the OpenCV2 way to get SIFT kps and descs
        # -- Keeping for reference in case there are any issues
        # detector = cv2.FeatureDetector_create(self.kpMethod)
        # kps = detector.detect(image)
        # extractor = cv2.DescriptorExtractor_create(self.descMethod)
        # (kps, descs) = extractor.compute(image, kps)

        # Resize image to improve comparison speed when matching
        image = resize(image, height=300)

        # Extract features
        sift = cv2.xfeatures2d.SIFT_create()
        (kps, descs) = sift.detectAndCompute(image, None)

        kps = np.float32([kp.pt for kp in kps])

        return (kps, descs)
