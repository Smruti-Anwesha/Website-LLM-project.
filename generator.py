def generate_code(layout):
    sections = layout["sections"]

    html_sections = ""

    for section in sections:
        if section == "hero":
            html_sections += """
            <section class="hero">
                <h1>Build Something Amazing</h1>
                <p>Your dream website, powered by AI</p>
                <button>Get Started</button>
            </section>
            """

        elif section == "gallery":
            html_sections += """
            <section class="gallery">
                <h2>Gallery</h2>
                <div class="cards">
                    <img src="https://source.unsplash.com/300x200/?bakery" />
                    <img src="https://source.unsplash.com/300x200/?dessert" />
                    <img src="https://source.unsplash.com/300x200/?cake" />
                </div>
            </section>
            """

        elif section == "menu":
            html_sections += """
            <section class="menu">
                <h2>Our Menu</h2>
                <div class="cards">
                    <div class="card">🍞 Bread</div>
                    <div class="card">🧁 Cupcakes</div>
                    <div class="card">🎂 Cakes</div>
                </div>
            </section>
            """

        elif section == "projects":
            html_sections += """
            <section class="projects">
                <h2>Projects</h2>
                <div class="cards">
                    <div class="card">AI Website</div>
                    <div class="card">Portfolio App</div>
                </div>
            </section>
            """

        elif section == "skills":
            html_sections += """
            <section class="skills">
                <h2>Skills</h2>
                <p>Python • AI • Web Dev • ML</p>
            </section>
            """

        elif section == "contact":
            html_sections += """
            <section class="contact">
                <h2>Contact</h2>
                <p>Email: contact@example.com</p>
            </section>
            """

    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>{layout['type'].capitalize()} Website</title>
        <link rel="stylesheet" href="style.css">
    </head>
    <body>

        <nav class="navbar">
            <h2>AI Builder</h2>
            <ul>
                <li>Home</li>
                <li>Gallery</li>
                <li>Contact</li>
            </ul>
        </nav>

        {html_sections}

        <footer>
            <p>© 2026 AI Generated Website</p>
        </footer>

    </body>
    </html>
    """

    css = """
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }

    body {
        font-family: 'Segoe UI', sans-serif;
        background: #0f172a;
        color: white;
    }

    /* NAVBAR */
    .navbar {
        display: flex;
        justify-content: space-between;
        padding: 20px;
        background: #020617;
    }

    .navbar ul {
        display: flex;
        list-style: none;
        gap: 20px;
    }

    /* HERO */
    .hero {
        height: 80vh;
        background: linear-gradient(to right, #6366f1, #ec4899);
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        text-align: center;
        animation: fadeIn 2s ease-in;
    }

    .hero button {
        margin-top: 15px;
        padding: 12px 25px;
        border: none;
        background: white;
        color: black;
        border-radius: 8px;
        cursor: pointer;
        transition: 0.3s;
    }

    .hero button:hover {
        transform: scale(1.1);
    }

    /* SECTIONS */
    section {
        padding: 60px 20px;
        text-align: center;
        animation: fadeUp 1s ease;
    }

    /* CARDS */
    .cards {
        display: flex;
        justify-content: center;
        gap: 20px;
        margin-top: 20px;
        flex-wrap: wrap;
    }

    .card {
        background: #1e293b;
        padding: 20px;
        width: 180px;
        border-radius: 12px;
        transition: 0.3s;
    }

    .card:hover {
        transform: translateY(-10px);
    }

    .cards img {
        width: 300px;
        border-radius: 10px;
    }

    /* FOOTER */
    footer {
        background: #020617;
        padding: 15px;
        text-align: center;
    }

    /* ANIMATIONS */
    @keyframes fadeIn {
        from {opacity: 0;}
        to {opacity: 1;}
    }

    @keyframes fadeUp {
        from {
            opacity: 0;
            transform: translateY(30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }

    /* RESPONSIVE */
    @media(max-width: 768px) {
        .navbar {
            flex-direction: column;
            align-items: center;
        }

        .cards {
            flex-direction: column;
            align-items: center;
        }
    }
    """

    return html, css