# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a comprehensive educational portfolio repository documenting a 5-month intensive AI Developer course (SeSac 2025). The repository contains systematic learning materials, practice notebooks, projects, and documentation across multiple technical domains including Python, databases, web development, algorithms, machine learning, and deep learning.

**Primary Language**: Korean and English (bilingual documentation)
**Repository Type**: Educational portfolio with chronological learning structure

## Navigation Guide

### Quick Access to Common Tasks
- **View daily learning notes**: Go to `*/md/MMDD_*_Summary.md` files
- **Run practice notebooks**: Go to `*/ipynb/MMDD_*_Practice.ipynb` files
- **Check homework solutions**: Look in `*/ipynb/homework/` subdirectories
- **Access datasets**: Check `*/data/` directories in each module
- **Find comprehensive guides**: Browse `99_etc/docs/` for complete reference guides

### Finding Specific Content
- **Python basics**: `01_Python/ipynb/0423_Python_Practice.ipynb` onwards
- **Database work**: `02_SQL/ipynb/` for MySQL-Python integration and `02_SQL/MongoDB/` for MongoDB
- **Web development**: `05_Full_Stack/backend/Django/` for Django projects
- **Machine learning**: `06_Machine_Learning/ipynb/0701~0704/` for fundamentals
- **Deep learning**: `07_Deep_Learning/ipynb/0717/` for CNN implementations
- **Latest work**: `08_PyTorch/` for current progress

## Environment Setup

### Python Environment
- **Primary Environment**: Conda environment using `enviroment.yml`
- **Alternative**: pip virtual environment using `requirements.txt`
- **Python Version**: 3.11 (recommended)
- **Key Dependencies**: TensorFlow 2.13+, PyTorch 2.0+, scikit-learn, pandas, numpy, Django 5.0+

### Setup Commands
```bash
# Conda setup (recommended)
conda env create -f enviroment.yml
conda activate sesac_ai

# pip setup (alternative)
python -m venv sesac_ai
# Windows: sesac_ai\Scripts\activate
# macOS/Linux: source sesac_ai/bin/activate
pip install -r requirements.txt
```

### System Dependencies
- **Java 11+**: Required for KoNLPy (Korean NLP). Set JAVA_HOME environment variable.
- **Graphviz**: For tree visualization in scikit-learn. Add to system PATH.
- **MySQL Server**: For database-related projects. Must be running for MySQL notebooks.
- **Visual Studio Build Tools**: May be needed on Windows for mysqlclient and other C extensions.

### Quick Environment Check
```bash
# Verify environment is working
python -c "import tensorflow as tf; print('TensorFlow:', tf.__version__)"
python -c "import torch; print('PyTorch:', torch.__version__)"
python -c "import pymysql; print('MySQL driver available')"
python -c "import cv2; print('OpenCV available')"
```

## Repository Structure & Architecture

### High-Level Organization
The repository follows a chronological learning structure with 8 main subject areas:

1. **01_Python/**: Python fundamentals and advanced concepts
2. **02_SQL/**: Database design, SQL queries, Python integration (MySQL + MongoDB)
3. **03_Git_and_Clean_Code/**: Version control and code quality practices
4. **04_Algorithm/**: Algorithm problem-solving and optimization
5. **05_Full_Stack/**: Web development (frontend + backend)
6. **06_Machine_Learning/**: ML algorithms and data science
7. **07_Deep_Learning/**: Neural networks and computer vision
8. **08_PyTorch/**: Advanced deep learning with PyTorch (in progress)
9. **99_etc/**: Additional resources and comprehensive guides

### Content Structure Pattern
Each learning module follows a consistent structure:
- **ipynb/**: Jupyter notebooks with hands-on practice
- **md/**: Daily summary notes and theoretical explanations
- **data/**: Datasets and supporting files
- **Additional files**: Projects, homework, or module-specific content

### Architecture Patterns & Design

#### Learning-Oriented Structure
The repository follows a **chronological learning architecture** with consistent patterns:
- **Theory-Practice-Project Pipeline**: Each module includes theoretical notes (md/), hands-on practice (ipynb/), and real-world projects
- **Progressive Complexity**: Modules build upon each other, from Python basics to advanced deep learning
- **Standardized Naming**: Date-based files (MMDD_Subject_Practice.ipynb) for easy tracking and navigation

#### Django Multi-Project Architecture (05_Full_Stack/backend/)
Each Django project follows **standard MVT (Model-View-Template) pattern**:
- **mysite1/**: Multi-app Django project (blog, guestbook, score apps)
  - Shared config/ directory with centralized settings
  - App-specific URLs, models, views, and templates
  - Template inheritance with base templates
- **myhome1/**: Blog-focused project with score management integration
- **myhome2/**: Minimal Django structure for learning

**Django App Structure Pattern**:
```
project_name/
├── manage.py
├── config/          # Project settings
│   ├── settings.py
│   ├── urls.py      # Root URL configuration
│   └── wsgi.py
├── app_name/        # Individual Django apps
│   ├── models.py    # Data models
│   ├── views.py     # Business logic
│   ├── urls.py      # App-specific URLs
│   ├── forms.py     # Form definitions
│   └── migrations/  # Database migrations
└── templates/       # HTML templates
    └── app_name/    # App-specific templates
```

#### Data Science Workflow Architecture

**Machine Learning Pipeline (06_Machine_Learning/)**:
- **Data Layer**: Organized datasets in data/csv/ with consistent preprocessing
- **Notebook Organization**: Date-based practice sessions with incremental complexity
- **Model Persistence**: Saved models and results in data/ subdirectories
- **Visualization Layer**: HTML reports (feature_importance.html, model_comparison.html)

**Deep Learning Architecture (07_Deep_Learning/)**:
- **Dataset Management**: Large-scale image datasets with structured organization
- **Model Development**: Date-organized notebooks with progressive CNN architectures
- **Transfer Learning**: Pre-trained model integration for image classification
- **Performance Monitoring**: Training history visualization and model evaluation

#### Key Project Types

#### Django Web Applications (05_Full_Stack/backend/Django/)
- **mysite1/**: Multi-app integration (blog, guestbook, grade management)
  - Demonstrates Django app modularity and URL routing
  - Uses Django ORM with SQLite backend
  - Template inheritance and form handling
- **myhome1/**: Personal blog platform with score management
  - Shows Django-MySQL integration patterns
  - Implements user authentication and session management
- **myhome2/**: Basic Django framework structure for learning

#### React Applications (05_Full_Stack/React/)
- **project/**: Modern React application with Vite
  - Component-based architecture (board, score, counter components)
  - React Router for navigation (home, about, nomatch pages)
  - Bootstrap and React-Bootstrap for styling
  - Axios for API communication with backend services

#### React Native Applications (05_Full_Stack/React_Native/)
- **Crud-Redux/**: CRUD operations with Redux state management
- **React-Redux/**: Redux integration patterns and state management
- **React-Redux-Crud-Master/**: Advanced CRUD with Redux architecture

#### SpringBoot Application (05_Full_Stack/React_Native/SpringBoot/)
- Java-based backend service with Maven configuration
- RESTful API development patterns
- Integration with frontend React Native applications

#### Machine Learning Projects (06_Machine_Learning/)
- **Supervised Learning**: Classification and regression models using scikit-learn
- **Data Processing**: Comprehensive pandas and numpy workflows
- **Model Evaluation**: Cross-validation, confusion matrices, ROC curves
- **Hyperparameter Optimization**: Optuna-based automated tuning
- **Interactive Visualizations**: HTML reports with Plotly and Bokeh

#### Deep Learning Projects (07_Deep_Learning/)
- **Computer Vision**: CNN architectures for image classification
  - **Binary Classification**: Cat/dog classifier with data augmentation
  - **Multi-class Classification**: Flower species identification
  - **Environmental AI**: Garbage classification system
- **Model Architecture**: TensorFlow/Keras implementation patterns
- **Performance Optimization**: Transfer learning and fine-tuning techniques

## Common Development Commands

### Environment Management
```bash
# Activate conda environment (recommended)
conda activate sesac_ai

# Activate pip virtual environment
# Windows:
sesac_ai\Scripts\activate
# macOS/Linux:
source sesac_ai/bin/activate

# Install additional packages
conda install <package_name>
pip install <package_name>

# Update environment files
conda env export > enviroment.yml
pip freeze > requirements.txt
```

### Running Jupyter Notebooks
```bash
# Start Jupyter Lab (recommended for data science)
jupyter lab

# Start classic Jupyter Notebook
jupyter notebook

# Run specific notebook from command line
jupyter nbconvert --execute --to notebook 06_Machine_Learning/ipynb/0701/0701_ML_Practice_1.ipynb
```

### Django Development
```bash
# Navigate to specific Django project
cd 05_Full_Stack/backend/Django/mysite1

# Run development server
python manage.py runserver
# Custom port: python manage.py runserver 8080

# Database migrations
python manage.py makemigrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Collect static files
python manage.py collectstatic

# Run tests
python manage.py test

# Django shell for debugging
python manage.py shell
```

### FastAPI Development
```bash
# Main FastAPI project (standalone)
cd 05_Full_Stack/backend
uvicorn FastAPI.main:app --reload
# Access at: http://localhost:8000
# API docs at: http://localhost:8000/docs

# Organized FastAPI projects with routers
cd 05_Full_Stack/backend/FastAPI/backend    # Board and score APIs
uvicorn main:app --reload --port 8000
# Routers: /board, /score
# Database: MySQL integration with PyMySQL

cd 05_Full_Stack/backend/FastAPI/backend2   # Board and predict APIs  
uvicorn main:app --reload --port 8001
# Routers: /board, /predict (ML model integration)
# Database: MySQL + ML model endpoints

# Health check and API info endpoints available at:
# GET / - Health check
# GET /info - Server information and available endpoints
# GET /docs - Swagger API documentation
# GET /redoc - ReDoc API documentation
```

### Common Issues & Troubleshooting
```bash
# Jupyter notebooks not finding packages
conda activate sesac_ai
python -m ipykernel install --user --name=sesac_ai

# MySQL connection errors
mysql --version  # Check if MySQL is installed
sudo systemctl start mysql  # Linux
brew services start mysql   # macOS

# Package conflicts
conda list                   # Check installed packages
pip check                    # Check for conflicts
```

### React Frontend Development
```bash
# React Vite Project
cd 05_Full_Stack/React/project

# Install dependencies
npm install

# Start development server
npm run dev

# Build for production
npm run build

# Run linting
npm run lint

# Preview production build
npm run preview
```

### React Native Development
```bash
# React Native projects with Redux integration
cd 05_Full_Stack/React_Native/Crud-Redux
npm install
npm start  # or yarn start

# Redux state management example
cd 05_Full_Stack/React_Native/React-Redux
npm install
npm start

# Check React Native environment
npx react-native doctor
```

### SpringBoot Development
```bash
# Navigate to SpringBoot project
cd 05_Full_Stack/React_Native/SpringBoot

# Build and run with Maven
mvn clean install
mvn spring-boot:run

# Or use Maven wrapper
./mvnw spring-boot:run  # macOS/Linux
mvnw.cmd spring-boot:run  # Windows
```

### Machine Learning Development
```bash
# Navigate to ML notebooks
cd 06_Machine_Learning/ipynb

# Organize by date for daily practice
cd 0701~0704  # Early ML concepts
cd 0707       # Advanced ML techniques
cd 0708       # Model evaluation
cd 0715       # Optimization and tuning

# Key data files are in ../data/csv/ and ../data/
# Models are saved to appropriate subdirectories
```

### Deep Learning Development
```bash
# Navigate to DL notebooks (organized by date)
cd 07_Deep_Learning/ipynb/0717  # Neural network basics
cd 07_Deep_Learning/ipynb/0725  # Advanced CNN projects

# Large datasets in ../data/
# cats_and_dogs/ - Binary classification
# flowers/ - Multi-class classification
# Garbageclassification/ - Environmental AI

# TensorFlow GPU check
python -c "import tensorflow as tf; print('GPU Available:', tf.config.list_physical_devices('GPU'))"

# PyTorch GPU check
python -c "import torch; print('CUDA Available:', torch.cuda.is_available())"
```

### PyTorch Development
```bash
# Navigate to PyTorch notebooks (in progress)
cd 08_PyTorch/ipynb

# Check PyTorch installation and version
python -c "import torch; print('PyTorch Version:', torch.__version__)"
python -c "import torch; print('CUDA Available:', torch.cuda.is_available())"

# Model saving/loading patterns used in this repository
# Saved models typically in 08_PyTorch/data/ as .pth files
# Example: iris_classifier_model.pth, iris_scaler.pkl
```

### Testing and Quality Assurance
```bash
# Run Python tests (if pytest is configured)
pytest

# Check code style (if configured)
flake8 .
black --check .

# For Django projects
python manage.py test

# For React projects
npm test

# Model validation and evaluation
# TensorFlow model evaluation
python -c "import tensorflow as tf; model = tf.keras.models.load_model('model.h5'); print(model.summary())"

# PyTorch model evaluation
python -c "import torch; model = torch.load('model.pth'); print(model)"

# Check GPU availability for deep learning
python -c "import tensorflow as tf; print('TensorFlow GPU:', tf.config.list_physical_devices('GPU'))"
python -c "import torch; print('PyTorch CUDA:', torch.cuda.is_available())"
```

### Database Operations
```bash
# MySQL connection test
python -c "import pymysql; print('MySQL driver available')"

# MongoDB connection test
python -c "import pymongo; print('MongoDB driver available')"

# Run SQL scripts
mysql -u username -p database_name < 02_SQL/sql/MySQL_Day_1-5.sql

# MongoDB operations (Python files in 02_SQL/MongoDB/)
cd 02_SQL/MongoDB
python mongodb연동.py
python mongodb연동2.py  # Advanced operations
python mongodb연동3.py  # Additional MongoDB examples
```

## Data Management

### Data Organization
- **CSV files**: Located in module-specific `data/csv/` directories
- **Image datasets**: In `data/` subdirectories with specific organization:
  - `cats_and_dogs/` - Binary classification dataset
  - `flowers/` - Multi-class flower classification with LICENSE.txt and CSV files
  - `flowers_renamed/` - Processed flower images with systematic naming (daisy.0.jpg, etc.)
  - `Garbageclassification/` - Environmental AI waste classification dataset (cardboard/, glass/, metal/, paper/, plastic/, trash/)
- **Database files**: SQL scripts in `02_SQL/sql/` and MongoDB Python scripts in `02_SQL/MongoDB/`
- **Processed data**: NPY/NPZ files for NumPy arrays
- **Model artifacts**: 
  - `06_Machine_Learning/data/` - ML models and HTML reports
  - `08_PyTorch/data/` - PyTorch model files (.pth) and scalers (.pkl)
- **NLP datasets**: 
  - `aclImdb/` - IMDB movie review sentiment analysis
  - `GoogleNews-vectors-negative300.bin` - Pre-trained word vectors
  - `glove.6B.100d.txt` - GloVe word embeddings

### Large Files and Memory Management
- Image datasets can be several GB in size (10,000+ images per category)
- Use data generators for large datasets to avoid memory overload
- Consider data augmentation for deep learning projects
- Use batch processing for large-scale model training
- Save intermediate results when working with computationally expensive operations

## Code Quality and Conventions

### Notebook Standards
- Each notebook includes clear markdown documentation
- Code cells are well-commented in Korean/English
- Results include both code output and visualizations
- Follow the pattern: theory explanation → code implementation → results analysis

### File Naming Convention
- Daily practice files: `MMDD_Subject_Practice.ipynb`
- Summary files: `MMDD_Subject_Summary.md`
- Homework files: Located in `homework/` subdirectories

### Korean Font Setup (Required for Matplotlib)
All notebooks include this standard setup for Korean text display:
```python
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'Malgun Gothic'  # Windows Korean font
plt.rcParams['axes.unicode_minus'] = False     # Fix minus sign display
```

### Standard Import Patterns
```python
# Core data manipulation
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Machine learning
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix

# Deep learning (TensorFlow primary)
import tensorflow as tf
from tensorflow import keras

# Utilities
import warnings
warnings.filterwarnings('ignore')
```

## Documentation

### Comprehensive Guides (99_etc/docs/)
The repository includes extensive documentation:
- **Python_Complete_Guide.md**: Complete Python reference covering fundamentals to advanced topics

### Additional Learning Resources (99_etc/ipynb/)
- **Selenium_Tutorial_Integrated.ipynb**: Web automation and testing with Selenium
- **Web_Crawing_Guide.ipynb**: Web scraping techniques and best practices

### Learning Summaries
Each module includes daily summary files documenting:
- Key concepts learned
- Important code patterns
- Problem-solving approaches
- Project outcomes and lessons learned

## Best Practices

### Working with Notebooks
- Always run cells in order
- Use markdown cells for explanations and section headers
- Include visualizations for data analysis
- Save intermediate results when working with large datasets
- **Always activate sesac_ai environment before running notebooks**

### Data Science Workflow
1. **Data Loading**: Use pandas for CSV, numpy for arrays
2. **Data Exploration**: Statistical summaries and visualizations
3. **Preprocessing**: Handle missing values, scaling, encoding
4. **Modeling**: Use scikit-learn for ML, TensorFlow for DL
5. **Evaluation**: Comprehensive metrics and visualizations
6. **Documentation**: Record findings and insights

### Environment Management
- Use the conda environment for all development
- Install additional packages through conda when possible
- Document any new dependencies
- Keep environment files updated

### Working with Large Datasets
- Image datasets in `07_Deep_Learning/data/` are several GB
- Use `tensorflow.data.Dataset` or generators for memory efficiency
- Consider using `--load-latest` for model checkpoints
- Save models in appropriate format (.h5 for TensorFlow, .pth for PyTorch)

## Troubleshooting

### Common Issues
- **Java not found**: Ensure JAVA_HOME is set for KoNLPy
- **MySQL connection errors**: Check if MySQL server is running
- **Memory issues**: Use data chunking for large datasets
- **Package conflicts**: Use conda environment isolation
- **Windows-specific**: May need Visual Studio Build Tools for some packages

### Performance Considerations
- Use vectorized operations in numpy/pandas
- Enable GPU for TensorFlow/PyTorch if available
- Use data generators for large image datasets
- Consider memory usage when loading multiple large files

## Development Patterns & Conventions

### Notebook Development Workflow
This repository follows a specific **learning-centered development pattern**:

1. **Daily Practice Structure**: Each learning day creates numbered practice files
   ```
   MMDD_Subject_Practice_N.ipynb  # N = 1,2,3,4 for multiple sessions per day
   ```

2. **Theoretical Documentation**: Corresponding markdown summaries
   ```
   MMDD_Subject_Summary.md        # Daily theoretical notes and key concepts
   ```

3. **Progressive Complexity**: Later-dated notebooks build on earlier concepts
   - Early notebooks (0423-0430): Python basics
   - Mid-term notebooks (0701-0710): ML fundamentals  
   - Advanced notebooks (0717-0725): Deep learning applications

### Data Science Code Patterns

#### Standard Import Block
All data science notebooks follow this import convention:
```python
# Core data manipulation
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Machine learning
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix

# Deep learning (TensorFlow primary)
import tensorflow as tf
from tensorflow import keras

# Utilities
import warnings
warnings.filterwarnings('ignore')
```

#### Model Development Pattern
1. **Data Loading & EDA**: Explore data characteristics and distributions
2. **Preprocessing Pipeline**: Scaling, encoding, train/test splits
3. **Model Implementation**: Start simple, then increase complexity
4. **Evaluation & Visualization**: Comprehensive metrics and plots
5. **Model Persistence**: Save models and results for later reference

#### Deep Learning Architecture Pattern
```python
# Standard CNN architecture used across image classification projects
model = Sequential([
    Conv2D(32, (3,3), activation='relu', input_shape=(180,180,3)),
    MaxPooling2D(2,2),
    Conv2D(64, (3,3), activation='relu'),
    MaxPooling2D(2,2),
    Conv2D(128, (3,3), activation='relu'),
    MaxPooling2D(2,2),
    Flatten(),
    Dropout(0.5),
    Dense(512, activation='relu'),
    Dense(num_classes, activation='softmax')  # or 'sigmoid' for binary
])
```

#### Notebook Content Structure Pattern
Notebooks in this repository follow a specific educational structure:
```python
# 1. Comprehensive headers with table of contents
# 머신러닝을 위한 NumPy & Pandas 완전 가이드
## 목차
1. [NumPy 기초](#1-numpy-기초)
2. [NumPy 배열 연산](#2-numpy-배열-연산)
...

# 2. Korean font setup for matplotlib (consistent across all notebooks)
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

# 3. Educational progression with emoji markers
print("🔍 행렬 정보")  # Investigation/Analysis
print("📊 기초 통계량")  # Statistics/Data
print("🎯 실습 문제")   # Practice/Exercise
print("⚡ 방법 2")      # Optimization/Performance

# 4. Bilingual documentation (Korean + English)
# Korean explanations for concepts, English for technical terms
```

### Django Development Patterns

#### URL Configuration Pattern
Each Django project uses **hierarchical URL routing**:
```python
# config/urls.py (project-level)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('guestbook/', include('guestbook.urls')),
    path('score/', include('score.urls')),
]

# app/urls.py (app-level)
urlpatterns = [
    path('', views.list_view, name='list'),
    path('write/', views.write_view, name='write'),
    path('view/<int:pk>/', views.detail_view, name='view'),
]
```

#### Model-Form-View Pattern
Consistent MVC implementation across all Django apps:
```python
# models.py - Data layer
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

# forms.py - Form handling  
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']

# views.py - Business logic
def write_view(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        form = PostForm()
    return render(request, 'blog/write.html', {'form': form})
```

### FastAPI Development Patterns

#### FastAPI Project Structure
FastAPI projects in this repository follow a modular router-based architecture:
```python
# main.py - Application entry point
app = FastAPI(
    title="Board API",
    description="게시판 및 성적 관리 API 서버",
    version="1.0.0"
)

# CORS configuration for frontend integration
ALLOWED_ORIGINS = [
    "http://127.0.0.1:5173",  # Vite dev server
    "http://localhost:5173",
    "http://www.sessac.com:5173"
]

# Router organization
app.include_router(board.router)
app.include_router(score.router)
# or predict.router for ML integration

# routers/board.py - Feature-specific routing
router = APIRouter(prefix="/board", tags=["board"])

@router.get("/list")
def get_board_list():
    # Implementation
    pass

@router.post("/insert")
def create_board_post():
    # Implementation
    pass
```

### File Organization Best Practices

#### Data File Management
- **CSV files**: Stored in module-specific `data/csv/` directories
- **Large datasets**: Separate `data/` directories per module
- **Processed data**: Use `.npy`/`.npz` for NumPy arrays to save space
- **Model artifacts**: Save in `data/models/` or similar subdirectories

#### Code Organization
- **Homework separation**: Use `homework/` subdirectories for assignments
- **Date-based organization**: Enables easy tracking of learning progression
- **Consistent naming**: Follow `MMDD_Subject_Practice.ipynb` pattern

### Database Connection Patterns

#### MySQL Integration
Standard pattern used across MySQL-related projects:
```python
import pymysql
from DBUtils.PooledDB import PooledDB

# Connection pool setup (recommended for production)
pool = PooledDB(
    creator=pymysql,
    maxconnections=10,
    host='localhost',
    user='username',
    password='password',
    database='dbname',
    charset='utf8'
)

# Usage pattern
def execute_query(sql, params=None):
    conn = pool.connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute(sql, params)
            return cursor.fetchall()
    finally:
        conn.close()
```

### Testing and Validation Patterns

#### Model Evaluation Standard
All ML/DL projects follow this evaluation pattern:
```python
# Model evaluation pipeline
def evaluate_model(model, X_test, y_test):
    predictions = model.predict(X_test)
    
    # Classification metrics
    print(classification_report(y_test, predictions))
    
    # Confusion matrix
    cm = confusion_matrix(y_test, predictions)
    sns.heatmap(cm, annot=True, fmt='d')
    plt.show()
    
    # Save results
    return {
        'accuracy': accuracy_score(y_test, predictions),
        'confusion_matrix': cm
    }
```