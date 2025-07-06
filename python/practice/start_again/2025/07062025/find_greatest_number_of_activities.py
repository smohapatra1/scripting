#   Given are the 10 activities with their start and end times. Compute a schedule where the greatest number of activities take place. 
#   https://www.google.com/search?q=Given+are+the+10+activities+with+their+start+and+end+times.+Compute+a+schedule+where+the+greatest+number+of+activities+take+place.+using+python%C2%A0&client=safari&sca_esv=ccb8066356fd07b7&rls=en&sxsrf=AE3TifNxNflLsIVF2YdFyK1FNgrmbgPdNw%3A1751840752818&udm=50&fbs=AIIjpHxU7SXXniUZfeShr2fp4giZ1Y6MJ25_tmWITc7uy4KIemkjk18Cn72Gp24fGkjjh6xc8y8oU3IJovU34XDyOFvEl9PQhCX-bXyx8AzQGU_JUmd7tO0Sp0t0qHqXwx4ZXWb8MG9UW3YmmJ7jnOpDFf7zDe6R0ySzsMzPcR5ELTvwcb0SbmEtrZ6i8BL_Ll7e2CjCTkfGrqQV0WeCBxGgvYCvX7WS9g&aep=1&ntc=1&sa=X&ved=2ahUKEwjSkJmuo6mOAxVDlu4BHRRqCWMQ2J8OegQIFhAC&biw=1729&bih=876&dpr=2&mstk=AUtExfDfAjMlL1Lm3w76lqUd1USql6MkuVP_AvsUTYda8ThnouvB91E_s2GzIBZzOToiwWWpjfbHJeyk3xWaRGX-2aOvwTGlvpD_8lm4LcE_5K53WG_0vpGx1ranFFs5vB2hvtygDjzCZ7D56TrmJmCzg0TqN5NP-_5S9pQ8SenB2toJ6NGTyYT__iJVfK9AvF3BZwf62N5GCZtxXmyJkn4ng7AdsWbHlq1cLguy6vASwC1AkslHrpHh8Rb7CYfXFZvyluN2ZK28g_JACSMVBvPC8eDPthDG-jNWwwt9mfzmSFgzZjM4Cj7nnhB93tpppjKqJFc-9ZZuWU3rtQ&csuir=1

def scheduled_Activities(activities):
    sorted_activities = sorted(activities, key=lambda x:x[1])
    selected_activities = [sorted_activities[0]]
    last_finish_time = sorted_activities[0][1]
    for activity in selected_activities[1:]:
        if activity[0] >= last_finish_time:
            selected_activities.append(activity)
            last_finish_time = activity[1]
    return selected_activities

activities = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 8), (5, 9), (6, 10), (8, 11), (8, 12), (2, 13), (12, 14)]
schedule = scheduled_Activities(activities)
print ("Maximum number of activities in the schedule : ", len(schedule))
print ("Selected activities :", schedule)
