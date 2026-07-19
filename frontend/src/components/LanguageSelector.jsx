import "./LanguageSelector.css";

function LanguageSelector({
  language,
  setLanguage,
  handleRun,
  handleClear,
  isRunning,
}) {
  return (
    <div className="toolbar">

      <div className="language-section">
        <label htmlFor="language">
          Language
        </label>

        <select
          id="language"
          value={language}
          onChange={(e) => setLanguage(e.target.value)}
        >
          <option value="python">Python</option>
          <option value="java">Java</option>
          <option value="c">C</option>
          <option value="cpp">C++</option>
        </select>
      </div>

      <div
        style={{
          display: "flex",
          gap: "10px",
        }}
      >
        <button
          className="clear-btn"
          onClick={handleClear}
        >
          Clear
        </button>

        <button
          className="run-btn"
          onClick={handleRun}
          disabled={isRunning}
        >
          {isRunning ? "⏳Running..." : "▶ Run Code"}
        </button>
      </div>

    </div>
  );
}

export default LanguageSelector;