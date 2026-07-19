import Editor from "@monaco-editor/react";
import "./CodeEditor.css";

function CodeEditor({ language, code, setCode, darkMode }) {
  return (
    <div className="editor-container">

      <div className="editor-header">
        <h3>Code Editor</h3>
      </div>

      <Editor
        height="500px"
        language={language}
        value={code}
        theme={darkMode ? "vs-dark" : "light"}
        onChange={(value) => setCode(value || "")}
        options={{
          fontSize: 16,
          minimap: {
            enabled: false,
          },
          fontSize: 16,
          placeholder: "Write your code here...",
          automaticLayout: true,
          scrollBeyondLastLine: false,
          roundedSelection: true,
          wordWrap: "on",
        }}
      />

    </div>
  );
}

export default CodeEditor;