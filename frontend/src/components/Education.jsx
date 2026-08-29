import { useEffect, useState } from "react"
import { getEducation } from "../services/api"

import "../App.css"


function Education({ username }) {

    const [education, setEducation] = useState([])
    const [loading, setLoading] = useState(true)
    const [error, setError] = useState("")


    useEffect(() => {

        setLoading(true)
        setError("")

        getEducation(username)

            .then((data) => {

                console.log("Education:", data)

                setEducation(data)

            })

            .catch((error) => {

                console.error(
                    "Error fetching education:",
                    error
                )

                setError(
                    "Failed to load education. Please try again."
                )

            })

            .finally(() => {

                setLoading(false)

            })

    }, [username])


    return (

        <section
            id="education"
            className="education-section"
        >

            <h2>Education</h2>

            {
                loading ? (

                    <p>Loading education...</p>

                ) : error ? (

                    <p>{error}</p>

                ) : education.length === 0 ? (

                    <p>No education information available.</p>

                ) : (

                    <div className="education-list">

                        {
                            education.map((item) => (

                                <article
                                    className="education-card"
                                    key={item.id}
                                >

                                    <h3>
                                        {item.institution}
                                    </h3>

                                    <p>
                                        {item.degree} - {item.field}
                                    </p>

                                </article>

                            ))
                        }

                    </div>

                )
            }

        </section>

    )
}


export default Education