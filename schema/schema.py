from enums.enum import Gender, Degree, EmploymentType

class CandidateProfile:
   def __init__(self):
      self.personal_information = PersonalInformation()
      self.education_background = []
      self.work_experience = WorkExperience()
      self.skills_and_expertise = SkillsAndExpertise()
      self.social_media_presence = SocialMediaPresence()
      self.publications_and_projects = []
      self.professional_interests = []
      self.additional_information = []

class WorkExperience:
   def __init__(self):
      self.company_name = ""
      self.job_title = ""
      self.employment_duration = ""
      self.responsibilities = ""
      self.skills_acquired = []
      self.employment_type = EmploymentType.FULL_TIME

class PersonalInformation:
   def __init__(self):
      self.name = ""
      self.contact_information = ContactInformation()
      self.date_of_birth = ""
      self.gender = Gender.MALE
      self.nationality = ""
      self.languages_spoken = []

class ContactInformation:
   def __init__(self):
      self.phone = ""
      self.email = ""
      self.address = ""

class Education:
   def __init__(self):
      self.degree = Degree.BACHELORS
      self.institution = ""
      self.major = ""
      self.graduation_year = ""

class WorkExperience:
   def __init__(self):
      self.company_name = ""
      self.job_title = ""
      self.employment_duration = ""
      self.responsibilities = ""
      self.skills_acquired = []

class SkillsAndExpertise:
   def __init__(self):
      self.technical_skills = []
      self.soft_skills = []
      self.certifications = []

class SocialMediaPresence:
   def __init__(self):
      self.linkedin_profile = ""
      self.twitter_handle = ""
      self.github_profile = ""

class PublicationProject:
   def __init__(self):
      self.title = ""
      self.type = ""  

class ProfessionalInterests:
   def __init__(self):
      self.industry_interests = []
      self.career_goals = []

