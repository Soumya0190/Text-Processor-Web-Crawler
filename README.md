# Text-Processor-Web-Crawler
1. https://canvas.eee.uci.edu/courses/26505/assignments/478119
2. https://canvas.eee.uci.edu/courses/26505/assignments/478120
3. https://canvas.eee.uci.edu/courses/26505/assignments/478121
4. https://canvas.eee.uci.edu/courses/26505/assignments/478122
5. https://canvas.eee.uci.edu/courses/26505/assignments/478123

---


To explain the **Text Processing** project using the STAR method, here's how you can break it down:

### **S - Situation:**
The assignment required building a text processing program to perform two tasks using Python. The first task was to process a text file, tokenize it, compute word frequencies, and print them in order of occurrence. The second task involved comparing two text files to find common tokens. This needed to be done using efficient algorithms, as the input text files could be large, and the program had to handle possible bad inputs gracefully without crashing.

### **T - Task:**
The task was to implement two separate parts:
- **Part A: Word Frequencies**: 
  - Create a program that reads a text file, tokenizes the content (breaking it down into alphanumeric words), and computes the frequency of each word. Then, print the word frequencies in descending order of frequency.
  
- **Part B: Intersection of Two Files**:
  - Write a program that takes two text files as input and determines the number of common tokens between them.

Additionally, both parts needed to:
- Be efficient, as they may need to process large files.
- Handle exceptions properly, skipping over bad input without crashing.
- Provide runtime complexity explanations as comments in the code.

### **A - Action:**
To address these tasks, I followed the steps below:

- **Part A: Word Frequencies**:
  1. **Tokenization**: I wrote a function `tokenize()` that read the input text file and split it into tokens (words) using Python's regular expressions to handle word boundaries and ignore case sensitivity.
  2. **Frequency Counting**: I created a `computeWordFrequencies()` method that counted occurrences of each token using a dictionary or a `Counter` from the `collections` module.
  3. **Printing**: I implemented a method `print()` to output the token frequencies in the required format (`<token> -> <freq>`), ensuring they were ordered by descending frequency.

- **Part B: Intersection of Two Files**:
  1. I reused the code from **Part A** to tokenize both input files.
  2. I used a set intersection technique to find the common tokens between the two files by converting the list of tokens from each file into sets and calculating their intersection.
  3. I printed the count of common tokens.

- **Exception Handling**: I added exception handling to ensure that any bad input (such as unsupported characters or formatting issues) was skipped without crashing the program.

- **Performance**: I optimized the program to minimize the time complexity of common tasks like tokenization and intersection by using efficient data structures like dictionaries and sets. I included comments explaining the runtime complexities.

### **R - Result:**
The result was a functional **Text Processing Program** that:
- Accurately tokenized text files and computed word frequencies in **Part A**, displaying them in the required format and order.
- Efficiently found and counted the **common tokens** between two files in **Part B**, even for large text files.
- Handled bad input gracefully, skipping over errors without interrupting the process.
- Provided clear explanations of the program's performance and complexities.

The project was submitted as required, meeting the functional specifications and achieving good performance on large inputs, which was a key aspect of the grading criteria.

---

To explain your project using the STAR method (Situation, Task, Action, Result), you can break it down like this:

### Situation:
In this project, I was part of a team assigned to implement a web crawler for a set of specified URLs from the University of California, Irvine's (UCI) websites. The goal was to collect data from these websites, analyze it, and answer specific questions related to the crawled content. The crawler was expected to adhere to strict guidelines, including politeness delays, avoiding infinite traps, and ensuring that we only crawled specific URLs.

### Task:
Our task was to build a web crawler that:
1. Crawled specific domains and paths defined in the assignment.
2. Extracted data to answer key questions such as finding unique pages, determining the longest page, identifying common words, and analyzing subdomains.
3. Ensured that the crawler was efficient, polite (adhering to politeness delays), and able to avoid traps or unnecessary pages.
4. Generated a report summarizing the analytics from the crawl.

### Action:
To tackle the project:
1. **Implemented the core web crawler**: I started by forking the crawler code provided and modifying the scraper function to fit the assignment's requirements. This involved ensuring that the scraper only crawled the specified domains and paths, correctly handled URLs (removing fragments), and parsed the HTML to count words, avoid traps, and track common words.
2. **Handled politeness and crawl efficiency**: We ensured the crawler respected politeness rules by setting appropriate delays between requests and avoiding issues like crawling very large files or dead URLs.
3. **Developed analytics**: I implemented methods to count unique pages, find the longest page by word count, identify the most common words, and list subdomains with their respective page counts.
4. **Collaboration**: As this was a group project, we split tasks to improve efficiency. Some of us focused on code, while others worked on analyzing the data and writing the report. We also ensured the crawler was tested and improved continuously during the project.

### Result:
The crawler successfully completed the assignment's objectives:
1. We were able to crawl all the specified domains and paths without violating any rules.
2. The crawler efficiently processed the pages and collected the necessary data to answer all the questions in the report.
3. The analytics were within the expected range, and we were able to submit a detailed report with our findings.
4. During the grader meeting, we were able to demonstrate our crawler’s operation and respond to questions about its implementation.
5. We avoided crawling infinite loops, traps, or irrelevant pages, ensuring a clean and efficient crawl.
   
This project helped me improve my web scraping skills and my understanding of crawl efficiency and politeness in real-world applications.

---

