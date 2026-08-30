import { useEffect, useState } from "react"
import { getSkills } from "../services/api"

import "../App.css"


function Skills({ username }) {

    const [skills, setSkills] = useState([])
    const [loading, setLoading] = useState(true)
    const [error, setError] = useState("")


    useEffect(() => {

        getSkills(username)
            .then((data) => {

                setSkills(data)

            })
            .catch((error) => {

                console.error(
                    "Error fetching skills:",
                    error
                )

                setError(
                    "Failed to load skills. Please try again."
                )

            })
            .finally(() => {

                setLoading(false)

            })

    }, [username])


    return (

        <section
            id="skills"
            className="skills-section"
        >

            <h2>
                My <span>Skills</span>
            </h2>


            {loading ? (

                <p>Loading skills...</p>

            ) : error ? (

                <p>{error}</p>

            ) : skills.length === 0 ? (

                <p>No skills available.</p>

            ) : (

                <div className="skills-grid">

                    {skills.map((skill) => (

                        <div
                            className="skill-item"
                            key={skill.id}
                        >

                            <div className="skill-icon">

                                {skill.image ? (

                                    <img
                                        src={skill.image}
                                        alt={skill.name}
                                    />

                                ) : (

                                    <span>💻</span>

                                )}

                            </div>


                            <div className="skill-info">

                                <div className="skill-header">

                                    <span>
                                        {skill.name}
                                    </span>

                                    <span className="skill-percentage">
                                        {skill.proficiency}%
                                    </span>

                                </div>


                                <div className="progress-bar">

                                    <div
                                        className="progress-fill"
                                        style={{
                                            width: `${skill.proficiency}%`
                                        }}
                                    />

                                </div>

                            </div>

                        </div>

                    ))}

                </div>

            )}

        </section>

    )
}


export default Skills