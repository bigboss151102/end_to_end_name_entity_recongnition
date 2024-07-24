import cv2
import predictions_v1 as pred

img = cv2.imread('E:/FILE of Trong/NLP Project/ner/datasets/54.jpg')

# cv2.namedWindow('Original', cv2.WINDOW_NORMAL)
# cv2.imshow('Original', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

img_result, entities = pred.getPredictions(img)
cv2.namedWindow('Result', cv2.WINDOW_NORMAL)
cv2.imshow('Result', img_result)
cv2.waitKey(0)
cv2.destroyAllWindows()
