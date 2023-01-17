# GPA CALCULATOR

<br />
<div align="center">

![splash](https://user-images.githubusercontent.com/98237169/212800767-5f6c2d05-7fd2-4d21-ac63-6fb39fd08291.png)

<h3 align="center"></h3>

  <p align="center">
This is a basic GPA calculator that can consider for various GPA types, including the transcript GPA, honors GPA, and major GPA. Grade policies are based upon NC A&T policies.

Code standardization is observed (PEP8), as well as modular programming. Object-Oriented Programming is implemented with the dataclass "Course" that stores course data. The dictionary data structure is used to store instances of courses. 

A retaken course is automatically detected based upon whether or not a course name is repeated in a differing semester. 
    <br />
  </p>
</div>

#### User Prompts Per Course

<div align="left">
    
   ```
    Enter Course Name: COMP 101
    Enter Course Letter Grade: C
    Enter Course Credit Hours: 3
    Is this course a major course? Y or N: Y
    Is this course a duplicate course Y or N: N
  
    Would you like to continue entering courses for this semester? Y or N: Y
   ```
  
#### Example User Prompts cont.
  
<div align="left">
  
   ```
    Enter Course Name: ENGL 101
    Enter Course Letter Grade: A
    Enter Course Credit Hours: 3
    Is this course a major course? Y or N: N
    Is this course a duplicate course Y or N: N

    Would you like to continue entering courses for this semester? Y or N: N

    Would you like to continue to next semester? Y or N: Y

    Enter Course Name: PHYS 101
    Enter Course Letter Grade: B
    Enter Course Credit Hours: 3
    Is this course a major course? Y or N: N
    Is this course a duplicate course Y or N: N

    Would you like to continue entering courses for this semester? Y or N: Y

    Enter Course Name: COMP 101
    Enter Course Letter Grade: A
    Enter Course Credit Hours: 3
    Is this course a major course? Y or N: Y
    Is this course a duplicate course Y or N: Y

    Would you like to continue entering courses for this semester? Y or N: N
  
    Would you like to continue to next semester? Y or N: N
   ```
</div>
    
#### Final GPA display to user
  
<div align="left">
  
   ```
    Transcript GPA: 3.67
    Honors GPA: 3.25
    Major GPA: 4.00
   ```

</div>

