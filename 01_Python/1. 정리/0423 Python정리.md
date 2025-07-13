# 🐍 파이썬(Python) 기초 개념 설명서

##### 🗓️ 2025.04.23
##### 📝 Writer : Moon19ht

---

## 📚 목차

1. [파이썬(Python)이란?](#1-파이썬python이란)
2. [파이썬의 특징](#2-파이썬의-특징)
3. [파이썬 설치](#3-파이썬-설치)

---

## 1. 파이썬(Python)이란?

> 파이썬은 다양한 프로그래밍 언어 중 하나입니다.
> 사람이 읽고 쓰기 쉬운 문법을 가진 프로그래밍 언어입니다.  
> 웹 개발, 데이터 분석, 인공지능(AI) 등 다양한 분야에서 널리 사용됩니다.

---

## 2. 파이썬의 특징

**1. 쉬운 사용성과 높은 가독성**
- 문법이 간결하고 직관적이라 초보자도 쉽게 배울 수 있습니다.
- 들여쓰기 기반 구조로 코드 가독성이 탁월합니다.

**2. 유연한 활용성과 확장성**
- 웹, 데이터 과학, 인공지능, 자동화 등 다양한 분야에 사용 가능합니다.
- 객체지향, 함수형 등 여러 프로그래밍 스타일을 지원합니다.
- C/C++ 등 다른 언어와도 쉽게 연동할 수 있습니다.

**3. 강력한 생태계와 도구 지원**
- 방대한 표준 라이브러리와 pip 패키지 시스템 제공
- TensorFlow, Pandas, Flask 등 다양한 프레임워크 지원
- 활발한 커뮤니티와 학습 자료가 풍부합니다.

---

## 3. 파이썬 설치

## Windows 11 환경에서 Python 설치 및 설정

### 1. Python 설치

#### 1.1 Python 다운로드
- 공식 사이트: [https://www.python.org/downloads/](https://www.python.org/downloads/)
- "Download Python 3.x.x" 버튼 클릭 (최신 버전 권장)

#### 1.2 설치 진행
1. 설치 파일 실행
2. 반드시 체크: `Add Python 3.x to PATH` 체크박스 활성화 (체크하지 않으면 명령어 인식이 안 될 수 있음)
3. "Customize installation" → 기본 옵션 그대로 유지
4. "Install for all users" 체크 (권장)
5. 설치 완료 후 "Disable path length limit" 선택

#### 1.3 설치 확인 및 pip 업그레이드
```bash
python --version
pip --version
python -m pip install --upgrade pip
```

#### 1.4 `py` 명령어를 통한 버전 확인 및 실행
```bash
py --version
py -3.10
py -3.10 -m venv myenv
```
> `py`는 Windows Python Launcher로 여러 버전 관리에 유리합니다. 설치된 Python 버전에 맞게 `-3.10` 등 버전 숫자를 조정하세요.

---

### 2. PowerShell에서 가상환경 활성화
```powershell
.\myenv\Scripts\Activate.ps1
```
> PowerShell에서는 `activate.bat` 대신 `Activate.ps1`을 사용해야 합니다.

- 비활성화: `deactivate`

---

### 3. Visual Studio Code 연동

#### 3.1 VS Code 설치
- 다운로드: [https://code.visualstudio.com/](https://code.visualstudio.com/)

#### 3.2 필수 확장 설치
- Python Extension (ms-python.python)
- Pylance (ms-python.vscode-pylance)

#### 3.3 인터프리터 선택
- `Ctrl+Shift+P` → `Python: Select Interpreter` → 가상환경(venv) 선택
- `.venv` 폴더가 프로젝트 루트에 있으면 자동 인식, 없으면 수동 선택

#### 3.4 VS Code 인터프리터 인식 문제 해결
- `Ctrl+Shift+P` → `Python: Refresh Interpreter List` 실행
- 그래도 안 보일 경우, VS Code를 재시작
- 가상환경이 인식되지 않으면 VS Code를 가상환경이 위치한 폴더에서 실행하거나, Python 확장 재설치

---

### 4. Anaconda 설치

#### 4.1 Anaconda 다운로드
- 공식 페이지: [https://www.anaconda.com/products/distribution](https://www.anaconda.com/products/distribution)

#### 4.2 설치 옵션
- "Just Me" 또는 "All Users" 선택
- "Add Anaconda to my PATH environment variable" 체크 안 함 (권장)
- 설치 후 `Anaconda Prompt` 실행

#### 4.3 Conda 설치 확인 및 초기화
```bash
conda --version
conda init
```
> PowerShell, bash 등에서 `conda activate` 명령을 쓰기 위해 필요. 실행 후 터미널 재시작 필수

#### 4.4 Anaconda Navigator 및 Jupyter 사용
- GUI로 환경 관리: `Anaconda Navigator` 실행
- 노트북 실행: `jupyter notebook` 또는 Navigator 내 실행

##### Miniconda 설치 (가벼운 대안)

Anaconda가 너무 무겁다면 Miniconda를 사용할 수 있습니다.

1. [Miniconda 공식 사이트](https://docs.conda.io/en/latest/miniconda.html)에서 다운로드
2. 설치 파일 실행 후 기본 설정으로 설치
3. 설치 완료 후 `Anaconda Prompt (miniconda3)` 실행

---

### 5. Conda 환경 생성 및 사용

```bash
conda create -n mycondaenv python=3.10
conda activate mycondaenv
```

- 환경 목록 확인: `conda env list`
- 환경 제거: `conda remove --name mycondaenv --all`

---

### 6. VS Code에서 Conda 환경 연동

1. `Anaconda Prompt`에서 `code` 명령어 사용하려면:
```bash
conda install -c anaconda vscode
```
2. VS Code에서 `Ctrl+Shift+P` → `Python: Select Interpreter`로 conda 환경 선택

---

### 7. PATH 및 환경변수 확인

```bash
where python
where conda
```

- `python`, `pip`, `conda` 명령어가 인식되지 않으면 `환경 변수 편집`에서 `Path`에 다음 추가:
  - Python: `C:\Users\<UserName>\AppData\Local\Programs\Python\Python3x\`
  - Conda
    - `C:\Users\<UserName>\anaconda3\Scripts\`
    - `C:\Users\<UserName>\anaconda3\Library\bin\`
    - `C:\Users\<UserName>\anaconda3\`
- 환경변수 변경 후에는 터미널/명령 프롬프트를 반드시 재시작

---

### 8. 설치 완료 후 테스트 및 패키지 설치

```bash
python -m pip install --upgrade pip
python -m pip install numpy pandas matplotlib
conda list
```

---

## MacOS 환경에서 Python 설치 및 설정

### 1. Xcode Command Line Tools 설치

```bash
xcode-select --install
```

### 2. Homebrew 설치 (이미 설치되어 있다면 생략)

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

### 3. Python 설치

```bash
brew install python
```

### 4. 버전 확인 및 pip 업그레이드

```bash
python3 --version
pip3 --version
pip3 install --upgrade pip
```

### 5. 가상환경 설정 (venv)

```bash
python3 -m venv myenv
source myenv/bin/activate  # 가상환경 활성화
deactivate                 # 가상환경 비활성화
```

> Mac에서는 기본적으로 `python`이 아니라 `python3` 명령어를 사용합니다. (구버전 Mac은 python이 2.x일 수 있음)

---

## Ubuntu 환경에서 Python 설치 및 설정

### 1. 시스템 패키지 업데이트

```bash
sudo apt update && sudo apt upgrade -y
```

### 2. Python 및 pip 설치

```bash
sudo apt install python3 python3-pip -y
```

### 3. 버전 확인 및 pip 업그레이드

```bash
python3 --version
pip3 --version
pip3 install --upgrade pip
```

### 4. 가상환경 설정 (venv)

```bash
sudo apt install python3-venv -y
python3 -m venv myenv
source myenv/bin/activate  # 가상환경 활성화
deactivate                 # 가상환경 비활성화
```

> Ubuntu에서도 기본적으로 `python3`, `pip3` 명령어를 사용합니다.

---

### 5. 추천 추가 설정

- Visual Studio Code 설치 및 Python 확장 설치
- `requirements.txt`로 패키지 관리

```bash
pip3 freeze > requirements.txt
pip3 install -r requirements.txt
```

---

## Arch Linux 환경에서 Python 설치 및 설정

### 1. 시스템 업데이트

```bash
sudo pacman -Syu
```

시스템을 최신 상태로 유지합니다.

---

### 2. Python 설치

```bash
sudo pacman -S python
```

기본적으로 설치되는 버전은 최신 안정화 버전입니다.

설치 후 버전 확인:

```bash
python --version
```

또는

```bash
python3 --version
```

---

### 3. pip 설치 및 확인

`pip`는 Python 패키지 관리자입니다.

Arch의 Python 패키지에 기본 포함되어 있어 다음과 같이 확인할 수 있습니다:

```bash
pip --version
```

만약 동작하지 않을 경우 아래 명령으로 설치:

```bash
sudo pacman -S python-pip
```

---

### 4. Python 버전별 설치 (옵션)

특정 버전이 필요하다면 `pyenv` 사용을 추천합니다.

#### pyenv 설치

```bash
sudo pacman -S pyenv
```

또는 `yay` 사용 시:

```bash
yay -S pyenv
```

#### pyenv 초기화 (zsh 예시)

```bash
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
echo 'command -v pyenv >/dev/null && eval "$(pyenv init -)"' >> ~/.zshrc
source ~/.zshrc
```

#### 특정 버전 설치 예시

```bash
pyenv install 3.11.9
pyenv global 3.11.9
```

---

### 5. 가상환경 설정 (venv)

프로젝트별 독립 환경 구성을 위해 `venv` 사용:

```bash
python -m venv venv
source venv/bin/activate
```

비활성화는 다음과 같이:

```bash
deactivate
```

---

### 6. 추가 도구 및 추천 패키지

| 패키지명     | 설명                                | 설치 명령어                        |
|--------------|-------------------------------------|------------------------------------|
| `ipython`    | 대화형 셸                          | `sudo pacman -S ipython`           |
| `jupyter`    | 노트북 환경                         | `pip install notebook`             |
| `black`      | 코드 포매터                         | `pip install black`                |
| `pylint`     | 정적 분석                           | `pip install pylint`               |
| `virtualenv` | 가상환경 생성 툴                    | `pip install virtualenv`           |

---

## [실무 TIP] 환경 관리 도구 비교

- **venv**: Python 표준 가상환경 도구. 가볍고 기본 제공. 프로젝트별 독립 환경에 적합.
- **conda**: 데이터 과학, 과학 컴퓨팅에 강점. 패키지/환경 관리가 편리. 대용량 패키지 설치에 유리.
- **pyenv**: 여러 Python 버전 관리에 특화. 시스템에 여러 버전이 필요한 경우 유용.

---

## [실무 TIP] 자주 발생하는 문제와 해결법

- PATH 문제로 python/pip/conda 명령어가 인식되지 않을 때: 환경변수 편집 후 터미널 재시작
- VS Code에서 가상환경이 안 잡힐 때: Python 확장 설치, 인터프리터 수동 선택, 폴더 위치 확인
- pip 업그레이드 후에도 패키지 설치가 안 될 때: 관리자 권한으로 실행, 또는 `python -m pip install --user 패키지명` 사용
- Mac/Linux에서 python과 python3 혼동 주의: 항상 python3, pip3 사용 권장
