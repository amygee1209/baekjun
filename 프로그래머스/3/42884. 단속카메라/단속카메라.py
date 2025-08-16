def solution(routes):
    routes.sort(key=lambda x: x[1])
    print(routes)
    cameraCount = 1
    lastCameraAt = routes[0][1]
    for r in routes:
        if r[0] <= lastCameraAt <= r[1]:
            continue
        lastCameraAt = r[1]
        cameraCount += 1
    return cameraCount