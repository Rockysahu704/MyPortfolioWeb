const API_BASE_URL = import.meta.env.VITE_API_BASE_URL

export async function getSkills() {
    const response = await fetch(`${API_BASE_URL}/skills/`)

    if (!response.ok){
        throw new Error("Failed to fetch skills")
    }

    return response.json()
}

export async function getProjects() {
    const response = await fetch(`${API_BASE_URL}/projects/`)

    if (!response.ok){
        throw new Error("Failed to fetch projects")
    }
    return response.json()
}

export async function sendContactMessage(contactData) {
    const response = await fetch(`${API_BASE_URL}/contact/`,{
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

export async function getEducation() {
    const response = await fetch(`${API_BASE_URL}/education/`)

    if (!response.ok){
        throw new Error("Failed to fetch education")
    }

    return response.json()
}

export async function getExperience() {
    const response = await fetch(`${API_BASE_URL}/experience/`)

    if (!response.ok) {
        throw new Error("Failed to fetch experience")
    }

    return response.json()
}