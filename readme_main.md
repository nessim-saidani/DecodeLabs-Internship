# DecodeLabs Internship Program - Batch 2026

## AI Projects Portfolio

This repository contains three comprehensive AI projects completed as part of the DecodeLabs Industrial Training Kit. Each project demonstrates fundamental AI concepts through hands-on implementation.

**Student Name:** Nessim Saidani
**Batch:** 2026
**Organization:** DecodeLabs
**Repository:** DecodeLabs-Internship

---

## Table of Contents

- [Overview](#overview)
- [Project Summary](#project-summary)
- [Repository Structure](#repository-structure)
- [Installation](#installation)
- [Technologies Used](#technologies-used)
- [Project Details](#project-details)
- [Key Skills Demonstrated](#key-skills-demonstrated)
- [How to Run Each Project](#how-to-run-each-project)
- [Results and Performance](#results-and-performance)
- [Contact Information](#contact-information)

---

## Overview

This repository showcases three progressive AI projects that build foundational knowledge in artificial intelligence:

1. **Task 1:** Rule-Based AI Chatbot (Control Flow & Logic)
2. **Task 2:** Data Classification Using AI (Supervised Learning)
3. **Task 3:** AI Movie Recommendation System (Pattern Matching & Similarity)

Each project is self-contained, fully documented, and ready for production use.

---

## Project Summary

### Task 1: Rule-Based AI Chatbot

**Objective:** Create a simple rule-based chatbot that responds to predefined user inputs.

**Key Features:**
- Greeting recognition and response
- Exit command handling
- Weather information queries
- Personal question answering
- Continuous conversation loop
- Random response variation

**Technologies:** Python (built-in libraries only)

**Files:**
- `task_1/chatbot.py` - Main chatbot script
- `task_1/README.md` - Detailed documentation

**Status:** Completed and Tested ✓

---

### Task 2: Data Classification Using AI

**Objective:** Build a basic classification model using the Iris dataset.

**Key Features:**
- Dataset loading and exploration
- Train-test data splitting (80-20 split)
- Multiple classification algorithms:
  - K-Nearest Neighbors (KNN)
  - Decision Tree Classifier
  - Logistic Regression
- Model evaluation and comparison
- Cross-validation analysis
- Accuracy: 100%

**Technologies:** Python, Pandas, Scikit-learn, NumPy

**Files:**
- `task_2/classification_model.py` - Classification script
- `task_2/iris.csv` - Dataset file
- `task_2/README.md` - Detailed documentation

**Status:** Completed with 100% Accuracy ✓

---

### Task 3: AI Movie Recommendation System

**Objective:** Create a recommendation system based on user genre preferences.

**Key Features:**
- User preference input
- Similarity matching algorithm
- Content-based recommendations
- Ranking by match score
- Genre filtering
- Extensible movie database

**Technologies:** Python (built-in libraries only)

**Files:**
- `task_3/recommendation_system.py` - Recommendation script
- `task_3/README.md` - Detailed documentation

**Status:** Completed and Tested ✓

---

## Repository Structure

```
DecodeLabs-Internship/
│
├── task_1/
│   ├── chatbot.py                    # Rule-based chatbot implementation
│   └── README.md                     # Task 1 documentation
│
├── task_2/
│   ├── classification_model.py       # Classification model implementation
│   ├── iris.csv                      # Iris dataset
│   └── README.md                     # Task 2 documentation
│
├── task_3/
│   ├── recommendation_system.py      # Recommendation system implementation
│   └── README.md                     # Task 3 documentation
│
├── README.md                         # This file - Main documentation
├── requirements.txt                  # Python dependencies
└── .gitignore                        # Git ignore rules
```

---

## Installation

### System Requirements

- Python 3.6 or higher
- pip (Python package manager)
- Git (for version control)

### Clone the Repository

```bash
git clone https://github.com/nessim-saidani/DecodeLabs-Internship.git
cd DecodeLabs-Internship
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Verify Installation

```bash
python --version
```

---

## Technologies Used

### Core Languages
- **Python 3.6+** - Primary programming language

### Libraries Used

**Task 1 (Chatbot):**
- Python built-in libraries only (random, sys)

**Task 2 (Classification):**
- pandas - Data manipulation and analysis
- scikit-learn - Machine learning algorithms
- numpy - Numerical computing
- matplotlib - Data visualization

**Task 3 (Recommendation):**
- Python built-in libraries only

### Version Control
- **Git** - Version control system
- **GitHub** - Repository hosting

---

## Project Details

### Task 1: Rule-Based AI Chatbot

**Description:**
A conversational AI that uses if-else logic to respond to user inputs. Demonstrates fundamental programming concepts through interactive dialogue.

**How It Works:**
1. Takes user input
2. Converts to lowercase for matching
3. Checks against predefined rules
4. Returns appropriate response
5. Continues until exit command

**Key Algorithms:**
- Pattern matching using string comparison
- Control flow with while loops and if-elif-else statements
- Random selection from response sets

**Run Command:**
```bash
python task_1/chatbot.py
```

**Example Interaction:**
```
welcome to the chatbot py

type 'exit' to end the conversation
BOT: how can i help you 
You: hello
BOT: Hi there!
You: how are you?
BOT: I am fine how are you ?
You: exit
BOT: Goodbye! Have a great day!
```

---

### Task 2: Data Classification Using AI

**Description:**
A machine learning project that trains multiple classification algorithms on the Iris dataset to predict flower species based on measurements.

**How It Works:**
1. Loads the Iris dataset (150 samples)
2. Explores data structure and statistics
3. Splits data into training (80%) and testing (20%) sets
4. Trains multiple classification algorithms
5. Evaluates model performance
6. Compares algorithm effectiveness

**Algorithms Used:**
- K-Nearest Neighbors (KNN) - k=3 and k=5
- Decision Tree Classifier
- Logistic Regression

**Performance Results:**
- KNeighborsClassifier (k=3): 100% accuracy
- DecisionTreeClassifier: 100% accuracy
- LogisticRegression: 100% accuracy
- KNeighborsClassifier (k=5): 96.67% accuracy

**Run Command:**
```bash
python task_2/classification_model.py
```

**Key Metrics:**
- Accuracy: 100%
- Precision: 100%
- Recall: 100%
- F1-Score: 100%

---

### Task 3: AI Movie Recommendation System

**Description:**
A content-based recommendation engine that suggests movies based on user genre preferences using similarity matching algorithms.

**How It Works:**
1. Takes user input (preferred genres)
2. Calculates similarity score for each movie
3. Filters movies by minimum score threshold
4. Ranks recommendations by match percentage
5. Displays results to user

**Similarity Formula:**
```
Match Score = (Matching Genres) / (Total User Genres) × 100%
```

**Movie Database:**
- 10 movies with 9 different genres
- Genres: Action, Animation, Comedy, Crime, Drama, Mystery, Romance, Sci-Fi, Thriller

**Run Command:**
```bash
python task_3/recommendation_system.py
```

**Example Interaction:**
```
welcome to the ai recommendation system
what genre of movies do you like (comma seperated): Action, Sci-Fi
You prefer: ['Action', 'Sci-Fi'] movies
we recommend you the following movies:
The Matrix with a score of 100.0%
Avengers with a score of 100.0%
Inception with a score of 50.0%
Interstellar with a score of 50.0%
The Dark Knight with a score of 50.0%
```

---

## Key Skills Demonstrated

### Programming Skills
- Python programming fundamentals
- Function definition and organization
- Data structures (lists, dictionaries, sets)
- String manipulation and formatting
- Input/output operations
- Error handling and validation
- Object-oriented principles

### Algorithm Design
- Control flow and decision logic
- Pattern matching algorithms
- Similarity calculation
- Sorting and filtering
- Data comparison techniques
- Algorithm complexity analysis

### Machine Learning Skills
- Supervised learning concepts
- Data preprocessing and exploration
- Train-test splitting methodology
- Model training and evaluation
- Algorithm comparison
- Cross-validation techniques
- Hyperparameter tuning

### AI/ML Concepts
- Rule-based AI systems
- Classification algorithms
- Recommendation systems
- Content-based filtering
- Similarity metrics
- User preference matching

### Software Engineering
- Version control with Git
- Repository management
- Code documentation
- README file creation
- Project organization
- Code commenting
- Best practices implementation

---

## How to Run Each Project

### Task 1: Chatbot

```bash
# Navigate to task_1 directory
cd task_1

# Run the chatbot
python chatbot.py

# Follow prompts to interact with the bot
# Type 'exit' to quit
```

### Task 2: Classification Model

```bash
# Navigate to task_2 directory
cd task_2

# Run the classification model
python classification_model.py

# View results and model evaluation metrics
# Check accuracy, precision, recall, and confusion matrix
```

### Task 3: Recommendation System

```bash
# Navigate to task_3 directory
cd task_3

# Run the recommendation system
python recommendation_system.py

# Enter movie genres you like (comma-separated)
# View personalized movie recommendations
```

---

## Results and Performance

### Task 1: Chatbot
- Status: Working perfectly
- Features: All working as expected
- Tested: Yes, interactive testing completed
- Documentation: Complete

### Task 2: Classification
- Accuracy: 100% on test set
- Training samples: 120
- Testing samples: 30
- Best model: K-Nearest Neighbors (k=3)
- Documentation: Complete with metrics

### Task 3: Recommendation System
- Functionality: Working as intended
- Test cases: Multiple genre combinations tested
- Recommendations quality: Accurate and relevant
- Documentation: Complete

---

## Project Progression

The three projects demonstrate a clear progression in AI understanding:

**Task 1 → Task 2 → Task 3**

```
Task 1: Rule-Based Logic
        ↓
Task 2: Data-Driven Learning (Supervised)
        ↓
Task 3: Pattern Matching & Similarity
```

Each project builds on programming fundamentals while introducing new AI concepts:
- Task 1: Control flow and basic logic
- Task 2: Data manipulation and machine learning
- Task 3: Algorithm design and pattern matching

---

## Requirements File

The `requirements.txt` contains all necessary packages:

```
pandas>=1.0.0
scikit-learn>=0.24.0
numpy>=1.19.0
matplotlib>=3.3.0
```

Install all requirements:
```bash
pip install -r requirements.txt
```

---

## GitHub Repository

**Repository URL:** https://github.com/nessim-saidani/DecodeLabs-Internship

**Repository Features:**
- Well-organized folder structure
- Complete documentation for each project
- Version history tracked with Git
- All code tested and working
- Ready for review and evaluation

---

## Submission Checklist

Before final submission, verify:

✓ Code is working properly
✓ All project files are complete
✓ GitHub repository is created and updated
✓ README files are added for all projects
✓ Main README documentation is complete
✓ All projects have been tested
✓ Code follows Python best practices
✓ Comments and docstrings are included
✓ No errors or warnings in execution
✓ Directory structure is organized
✓ Requirements.txt is present
✓ Git commits are meaningful
✓ All files are pushed to GitHub

---

## Learning Journey

### Concepts Learned

**Programming Fundamentals:**
- Variables, data types, and operations
- Control structures (loops, conditionals)
- Functions and code organization
- Data structures (lists, dictionaries)
- String manipulation

**AI/ML Fundamentals:**
- Rule-based systems
- Supervised learning
- Classification algorithms
- Data preprocessing
- Model evaluation metrics
- Recommendation systems
- Similarity matching

**Software Development:**
- Version control (Git)
- Repository management
- Documentation practices
- Testing and validation
- Code organization

---

## Future Enhancements

### Task 1 Enhancements
- Add natural language processing
- Implement sentiment analysis
- Add database for conversation logging
- Implement machine learning adaptation

### Task 2 Enhancements
- Test on additional datasets
- Implement deep learning models
- Add feature engineering
- Deploy as REST API
- Add model persistence (save/load)

### Task 3 Enhancements
- Add collaborative filtering
- Implement user ratings
- Add movie information (plot, ratings)
- Create web interface
- Deploy as recommendation service

---

## Troubleshooting

### Common Issues

**Issue 1: Python not found**
```bash
# Solution: Verify Python installation
python --version
```

**Issue 2: Module not found**
```bash
# Solution: Install requirements
pip install -r requirements.txt
```

**Issue 3: File not found in task folder**
```bash
# Solution: Navigate to correct directory
cd task_1  # or task_2, task_3
```

**Issue 4: Git push fails**
```bash
# Solution: Pull updates first
git pull origin main
git push origin main
```

---

## Contact Information

**DecodeLabs Industrial Training Kit**

- Phone: +91 89330 06408
- Email: decodelabs.tech@gmail.com
- Website: www.decodelabs.tech
- Location: Greater Lucknow, India

**Student Information**
- Name: Nessim Saidani
- Batch: 2026
- GitHub: https://github.com/nessim-saidani

---

## Version History

### Version 1.0 (May 2026)

**Task 1: Rule-Based Chatbot**
- Initial project completion
- Greeting and exit command handling
- Weather query support
- Continuous conversation loop

**Task 2: Data Classification**
- Model training with multiple algorithms
- 100% accuracy achieved
- Cross-validation analysis
- Complete model evaluation

**Task 3: Recommendation System**
- Content-based filtering implementation
- Similarity score calculation
- Movie recommendation engine
- Genre-based matching

---

## Acknowledgments

- **DecodeLabs Team** - For the comprehensive training program
- **Batch 2026 Cohort** - For collaborative learning
- **Python Community** - For excellent libraries and documentation

---

## License

This project is part of the DecodeLabs Industrial Training Kit. All code and documentation are provided for educational purposes within the training program.

---

## Final Notes

This repository demonstrates:
- **Practical AI Implementation:** Real-world application of AI concepts
- **Complete Solutions:** Each project is production-ready
- **Clear Documentation:** Well-documented code and comprehensive READMEs
- **Professional Approach:** Following best practices in software development
- **Learning Progression:** Clear advancement from basic to intermediate concepts

All projects are ready for expert review and evaluation.

---

**Last Updated:** May 2026
**Status:** Ready for Submission ✓

---

## Quick Links

- [Task 1 README](task_1/README.md) - Rule-Based Chatbot Documentation
- [Task 2 README](task_2/README.md) - Classification Model Documentation
- [Task 3 README](task_3/README.md) - Recommendation System Documentation
- [GitHub Repository](https://github.com/nessim-saidani/DecodeLabs-Internship) - Full project repository

---

End of Main README Documentation