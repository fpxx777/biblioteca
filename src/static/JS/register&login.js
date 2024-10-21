document.getElementById('volver').addEventListener('click', function () {
    document.getElementById('left').classList.add('move-right');
    document.getElementById('right').classList.add('move-left');
    document.getElementById('cambiar').style.display = 'block';
    document.getElementById('volver').style.display = 'none';
    document.getElementById('cambio-p').style.display = 'block';
    document.getElementById('volver-p').style.display = 'none';


    setTimeout(() => {
        changeForm('login');
    }, 250);
});

document.getElementById('cambiar').addEventListener('click', function () {
    document.getElementById('left').classList.remove('move-right');
    document.getElementById('right').classList.remove('move-left');
    document.getElementById('volver').style.display = 'block';
    document.getElementById('cambiar').style.display = 'none';
    document.getElementById('cambio-p').style.display = 'none';
    document.getElementById('volver-p').style.display = 'block';


    setTimeout(() => {
        changeForm('signup');
    }, 250);
});

function changeForm(type) {
    const formContainer = document.getElementById('form-container');
    if (type === 'login') {
        formContainer.innerHTML = `
            <form id="login-form">
                <svg xmlns="http://www.w3.org/2000/svg" width="2.5vw" viewBox="0 0 256 256" class="logo">
                    <path fill="#F8F1DF"
                            d="M208 20H72a36 36 0 0 0-36 36v168a12 12 0 0 0 12 12h144a12 12 0 0 0 0-24H60v-4a12 12 0 0 1 12-12h136a12 12 0 0 0 12-12V32a12 12 0 0 0-12-12m-88 24h36v59l-10.51-8.41a12 12 0 0 0-15 0L120 103Zm76 128H72a35.6 35.6 0 0 0-12 2.06V56a12 12 0 0 1 12-12h24v84a12 12 0 0 0 19.5 9.37l22.49-18l22.51 18A12 12 0 0 0 180 128V44h16Z" />
                </svg>
                <h2>Inicia sesión en tu cuenta</h2>
                <div class="rellenar">
                    <label for="email">Email</label>
                    <input type="email" id="email" required>
                </div>
                <div class="rellenar">
                    <label for="password">Contraseña</label>
                    <input type="password" id="password" required>
                </div>
                <div class="opciones">
                    <div class="checkbox">
                        <input type="checkbox" id="remember">
                        <label for="remember">Recuérdame</label>
                    </div>
                    <a href="#" class="forgot-contraseña">¿Olvidaste tu contraseña?</a>
                </div>
                <button type="submit">Iniciar Sesión</button>
                <style>
                    button {
                        background-color: var(--contrast2-bg-color);
                        color: var(--dark-bg-color);
                    }
                    button:hover {
                        background-color: var(--dark2-bg-color);
                        color: var(--contrast2-bg-color);
                    }
                </style>

            </form>
        `;
    } else {
        formContainer.innerHTML = `
            <form id="signup-form">
                <svg xmlns="http://www.w3.org/2000/svg" width="2.5vw" viewBox="0 0 256 256" class="logo">
                    <path fill="#F8F1DF"
                            d="M208 20H72a36 36 0 0 0-36 36v168a12 12 0 0 0 12 12h144a12 12 0 0 0 0-24H60v-4a12 12 0 0 1 12-12h136a12 12 0 0 0 12-12V32a12 12 0 0 0-12-12m-88 24h36v59l-10.51-8.41a12 12 0 0 0-15 0L120 103Zm76 128H72a35.6 35.6 0 0 0-12 2.06V56a12 12 0 0 1 12-12h24v84a12 12 0 0 0 19.5 9.37l22.49-18l22.51 18A12 12 0 0 0 180 128V44h16Z" />
                </svg>
                <h2 style="color:var(--contrast-bg-color)">Crea tu cuenta</h2>
                <div class="rellenar">
                    <label for="email" style="color:var(--contrast-bg-color)">Email</label>
                    <input type="email" id="email" required>
                </div>
                <div class="rellenar">
                    <label for="username" style="color:var(--contrast-bg-color)">Nombre usuario</label>
                    <input type="text" name="username" id="username" required>
                </div>
                <div class="rellenar">
                    <label for="password" style="color:var(--contrast-bg-color)">Contraseña</label>
                    <input type="password" id="password" required>
                </div>
                <div class="rellenar">
                    <label for="confirm-password" style="color:var(--contrast-bg-color)">Confirma tu contraseña</label>
                    <input type="password" id="confirm-password" required>
                </div>
                
                <button type="submit";>Crear Cuenta</button>
            </form>
        `;
    }
}