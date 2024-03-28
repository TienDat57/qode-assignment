from enum import Enum

class Gender(Enum):
   MALE = "Male"
   FEMALE = "Female"
   OTHER = "Other"

class Degree(Enum):
   BACHELORS = "Bachelor's"
   MASTERS = "Master's"
   DOCTORATE = "Doctorate"
   DIPLOMA = "Diploma"
   CERTIFICATE = "Certificate"
   OTHER = "Other"

class EmploymentType(Enum):
   FULL_TIME = "Full-time"
   PART_TIME = "Part-time"
   CONTRACT = "Contract"
   INTERNSHIP = "Internship"
   FREELANCE = "Freelance"
   OTHER = "Other"
