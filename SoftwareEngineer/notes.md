##Clean and Modular Code

- Production code - code that meets expectations
- Clean - readable, simple, and concise
- Modular - functions, modules, organized, efficient, and reusable
- Module - the ability to reuse a file by encapsulating into files that can be imported into other files.

##Refactoring Code

- Restructuring code without changing external code
- Why have to restructure code?

###Tips

- Use vector operations over loops whenever possible
- Know data structure to use faster method
  - numpy.intersect1d() vs. set.intersection()
- Optimizing 
  - sum(i for i in list()) vs. list[list].sum()
- Documentation 
  - Types
    - Line level - inline comments
      - Docstrings """ """ - a function should have docstrings 
    - Function or module level 
    - Project level - README
- Test Driven 
  - Unit Tests - Test that covers a small unit of a project 
  - Test Driven Development and Data Science
- Logging - Understanding the events what occur while running a program
- 