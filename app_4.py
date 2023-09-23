segment1_start = int(input())
segment1_end = int(input())

segment2_start = int(input())
segment2_end = int(input())

if segment1_start > segment1_end:
    segment1_start, segment1_end = segment1_end, segment1_start
if segment2_start > segment2_end:
    segment2_start, segment2_end = segment2_end, segment2_start

if segment1_end < segment2_start or segment2_end < segment1_start:
    print("Отрезки не пересекаются")
else:
    intersection_start = max(segment1_start, segment2_start)
    intersection_end = min(segment1_end, segment2_end)
    dist = max(intersection_start, intersection_end) - min(intersection_start, intersection_end)
    if dist == 0:
        print("Отрезки пересекаются в точке", intersection_start)
    else:
        print("Длина пересечения отрезков",dist)