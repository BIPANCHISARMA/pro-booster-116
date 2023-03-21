import cv2
img = cv2.imread("solar-system.jpg")

cv2.putText(
    img,
    "Sun",
    (100,80),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255,255,265)
)

cv2.putText(
    img,
    "Mercury",
    (120,185),
    cv2.FONT_HERSHEY_COMPLEX,
    0.3,
    (255,255,275)
)

cv2.putText(
    img,
    "Venus",
    (180,185),
    cv2.FONT_HERSHEY_COMPLEX,
    0.3,
    (255,255,265)
)
cv2.putText(
    img,
    "Earth",
    (260,185),
    cv2.FONT_HERSHEY_COMPLEX,
    0.3,
    (255,255,275)
)

cv2.putText(
    img,
    "Mars",
    (370,185),
    cv2.FONT_HERSHEY_COMPLEX,
    0.3,
    (255,255,265)
)

cv2.putText(
    img,
    "Jupiter",
    (490,50),
    cv2.FONT_HERSHEY_COMPLEX,
    0.4,
    (255,255,275)
)

cv2.putText(
    img,
    "Saturn",
    (790,140),
    cv2.FONT_HERSHEY_COMPLEX,
    0.4,
    (255,255,275)
)
cv2.putText(
    img,
    "Uranus",
    (990,140),
    cv2.FONT_HERSHEY_COMPLEX,
    0.4,
    (255,255,275)
)
cv2.putText(
    img,
    "Neptune",
    (1090,140),
    cv2.FONT_HERSHEY_COMPLEX,
    0.4,
    (255,255,275)
)



cv2.imshow("output",img)
cv2.waitKey(0)

cv2.imwrite("solar_systemwithname.jpg",img)