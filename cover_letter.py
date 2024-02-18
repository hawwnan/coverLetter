from jinja2 import Template

def generate_cover_letter(company_name, position, other_info):
    # Generic part of the cover letter
    template = f"""
    Dear Hiring Manager,

    I am writng this letter to express my interest in the position of {position} at 
    
    your company {company_name}.

    Previously I have worked as a backend intern in a dynamic 365 team focusing on

    warehousing, inventory and other modules. That was a great learning experience for

    me and helped me in getting an understanding of the corporate side of this business.

    I do not have years worth of experience, but whatever it is that I lack I am

    willing to rectify that with hard-work and a desire to get better. So, this will be a great

    opening for me to gain real world experience and grow as a person and professional.

    {other_info}

    Thank you for considering my application. I look forward to the opportunity to discuss 
    
    how my skills and experiences align with the needs of {company_name}.

    Sincerely,
    
    Muhammad Hannan
    """

    return template


company_name = "ABC Corp"
position = "Back-End Developer"
other_info = "I am excited about the opportunity to contribute to your innovative projects."
cover_letter = generate_cover_letter(company_name, position, other_info,)
print(cover_letter)