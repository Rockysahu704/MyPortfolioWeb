import "../App.css"
function Hero() {
    return (
        <section id="home" className="hero-section">

            <div className="hero-content">

                <p className="hero-greeting">
                    Hello, I'm
                </p>

                <h1>
                    Rocky Sahu
                </h1>

                <h2>
                    Python Full Stack Developer
                </h2>

                <p className="hero-description">
                    I build web applications using Python,
                    Django, React, and modern web technologies.
                </p>

                <div className="hero-buttons">

                    <a
                        href="#projects"
                        className="primary-button"
                    >
                        View Projects
                    </a>

                    <a
                        href="#contact"
                        className="secondary-button"
                    >
                        Contact Me
                    </a>

                </div>

            </div>

        </section>
    )
}

export default Hero