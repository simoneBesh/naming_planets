import cv2

img = cv2.imread("solar-system.jpg")

txt1 = "Mercury"
cv2.putText(img, txt1, (110, 190), fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=1, color=(255,255,255))

txt2 = "Venus"
cv2.putText(img, txt2, (200, 170), fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=1, color=(255,255,255))

txt3 = "Earth"
cv2.putText(img, txt3, (290, 170), fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=1, color=(255,255,255))

txt4 = "Mars"
cv2.putText(img, txt4, (375, 170), fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=1, color=(255,255,255))

txt5 = "Jupiter"
cv2.putText(img, txt5, (560, 50), fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=1, color=(255,255,255))

txt6 = "Saturn"
cv2.putText(img, txt6, (750, 120), fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=1, color=(255,255,255))

txt7 = "Uranus"
cv2.putText(img, txt7, (960, 120), fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=1, color=(255,255,255))

txt8 = "Neptune"
cv2.putText(img, txt8, (1100, 120), fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=1, color=(255,255,255))

cv2.imwrite("planets_named.jpg", img)

cv2.imshow("solar system", img)
cv2.waitKey(0)
