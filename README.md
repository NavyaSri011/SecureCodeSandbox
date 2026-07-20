# SecureCodeSandbox

A secure, Docker-powered online code execution platform that enables users to write, compile, and execute code in multiple programming languages inside isolated containers.

Built using React, FastAPI, and Docker, the application focuses on secure execution, resource isolation, and a clean developer experience.

---

## Features

- Secure code execution using Docker containers
- Isolated execution environment
- Internet access disabled during execution
- Multi-language support
  - Python
  - C
  - C++
  - Java
- Upload source code files
- Interactive code editor
- Copy output with one click
- Execution time display
- Compiler and runtime error handling
- Modern dark-themed interface
- Resource limits for secure execution

---

## Tech Stack

### Frontend

- React.js
- Vite
- JavaScript (ES6+)
- CSS3
- Axios

### Backend

- FastAPI
- Python
- Docker

---

## Project Structure

```
SecureCodeSandbox
│
├── backend
│   ├── compiler.py
│   ├── config.py
│   ├── docker_runner.py
│   ├── executor.py
│   ├── file_manager.py
│   ├── main.py
│   ├── models.py
│
├── frontend
│   ├── index.html
│   ├── package.json
│   ├── package-lock.json
│   ├── vite.config.js
│   │
│   └── src
│       ├── App.jsx
│       ├── main.jsx
│       ├── index.css
│       │
│       ├── components
│       │   ├── CodeEditor.jsx
│       │   ├── CodeEditor.css
│       │   ├── FileUpload.jsx
│       │   ├── FileUpload.css
│       │   ├── InputBox.jsx
│       │   ├── InputBox.css
│       │   ├── LanguageSelector.jsx
│       │   ├── LanguageSelector.css
│       │   ├── Navbar.jsx
│       │   ├── Navbar.css
│       │   ├── Output.jsx
│       │   ├── Output.css
│       │   ├── SecurityPanel.jsx
│       │   └── SecurityPanel.css
│       │
│       ├── services
│       │   └── api.js
│       │
│       └── styles
│           ├── App.css
│           └── Theme.css
│
└── README.md
```

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/<your-username>/SecureCodeSandbox.git
cd SecureCodeSandbox
```

### Backend Setup

Create a virtual environment:

```bash
python -m venv venv
```

Activate it:

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Start the backend:

```bash
uvicorn main:app --reload
```

### Frontend Setup

Navigate to the frontend directory:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Run the development server:

```bash
npm run dev
```

---

## Docker Requirements

Ensure Docker Desktop is installed and running before executing code.

Each program executes inside an isolated Docker container with:

- No internet access
- Limited CPU usage
- Limited memory allocation
- Automatic container removal after execution
- Temporary file cleanup

---

## Security Features

- Docker container isolation
- Network access disabled
- CPU and memory limits
- Temporary file management
- Secure execution environment
- Runtime error handling
- Automatic cleanup after execution

---

## Supported Languages

| Language | Support |
|----------|---------|
| Python   | Yes     |
| C        | Yes     |
| C++      | Yes     |
| Java     | Yes     |

---

## Future Enhancements

- Interactive terminal
- User authentication
- Code history
- Theme customization
- Multiple file support
- AI-powered code suggestions
- Execution history
- Collaborative coding
- Code sharing

---

## Author

Developed as a secure code execution sandbox project using React, FastAPI, and Docker.

---

## License

This project is licensed under the MIT License.
