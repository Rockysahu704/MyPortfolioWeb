const API_BASE_URL = import.meta.env.VITE_API_BASE_URL

export async function getSkills(username) {
    const response = await fetch(`${API_BASE_URL}/portfolio/${username}/skills/`)

    if (!response.ok){
        throw new Error("Failed to fetch skills")
    }

    return response.json()
}

export async function getProjects(username) {
    const response = await fetch(`${API_BASE_URL}/portfolio/${username}/projects/`)

    if (!response.ok){
        throw new Error("Failed to fetch projects")
    }
    return response.json()
}

export async function sendContactMessage(username,contactData) {
    const response = await fetch(`${API_BASE_URL}/portfolio/${username}/contact/`,{
        method:"POST",
        headers:{
            "Content-Type":"application/json",
        },
        body:JSON.stringify(contactData),

    } )

    if (!response.ok){
        throw new Error("Failed to send message")

    }

    return response.json()
}

export async function getEducation(username) {
    const response = await fetch(`${API_BASE_URL}/portfolio/${username}/education/`)

    if (!response.ok){
        throw new Error("Failed to fetch education")
    }

    return response.json()
}

export async function getExperience(username) {
    const response = await fetch(`${API_BASE_URL}/portfolio/${username}/experience/`)

    if (!response.ok) {
        throw new Error("Failed to fetch experience")
    }

    return response.json()
}

export async function getSocialMedia(username) {

    const response = await fetch(
        `${API_BASE_URL}/portfolio/${username}/social/`
    )

    if (!response.ok) {
        throw new Error("Failed to fetch social media")
    }

    return response.json()
}