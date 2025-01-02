const redirectUri = 'http://localhost:5173/auth/github/callback/'
const client_id = 'Iv23lim09iJEF9230TOJ'

function githubRedirect() {
	const githubAuthUrl = `https://github.com/login/oauth/authorize?client_id=${client_id}&redirect_uri=${encodeURIComponent(
		redirectUri
	)}&scope=user`
	window.location.href = githubAuthUrl
}

export { githubRedirect }
