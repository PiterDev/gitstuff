<script lang="ts">
  interface RepoInfo {
    id: number;
    name: string;
    full_name: string;
    html_url: string;
    description: string | null;
    stargazers_count: number;
    forks_count: number;
    open_issues_count: number;
    watchers_count: number;
    owner: {
      login: string;
      avatar_url: string;
      html_url: string;
    };
    license?: { name: string } | null;
    language?: string | null;
    error?: string;
  }

  export let repoInfo: RepoInfo | null;
</script>

{#if repoInfo && !repoInfo.error}
  <div class="repo-card">
    <div class="repo-header">
      <img src={repoInfo.owner.avatar_url} alt="Owner avatar" class="avatar" width="48" height="48" />
      <div class="repo-title">
        <a href={repoInfo.html_url} target="_blank" rel="noopener noreferrer">
          <h2>{repoInfo.full_name}</h2>
        </a>
        <a class="owner-link" href={repoInfo.owner.html_url} target="_blank" rel="noopener noreferrer">
          @{repoInfo.owner.login}
        </a>
      </div>
    </div>
    <p class="repo-description">{repoInfo.description}</p>
    <div class="repo-details-vertical">
      <div class="repo-details-col">
        <div><span>⭐</span> {repoInfo.stargazers_count} Stars</div>
        <div><span>🍴</span> {repoInfo.forks_count} Forks</div>
        <div><span>👀</span> {repoInfo.watchers_count} Watchers</div>
      </div>
      <div class="repo-details-col">
        <div><span>🐛</span> {repoInfo.open_issues_count} Open Issues</div>
        <div><span>🛡</span> {repoInfo.license?.name ?? 'No license'}</div>
        <div><span>📝</span> {repoInfo.language ?? 'Unknown'}</div>
      </div>
    </div>
  </div>
{:else if repoInfo && repoInfo.error}
  <div class="error">{repoInfo.error}</div>
{:else}
  <div>Loading repository info...</div>
{/if}

<style>
  .repo-card {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    border: 1px solid #444;
    border-radius: 10px;
    padding: 2rem;
    margin: 1.5rem 0;
    background: #232323;
    color: #fff;
    width: 100%;
    max-width: 40rem;
    box-shadow: 0 2px 8px rgba(0,0,0,0.10);
  }
  .repo-header {
    display: flex;
    align-items: center;
    gap: 1rem;
    margin-bottom: 0.5rem;
    width: 100%;
  }
  .avatar {
    border-radius: 50%;
    border: 2px solid #444;
    width: 48px;
    height: 48px;
    background: #fff;
  }
  .repo-title {
    display: flex;
    flex-direction: column;
    gap: 0.2rem;
  }
  .repo-title h2 {
    margin: 0;
    font-size: 1.4rem;
    color: #fff;
    font-weight: 600;
    line-height: 1.2;
  }
  .owner-link {
    color: #aaa;
    font-size: 1rem;
    text-decoration: none;
  }
  .repo-description {
    margin: 0.5rem 0 1.5rem 0;
    color: #ccc;
    font-size: 1.05rem;
    line-height: 1.4;
    width: 100%;
  }
  .repo-details-vertical {
    display: flex;
    flex-direction: row;
    gap: 2rem;
    width: 100%;
    margin-top: 0.5rem;
  }
  .repo-details-col {
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
  }
  .repo-details-col div {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    font-size: 1rem;
    color: #e0e0e0;
    background: #292929;
    border-radius: 6px;
    padding: 0.4rem 0.8rem;
    margin-bottom: 0.1rem;
    width: fit-content;
  }
  .error {
    color: #ff6b6b;
    font-weight: bold;
    margin: 1rem 0;
  }
</style>