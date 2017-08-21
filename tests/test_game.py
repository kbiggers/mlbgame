#!/usr/bin/env python

import unittest

import mlbgame

from datetime import datetime


class TestGame(unittest.TestCase):

    def test_day(self):
        games = mlbgame.day(2016, 8, 2)
        for game in games:
            if game.home_team == 'Mets':
                g = game
            self.assertIsInstance(game.away_team, str)
            self.assertIsInstance(game.away_team_errors, int)
            self.assertIsInstance(game.away_team_hits, int)
            self.assertIsInstance(game.away_team_runs, int)
            self.assertIsInstance(game.date, datetime)
            self.assertIsInstance(game.game_id, str)
            self.assertIsInstance(game.game_league, str)
            self.assertIsInstance(game.game_start_time, str)
            self.assertIsInstance(game.game_status, str)
            self.assertIsInstance(game.game_tag, str)
            self.assertIsInstance(game.home_team, str)
            self.assertIsInstance(game.home_team_errors, int)
            self.assertIsInstance(game.home_team_hits, int)
            self.assertIsInstance(game.home_team_runs, int)
            self.assertIsInstance(game.l_pitcher, str)
            self.assertIsInstance(game.l_pitcher_losses, int)
            self.assertIsInstance(game.l_pitcher_wins, int)
            self.assertIsInstance(game.l_team, str)
            self.assertIsInstance(game.sv_pitcher, str)
            self.assertIsInstance(game.sv_pitcher_saves, int)
            self.assertIsInstance(game.w_pitcher, str)
            self.assertIsInstance(game.w_pitcher_losses, int)
            self.assertIsInstance(game.w_pitcher_wins, int)
            self.assertIsInstance(game.w_team, str)
            self.assertIsInstance(game.nice_score(), str)
        game = g
        self.assertEqual(game.away_team, 'Yankees')
        self.assertEqual(game.away_team_errors, 2)
        self.assertEqual(game.away_team_hits, 6)
        self.assertEqual(game.away_team_runs, 1)
        self.assertEqual(game.date, datetime(2016, 8, 2, 18, 10))
        self.assertEqual(game.game_id, '2016_08_02_nyamlb_nynmlb_1')
        self.assertEqual(game.game_league, 'AN')
        self.assertEqual(game.game_start_time, '7:10PM')
        self.assertEqual(game.game_status, 'FINAL')
        self.assertEqual(game.game_tag, 'go_game')
        self.assertEqual(game.home_team, 'Mets')
        self.assertEqual(game.home_team_errors, 0)
        self.assertEqual(game.home_team_hits, 10)
        self.assertEqual(game.home_team_runs, 7)
        self.assertEqual(game.l_pitcher, 'M. Tanaka')
        self.assertEqual(game.l_pitcher_losses, 4)
        self.assertEqual(game.l_pitcher_wins, 7)
        self.assertEqual(game.l_team, 'Yankees')
        self.assertEqual(game.sv_pitcher, '. ')
        self.assertEqual(game.sv_pitcher_saves, 0)
        self.assertEqual(game.w_pitcher, 'J. deGrom')
        self.assertEqual(game.w_pitcher_losses, 5)
        self.assertEqual(game.w_pitcher_wins, 7)
        self.assertEqual(game.w_team, 'Mets')
        self.assertEqual(game.__str__(), 'Yankees (1) at Mets (7)')

    def test_day_empty(self):
        games = mlbgame.day(1000, 1, 1)
        self.assertEqual(games, [])

    def test_games(self):
        games = mlbgame.games(2016, 7)
        self.assertIsInstance(games, list)
        for day in games:
            self.assertIsInstance(day, list)
            for game in day:
                self.assertIsInstance(game, mlbgame.game.GameScoreboard)
        games = mlbgame.combine_games(games)
        for game in games:
            self.assertIsInstance(game.away_team, str)
            self.assertIsInstance(game.away_team_errors, int)
            self.assertIsInstance(game.away_team_hits, int)
            self.assertIsInstance(game.away_team_runs, int)
            self.assertIsInstance(game.date, datetime)
            self.assertIsInstance(game.game_id, str)
            self.assertIsInstance(game.game_league, str)
            self.assertIsInstance(game.game_start_time, str)
            self.assertIsInstance(game.game_status, str)
            self.assertIsInstance(game.game_tag, str)
            self.assertIsInstance(game.home_team, str)
            self.assertIsInstance(game.home_team_errors, int)
            self.assertIsInstance(game.home_team_hits, int)
            self.assertIsInstance(game.home_team_runs, int)
            self.assertIsInstance(game.nice_score(), str)
            if game.game_tag == 'go_game':
                self.assertIsInstance(game.l_pitcher, str)
                self.assertIsInstance(game.l_pitcher_losses, int)
                self.assertIsInstance(game.l_pitcher_wins, int)
                self.assertIsInstance(game.l_team, str)
                self.assertIsInstance(game.sv_pitcher, str)
                self.assertIsInstance(game.sv_pitcher_saves, int)
                self.assertIsInstance(game.w_pitcher, str)
                self.assertIsInstance(game.w_pitcher_losses, int)
                self.assertIsInstance(game.w_pitcher_wins, int)
                self.assertIsInstance(game.w_team, str)

    def test_box_score(self):
        box_score = mlbgame.box_score('2016_08_02_nyamlb_nynmlb_1')
        self.assertEqual(box_score.game_id, '2016_08_02_nyamlb_nynmlb_1')
        self.assertIsInstance(box_score.innings, list)
        for inning in box_score:
            self.assertIn('inning', inning)
            self.assertIn('away', inning)
            self.assertIn('home', inning)
        self.assertEqual(box_score.innings[0]['inning'], 1)
        self.assertEqual(box_score.innings[0]['away'], 0)
        self.assertEqual(box_score.innings[0]['home'], 0)
        self.assertEqual(box_score.innings[1]['inning'], 2)
        self.assertEqual(box_score.innings[1]['away'], 0)
        self.assertEqual(box_score.innings[1]['home'], 0)
        self.assertEqual(box_score.innings[2]['inning'], 3)
        self.assertEqual(box_score.innings[2]['away'], 0)
        self.assertEqual(box_score.innings[2]['home'], 2)
        self.assertEqual(box_score.innings[3]['inning'], 4)
        self.assertEqual(box_score.innings[3]['away'], 0)
        self.assertEqual(box_score.innings[3]['home'], 0)
        self.assertEqual(box_score.innings[4]['inning'], 5)
        self.assertEqual(box_score.innings[4]['away'], 0)
        self.assertEqual(box_score.innings[4]['home'], 1)
        self.assertEqual(box_score.innings[5]['inning'], 6)
        self.assertEqual(box_score.innings[5]['away'], 0)
        self.assertEqual(box_score.innings[5]['home'], 0)
        self.assertEqual(box_score.innings[6]['inning'], 7)
        self.assertEqual(box_score.innings[6]['away'], 0)
        self.assertEqual(box_score.innings[6]['home'], 4)
        self.assertEqual(box_score.innings[7]['inning'], 8)
        self.assertEqual(box_score.innings[7]['away'], 0)
        self.assertEqual(box_score.innings[7]['home'], 0)
        self.assertEqual(box_score.innings[8]['inning'], 9)
        self.assertEqual(box_score.innings[8]['away'], 1)
        self.assertEqual(box_score.innings[8]['home'], 'x')
        self.assertEqual(box_score.print_scoreboard(), (
            'Inning\t1 2 3 4 5 6 7 8 9 \n'
            '---------------------------\n'
            'Away\t0 0 0 0 0 0 0 0 1 \n'
            'Home\t0 0 2 0 1 0 4 0 x '
            ))

    def test_box_score_empty(self):
        self.assertRaises(ValueError, lambda: mlbgame.box_score('game_id'))
        self.assertRaises(ValueError, lambda: mlbgame.box_score('2016_08_02_nymlb_nymlb_1'))

    def test_overview(self):
        overview = mlbgame.overview('2016_08_02_nyamlb_nynmlb_1')
        self.assertEqual(overview.ampm, 'PM')
        self.assertEqual(overview.aw_lg_ampm, 'PM')
        self.assertEqual(overview.away_ampm, 'PM')
        self.assertEqual(overview.away_code, 'nya')
        self.assertEqual(overview.away_division, 'E')
        self.assertEqual(overview.away_file_code, 'nyy')
        self.assertEqual(overview.away_games_back, 9.0)
        self.assertEqual(overview.away_games_back_wildcard, 5.0)
        self.assertEqual(overview.away_league_id, 103)
        self.assertEqual(overview.away_loss, 53)
        self.assertEqual(overview.away_name_abbrev, 'NYY')
        self.assertEqual(overview.away_preview_link, '/mlb/gameday/index.jsp?gid=2016_08_02_nyamlb_nynmlb_1&mode=preview&c_id=mlb')
        self.assertEqual(overview.away_recap_link, '/mlb/gameday/index.jsp?gid=2016_08_02_nyamlb_nynmlb_1&mode=recap&c_id=mlb')
        self.assertEqual(overview.away_sport_code, 'mlb')
        self.assertEqual(overview.away_team_city, 'NY Yankees')
        self.assertEqual(overview.away_team_errors, 2)
        self.assertEqual(overview.away_team_hits, 6)
        self.assertEqual(overview.away_team_id, 147)
        self.assertEqual(overview.away_team_name, 'Yankees')
        self.assertEqual(overview.away_team_runs, 1)
        self.assertEqual(overview.away_time, '7:10')
        self.assertEqual(overview.away_time_zone, 'ET')
        self.assertEqual(overview.away_win, 53)
        self.assertEqual(overview.balls, 0)
        self.assertEqual(overview.day, 'TUE')
        self.assertEqual(overview.double_header_sw, 'N')
        self.assertEqual(overview.first_pitch_et, '')
        self.assertEqual(overview.game_data_directory, '/components/game/mlb/year_2016/month_08/day_02/gid_2016_08_02_nyamlb_nynmlb_1')
        self.assertEqual(overview.game_nbr, 1)
        self.assertEqual(overview.game_pk, 448453)
        self.assertEqual(overview.game_type, 'R')
        self.assertEqual(overview.gameday_link, '2016_08_02_nyamlb_nynmlb_1')
        self.assertEqual(overview.gameday_sw, 'P')
        self.assertEqual(overview.hm_lg_ampm, 'PM')
        self.assertEqual(overview.home_ampm, 'PM')
        self.assertEqual(overview.home_code, 'nyn')
        self.assertEqual(overview.home_division, 'E')
        self.assertEqual(overview.home_file_code, 'nym')
        self.assertEqual(overview.home_games_back, 8.0)
        self.assertEqual(overview.home_games_back_wildcard, '-')
        self.assertEqual(overview.home_league_id, 104)
        self.assertEqual(overview.home_loss, 51)
        self.assertEqual(overview.home_name_abbrev, 'NYM')
        self.assertEqual(overview.home_preview_link, '/mlb/gameday/index.jsp?gid=2016_08_02_nyamlb_nynmlb_1&mode=preview&c_id=mlb')
        self.assertEqual(overview.home_recap_link, '/mlb/gameday/index.jsp?gid=2016_08_02_nyamlb_nynmlb_1&mode=recap&c_id=mlb')
        self.assertEqual(overview.home_sport_code, 'mlb')
        self.assertEqual(overview.home_team_city, 'NY Mets')
        self.assertEqual(overview.home_team_errors, 0)
        self.assertEqual(overview.home_team_hits, 10)
        self.assertEqual(overview.home_team_id, 121)
        self.assertEqual(overview.home_team_name, 'Mets')
        self.assertEqual(overview.home_team_runs, 7)
        self.assertEqual(overview.home_time, '7:10')
        self.assertEqual(overview.home_time_zone, 'ET')
        self.assertEqual(overview.home_win, 55)
        self.assertEqual(overview.id, '2016/08/02/nyamlb-nynmlb-1')
        self.assertEqual(overview.ind, 'F')
        self.assertEqual(overview.inning, 9)
        self.assertEqual(overview.inning_state, '')
        self.assertEqual(overview.is_no_hitter, 'N')
        self.assertEqual(overview.is_perfect_game, 'N')
        self.assertEqual(overview.league, 'AN')
        self.assertEqual(overview.location, 'Flushing, NY')
        self.assertEqual(overview.note, '')
        self.assertEqual(overview.original_date, '2016/08/02')
        self.assertEqual(overview.outs, 3)
        self.assertEqual(overview.photos_link, '/mlb/gameday/index.jsp?gid=2016_08_02_nyamlb_nynmlb_1&mode=photos')
        self.assertEqual(overview.preview, '/mlb/gameday/index.jsp?gid=2016_08_02_nyamlb_nynmlb_1&mode=preview&c_id=mlb')
        self.assertEqual(overview.scheduled_innings, 9)
        self.assertEqual(overview.status, 'Final')
        self.assertEqual(overview.strikes, 0)
        self.assertEqual(overview.tbd_flag, 'N')
        self.assertEqual(overview.tiebreaker_sw, 'N')
        self.assertEqual(overview.time, '7:10')
        self.assertEqual(overview.time_aw_lg, '7:10')
        self.assertEqual(overview.time_date, '2016/08/02 7:10')
        self.assertEqual(overview.time_date_aw_lg, '2016/08/02 7:10')
        self.assertEqual(overview.time_date_hm_lg, '2016/08/02 7:10')
        self.assertEqual(overview.time_hm_lg, '7:10')
        self.assertEqual(overview.time_zone, 'ET')
        self.assertEqual(overview.time_zone_aw_lg, -4)
        self.assertEqual(overview.time_zone_hm_lg, -4)
        self.assertEqual(overview.top_inning, 'Y')
        self.assertEqual(overview.tv_station, 'WPIX')
        self.assertEqual(overview.tz_aw_lg_gen, 'ET')
        self.assertEqual(overview.tz_hm_lg_gen, 'ET')
        self.assertEqual(overview.venue, 'Citi Field')
        self.assertEqual(overview.venue_id, 3289)
        self.assertEqual(overview.venue_w_chan_loc, 'USNY0504')
        self.assertEqual(overview.wrapup_link, '/mlb/gameday/index.jsp?gid=2016_08_02_nyamlb_nynmlb_1&mode=wrap&c_id=mlb')

    def test_players(self):
        players = mlbgame.players('2016_08_02_nyamlb_nynmlb_1')
        coaches = players.home_coaches + players.away_coaches
        umpires = players.umpires
        players = players.home_players + players.away_players
        for coach in coaches:
            self.assertIsInstance(coach.first, str)
            self.assertIsInstance(coach.id, int)
            self.assertIsInstance(coach.last, str)
            self.assertIsInstance(coach.num, (int, str))
            self.assertIsInstance(coach.position, str)
        for player in players:
            self.assertIsInstance(player.avg, float)
            self.assertIsInstance(player.bats, str)
            self.assertIsInstance(player.boxname, str)
            self.assertIsInstance(player.first, str)
            self.assertIsInstance(player.hr, int)
            self.assertIsInstance(player.id, int)
            self.assertIsInstance(player.last, str)
            self.assertIsInstance(player.num, (int, str))
            self.assertIsInstance(player.parent_team_abbrev, str)
            self.assertIsInstance(player.parent_team_id, int)
            self.assertIsInstance(player.position, str)
            self.assertIsInstance(player.rbi, int)
            self.assertIsInstance(player.rl, str)
            self.assertIsInstance(player.status, str)
            self.assertIsInstance(player.team_abbrev, str)
            self.assertIsInstance(player.team_id, int)
        for ump in umpires:
            self.assertIsInstance(ump.first, str)
            self.assertIsInstance(ump.id, int)
            self.assertIsInstance(ump.last, str)
            self.assertIsInstance(ump.name, str)
            self.assertIsInstance(ump.position, str)
        coach = coaches[0]
        player = players[0]
        ump = umpires[0]
        self.assertEqual(coach.first, 'Terry')
        self.assertEqual(coach.id, 492632)
        self.assertEqual(coach.last, 'Collins')
        self.assertEqual(coach.num, 10)
        self.assertEqual(coach.position, 'manager')
        self.assertEqual(player.avg, 0.079)
        self.assertEqual(player.bats, 'R')
        self.assertEqual(player.boxname, 'Colon')
        self.assertEqual(player.era, 3.58)
        self.assertEqual(player.first, 'Bartolo')
        self.assertEqual(player.hr, 1)
        self.assertEqual(player.id, 112526)
        self.assertEqual(player.last, 'Colon')
        self.assertEqual(player.losses, 6)
        self.assertEqual(player.num, 40)
        self.assertEqual(player.parent_team_abbrev, 'NYM')
        self.assertEqual(player.parent_team_id, 121)
        self.assertEqual(player.position, 'P')
        self.assertEqual(player.rbi, 2)
        self.assertEqual(player.rl, 'R')
        self.assertEqual(player.status, 'A')
        self.assertEqual(player.team_abbrev, 'NYM')
        self.assertEqual(player.team_id, 121)
        self.assertEqual(player.wins, 9)
        self.assertEqual(ump.first, 'Brian')
        self.assertEqual(ump.id, 427192)
        self.assertEqual(ump.last, 'Gorman')
        self.assertEqual(ump.name, 'Brian Gorman')
        self.assertEqual(ump.position, 'home')
