export type Task = {
	name: string;
	description: string;
	done: boolean;
};

export type TaskListProps = {
	tasks: Task[];
};
