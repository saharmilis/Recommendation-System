test_user=500

# Take the top-10 simular users
for d in sorted_distances[test_user][::-1][0:10]:
    print(d)