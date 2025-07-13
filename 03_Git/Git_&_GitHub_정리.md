# 🛠️ Git & GitHub 설명서

##### 🗓️ 2025.05.22~23
##### 📝 Writer : Moon19ht

---

## 📚 목차

1. [Git 시작하기](#1-git-시작하기)
2. [Git 기본 사용법](#2-git-기본-사용법)
3. [브랜치(Branch) 관리](#3-브랜치branch-관리)
4. [GitHub 백업 및 협업](#4-github-백업-및-협업)
5. [GitHub 소통 및 문서화](#5-github-소통-및-문서화)
6. [오픈소스 프로젝트 참여](#6-오픈소스-프로젝트-참여)
7. [VSCode에서 Git 사용하기](#7-vscode에서-git-사용하기)
8. [팀 프로젝트 관리](#8-팀-프로젝트-관리)

---

## 1. Git 시작하기

### 1.1 Git이란?

**Git**은 2005년 리누스 토르발스가 개발한 분산 버전 관리 시스템입니다.

#### 주요 특징
- **버전 관리**: 소스 코드의 변경사항을 체계적으로 관리
- **분산형 시스템**: 중앙 서버 없이도 독립적인 작업 가능
- **협업 지원**: 여러 개발자가 동시에 작업할 수 있는 환경 제공

#### Git의 3가지 핵심 기능

1. **버전 관리(Version Control)**
   - 문서를 수정할 때마다 변경 이력을 추적
   - 이전 버전으로 언제든 되돌리기 가능

2. **백업(Backup)**
   - 원격 저장소(GitHub 등)를 통한 안전한 백업
   - 여러 위치에 데이터 보관 가능

3. **협업(Collaboration)**
   - 팀원들과 파일을 안전하게 공유
   - 누가, 언제, 무엇을 변경했는지 추적 가능

### 1.2 Git 설치하기

#### Windows
1. [https://git-scm.com](https://git-scm.com)에서 Git 다운로드
2. 설치 후 'Git Bash' 실행하여 확인

#### macOS
```bash
# Homebrew 설치
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Git 설치
brew install git
```

#### 설치 확인
```bash
git
```

### 1.3 Git 환경 설정

```bash
# 사용자 정보 설정 (필수)
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# 설정 확인
git config --list
```

### 1.4 기본 리눅스 명령어

Git을 효과적으로 사용하기 위해 알아야 할 기본 명령어들:

```bash
# 현재 디렉터리 경로 확인
pwd

# 파일 및 디렉터리 목록 보기
ls
ls -la  # 상세 정보 포함

# 디렉터리 이동
cd <directory_name>    # 하위 디렉터리로 이동
cd ..                  # 상위 디렉터리로 이동
cd ~                   # 홈 디렉터리로 이동

# 디렉터리 생성 및 삭제
mkdir <directory_name>
rm -r <directory_name>

# 화면 지우기
clear
```

### 1.5 Vim 에디터 기본 사용법

```bash
# 파일 열기/생성
vim filename.txt
```

#### Vim 모드 전환
- **입력 모드**: `A` 또는 `I` 키 (텍스트 입력 가능)
- **명령 모드**: `Esc` 키 (파일 저장/종료)

#### 주요 명령어
- `:w` - 저장
- `:q` - 종료
- `:wq` - 저장 후 종료
- `:q!` - 저장하지 않고 강제 종료

---

## 2. Git 기본 사용법

### 2.1 Git 저장소 만들기

```bash
# 새 프로젝트 디렉터리 생성
mkdir my-project
cd my-project

# Git 저장소 초기화
git init
```

### 2.2 Git의 3가지 영역

```
작업 트리(Working Tree) → 스테이지(Stage) → 저장소(Repository)
      ↓                       ↓                    ↓
   파일 수정              git add             git commit
```

- **작업 트리**: 실제 파일을 수정하는 공간
- **스테이지**: 커밋할 파일들이 대기하는 공간
- **저장소**: 버전 이력이 저장되는 공간

### 2.3 첫 번째 버전 만들기

```bash
# 1. 파일 생성 및 수정
vim hello.txt
# 내용 입력 후 저장

# 2. 파일 상태 확인
git status

# 3. 스테이지에 추가
git add hello.txt
# 또는 모든 파일 추가: git add .

# 4. 커밋 (버전 생성)
git commit -m "첫 번째 커밋"

# 5. 커밋 이력 확인
git log
```

### 2.4 유용한 Git 명령어

```bash
# 한 번에 스테이징과 커밋 (기존 파일만)
git commit -am "커밋 메시지"

# 변경 사항 확인
git diff

# 커밋 로그 한 줄로 보기
git log --oneline

# 상태 확인
git status
```

### 2.5 .gitignore 파일

특정 파일을 Git에서 제외하고 싶을 때 사용:

```bash
# .gitignore 파일 생성
vim .gitignore
```

```gitignore
# 로그 파일 제외
*.log

# 임시 파일 제외
temp/

# 특정 파일 제외
config.secret

# 현재 경로의 특정 파일만 제외
/local-config.txt
```

### 2.6 작업 되돌리기

```bash
# 작업 트리의 변경 사항 되돌리기
git restore <filename>

# 스테이징 취소
git restore --staged <filename>

# 최신 커밋 취소 (파일은 작업 트리에 유지)
git reset HEAD^

# 특정 커밋으로 되돌리기 (이후 커밋 삭제)
git reset --hard <commit_hash>

# 특정 커밋 취소 (새로운 커밋 생성)
git revert <commit_hash>
```

---

## 3. 브랜치(Branch) 관리

### 3.1 브랜치란?

브랜치는 독립적인 작업 공간을 만들어 주는 Git의 핵심 기능입니다.

```
main ──●──●──●──●
       │
       └──●──● feature
```

### 3.2 브랜치 기본 명령어

```bash
# 브랜치 목록 확인
git branch

# 새 브랜치 생성
git branch <branch_name>

# 브랜치 전환
git switch <branch_name>
# 또는: git checkout <branch_name>

# 브랜치 생성과 동시에 전환
git switch -c <branch_name>
```

### 3.3 브랜치 작업 실습

```bash
# 1. 새 브랜치 생성 및 전환
git switch -c feature-login

# 2. 작업 수행
vim login.py
git add login.py
git commit -m "로그인 기능 추가"

# 3. main 브랜치로 돌아가기
git switch main

# 4. 브랜치 병합
git merge feature-login
```

### 3.4 브랜치 정보 확인

```bash
# 모든 브랜치의 커밋 로그
git log --oneline --branches

# 브랜치 간 차이점 확인
git log main..feature-branch

# 브랜치 간 파일 차이
git diff main feature-branch
```

### 3.5 병합 충돌 해결

충돌이 발생하면 파일에 다음과 같은 표시가 나타납니다:

```markdown
<<<<<<< HEAD
현재 브랜치의 내용
=======
병합할 브랜치의 내용
>>>>>>> feature-branch
```

충돌 해결 방법:
1. 충돌 부분을 수동으로 수정
2. 충돌 마커(`<<<<<<<`, `=======`, `>>>>>>>`) 삭제
3. 파일 저장 후 커밋

```bash
git add <resolved_file>
git commit -m "충돌 해결"
```

---

## 4. GitHub 백업 및 협업

### 4.1 GitHub란?

GitHub는 Git 저장소를 위한 클라우드 호스팅 서비스입니다.

#### 주요 기능
- **원격 저장소 제공**: 코드를 온라인에 안전하게 보관
- **협업 도구**: 팀 프로젝트를 위한 다양한 기능
- **오픈소스 플랫폼**: 전 세계 개발자들과 코드 공유

### 4.2 GitHub 시작하기

1. [github.com](https://github.com)에서 계정 생성
2. 이메일 인증 완료
3. 새 저장소(Repository) 생성

### 4.3 원격 저장소 연결

```bash
# 원격 저장소 등록
git remote add origin https://github.com/username/repository.git

# 연결 확인
git remote -v

# 브랜치 이름 변경 (필요시)
git branch -M main
```

### 4.4 GitHub에 업로드 (Push)

```bash
# 처음 업로드
git push -u origin main

# 이후 업로드
git push
```

### 4.5 GitHub에서 다운로드 (Pull)

```bash
# 원격 저장소의 최신 변경사항 가져오기
git pull origin main

# 단축 명령 (이미 연결된 경우)
git pull
```

### 4.6 원격 저장소 복제 (Clone)

```bash
# 기존 저장소를 로컬로 복제
git clone https://github.com/username/repository.git

# 특정 폴더명으로 복제
git clone https://github.com/username/repository.git my-folder
```

### 4.7 협업 워크플로우

```bash
# 1. 최신 코드 받기
git pull origin main

# 2. 새 브랜치에서 작업
git switch -c feature-new-function

# 3. 작업 후 커밋
git add .
git commit -m "새 기능 추가"

# 4. 원격에 브랜치 푸시
git push origin feature-new-function

# 5. GitHub에서 Pull Request 생성
# (웹 인터페이스에서 진행)
```

---

## 5. GitHub 소통 및 문서화

### 5.1 README 파일 작성

README.md는 프로젝트의 첫인상을 결정하는 중요한 파일입니다.

```markdown
# 프로젝트 이름

프로젝트에 대한 간단한 설명을 여기에 작성합니다.

## 설치 방법

```bash
npm install
```

## 사용법

```python
python main.py
```

## 기여 방법

1. 이 저장소를 포크합니다
2. 새 브랜치를 만듭니다
3. 변경사항을 커밋합니다
4. Pull Request를 생성합니다

## 라이선스

MIT License
```

### 5.2 마크다운 문법

#### 제목
```markdown
# 첫 번째 제목 (가장 큰 제목)
## 두 번째 제목
### 세 번째 제목
#### 네 번째 제목
##### 다섯 번째 제목
###### 여섯 번째 제목 (가장 작은 제목)
```

#### 텍스트 강조
```markdown
**굵은 글씨**
*기울임 글씨*
***굵은 기울임***
~~취소선~~
```

#### 목록
```markdown
# 순서 있는 목록
1. 첫 번째 항목
2. 두 번째 항목
3. 세 번째 항목

# 순서 없는 목록
- 항목 1
- 항목 2
  - 하위 항목 2-1
  - 하위 항목 2-2
- 항목 3
```

#### 코드
```markdown
# 인라인 코드
`console.log("Hello World")`

# 코드 블록
```python
def hello_world():
    print("Hello, World!")
```
```

#### 링크 및 이미지
```markdown
# 링크
[GitHub](https://github.com)
<https://github.com>

# 이미지
![대체 텍스트](image.png)
```

#### 표
```markdown
| 이름 | 나이 | 직업 |
|------|------|------|
| 홍길동 | 25 | 개발자 |
| 김철수 | 30 | 디자이너 |
```

#### 구분선
```markdown
---
***
```

### 5.3 GitHub 프로필 관리

#### 컨트리뷰션 그래프
- 매일의 GitHub 활동을 시각적으로 표시
- 초록색이 진할수록 많은 활동을 의미
- 꾸준한 활동으로 개발 포트폴리오 구축 가능

---

## 6. 오픈소스 프로젝트 참여

### 6.1 오픈소스 프로젝트 기여 과정

1. **Fork**: 원본 저장소를 본인 계정으로 복사
2. **Clone**: 포크한 저장소를 로컬로 복제
3. **Branch**: 새로운 기능을 위한 브랜치 생성
4. **Commit**: 변경사항을 커밋
5. **Push**: 본인의 GitHub 저장소에 푸시
6. **Pull Request**: 원본 저장소에 병합 요청

### 6.2 실습: 오픈소스 프로젝트 기여하기

```bash
# 1. GitHub에서 프로젝트 Fork 후 Clone
git clone https://github.com/your-username/forked-project.git
cd forked-project

# 2. 새 브랜치 생성
git switch -c fix-bug-123

# 3. 코드 수정
vim file.py

# 4. 변경사항 커밋
git add .
git commit -m "Fix bug #123: 상세한 설명"

# 5. 본인 저장소에 푸시
git push origin fix-bug-123

# 6. GitHub에서 Pull Request 생성
```

### 6.3 Pull Request 작성 요령

#### 좋은 PR 제목
```
Fix: 로그인 버튼 클릭 시 오류 수정
Add: 사용자 프로필 편집 기능 추가
Update: README에 설치 가이드 추가
```

#### 좋은 PR 설명
```markdown
## 변경사항
- 로그인 버튼 클릭 시 발생하는 null pointer exception 수정
- 입력 유효성 검사 로직 추가

## 테스트
- [ ] 로그인 성공 케이스 테스트
- [ ] 로그인 실패 케이스 테스트
- [ ] 빈 입력값 테스트

## 관련 이슈
Fixes #123
```

---

## 7. VSCode에서 Git 사용하기

### 7.1 VSCode Git 설정

#### GitHub 계정 연동
1. VSCode에서 GitHub 확장 설치
2. `Ctrl + Shift + P` → "GitHub: Sign in"
3. 브라우저에서 인증 완료

### 7.2 VSCode에서 Git 기본 작업

#### 저장소 초기화
```bash
# 터미널에서
git init
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

#### Source Control 패널 사용
1. **변경사항 확인**: Source Control 패널에서 수정된 파일 확인
2. **스테이징**: 파일 옆 `+` 버튼 클릭
3. **커밋**: 커밋 메시지 입력 후 `Ctrl + Enter`
4. **푸시**: `...` 메뉴에서 "Push" 선택

#### 브랜치 관리
- 하단 상태바에서 현재 브랜치 확인
- 브랜치명 클릭으로 브랜치 전환
- `Ctrl + Shift + P` → "Git: Create Branch"

### 7.3 VSCode Git 확장 기능

#### GitLens 확장
- 코드 작성자 정보 표시
- 커밋 히스토리 시각화
- 블레임(blame) 정보 제공

#### Git History 확장
- 그래픽 커밋 히스토리
- 브랜치 시각화
- 파일별 변경 이력

---

## 8. 팀 프로젝트 관리

### 8.1 팀장 역할

#### 저장소 설정
1. **새 저장소 생성**
2. **브랜치 보호 규칙 설정**
   - Settings → Branches → Add rule
   - "Require pull request reviews before merging" 체크
   - "Require status checks to pass" 체크

3. **팀원 초대**
   - Settings → Collaborators → Add people

#### 초기 프로젝트 설정
```bash
# 1. 프로젝트 초기화
mkdir team-project
cd team-project
git init

# 2. 초기 파일 생성
echo "# Team Project" > README.md
git add .
git commit -m "Initial commit"

# 3. 원격 저장소 연결
git branch -M main
git remote add origin https://github.com/username/team-project.git
git push -u origin main
```

### 8.2 팀원 역할

#### 프로젝트 참여
```bash
# 1. 저장소 클론
git clone https://github.com/team/project.git
cd project

# 2. 본인 브랜치 생성
git switch -c feature/member-name

# 3. 작업 수행
# ... 코드 작성 ...

# 4. 커밋 및 푸시
git add .
git commit -m "기능 구현: 상세 설명"
git push origin feature/member-name

# 5. Pull Request 생성 (GitHub에서)
```

### 8.3 협업 워크플로우

#### Git Flow 전략
```
main (배포용)
├── develop (개발용)
    ├── feature/login (기능 개발)
    ├── feature/payment (기능 개발)
    └── hotfix/bug-fix (긴급 수정)
```

#### 일반적인 작업 과정
```bash
# 1. 최신 코드 동기화
git switch main
git pull origin main

# 2. 새 기능 브랜치 생성
git switch -c feature/new-feature

# 3. 작업 및 커밋
git add .
git commit -m "새 기능 추가"

# 4. 정기적으로 main과 동기화
git switch main
git pull origin main
git switch feature/new-feature
git merge main

# 5. 작업 완료 후 푸시
git push origin feature/new-feature

# 6. Pull Request 생성 및 코드 리뷰
```

### 8.4 코드 리뷰 프로세스

#### Pull Request 검토사항
- [ ] 코드가 요구사항을 만족하는가?
- [ ] 코딩 스타일이 일관적인가?
- [ ] 테스트가 포함되어 있는가?
- [ ] 문서가 업데이트되었는가?
- [ ] 성능에 영향을 미치지 않는가?

#### 리뷰 댓글 작성 요령
```
# 좋은 예
"이 함수는 너무 길어 보입니다. 더 작은 함수로 분리하는 것은 어떨까요?"

# 나쁜 예
"이 코드는 틀렸습니다."
```

---

## 마무리

Git과 GitHub는 현대 소프트웨어 개발에서 필수적인 도구입니다. 이 가이드를 통해 다음과 같은 능력을 기를 수 있습니다:

### 기본 역량
- ✅ Git의 기본 개념과 명령어 이해
- ✅ 버전 관리 시스템 활용
- ✅ 브랜치를 통한 병렬 개발

### 협업 역량
- ✅ GitHub를 통한 코드 공유
- ✅ Pull Request 프로세스 이해
- ✅ 코드 리뷰 참여

### 고급 활용
- ✅ 오픈소스 프로젝트 기여
- ✅ 팀 프로젝트 관리
- ✅ 개발 도구 통합 (VSCode)

### 추가 학습 리소스

- **공식 문서**: [git-scm.com](https://git-scm.com/doc)
- **GitHub 가이드**: [GitHub Learning Lab](https://lab.github.com/)
- **실습 사이트**: [learngitbranching.js.org](https://learngitbranching.js.org/)

---

> 💡 **팁**: Git과 GitHub 사용법은 실습을 통해 익혀야 합니다. 작은 프로젝트부터 시작하여 점차 복잡한 협업 프로젝트에 참여해보세요!

