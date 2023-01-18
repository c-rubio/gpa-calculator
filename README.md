# GPA CALCULATOR

<br />
<div align="left">

![splash](https://user-images.githubusercontent.com/98237169/212800767-5f6c2d05-7fd2-4d21-ac63-6fb39fd08291.png)

  <p align="left">
The GPA calculator can consider for various GPA types, including the transcript GPA, honors GPA, and major GPA. Grade policies are based upon NC A&T policies.

Code standardization is observed (PEP8), as well as modular programming. Object-Oriented Programming is implemented with the dataclass "Course" that stores course data. The dictionary data structure is used to store instances of courses. 

  </p>
</div>


<h3 align="left">Features</h3>


  - Calculation of NC A&T Transcript, Honors, and Major GPA
  - Write to .csv files for persistent storage of new transcript
  - Read .csv files to calculate GPA
  - Implementation of dataclass module to simplify course storage and access
  - Automatic retaken course detection


#### User Prompts Per Course

<div align="left">
    
   ```
    Enter Course Name: COMP 101
    Enter Course Letter Grade: C
    Enter Course Credit Hours: 3
    Is this course a major course? Y or N: Y
  
    Would you like to continue entering courses for this semester? Y or N: N 
    
    Would you like to continue to next semester? Y or N: Y
   ```
#### Example GPA display to user
  
<div align="left">
  
   ```
    Transcript GPA: 3.67
    Honors GPA: 3.25
    Major GPA: 4.00
   ```

</div>

#### Dataclass implementation
  
<div align="left">
  
   ```python
  @dataclass
  class Course:
    name : str = ""
    grade : float = 0.00
    hours : float = 0.00
    is_major : bool = False
    is_retaken : bool = False
    semester: int = 0
   ```
</div>
