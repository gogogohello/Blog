use test;

create table books(
	`id` varchar(50) not null,
	`name` varchar(100) not null,
	`image` varchar(500),
	`url` varchar(500),
	`year` smallint unsigned not null,
	`created_at` real not null,
	`introduction` varchar(500) not null,
	key `idx_created_at` (`created_at`),
	primary key (`id`)
)
