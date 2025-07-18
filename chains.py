import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException 
from dotenv import load_dotenv


load_dotenv()
class Chain:
    def __init__(self):

        self.llm=ChatGroq(
        model="llama-3.1-8b-instant",
        groq_api_key=os.getenv('GROQ_API_KEY'),
        temperature=0.0,
        max_retries=2,
        # other params...
        )

    def extract_jobs(self,cleaned_text):
        prompt_extract=PromptTemplate.from_template(
            """
            #### SCRAPED TEXT FROM WEBSITE:
            {page_data}
            ### INSTRUCTIONS:
            The scraped text id from the career's page of a website.
            Your job to extract the job posting and return them in JSON format containing 
            following keys:'role', 'experience', 'skills' and 'description'.
            Only return the valid JSON.
            ### VALID JSON (NO PREAMBLE):
            """
        )

        chain_extract = prompt_extract | self.llm
        res=chain_extract.invoke(input={'page_data':cleaned_text})
        try:
            json_parser=JsonOutputParser()
            res=json_parser.parse(res.content)
        except OutputParserException:
            raise OutputParserException("Context too big, unable to parse jobs.")
        return res if isinstance(res,list) else [res]
    
    def write_mail(self, job, links):
        prompt_email = PromptTemplate.from_template(
            """
            ### JOB DESCRIPTION 
            {job_description}

            ### INSTRUCTIONS:
            You are a business development executive at an AI & Software Consulting company dedicated to facilitating the seamless integration of business processes through automated tools.
            Over our experience, we have empowered numerous enterprises with tailored solutions, fostering scalability,process optimization, cost reduction, and heightened overall efficiency. 
            Your job is to write a cold email to the client regarding the job mentioned above describing the capability of the company in fulfilling their needs.Also add the most relevant ones from the following links to showcase companys portfolio: {link_list}
            Remember you are BDE. Add Place holders wherever necessary.and remember you are writing it to the hiring manager. Do not provide a preamble.
            ### EMAIL (NO PREAMBLE):
            """
        )
        chain_email=prompt_email | self.llm
        res=chain_email.invoke({"job_description": str(job), "link_list": links})
        return res.content 
    
    






