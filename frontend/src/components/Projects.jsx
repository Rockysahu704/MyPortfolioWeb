import { useEffect, useState } from "react"

import { getProjects, getSkills } from "../services/api"

import ProjectCard from "./ProjectCard"

import "../App.css"


function Projects({ username }) {

    const [projects, setProjects] = useState([])

    const [skills, setSkills] = useState([])

    const [loading, setLoading] = useState(true)

    const [error, setError] = useState("")


    useEffect(() => {

        setLoading(true)

        setError("")


        Promise.all([
            getProjects(username),
            getSkills(username)
        ])

            .then(([projectsData, skillsData]) => {

                setProjects(projectsData.results)

                setSkills(skillsData)

            })

            .catch((error) => {

                console.error(
                    "Error fetching project data:",
                    error
                )

                setError(
                    "Failed to load projects. Please try again."
                )

            })

            .finally(() => {

                setLoading(false)

            })

    }, [username])


    return (

        <section
            className="projects-section"
            id="projects"
        >

            <h2>My Projects</h2>

            {
                loading ? (

                    <p>Loading projects...</p>

                ) : error ? (

                    <p>{error}</p>

                ) : projects.length === 0 ? (

                    <p>No projects available.</p>

                ) : (

                    <div className="projects-grid">

                        {
                            projects.map((project) => (

                                <ProjectCard
                                    key={project.id}
                                    project={project}
                                    skills={skills}
                                />

                            ))
                        }

                    </div>

                )
            }

        </section>

    )

}


export default Projects