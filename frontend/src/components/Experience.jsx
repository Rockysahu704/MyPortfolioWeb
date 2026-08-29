import { useEffect, useState } from "react"
import { getExperience } from "../services/api"

import "../App.css"


function Experience({ username }) {

    const [experience, setExperience] = useState([])
    const [loading, setLoading] = useState(true)
    const [error, setError] = useState("")


    useEffect(() => {

        setLoading(true)
        setError("")

        getExperience(username)

            .then((data) => {

                console.log("Experience:", data)

                setExperience(data)

            })

            .catch((error) => {

                console.error(
                    "Error fetching experience:",
                    error
                )

                setError(
                    "Failed to load experience. Please try again."
                )

            })

            .finally(() => {

                setLoading(false)

            })

    }, [username])


    function formatDate(date) {

        if (!date) return ""

        return new Date(date).toLocaleDateString(
            "en-US",
            {
                month: "short",
                year: "numeric"
            }
        )
    }


    return (

        <section
            id="experience"
            className="experience-section"
        >

            <h2>Experience</h2>

            {
                loading ? (

                    <p>Loading experience...</p>

                ) : error ? (

                    <p>{error}</p>

                ) : experience.length === 0 ? (

                    <p>No experience available</p>

                ) : (

                    <div className="experience-list">

                        {
                            experience.map((item) => (

                                <article
                                    className="experience-card"
                                    key={item.id}
                                >

                                    <div className="experience-header">

                                        <div>

                                            <h3>
                                                {item.position}
                                            </h3>

                                            <h4>
                                                {item.company}
                                            </h4>

                                        </div>

                                        <span className="experience-date">

                                            {formatDate(item.start_date)}

                                            {" - "}

                                            {
                                                item.is_current
                                                    ? "Present"
                                                    : formatDate(item.end_date)
                                            }

                                        </span>

                                    </div>

                                    <p>
                                        {item.description}
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


export default Experience