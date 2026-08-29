// Same-origin by default: the production build is served by nginx, which
// proxies /api, /auth, /admin and /token to gunicorn. Local dev overrides this
// via REACT_APP_API_SERVER in .env.development (CRA inlines it at build time).
export const API_SERVER = process.env.REACT_APP_API_SERVER ?? ''

export const IMAGE_PATH = '/images/npc_creator/'