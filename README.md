# job-ready-cv
resume generator that helps users quickly build job-ready CVs with structured layouts and downloadable PDF support.

Do you need a quick and easy resume builder to build a resume which you can actually use(shocking, right?) for applying to a tech job?
job-ready-cv is at rescue!!
You can drag to reorder form lists and resume sections from the side bar, live preview with side-by-side edit mode and preview & save your application-ready resume PDF with 2 clicks!
Disclaimer
The format of the rendered resume was heavily dependent on the template provided by Colin at Sheets & Giggles in one of the top posts on the r/jobs subreddit. 

🚀 Planned Features / To-Do
These are the features I wanted to implement but could not prioritize due to my self-imposed time constraints. I will be adding them gradually whenever time permits.

Add an Achievements section in the form.
Keep navigation buttons fixed in place (so buttons don’t shift when the opposite side becomes inactive).
Refine input placeholders for better clarity.
Show warnings when recommended fields are left blank.
Replace skill checkboxes with sliding toggle switches.
Fix issue where edit mode turns off after deleting a section.
Add animations for smoother interactions.
Welcome page unmounting
Live preview mounting
Add support for inserting new sections directly from the sidebar.
Show a section indicator during navigation.
Provide an option to add or change the accent color (lines and subheadings).
Improve overall responsiveness of the app across devices.
Enhance PDF rendering efficiency.
Add an option to center-align the resume header (name, title, links, etc.).

What I Learned

While working on this project, I gained experience in both React fundamentals and practical development workflows:
React Basics:
Setting up a React app with Create React App (CRA).
Explored alternatives like Vite and Next.js, but used CRA since it was recommended by The Odin Project for beginners — still a valid choice for learning.
Component Architecture:
Worked with class components and lifecycle methods.
Migrated to function components using Hooks such as useEffect.
Learned to manage inputs, render lists, and handle controlled components.
State Management:
Learned to manage local state effectively.
Used Zustand for global state management to simplify and scale state handling.
Libraries & Integrations:
react-pdf for generating resumes as downloadable PDFs.
dndkit for implementing drag-and-drop sortable lists.
Deployment:
Deployed the app using Cloudflare Pages, gaining hands-on experience with PaaS deployment workflows.
