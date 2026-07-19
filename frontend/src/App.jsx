import { useState } from "react";
import API from "./services/api";

import Navbar from "./components/Navbar";
import LanguageSelector from "./components/LanguageSelector";
import CodeEditor from "./components/CodeEditor";
import InputBox from "./components/InputBox";
import Output from "./components/Output";
import SecurityPanel from "./components/SecurityPanel";
import FileUpload from "./components/FileUpload";

import "./styles/theme.css";
import "./styles/App.css";

function App() {
  const [darkMode, setDarkMode] = useState(true);

  const [language, setLanguage] = useState("python");

  const [code, setCode] = useState('print("Hello, World!")');

  const [input, setInput] = useState("");

  const [output, setOutput] = useState("");

  const [executionTime, setExecutionTime] = useState("");

  const [isRunning, setIsRunning] = useState(false);

  // Clear Editor, Input and Output
  const handleClear = () => {
    setCode("");
    setInput("");
    setOutput("");
    setExecutionTime("");
  };

  // Run Code
  const handleRun = async () => {
    setIsRunning(true);

    try {
      const response = await API.post("/run", {
        language,
        code,
        input,
      });

      const result = response.data;

      if (result.error) {
        setOutput(`Error:\n${result.error}`);
      } else {
        setOutput(result.output);
      }

      setExecutionTime(result.execution_time);
    } catch (error) {
      console.error(error);

      setOutput("Error connecting to backend.");

      setExecutionTime("");
    } finally {
      setIsRunning(false);
    }
  };

  return (
    <div className={darkMode ? "dark app" : "light app"}>
      <Navbar
        darkMode={darkMode}
        setDarkMode={setDarkMode}
      />

      <div className="workspace">
        <LanguageSelector
          language={language}
          setLanguage={setLanguage}
          handleRun={handleRun}
          handleClear={handleClear}
          isRunning={isRunning}
        />

        <FileUpload
          setCode={setCode}
        />

        <CodeEditor
          language={language}
          code={code}
          setCode={setCode}
          darkMode={darkMode}
        />

        <div className="bottom-panels">
          <InputBox
            input={input}
            setInput={setInput}
          />

          <Output
            output={output}
            executionTime={executionTime}
          />

          <SecurityPanel />
        </div>
      </div>
    </div>
  );
}

export default App;