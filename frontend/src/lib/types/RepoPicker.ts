export type RepoPickerProps = {
	repos: Repo[];
	onChange: (repo: Repo) => void;
};

export type Repo = {
	repoName: string;
};

export type JsonRepoList = {
	repos: JsonRepo[];
};

export type JsonRepo = {
	full_name: string;
};
