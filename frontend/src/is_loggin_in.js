
function is_logged_in() {
    return localStorage.getItem('refresh_token') !== null
}

export default is_logged_in;