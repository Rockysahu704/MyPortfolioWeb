function ProjectCard({ project, skills = [] }) {

    const projectSkills = skills.filter((skill) =>
        project.skills?.includes(skill.id)
    )

    return (
        <article className="project-card">

            {project.image && (
                <img
                    src={project.image}
                    alt={project.title}
                />
            )}

            <h3>{project.title}</h3>

            <p>{project.description}</p>

            <div className="project-links">

                {project.github_url && (
                    <a
                        href={project.github_url}
                        target="_blank"
                        rel="noreferrer"
                        className="github-button"
                    >
                        GitHub
                    </a>
                )}

                {project.live_url && (
                    <a
                        href={project.live_url}
                        target="_blank"
                        rel="noreferrer"
                        className="live-button"
                    >
                        Live Demo
                    </a>
                )}

            </div>

            <div className="project-skills">

                {projectSkills.map((skill) => (
                    <span
                        className="skill-badge"
                        key={skill.id}
                    >
                        {skill.name}
                    </span>
                ))}

            </div>

        </article>
    )
}

export default ProjectCard