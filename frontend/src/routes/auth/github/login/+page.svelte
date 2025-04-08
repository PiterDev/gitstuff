<script lang="ts">
	import { PUBLIC_GH_CLIENT_ID } from "$env/static/public";

    let { data } = $props();
    
    const githubAuthUrl = 'https://github.com/login/oauth/authorize';
    const clientId = PUBLIC_GH_CLIENT_ID;
    const scope = 'user repo';
    const redirectUri = 'http://localhost:5173/auth/github/callback';

    function githubRedirect() {
        const url = `${githubAuthUrl}?client_id=${clientId}&redirect_uri=${redirectUri}&scope=${scope}`;
        window.location.href = url;
    }
</script>

{#if data.sessionExpired}
    <p>Your session has expired. Please login again.</p>
{/if}
<button onclick={githubRedirect}>Login with GitHub</button>
