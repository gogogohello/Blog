use test;

create table books(
	`id` varchar(50) not null,
	`name` varchar(100) not null,
	`author` varchar(100) not null,
	`image` varchar(500),
	`content` mediumtext not null, 
	`url` varchar(500),
	`year` smallint unsigned,
	`created_at` real not null,
	`introduction` varchar(500) not null,
	key `idx_created_at` (`created_at`),
	primary key (`id`)
) engine=innodb default charset=utf8;


create table bookreviews(                  
    `id` varchar(50) not null,          
    `book_id` varchar(50) not null,     
    `user_id` varchar(40) not null,     
    `user_name` varchar(50) not null,   
    `user_image` varchar(500) not null, 
    `content` mediumtext not null,      
    `created_at` real not null,         
    key `idx_created_at` (`created_at`),
    primary key (`id`)                  
) engine=innodb default charset=utf8;

