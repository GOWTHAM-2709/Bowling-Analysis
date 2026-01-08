import cv2
import mediapipe as mp
import math
import json
import sys
import time

input_path = sys.argv[1]
output_path = input_path.replace(".mp4", "_skeleton.mp4")

mp_pose = mp.solutions.pose
pose = mp_pose.Pose()
draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(input_path)
w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

out = cv2.VideoWriter(
    output_path,
    cv2.VideoWriter_fourcc(*"mp4v"),
    fps,
    (w, h)
)

prev_x = None
prev_t = None
speed = 0

lean_angle = 0
weight_transfer = "Unknown"
head_position = "Unknown"
shoulder_status = "Unknown"

def angle(a, b, c):
    ab = (a[0]-b[0], a[1]-b[1])
    cb = (c[0]-b[0], c[1]-b[1])
    dot = ab[0]*cb[0] + ab[1]*cb[1]
    mag = math.hypot(*ab) * math.hypot(*cb)
    return 0 if mag == 0 else abs(math.degrees(math.acos(dot/mag)))

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    res = pose.process(rgb)

    if res.pose_landmarks:
        lm = res.pose_landmarks.landmark
        draw.draw_landmarks(frame, res.pose_landmarks, mp_pose.POSE_CONNECTIONS)

        l_sh = (int(lm[11].x*w), int(lm[11].y*h))
        r_sh = (int(lm[12].x*w), int(lm[12].y*h))
        hip = (int(lm[24].x*w), int(lm[24].y*h))

        lean_angle = angle(l_sh, hip, r_sh)

        center_x = hip[0]
        now = time.time()
        if prev_x is not None:
            dx = center_x - prev_x
            dt = now - prev_t
            if dt > 0:
                speed = abs(dx/dt) * 3.6

        prev_x = center_x
        prev_t = now

        weight_transfer = "Good Transfer" if speed > 15 else "Poor Transfer"
        head_position = "Head Lean Right" if lm[0].x > lm[11].x else "Head Lean Left"
        shoulder_status = "Open Shoulder"

        cv2.putText(frame, f"Lean Angle: {lean_angle:.1f}",
                    (30,40), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,255,0),2)
        cv2.putText(frame, f"Speed: {speed:.1f} km/h",
                    (30,70), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,255,255),2)
        cv2.putText(frame, f"Weight: {weight_transfer}",
                    (30,100), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255,255,0),2)

    out.write(frame)

cap.release()
out.release()

# 🔥 ONLY JSON — NO LOGS
print(json.dumps({
    "video": output_path.replace("\\", "/"),
    "leanAngle": round(lean_angle, 2),
    "shoulder": shoulder_status,
    "head": head_position,
    "weightTransfer": weight_transfer,
    "speed": round(speed, 2)
}))
