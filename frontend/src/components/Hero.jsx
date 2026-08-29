import "../App.css"
import profileImage from "../assets/images/RockyPfp.jpeg"
import "../../public/Resume.pdf"

function Hero() {
    return (
        <section id="home" className="hero-section">

            {/* Left Side */}
            <div className="hero-content">

                <p className="hero-greeting">
                    Hello, I'm
                </p>

                <h1>
                    Rocky Sahu
                </h1>

               <h2 className="hero-role">
                    <span className="role-prefix">And I'm a </span>
                    <span className="role-highlight">
                        Python Full Stack Developer
                    </span>
                </h2>

                <p className="hero-description">
                   I build modern web applications with Python, Django, and React.
                    I also work with AI/ML and explore Agentic AI to build intelligent,
                    scalable, and impactful solutions.
                </p>

                <div className="hero-buttons">

                    <a
                        href="#projects"
                        className="primary-button"
                    >
                        View Projects
                    </a>

                    <a
                        href="/Resume.pdf"
                        className="primary-button"
                    >
                         Download CV
                        
                    </a>

                    <a
                        href="#contact"
                        className="secondary-button"
                    >
                        Contact Me
                    </a>

                </div>

            </div>


            {/* Right Side - Profile Image */}
            <div className="hero-image-container">

                <div className="image-background"></div>

            <div className="profile-glow-wrapper">

                  <div className="profile-image-wrapper">
                    <img
                        src={profileImage}
                        alt="Rocky Sahu"
                        className="profile-image"
                    />
                </div>



            </div>

              
            </div>

        </section>
    )
}

export default Hero