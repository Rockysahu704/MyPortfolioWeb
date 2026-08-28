
import { useState, useEffect } from 'react'
import Home from './pages/Home'
import "./App.css"
function App() {

  const [isDarkMode, setIsDarkMode] = useState(() => {

        const savedTheme = localStorage.getItem("theme")

        return savedTheme === "dark"

    })

function toggleTheme() {

        setIsDarkMode((previousTheme) => {
            return !previousTheme
        })

    }

    useEffect(() => {

        if (isDarkMode) {
            localStorage.setItem("theme", "dark")
        } else {
            localStorage.setItem("theme", "light")
        }

    }, [isDarkMode])

    
  return (
     <div className={isDarkMode ? "app dark" : "app"}>
            <Home
                isDarkMode={isDarkMode}
                toggleTheme={toggleTheme}
            />
        </div>
  )
    
  
}

export default App
