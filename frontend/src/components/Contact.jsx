import { useState } from "react"
import { sendContactMessage } from "../services/api"
import "../App.css"


function Contact({ username }) {

    const [formData, setFormData] = useState({
        name: "",
        email: "",
        subject: "",
        message: ""
    })

    const [status, setStatus] = useState("")

    const [isSubmitting, setIsSubmitting] = useState(false)


    function handleChange(event) {

        const { name, value } = event.target

        setFormData({
            ...formData,
            [name]: value
        })

    }


    async function handleSubmit(event) {

        event.preventDefault()

        try {

            setIsSubmitting(true)

            setStatus("Sending...")

            await sendContactMessage(
                username,
                formData
            )

            console.log("Message sent successfully")

            setStatus("Message sent successfully!")

            setFormData({
                name: "",
                email: "",
                subject: "",
                message: ""
            })

        } catch (error) {

            console.error(
                "Error sending message:",
                error
            )

            setStatus(
                "Failed to send message. Please try again."
            )

        } finally {

            setIsSubmitting(false)

        }

    }


    return (

        <section
            id="contact"
            className="contact-section"
        >

            <h2>Contact Me</h2>

            <form
                className="contact-form"
                onSubmit={handleSubmit}
            >

                <div className="form-group">

                    <label>Name</label>

                    <input
                        type="text"
                        name="name"
                        value={formData.name}
                        onChange={handleChange}
                        required
                    />

                </div>


                <div className="form-group">

                    <label>Email</label>

                    <input
                        type="email"
                        name="email"
                        value={formData.email}
                        onChange={handleChange}
                        required
                    />

                </div>


                <div className="form-group">

                    <label>Subject</label>

                    <input
                        type="text"
                        name="subject"
                        value={formData.subject}
                        onChange={handleChange}
                        required
                    />

                </div>


                <div className="form-group">

                    <label>Message</label>

                    <textarea
                        name="message"
                        value={formData.message}
                        onChange={handleChange}
                        required
                    />

                </div>


                <button
                    type="submit"
                    disabled={isSubmitting}
                >
                    {
                        isSubmitting
                            ? "Sending..."
                            : "Send Message"
                    }
                </button>


                {
                    status && (
                        <p className="form-status">
                            {status}
                        </p>
                    )
                }

            </form>

        </section>

    )
}


export default Contact