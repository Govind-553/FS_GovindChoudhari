function matchRoutes(student_location, student_destination, time_window, preferences):
    possible_matches = []
    
    all_students = getStudentsNearby(student_location, radius=10km)

    for other in all_students:
        if timeOverlap(student_location.time, other.time, time_window):
            route_similarity = compareRoutes(student_location, other.location, student_destination, other.destination)
            if route_similarity > THRESHOLD:
                if isPreferenceMatch(preferences, other.preferences):
                    possible_matches.append({
                        "username": generatePseudonym(other.id),
                        "route_similarity": route_similarity,
                        "eta_difference": calculateETA(student_location, other.location)
                    })
    
    sorted_matches = sortByRouteSimilarity(possible_matches)
    return sorted_matches[:MAX_RESULTS]
