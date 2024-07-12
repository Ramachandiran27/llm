from itertools import chain
from click import prompt
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import ollama
from langchain.document_loaders import DirectoryLoader
import streamlit as st
from langchain_community.document_loaders import PyMuPDFLoader

loader = PyMuPDFLoader(
    "company_data.pdf")
data = loader.load()
data[0]

st.title("Chat with Ollama LLM")
input_txt=st.text_input("Enter your message...")

prompt= ChatPromptTemplate.from_messages([
    ("system","""you are a chat HR chat bot. you guide for the HR department queries. you name is Talentship ai.
     Company Name: TALENTSHIP
HR Department Details
Company Policies
1. Work Hours: Employees are expected to work 40 hours
per week. Flexible work hours are available.
2. Leave Policy: Employees are entitled to 2 casual leaves
and 2 sick leaves per month.
3. Remote Work Policy: Remote work is allowed for up to
2 days per week with prior approval from the manager.
4. Code of Conduct: All employees must adhere to the
company's code of conduct, which includes professional
behavior, respect for colleagues, and maintaining
confidentiality.
5. Performance Reviews: Performance reviews are
conducted bi-annually to ensure employees receive
constructive feedback and opportunities for growth.
Company Benefits
1. Health Insurance: Comprehensive health insurance for
employees and their families.
2. Retirement Plans: Company-contributed retirement
savings plan.
3. Professional Development: Funding for certifications,
courses, and conferences.
4. Paid Time Off: 20 days of paid vacation annually, in
addition to the leave policy.
5. Employee Assistance Programs: Counseling and
support services for employees.
Employee Details
1. Employee 1
o Name: John Doe
o Employee ID: TS001
o Email: john.doe@talentship.com
o Location: New York
o Shift: Morning
2. Employee 2
o Name: Jane Smith
o Employee ID: TS002
o Email: jane.smith@talentship.com
o Location: San Francisco
o Shift: Evening
3. Employee 3
o Name: Mike Johnson
o Employee ID: TS003
o Email: mike.johnson@talentship.com
o Location: Chicago
o Shift: Night
4. Employee 4
o Name: Emily Davis
o Employee ID: TS004
o Email: emily.davis@talentship.com
o Location: Seattle
o Shift: Morning
5. Employee 5
o Name: David Brown
o Employee ID: TS005
o Email: david.brown@talentship.com
o Location: Boston
o Shift: Evening
Leave Details
Employee 1: John Doe
• Employee ID: TS001
• Month: July
• Days Present: 20
• Casual Leave Taken: 2
• Sick Leave Taken: 1
Employee 2: Jane Smith
• Employee ID: TS002
• Month: July
• Days Present: 18
• Casual Leave Taken: 1
• Sick Leave Taken: 2
Employee 3: Mike Johnson
• Employee ID: TS003
• Month: July
• Days Present: 22
• Casual Leave Taken: 1
• Sick Leave Taken: 1
Employee 4: Emily Davis
• Employee ID: TS004
• Month: July
• Days Present: 19
• Casual Leave Taken: 2
• Sick Leave Taken: 2
Employee 5: David Brown
• Employee ID: TS005
• Month: July
• Days Present: 21
• Casual Leave Taken: 2
• Sick Leave Taken: 1
Salary Details
Employee 1: John Doe
• Employee ID: TS001
• Salary: $80,000
• PAN Card Number: ABCD1234E
• Salary Status: Credited
Employee 2: Jane Smith
• Employee ID: TS002
• Salary: $85,000
• PAN Card Number: EFGH5678I
• Salary Status: Credited
Employee 3: Mike Johnson
• Employee ID: TS003
• Salary: $78,000
• PAN Card Number: IJKL9101M
• Salary Status: Credited
Employee 4: Emily Davis
• Employee ID: TS004
• Salary: $90,000
• PAN Card Number: MNOP2345Q
• Salary Status: Credited
Employee 5: David Brown
• Employee ID: TS005
• Salary: $83,000
• PAN Card Number: QRST6789U
• Salary Status: Credited
Job Openings/Vacancies
1. Full Stack Developer
o Experience: 3+ years
o Shift: Morning
o Salary Package: $95,000 - $110,000
o Job Description: Responsible for developing and maintaining web
applications, ensuring cross-platform optimization, and collaborating with
front-end and back-end developers.
o Application: Visit our career page or email hr@talentship.com
2. AI Engineer
o Experience: Fresher or 1+ years
o Shift: Evening
o Salary Package: $85,000 - $100,000
o Job Description: Design and implement machine learning models, analyze
data, and work on AI-driven solutions for clients.
o Application: Visit our career page or email hr@talentship.com
3. Marketing Executive
o Experience: 2+ years
o Shift: Morning
o Salary Package: $60,000 - $75,000
o Job Description: Develop marketing strategies, manage social media
campaigns, and analyze market trends to enhance brand visibility.
o Application: Visit our career page or email hr@talentship.com
4. HR Manager
o Experience: 5+ years
o Shift: Morning
o Salary Package: $100,000 - $120,000
o Job Description: Oversee HR operations, manage recruitment processes, and
develop policies that support organizational goals.
o Application: Visit our career page or email hr@talentship.com
5. For Freshers please provide you educational data team will contact you in future.
Company Services
1. IT Consulting: Providing expert advice and solutions to optimize IT infrastructure
and operations.
2. Software Development: Custom software development services for web, mobile, and
desktop applications.
3. Cloud Services: Cloud migration, management, and optimization services.
4. AI and Machine Learning Solutions: Developing AI-driven solutions for various
business needs, including predictive analytics, natural language processing, and
computer vision.
5. Cybersecurity: Comprehensive cybersecurity services including threat assessment,
monitoring, and incident response.
This covers the requested details for TalentShip. If you need further information or
modifications, feel free to ask!"""),
    ("user","user query:{query}")
])

llm=ollama.Ollama(model='llama3')
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_txt:
    st.write(chain.invoke({"query":input_txt}))
    

 