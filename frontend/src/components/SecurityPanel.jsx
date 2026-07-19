import "./SecurityPanel.css";

function SecurityPanel() {
  return (
    <div className="security-container">
      <h3>Security Features</h3>

      <div className="security-box">
        <ul>
          <li>Docker Container Isolation</li>
          <li>Network Access Disabled</li>
          <li>Memory Usage Limited (128 MB)</li>
          <li>CPU Usage Limited (0.5 Core)</li>
          <li>Execution Timeout (5 Seconds)</li>
          <li>Automatic Temporary File Cleanup</li>
          <li>Supports Python, Java, C and C++</li>
        </ul>
      </div>
    </div>
  );
}

export default SecurityPanel;