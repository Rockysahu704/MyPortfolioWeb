import { useEffect, useState } from "react"
import { getSkills } from "../services/api"


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
                    "Error fetching skills: ",
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

        <section id="skills">

            <h2>My Skills</h2>

            {
                loading ? (

                    <p>Loading skills...</p>

                ) : error ? (

                    <p>{error}</p>

                ) : skills.length === 0 ? (

                    <p>No skills available.</p>

                ) : (

                    <ul>

                        {skills.map((skill) => (

                            <li key={skill.id}>
                                {skill.name}
                            </li>

                        ))}

                    </ul>

                )
            }

        </section>

    )
}


export default Skills