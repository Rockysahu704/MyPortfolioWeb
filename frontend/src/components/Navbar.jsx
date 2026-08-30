import "../App.css"
// import logo from "../assets/images/logo_dark_bg.png"

function Navbar({ isDarkMode, toggleTheme }) {
    return (
        <nav className="navbar">

            <div className="nav-container">

                {/* Logo + Name */}
                <a href="#about" className="brand">

                    {/* <img
                        src={logo}
                        alt="Rocky Sahu Logo"
                        className="brand-logo"
                    /> */}

                    <div className="brand-name">
                        <span className="first-name">
                            ROCKY
                        </span>

                        <span className="last-name">
                            SAHU
                        </span>
                    </div>

                </a>


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