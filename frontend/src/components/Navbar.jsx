import "../App.css"
function Navbar({ isDarkMode, toggleTheme }) {
    return (
        <nav className="navbar">

            <div className="nav-container">

                <h2 className="logo">
                    My Portfolio
                </h2>

                 <div className="nav-right">

                        <div className="nav-links">
                            <a href="#about">About</a>
                            <a href="#skills">Skills</a>
                            <a href="#projects">Projects</a>
                            <a href="#experience">Experience</a>
                            <a href="#education">Education</a>
                            <a href="#contact">Contact</a>
                        </div>

                      <button
                        className={`theme-toggle ${
                            isDarkMode ? "dark-toggle" : ""
                        }`}
                        onClick={toggleTheme}
                        aria-label="Toggle theme"
                    >
                        <span className="toggle-icon">
                            {isDarkMode ? "🌙" : "☀️"}
                        </span>
                    </button>


                 </div>

             

            </div>

        </nav>
    )
}

export default Navbar