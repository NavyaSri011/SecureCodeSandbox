import "./InputBox.css";

function InputBox({ input, setInput }) {
  return (
    <div className="input-container">

      <h3>Program Input</h3>

      <textarea
        placeholder="Enter input for your program..."
        value={input}
        onChange={(e) => setInput(e.target.value)}
      />

    </div>
  );
}

export default InputBox;