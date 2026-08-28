import { useEffect, useState } from "react"
import { getProjects, getSkills } from "../services/api"
import ProjectCard from "./ProjectCard"
import "../App.css"

function Projects() {
    const  [projects, setProjects] = useState([])
    const [skills, setSkills] = useState([])
    const [loading, setLoading] = useState(true)
    const [error, setError] = useState("")
    useEffect(() => {
        getProjects()
        .then((data) => {
            setProjects(data.results)
            // console.log("data result: ", data.results)
        })
        .catch((error) => {
            console.error("Error fetching projects: ", error)
        })

        getSkills()
        .then((data) => {
            setSkills(data)
            // console.log("Skills:", data.results)
        })
        .catch((error) => {
            console.error("Error fetching skills:", error)
        })
    }, [])

    useEffect(() => {

    Promise.all([
        getProjects(),
        getSkills()
    ])
        .then(([projectsData, skillsData]) => {

            setProjects(projectsData.results)
            setSkills(skillsData)

        })
        .catch((error) => {
            console.error("Error fetching data:", error)
            setError(

                "Failed to load projects. Please try again."

            )
        })
        .finally(() => {
            setLoading(false)
        })

}, [])

    return(
    <section className="projects-section" id="projects">
        <h2> My Projects</h2>
        {
            loading ? (
                <p> Loading projects...</p>

            ) : error ? (
                <p>{error}</p>
            ) : projects.length === 0 ? (
                <p> No projects available</p>
            ) : (
                <div className="projects-grid">
                    {
                        projects.map((project) => (
                            <ProjectCard
                                key={project.id}
                                project={project}
                                skills={skills}
                            />
                        ))}
                </div>
            )
        }
    </section>)
}

export default Projects