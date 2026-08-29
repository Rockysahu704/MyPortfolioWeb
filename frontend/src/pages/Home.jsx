import { useParams } from "react-router-dom"

import About from "../components/About"
import Contact from "../components/Contact"
import Education from "../components/Education"
import Experience from "../components/Experience"
import Hero from "../components/Hero"
import Navbar from "../components/Navbar"
import Projects from "../components/Projects"
import Skills from "../components/Skills"


function Home({ isDarkMode, toggleTheme }) {

    const { username } = useParams()

    return (
        <div>

            <Navbar
                isDarkMode={isDarkMode}
                toggleTheme={toggleTheme}
            />

            <main>

                <Hero />

                <About />

                <Skills username={username} />

                <Projects username={username} />

                <Experience username={username} />

                <Education username={username} />

                <Contact username={username} />

            </main>

        </div>
    )
}


export default Home