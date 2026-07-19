import "./Output.css";
import { useState } from "react";

function Output({ output, executionTime }) {

  const [copied, setCopied] = useState(false);

  const isError = output?.startsWith("Error:");

  const copyOutput = () => {
    navigator.clipboard.writeText(output || "");

    setCopied(true);

    setTimeout(() => {
      setCopied(false);
    }, 1500);
  };

  return (
    <div className="output-container">

      <h3>Output</h3>

      <div className={isError ? "output-box error" : "output-box"}>

        <button className="copy-btn" onClick={copyOutput}>
          {copied ? "✓" : "⧉"}
        </button>

        <pre>
          {output || "Program output will appear here..."}
        </pre>

      </div>


      <div className="output-info">

        <div>
          <span>Execution Time :</span>
          <br />
          {executionTime || "0"} s
        </div>

        <div>
          <span>Status :</span>
          <br />
          {isError ? "Failed" : "Success"}
        </div>

      </div>

    </div>
  );
}

export default Output;