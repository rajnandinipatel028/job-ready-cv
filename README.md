# job-ready-cv
resume generator that helps users quickly build job-ready CVs with structured layouts and downloadable PDF support.

Do you need a quick and easy resume builder to build a resume which you can actually use(shocking, right?) for applying to a tech job?
job-ready-cv is at rescue!!
You can drag to reorder form lists and resume sections from the side bar, live preview with side-by-side edit mode and preview & save your application-ready resume PDF with 2 clicks!
Disclaimer
The format of the rendered resume was heavily dependent on the template provided by Colin at Sheets & Giggles in one of the top posts on the r/jobs subreddit. 

## 🚀 Planned Features  

These are the features I wanted to implement but did not prioritize due to time constraints. I plan to add them gradually in future updates:  

- Add an **Achievements** section in the form.  
- Keep **navigation buttons fixed in place** so they don’t shift when one side becomes inactive.  
- Refine **input placeholders** for better clarity.  
- Show **warnings** when recommended fields are left blank.  
- Replace **skill checkboxes** with sliding toggle switches.  
- Fix issue where **edit mode** turns off after deleting a section.  
- Add smooth **animations**, including:  
  - Welcome page unmounting  
  - Live preview mounting  
- Allow adding new sections directly from the **sidebar**.  
- Show a **section indicator** during navigation.  
- Provide an option to **customize accent color** (lines and subheadings).  
- Improve overall **responsiveness** across devices.  
- Enhance **PDF rendering efficiency**.  
- Add an option to **center-align the resume header** (name, title, links, etc.).  

## 📚 What I Learned  

While working on this project, I learned:  

- **React Fundamentals**  
  - Creating a React app with **Create React App (CRA)**.  
  - Explored better alternatives like **Vite** and **Next.js**, but stuck with CRA since *The Odin Project* recommended it.  
  - Still a fine choice for learning purposes.  

- **Component Architecture**  
  - Worked with **class components** and lifecycle methods.  
  - Migrated to **function components** with hooks (e.g., `useEffect`).  
  - Learned to manage controlled inputs and render lists effectively.  

- **State Management**  
  - Gained experience in managing local state.  
  - Used **Zustand** for global state management.  

- **Libraries & Integrations**  
  - **react-pdf** → for PDF resume generation.  
  - **dndkit** → for drag-and-drop sortable lists.  

- **Deployment**  
  - Deployed the app on **Cloudflare Pages** using PaaS workflows.  

dndkit for implementing drag-and-drop sortable lists.
Deployment:
Deployed the app using Cloudflare Pages, gaining hands-on experience with PaaS deployment workflows.
