import "./Navbar.css";

function Navbar({ darkMode, setDarkMode }) {
  return (
    <nav className="navbar">

      <div className="navbar-left">
        <h1>Secure Code Sandbox</h1>
        <p>Execute code safely inside isolated containers.</p>
      </div>

      <div className="navbar-right">

        <span className="theme-label">
          Appearance
        </span>

        <span className="mode-text">
          {darkMode ? "Dark" : "Light"}
        </span>

        <label className="switch">
          <input
            type="checkbox"
            checked={darkMode}
            onChange={() => setDarkMode(!darkMode)}
          />
          <span className="slider"></span>
        </label>

      </div>

    </nav>
  );
}

export default Navbar;