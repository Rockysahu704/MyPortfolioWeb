import "../App.css"

function About() {
    return (
        <section id="about" className="about-section">

            <div className="about-content">

                <p className="section-subtitle">
                    Get To Know More
                </p>

                <h2>About Me</h2>

                <div className="about-intro">

                    <div className="about-text">

                        <p>
                            I'm a passionate developer with a strong
                            interest in building modern, scalable, and
                            user-friendly applications.
                        </p>

                        <p>
                            My primary focus is Python Full Stack
                            Development, where I work with technologies
                            such as Python, Django, Django REST Framework,
                            React, PostgreSQL, JavaScript, HTML, and CSS.
                        </p>

                        <p>
                            Along with web development, I am also exploring
                            AI/ML and Agentic AI. I enjoy learning how
                            intelligent systems and AI-powered applications
                            can solve real-world problems.
                        </p>

                    </div>

                    <div className="about-highlights">

                        <div className="highlight-card">
                            <span>💻</span>
                            <h3>Full Stack</h3>
                            <p>
                                Building complete web applications
                                from frontend to backend.
                            </p>
                        </div>

                        <div className="highlight-card">
                            <span>🤖</span>
                            <h3>AI & ML</h3>
                            <p>
                                Exploring machine learning and
                                AI-powered applications.
                            </p>
                        </div>

                        <div className="highlight-card">
                            <span>🧠</span>
                            <h3>Agentic AI</h3>
                            <p>
                                Learning to build intelligent
                                AI agents and workflows.
                            </p>
                        </div>

                    </div>

                </div>

            </div>

        </section>
    )
}

export default About