INSERT INTO `news`
(
	`title`,
	`source`,
	`create_date`,
	`description`,
	`look`
) VALUES(
	'勞動部聯手TibaMe全額補助培育AI工程師',
	'經濟日報 (新聞發布)',
	'2019-09-25',
	'有鑑於產業人才需求，最貼近產業趨勢的培訓品牌TibaMe與勞動部勞動力發展署北基宜花金馬分署及桃竹苗分署合作，安排具產業實務經驗的師資 ...',
	'100'
);

UPDATE `news` SET `look`='999',`title`='xxxx';
UPDATE `news` SET `look`='100' WHERE `id`='3';
UPDATE `news` SET `look`='500' WHERE `id`<>'3';
UPDATE `news` SET `look`='777' WHERE `id` IN ('3','4','5');
UPDATE `news` SET `look`='10' WHERE `description` LIKE '%AI%';
UPDATE `news` SET `look`='0' WHERE `create_date` BETWEEN '2019-01-01' AND '2020-03-31';

UPDATE `news` SET `look`='100' WHERE `id`='3' OR `id`='4';
UPDATE `news` SET `look`='100' WHERE `id`='3' AND `create_date` BETWEEN '2019-01-01' AND '2020-03-31';

DELETE FROM `news`;
DELETE FROM `news` WHERE `id`='3';



SELECT `title`,`source` FROM `news` WHERE `id`>'1';
SELECT * FROM `news` WHERE `id`>'1';

SELECT * FROM `news` WHERE `id`>'1' ORDER BY `look` ASC;
SELECT * FROM `news` WHERE `id`>'1' ORDER BY `look` DESC,`id` DESC;

SELECT COUNT(`id`) FROM `news` WHERE `id`>'1';
SELECT SUM(`look`) FROM `news` WHERE `id`>'1';
SELECT AVG(`look`) AS `AVG` FROM `news` WHERE `id`>'1';

SELECT * FROM `news` LIMIT 1,2;
SELECT * FROM `news` LIMIT 0,2;
SELECT * FROM `news` ORDER BY `id` DESC LIMIT 0,2;

