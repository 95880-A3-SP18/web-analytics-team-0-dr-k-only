# UI Wireframe Review

Our web application serves as a one-stop portal for job seekers to analyse current job scenario. The web application
has 3 components.

1. User Sign in: The user is requested for a user name and password and registered with the web site.
		 User details will be stored in Sqlite3 database that commes with Django.




2. Insights: Various details about current jobs are scraped from two of the most popular job web sites - namely Glassdoor and indeed. 
	     This data is transformed to generate the following useful insights
	     1. Most popular companies that post maximum number of jobs.
	     2. Top jobs based on the number of current open positions.
	     3. Top Locations based on the locations that have maximum openings.
	     4. Job Site comparison that informs how many jobs have been posted in both the website and how many individually.
		This insight can even be used by the two companies to understand any jobs that they may not have captured.
    
    
    
    
	     
3. About us: This page explains about the team of 3 involved in developing this web application.
