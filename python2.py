import math

# Noktaları içeren liste
points =  [(3, 4), (6, 8)]
# Öklid mesafesini hesaplayan fonksiyon
def euclideanDistance(point1, point2):
    return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)

# Mesafeleri içeren liste
distances = []

# Her iki nokta  arasındaki mesafeyi hesapla
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

# Minimum mesafeyi bul
min_distance = min(distances)

print("Hesaplanan mesafeler:", distances)
print("Minimum mesafe:", min_distance)