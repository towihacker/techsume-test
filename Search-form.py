import requests

# Check if the title input is set
if 'title' in request.POST:
    # Store the job title in a variable
    title = request.POST['title']

    # Build the API request URL
    url = f"https://api.adzuna.com/v1/api/jobs/gb/search/1?app_id=YourAppIDHere&app_key=YourAppKeyHere&what={title}"

    # Use requests to retrieve the API response
    response = requests.get(url)

    # Check if the response is successful (status code 200)
    if response.status_code == 200:
        data = response.json()

        # Check if the response is not empty
        if data:
            print("<div class='box'>")
            print("<table class='table is-striped is-narrow is-hoverable is-fullwidth'>")
            print("<thead>")
            print("<tr>")
            print("<th>Job Title</th>")
            print("<th>Company Name</th>")
            print("<th>$$$ Salary</th>")
            print("<th>Action</th>")
            print("</tr>")
            print("</thead>")
            print("<tbody>")

            # Loop through the jobs in the response
            for job in data['results']:
                print("<tr>")

                # Print the job title, company name, and salary
                print(f"<td>{job['title']}</td>")
                print(f"<td>{job['company']['display_name']}</td>")
                print(f"<td>${job['salary_min']} - ${job['salary_max']}</td>")

                # Add the apply button
                print(f"<td><a class='button is-primary' href='{job['redirect_url']}'>Apply</a></td>")

                print("</tr>")
            print("</tbody>")
            print("</table>")
            print("</div>")
        else:
            # Print an error message
            print(f"<p class='title is-4'>Sorry, no results were found for the job title '{title}'. Please try a different title.</p>")
    else:
        # Print an error message for unsuccessful API request
        print(f"<p class='title is-4'>Error: Unable to retrieve data from the API. Please try again later.</p>")
else:
    # Print an error message if title is not set
    print("<p class='title is-4'>Error: Job title not provided.</p>")
