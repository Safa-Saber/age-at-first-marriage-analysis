# Final Reflection: Age at First Marriage in Asia Research Project

**Researcher:** Safa Saber  
**Program:** MIT Emerging Talent Program  
**Project Period:** November 29 - December 6, 2024

---

## Were the Original Project Objectives Achieved?

Yes, I successfully achieved all the original project objectives, though the journey was significantly compressed compared to the intended timeline. I set out to explore marriage age patterns across Asia and compare them with global trends, and I accomplished this through a complete data science workflow: problem identification, data collection via web scraping, statistical analysis, and communication of findings through visual artifacts.

My research question - "How does age at first marriage in Asia compare to global patterns, and what do gender differences reveal about regional diversity?" - was fully answered. I analyzed 192 countries across 5 continents, with particular focus on Asia's 48 countries. The findings revealed Asia's remarkable diversity, from Nepal and Laos at 21.9 years to South Korea at 38 years, and positioned Asia as ranking 3rd globally with an average of 27.20 years. The gender gap analysis showed Asia's moderate 3.01-year difference, situated between Europe's minimal gap and Africa's larger gap.

However, I must acknowledge a significant constraint: I completed this entire project in just 9 days when it was designed for a 2-month timeline. This time pressure meant I had to prioritize breadth over depth in some areas, particularly in the domain study where I could have explored more academic literature, and in the analysis where I focused on descriptive statistics rather than attempting more complex inferential or predictive modeling.

## Most Valuable Learning

The most valuable learning from this project was understanding the complete data science workflow from end to end. Before this project, I had worked on individual components - cleaning data here, creating visualizations there - but never orchestrated an entire research project independently. I learned that data science is not just about running statistical tests or creating pretty charts; it's about asking meaningful questions, making methodological decisions, managing data quality issues, and communicating findings to diverse audiences.

Specifically, web scraping taught me about the messiness of real-world data. The Wikipedia tables seemed straightforward initially, but country names had parenthetical notes, data types were inconsistent, and missing values required careful handling. I learned to write defensive code that anticipates these problems rather than assuming clean inputs.

The communication phase was particularly enlightening. Creating the visual infographic forced me to distill complex statistical findings into accessible insights. I had to ask myself: "What would policymakers care about? What would educators find useful? What would interest the general public?" This audience-centered thinking transformed how I approach data communication - it's not about showcasing all the analysis I did, but about highlighting what matters most to different stakeholders.

## Individual Project Reflection: Task Delegation

If I were to approach this project as a team in the future, I would carefully delegate tasks based on both efficiency and learning opportunities. I would take ownership of the problem identification and research question development, as well as the final integration and communication strategy. These bookend phases require a unified vision and consistent voice that benefits from single-person ownership.

However, I would delegate the data collection and cleaning to a team member with strong programming skills and attention to detail. Web scraping and data preparation consumed a disproportionate amount of time in my compressed timeline, and having someone dedicated to ensuring data quality would have freed me to focus on deeper analysis. I would also delegate the creation of individual visualizations to someone with design skills, while I would maintain ownership of the overall narrative and how visualizations support the research questions.

The statistical analysis phase would benefit from collaboration - having multiple people examining the same data often reveals patterns or questions that a solo researcher might miss. I would structure this as a collaborative analysis phase where team members work independently on different aspects (one on continental comparisons, another on gender gaps, another on temporal patterns) and then come together to synthesize findings.

## Navigating Project Management

Project management was both my greatest challenge and most important skill development area. Working alone meant I was simultaneously the researcher, developer, analyst, designer, and project manager. I learned to break the work into clear milestones aligned with the course requirements, which provided structure and prevented scope creep.

I created a simple tracking system using the GitHub project board with three columns: To Do, In Progress, and Done. Each milestone had specific deliverables, and I forced myself to mark tasks as complete before moving forward. This prevented the common trap of endless refinement - I had to accept "good enough" given the time constraints rather than pursuing perfection.

The biggest project management lesson was about time estimation. I significantly underestimated how long data cleaning would take (it consumed almost 40% of my total project time) and overestimated how long analysis would take once I had clean data. In future projects, I'll build in more buffer time for data preparation and validation, recognizing that this is typically the most time-consuming and unpredictable phase.

I also learned the value of documentation as I progressed rather than retrospectively. I created the domain study README while conducting background research, documented data collection decisions while writing the scraping code, and drafted the non-technical summary alongside the statistical analysis. This "document as you go" approach saved significant time at the end and ensured I captured rationale and decisions while they were fresh.

## Choosing the Public-Facing Artifact

I chose a one-page visual HTML infographic as my primary communication artifact for several strategic reasons. First, it addresses the multi-audience challenge - policymakers need quick insights, researchers want methodology details, educators seek accessible explanations, and the general public wants visual clarity. A single-page format forces prioritization of the most important findings while the HTML format allows for easy printing to PDF or viewing in any browser without special software.

The infographic format was ideal for this project because marriage age patterns are inherently comparative - Asia versus other continents, men versus women, developed versus developing nations. Visual comparisons through bar charts, scatter plots, and color-coded displays make these relationships immediately apparent in ways that text-heavy reports cannot achieve.

I considered alternatives like a traditional research paper or an interactive dashboard. However, a research paper would have limited reach beyond academic audiences and wouldn't serve policymakers or educators effectively. An interactive dashboard would require hosting infrastructure and technical skills from users, creating barriers to access. The HTML infographic strikes the balance: professional enough for academic contexts, accessible enough for general audiences, and portable enough for easy sharing.

The three embedded visualizations (global country comparison, gender differences by continent, and data collection timeline) were chosen specifically to answer the core research questions visually. Each chart tells a distinct part of the story - global context, gender patterns, and data quality considerations - creating a complete narrative.

## Most Useful Elements of Emerging Talent Program

Several program elements proved invaluable. The structured milestone framework provided scaffolding that prevented me from feeling overwhelmed by the project's scope. Breaking the work into problem identification, data collection, analysis, communication, and presentation made the timeline manageable even when compressed.

The emphasis on open-source practices and repository organization was initially frustrating - why spend time on README files when I could be analyzing data? - but ultimately essential. The structured folder system (domain_study, data_collection, exploration, analysis, communication) made it easy to find files later and will make the project reproducible for others. The requirement to document methodology and create non-technical summaries forced me to think about accessibility and transparency.

The focus on communication for diverse audiences was perhaps the most transformative element. Many data science courses emphasize technical skills but neglect communication. This program's requirement to create both technical documentation and accessible artifacts pushed me beyond my comfort zone. I learned that being able to explain findings clearly is just as important as conducting the analysis correctly.

The GitHub workflow and version control requirements initially seemed like overhead but became essential as the project progressed. Being able to track changes, document decisions through commit messages, and organize work through branches and project boards provided structure that would have been chaos otherwise.

## Additional Reflections and Limitations

The most significant limitation of this project was the extreme time constraint - completing a 2-month project in 9 days. This compressed timeline had several consequences. First, I couldn't conduct as thorough a literature review as I would have liked. A more comprehensive domain study would have revealed additional research questions and potentially different analytical approaches. Second, I focused exclusively on descriptive statistics rather than exploring inferential methods or predictive modeling. With more time, I could have tested hypotheses about what factors predict marriage age differences or built models to identify which countries are outliers and why.

The data quality challenges were significant. Countries collected marriage age data in different years (1991-2023), which makes direct comparisons problematic since marriage patterns change over time. I documented this limitation clearly but couldn't resolve it - ideally, I would want all data from the same time period. Additionally, definitions of "marriage age" might vary across countries (legal marriage versus traditional ceremonies, median versus mean ages), but the Wikipedia source didn't always clarify these distinctions.

Working alone on what was designed as a collaborative project taught me that I strongly prefer working in a team. While I had complete autonomy over decisions and didn't need to coordinate schedules, I deeply missed the benefits of collaboration. Someone with a different cultural background might have noticed patterns I overlooked, someone with stronger statistical skills might have suggested better analytical approaches, and someone with design experience might have created more compelling visualizations. The isolation of solo work also meant I had no one to discuss ideas with, bounce questions off, or celebrate milestones with. In future projects, I would actively seek out collaborative opportunities because the synergy and diverse perspectives of teamwork produce stronger outcomes than individual effort alone.

Despite these limitations, I'm proud of what I accomplished. This project demonstrated that I can manage a complete data science workflow independently, from identifying a meaningful research question through communicating findings to diverse audiences. The findings themselves are substantive - revealing Asia's remarkable diversity in marriage patterns and positioning these patterns in global context - and could inform policy discussions about education, gender equality, and social development.

Looking forward, I would approach similar projects with more realistic time estimation, particularly for data cleaning and preparation. I would also build in checkpoints for feedback from others, even in solo projects, because external perspectives improve quality. Most importantly, I learned that constraints - even extreme ones like my 9-day timeline - force prioritization and decision-making that can lead to tighter, more focused work. The project would have been different with more time, but not necessarily better in all ways.

---

**Word Count:** 987 words