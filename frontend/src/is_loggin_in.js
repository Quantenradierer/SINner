
function is_logged_in() {
    return localStorage.getItem('auth_token') !== null
}

export default is_logged_in;