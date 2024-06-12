-- 运动员信息
INSERT INTO athlete
    (name, unit, "group", status, place)
VALUES ('李文龙', '雷科防务', 75, 0, 0);
INSERT INTO athlete
    (name, unit, "group", status, place)
VALUES ('李彪', '根网科技', 75, 2, 0);
INSERT INTO athlete
    (name, unit, "group", status, place)
VALUES ('云炜铭', '金证股份', 60, 2, 1);
INSERT INTO athlete
    (name, unit, "group", status, place)
VALUES ('鲜俊', '某施工单位', 75, 2, 1);
INSERT INTO athlete
    (name, unit, "group", status, place)
VALUES ('马航艳', '某车队', 60, 2, 1);
INSERT INTO athlete
    (name, unit, "group", status, place)
VALUES ('张春鹏', '某涉密单位', 75, 2, 1);


-- 创建赛程

INSERT INTO schedule
(name, site_id, status, red_score, red_foul, cyan_score, cyan_foul, video_path, red_id, cyan_id, red_name, cyan_name,
 red_unit,
 cyan_unit, winner_id)
VALUES ('赛程1', 101, 0, 10, 1, 8, 2, '/videos/schedule1.mp4', 201, 301, '红方选手1', '青方选手1', '红方单位1',
        '青方单位1', 201);
INSERT INTO schedule
(name, site_id, status, red_score, red_foul, cyan_score, cyan_foul, video_path, red_id, cyan_id, red_name, cyan_name,
 red_unit,
 cyan_unit, winner_id)
VALUES ('赛程2', 102, 1, 15, 0, 14, 1, '/videos/schedule2.mp4', 202, 302, '红方选手2', '青方选手2', '红方单位2',
        '青方单位2', 202);
INSERT INTO schedule
(name, site_id, status, red_score, red_foul, cyan_score, cyan_foul, video_path, red_id, cyan_id, red_name, cyan_name,
 red_unit,
 cyan_unit, winner_id)
VALUES ('赛程3', 103, 2, 12, 2, 12, 3, '/videos/schedule3.mp4', 203, 303, '红方选手3', '青方选手3', '红方单位3',
        '青方单位3', 203);
INSERT INTO schedule
(name, site_id, status, red_score, red_foul, cyan_score, cyan_foul, video_path, red_id, cyan_id, red_name, cyan_name,
 red_unit,
 cyan_unit, winner_id)
VALUES ('赛程4', 104, 1, 9, 1, 10, 2, '/videos/schedule4.mp4', 204, 304, '红方选手4', '青方选手4', '红方单位4',
        '青方单位4', 304);
