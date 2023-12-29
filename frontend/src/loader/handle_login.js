import api from "../axios";


function handleLogin(username, password, errorHandler) {
    api.defaults.xsrfCookieName = 'csrftoken'
    api.defaults.xsrfHeaderName = 'X-CSRFToken'

    const url = `auth/token/login/`;
    api.post(url, {
        username: username,
        password: password
    })
    .then((response) => {
        localStorage.setItem('auth_token', response.data.auth_token);
                api.defaults.headers = { 'Authorization': `Token ${response.data.auth_token}`,}
        window.location.href = '/';
    })
    .catch(errorHandler);
}

export default handleLogin;
