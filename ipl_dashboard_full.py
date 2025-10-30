# # # ============================================================
# # # 🏏 Simple IPL Analytics Dashboard (Streamlit)
# # # ============================================================

# # import streamlit as st
# # import pandas as pd
# # import plotly.express as px

# # # ------------------------------------------------------------
# # # Page Setup
# # # ------------------------------------------------------------
# # st.set_page_config(page_title="IPL Analytics Dashboard", layout="wide")
# # st.title("🏏 IPL Comprehensive Analytics Dashboard")

# # # ------------------------------------------------------------
# # # Upload / Load Data
# # # ------------------------------------------------------------
# # st.sidebar.header("📂 Data Input")
# # uploaded_file = st.sidebar.file_uploader("Upload IPL CSV file", type=["csv"], accept_multiple_files=False)

# # if uploaded_file is not None:
# #     df = pd.read_csv(uploaded_file)
# # else:
# #     st.info("Upload `ipl_data.csv` to get started.")
    
# #     st.stop()

# # # ------------------------------------------------------------
# # # Sidebar Filters
# # # ------------------------------------------------------------
# # teams = sorted(df['batting_team'].unique())
# # players = sorted(df['batter'].unique())

# # selected_team = st.sidebar.selectbox("Select Team", teams)
# # selected_player = st.sidebar.selectbox("Select Player", players)

# # # ------------------------------------------------------------
# # # Tabs for Sections
# # # ------------------------------------------------------------
# # tabs = st.tabs(["📊 Overview", "🏏 Team Insights", "👤 Player Insights", "📄 PDF Report"])

# # # ------------------------------------------------------------
# # # 📊 Overview
# # # ------------------------------------------------------------
# # with tabs[0]:
# #     st.subheader("General / Overview Insights")
# #     total_matches = df['match_id'].nunique()
# #     total_teams = df['batting_team'].nunique()
# #     total_runs = df['total_runs'].sum()
# #     total_wickets = df['is_wicket'].sum()
# #     total_balls = len(df)
# #     total_overs = total_balls / 6
# #     run_rate = total_runs / total_overs

# #     c1, c2, c3 = st.columns(3)
# #     c1.metric("Total Matches", total_matches)
# #     c2.metric("Total Teams", total_teams)
# #     c3.metric("Total Runs", f"{total_runs:,}")

# #     c4, c5, c6 = st.columns(3)
# #     c4.metric("Total Wickets", f"{total_wickets:,}")
# #     c5.metric("Total Overs", f"{total_overs:,.0f}")
# #     c6.metric("Run Rate", f"{run_rate:.2f}")

# #     st.divider()
# #     st.write("### Runs Distribution by Team")
# #     team_runs = df.groupby('batting_team')['total_runs'].sum().sort_values(ascending=False)
# #     fig = px.bar(team_runs, x=team_runs.index, y=team_runs.values, title="Total Runs by Team", color=team_runs.values, color_continuous_scale="sunset")
# #     st.plotly_chart(fig, use_container_width=True)

# # # ------------------------------------------------------------
# # # 🏏 Team Insights
# # # ------------------------------------------------------------
# # with tabs[1]:
# #     st.subheader(f"Team Analysis – {selected_team}")
# #     team_df = df[df['batting_team'] == selected_team]

# #     total_team_runs = team_df['total_runs'].sum()
# #     total_team_wkts = team_df['is_wicket'].sum()
# #     overs_team = len(team_df) / 6
# #     rr_team = total_team_runs / overs_team

# #     st.write(f"**Total Runs:** {total_team_runs:,} | **Wickets:** {total_team_wkts:,} | **Run Rate:** {rr_team:.2f}")

# #     phase_df = team_df.copy()
# #     phase_df['phase'] = pd.cut(phase_df['over'], bins=[0,6,15,20], labels=['Powerplay','Middle','Death'])
# #     phase_summary = phase_df.groupby('phase')['total_runs'].mean()

# #     fig = px.bar(phase_summary, x=phase_summary.index, y=phase_summary.values, title="Average Runs per Over by Phase", color=phase_summary.values)
# #     st.plotly_chart(fig, use_container_width=True)

# # # ------------------------------------------------------------
# # # 👤 Player Insights
# # # ------------------------------------------------------------
# # with tabs[2]:
# #     st.subheader(f"Player Analysis – {selected_player}")
# #     player_df = df[df['batter'] == selected_player]

# #     if len(player_df) > 0:
# #         total_runs_player = player_df['batsman_runs'].sum()
# #         balls_faced = len(player_df)
# #         fours = len(player_df[player_df['batsman_runs'] == 4])
# #         sixes = len(player_df[player_df['batsman_runs'] == 6])
# #         dismissals = player_df['is_wicket'].sum()
# #         avg = total_runs_player / dismissals if dismissals > 0 else total_runs_player
# #         sr = (total_runs_player / balls_faced) * 100

# #         st.write(f"**Runs:** {total_runs_player:,} | **Average:** {avg:.2f} | **Strike Rate:** {sr:.2f} | **4s:** {fours} | **6s:** {sixes}")

# #         st.divider()
# #         st.write("### Runs by Over")
# #         over_summary = player_df.groupby('over')['batsman_runs'].sum()
# #         fig = px.line(over_summary, x=over_summary.index, y=over_summary.values, markers=True, title=f"{selected_player} - Runs by Over")
# #         st.plotly_chart(fig, use_container_width=True)
# #     else:
# #         st.warning("No data available for this player in the dataset.")

# # # ------------------------------------------------------------
# # # 📄 PDF Report
# # # ------------------------------------------------------------
# # with tabs[3]:
# #     st.subheader("📄 IPL Insights PDF Report")
# #     try:
# #         with open("IPL_Comprehensive_Match_Insights.pdf", "rb") as pdf_file:
# #             st.download_button("⬇️ Download More Analytics PDF Report", data=pdf_file, file_name="ipl_report.pdf", mime="application/pdf")
# #         st.write("Preview of your report:")
# #         st.pdf("IPL_Comprehensive_Match_Insights.pdf")
# #     except FileNotFoundError:
# #         st.error("No `ipl_report.pdf` found in your folder. Please add it and refresh.")

# # # ------------------------------------------------------------
# # # End of App
# # # ------------------------------------------------------------
# # st.caption("© IPL Analytics Dashboard | Built with Streamlit")

# """
# ipl_dashboard_advanced.py
# Streamlit app: IPL Analytics Dashboard (Advanced: General -> Team -> Player Insights)
# Place this file in the same folder as:
#  - ipl_data.csv
#  - (optional) ipl_report.pdf

# Run:
#   python -m streamlit run ipl_dashboard_advanced.py
# """

# # import streamlit as st
# # import pandas as pd
# # import numpy as np
# # import plotly.express as px
# # import plotly.graph_objects as go
# # from io import BytesIO
# # import os

# # st.set_page_config(page_title="IPL Analytics — Advanced", layout="wide")
# # st.title("🏏 IPL Analytics — Advanced (General • Team • Player)")

# # # -------------------------
# # # Helper utilities
# # # -------------------------
# # @st.cache_data
# # def load_data(path="ipl_data.csv"):
# #     if not os.path.exists(path):
# #         st.error(f"Data file not found: {path}. Please upload or place it in the app folder.")
# #         return None
# #     df = pd.read_csv(path)
# #     # standardize column names to lower-case
# #     df.columns = [c.strip() for c in df.columns]
# #     # ensure numeric columns exist
# #     for col in ['total_runs', 'batsman_runs', 'extra_runs', 'is_wicket', 'over', 'ball', 'match_id']:
# #         if col not in df.columns:
# #             # Some datasets use different names; attempt best-effort mapping
# #             # Minimal fallback: create zeros/nans so code runs but warns
# #             st.warning(f"Column '{col}' not found in CSV — some metrics depending on it won't work.")
# #             if col == 'is_wicket':
# #                 df[col] = df.get(col, 0)
# #             else:
# #                 df[col] = df.get(col, 0)
# #     # attempt to parse season/year if present
# #     if 'season' not in df.columns and 'date' in df.columns:
# #         try:
# #             df['date'] = pd.to_datetime(df['date'], errors='coerce')
# #             df['season'] = df['date'].dt.year
# #         except Exception:
# #             pass
# #     # create handy columns
# #     if 'batter' not in df.columns and 'batsman' in df.columns:
# #         df.rename(columns={'batsman': 'batter'}, inplace=True)
# #     if 'bowler' not in df.columns:
# #         st.warning("Column 'bowler' missing — bowler-related metrics will be limited.")
# #     # fill NAs for grouping keys
# #     df['batting_team'] = df.get('batting_team', pd.Series(['Unknown']*len(df))).fillna('Unknown')
# #     df['bowling_team'] = df.get('bowling_team', pd.Series(['Unknown']*len(df))).fillna('Unknown')
# #     return df

# # def phase_from_over(o):
# #     if pd.isna(o):
# #         return "Other"
# #     try:
# #         o = int(o)
# #     except Exception:
# #         return "Other"
# #     if 1 <= o <= 6:
# #         return 'Powerplay'
# #     elif 7 <= o <= 15:
# #         return 'Middle'
# #     elif 16 <= o <= 20:
# #         return 'Death'
# #     else:
# #         return 'Other'

# # def safe_groupby_count(df, by, col):
# #     if col in df.columns:
# #         return df.groupby(by)[col].count().reset_index(name='count')
# #     else:
# #         return df.groupby(by).size().reset_index(name='count')

# # # -------------------------
# # # Load dataset (main)
# # # -------------------------
# # st.sidebar.header("Data")
# # uploaded = st.sidebar.file_uploader("Upload CSV (optional) — will override default ipl_data.csv", type=['csv'])
# # if uploaded is not None:
# #     df = pd.read_csv(uploaded)
# #     st.sidebar.success("Uploaded CSV loaded.")
# # else:
# #     df = load_data("ipl_data.csv")

# # if df is None:
# #     st.stop()

# # # Ensure key columns exist and have expected types
# # for c in ['total_runs', 'batsman_runs', 'extra_runs', 'over', 'match_id', 'ball']:
# #     if c in df.columns:
# #         df[c] = pd.to_numeric(df[c], errors='coerce').fillna(0)

# # # Create derived columns
# # if 'is_wicket' not in df.columns:
# #     # Try to infer from dismissal_kind
# #     if 'dismissal_kind' in df.columns:
# #         df['is_wicket'] = df['dismissal_kind'].notna().astype(int)
# #     else:
# #         df['is_wicket'] = 0

# # if 'season' not in df.columns:
# #     if 'date' in df.columns:
# #         try:
# #             df['date'] = pd.to_datetime(df['date'], errors='coerce')
# #             df['season'] = df['date'].dt.year
# #         except Exception:
# #             df['season'] = np.nan
# #     else:
# #         df['season'] = np.nan

# # df['phase'] = df['over'].apply(phase_from_over)

# # # Sidebar selectors
# # st.sidebar.subheader("Filters")
# # teams = sorted(df['batting_team'].dropna().unique())
# # players = sorted(df.get('batter', pd.Series([])).dropna().unique()) if 'batter' in df.columns else []
# # seasons = sorted([int(x) for x in df['season'].dropna().unique()]) if 'season' in df.columns else []

# # selected_team = st.sidebar.selectbox("Team (for Team Insights)", options=['All'] + teams)
# # selected_player = st.sidebar.selectbox("Player (for Player Insights)", options=['Select player'] + players)
# # selected_season = None
# # if seasons:
# #     selected_season = st.sidebar.selectbox("Season (optional filter)", options=['All'] + seasons)

# # # Main tabs
# # tabs = st.tabs(["Overview", "Team Insights", "Player Insights", "PDF Report"])

# # # -------------------------
# # # Overview tab
# # # -------------------------
# # with tabs[0]:
# #     st.header("General / Overview Insights")
# #     # Basic KPIs
# #     total_matches = int(df['match_id'].nunique())
# #     total_teams = int(df['batting_team'].nunique())
# #     total_runs = int(df['total_runs'].sum())
# #     total_wickets = int(df['is_wicket'].sum())
# #     total_balls = len(df)
# #     total_overs = total_balls / 6 if total_balls > 0 else 0
# #     overall_run_rate = total_runs / total_overs if total_overs > 0 else 0

# #     k1, k2, k3, k4 = st.columns(4)
# #     k1.metric("Total Matches", total_matches)
# #     k2.metric("Total Teams", total_teams)
# #     k3.metric("Total Runs", f"{total_runs:,}")
# #     k4.metric("Total Wickets", f"{total_wickets:,}")

# #     k5, k6, k7 = st.columns(3)
# #     k5.metric("Total Overs (approx.)", f"{total_overs:,.1f}")
# #     k6.metric("Total Balls", f"{total_balls:,}")
# #     k7.metric("Overall Run Rate (R/O)", f"{overall_run_rate:.2f}")

# #     st.markdown("---")

# #     # Dismissal distribution
# #     st.subheader("Dismissal Types Distribution")
# #     if 'dismissal_kind' in df.columns:
# #         dismiss_counts = df['dismissal_kind'].fillna('Not out').value_counts()
# #         fig = px.pie(names=dismiss_counts.index, values=dismiss_counts.values, title="Dismissal Types")
# #         st.plotly_chart(fig, use_container_width=True)
# #     else:
# #         st.info("No 'dismissal_kind' column found — can't compute dismissal distribution.")

# #     st.markdown("---")

# #     # Top batters and bowlers overall
# #     st.subheader("Top Players (Overall)")
# #     col1, col2 = st.columns(2)
# #     if 'batter' in df.columns:
# #         top_bat = df.groupby('batter')['batsman_runs'].sum().sort_values(ascending=False).head(15)
# #         col1.write("Top Batters (by runs)")
# #         col1.plotly_chart(px.bar(x=top_bat.index, y=top_bat.values, title="Top Batters by Runs"), use_container_width=True)
# #     else:
# #         col1.info("No 'batter' column.")

# #     if 'bowler' in df.columns:
# #         top_bowl = df[df['is_wicket']==1].groupby('bowler')['is_wicket'].sum().sort_values(ascending=False).head(15)
# #         col2.write("Top Wicket-Takers")
# #         col2.plotly_chart(px.bar(x=top_bowl.index, y=top_bowl.values, title="Top Wicket-Takers"), use_container_width=True)
# #     else:
# #         col2.info("No 'bowler' column to compute top wicket-takers.")

# #     st.markdown("---")

# #     # Match timeline by season (if season info available)
# #     st.subheader("Match / Runs Trend by Season")
# #     if 'season' in df.columns and df['season'].notna().any():
# #         season_runs = df.groupby('season')['total_runs'].sum().reset_index()
# #         fig = px.line(season_runs, x='season', y='total_runs', markers=True, title="Total Runs by Season")
# #         st.plotly_chart(fig, use_container_width=True)
# #     else:
# #         st.info("No 'season' or 'date' information found to show timeline.")

# # # -------------------------
# # # Team Insights tab
# # # -------------------------
# # with tabs[1]:
# #     st.header("Team Insights")

# #     # if team filter is 'All', show league-level comparisons
# #     if selected_team == 'All':
# #         st.subheader("League-level Team Summaries")
# #         runs_by_team = df.groupby('batting_team')['total_runs'].sum().sort_values(ascending=False)
# #         c1, c2 = st.columns([2,1])
# #         c1.plotly_chart(px.bar(x=runs_by_team.index, y=runs_by_team.values, title="Total Runs by Team"), use_container_width=True)
# #         # extras per over (discipline)
# #         st.markdown("### Discipline & Extras")
# #         if 'extra_runs' in df.columns:
# #             team_extras = df.groupby('bowling_team')['extra_runs'].sum().reset_index()
# #             overs_bowled = df.groupby(['bowling_team','match_id'])['over'].nunique().groupby('bowling_team').sum().reset_index(name='overs_bowled')
# #             team_extras = team_extras.merge(overs_bowled, on='bowling_team', how='left').fillna(0)
# #             team_extras['extras_per_over'] = (team_extras['extra_runs'] / team_extras['overs_bowled']).replace([np.inf, -np.inf], 0).round(2)
# #             st.plotly_chart(px.bar(team_extras.sort_values('extras_per_over'), x='bowling_team', y='extras_per_over', title='Extras per Over (lower=better)'), use_container_width=True)
# #         else:
# #             st.info("No 'extra_runs' column found.")

# #         st.markdown("---")
# #         st.subheader("Phase-wise Run Rates (All Teams)")
# #         phase_runrate = df.groupby(['batting_team','phase']).agg(runs=('total_runs','sum'), balls=('ball','count')).reset_index()
# #         phase_runrate['overs'] = phase_runrate['balls'] / 6
# #         phase_runrate['run_rate'] = (phase_runrate['runs'] / phase_runrate['overs']).replace([np.inf, -np.inf], 0)
# #         pivot = phase_runrate.pivot(index='batting_team', columns='phase', values='run_rate').fillna(0).reset_index()
# #         st.dataframe(pivot.sort_values(by=['Powerplay','Middle','Death'] if {'Powerplay','Middle','Death'}.issubset(pivot.columns) else pivot.columns.tolist()).head(20))
# #     else:
# #         # selected specific team
# #         st.subheader(f"Team: {selected_team}")
# #         team_df = df[df['batting_team'] == selected_team]

# #         # basic stats
# #         total_team_runs = int(team_df['total_runs'].sum())
# #         total_team_wickets = int(team_df['is_wicket'].sum())
# #         team_balls = len(team_df)
# #         team_overs = team_balls / 6 if team_balls>0 else 0
# #         rr = total_team_runs / team_overs if team_overs>0 else 0

# #         t1, t2, t3 = st.columns(3)
# #         t1.metric("Total Runs", f"{total_team_runs:,}")
# #         t2.metric("Total Wickets Conceded", f"{total_team_wickets:,}")
# #         t3.metric("Run Rate (R/O)", f"{rr:.2f}")

# #         st.markdown("---")
# #         # Phase-wise run rates for team
# #         st.subheader("Phase-wise Run Rate (Powerplay / Middle / Death)")
# #         phase_team = team_df.groupby('phase').agg(runs=('total_runs','sum'), balls=('ball','count')).reset_index()
# #         phase_team['overs'] = phase_team['balls'] / 6
# #         phase_team['run_rate'] = (phase_team['runs'] / phase_team['overs']).replace([np.inf, -np.inf], 0)
# #         fig = px.bar(phase_team, x='phase', y='run_rate', title=f"{selected_team} - Run Rate by Phase")
# #         st.plotly_chart(fig, use_container_width=True)

# #         st.markdown("---")
# #         # Top 3 batsmen and bowlers for this team
# #         st.subheader("Top Performers (Team)")
# #         if 'batter' in df.columns:
# #             top3_bats = team_df.groupby('batter')['batsman_runs'].sum().sort_values(ascending=False).head(10)
# #             st.write("Top batters for the team (by runs):")
# #             st.plotly_chart(px.bar(x=top3_bats.index, y=top3_bats.values, title="Top Batters (Team)"), use_container_width=True)
# #         else:
# #             st.info("No 'batter' column to show top batsmen.")

# #         if 'bowler' in df.columns:
# #             # bowlers when this team was bowling (bowling_team == selected_team)
# #             bowl_df = df[df['bowling_team'] == selected_team]
# #             top3_bowl = bowl_df[bowl_df['is_wicket']==1].groupby('bowler')['is_wicket'].sum().sort_values(ascending=False).head(10)
# #             st.write("Top wicket-takers for the team:")
# #             st.plotly_chart(px.bar(x=top3_bowl.index, y=top3_bowl.values, title="Top Bowlers (Team)"), use_container_width=True)
# #         else:
# #             st.info("No 'bowler' column to show top bowlers.")

# #         st.markdown("---")
# #         # Extras & discipline for this team when bowling
# #         if 'extra_runs' in df.columns:
# #             team_ex = df[df['bowling_team']==selected_team].groupby('match_id')['extra_runs'].sum().reset_index()
# #             st.write("Distribution of match extras conceded (by match):")
# #             st.plotly_chart(px.histogram(team_ex, x='extra_runs', nbins=20, title="Extras per Match (bowling)"), use_container_width=True)
# #         else:
# #             st.info("No 'extra_runs' column found.")

# #         st.markdown("---")
# #         # Team year-wise trend (if season present)
# #         if 'season' in df.columns and df['season'].notna().any():
# #             st.write("Year / Season trend — Total runs by season for team")
# #             team_season = team_df.groupby('season')['total_runs'].sum().reset_index()
# #             fig = px.line(team_season, x='season', y='total_runs', markers=True, title=f"{selected_team} - Runs by Season")
# #             st.plotly_chart(fig, use_container_width=True)
# #         else:
# #             st.info("No season/date column to show year-wise trend.")

# # # -------------------------
# # # Player Insights tab
# # # -------------------------
# # with tabs[2]:
# #     st.header("Player Insights")

# #     if selected_player == 'Select player':
# #         st.info("Choose a player from the sidebar to see detailed player insights.")
# #     else:
# #         if 'batter' not in df.columns:
# #             st.error("No 'batter' column found in dataset — player insights require batter column.")
# #         else:
# #             player_df = df[df['batter'] == selected_player].copy()
# #             if selected_season and selected_season != 'All':
# #                 player_df = player_df[player_df['season'] == int(selected_season)]

# #             if player_df.empty:
# #                 st.warning("No records found for this player with current filters.")
# #             else:
# #                 total_runs_player = int(player_df['batsman_runs'].sum())
# #                 balls_faced = int(player_df.shape[0])
# #                 fours = int((player_df['batsman_runs'] == 4).sum())
# #                 sixes = int((player_df['batsman_runs'] == 6).sum())
# #                 dismissals = int(player_df['is_wicket'].sum())
# #                 batting_avg = (total_runs_player / dismissals) if dismissals>0 else total_runs_player
# #                 strike_rate = (total_runs_player / balls_faced * 100) if balls_faced>0 else 0

# #                 c1, c2, c3, c4 = st.columns(4)
# #                 c1.metric("Total Runs", f"{total_runs_player:,}")
# #                 c2.metric("Balls Faced", f"{balls_faced:,}")
# #                 c3.metric("Batting Average", f"{batting_avg:.2f}")
# #                 c4.metric("Strike Rate", f"{strike_rate:.2f}")
# #                 st.markdown(f"**Boundaries:** 4s = {fours} | 6s = {sixes}")

# #                 st.markdown("---")
# #                 # Runs by over
# #                 st.subheader("Runs by Over (player)")
# #                 over_summary = player_df.groupby('over')['batsman_runs'].sum().reset_index()
# #                 fig = px.line(over_summary, x='over', y='batsman_runs', markers=True, title=f"{selected_player} - Runs by Over")
# #                 st.plotly_chart(fig, use_container_width=True)

# #                 st.markdown("---")
# #                 # Dismissal types for player
# #                 if 'dismissal_kind' in player_df.columns:
# #                     st.subheader("Dismissal Types (player)")
# #                     dk = player_df['dismissal_kind'].fillna('Not out').value_counts()
# #                     st.plotly_chart(px.pie(names=dk.index, values=dk.values, title=f"{selected_player} - Dismissal Types"), use_container_width=True)
# #                 else:
# #                     st.info("No 'dismissal_kind' column found for dismissal breakdown.")

# #                 st.markdown("---")
# #                 # Favorite bowlers faced and most runs vs single bowler
# #                 st.subheader("Favorite / Most Successful Bowlers vs Player")
# #                 if 'bowler' in df.columns:
# #                     faced = player_df.groupby('bowler')['batsman_runs'].sum().sort_values(ascending=False).head(15)
# #                     st.write("Top bowlers conceded most runs to (i.e., bowlers the player scored most off):")
# #                     st.plotly_chart(px.bar(x=faced.index, y=faced.values, title=f"Most runs off bowlers vs {selected_player}"), use_container_width=True)
# #                     # most dismissals by bowler on player
# #                     dismissals_by_bowler = player_df[player_df['is_wicket']==1].groupby('bowler')['is_wicket'].sum().sort_values(ascending=False).head(10)
# #                     st.write("Bowlers who dismissed this player most often:")
# #                     st.plotly_chart(px.bar(x=dismissals_by_bowler.index, y=dismissals_by_bowler.values, title=f"Bowlers dismissing {selected_player} most"), use_container_width=True)
# #                 else:
# #                     st.info("No 'bowler' column present to analyze bowlers vs player.")

# #                 st.markdown("---")
# #                 # Year-wise performance (if season exists)
# #                 if 'season' in df.columns and df['season'].notna().any():
# #                     st.subheader("Season-wise Performance")
# #                     season_summary = player_df.groupby('season')['batsman_runs'].sum().reset_index()
# #                     st.plotly_chart(px.bar(season_summary, x='season', y='batsman_runs', title=f"{selected_player} - Runs by Season"), use_container_width=True)
# #                 else:
# #                     st.info("No 'season' info to show season-wise trend.")

# #                 st.markdown("---")
# #                 # Partnership analysis (batter + non_striker)
# #                 if 'non_striker' in df.columns:
# #                     st.subheader("Top Partnerships (player with non-strikers)")
# #                     pairs = player_df.groupby('non_striker')['batsman_runs'].sum().sort_values(ascending=False).head(15)
# #                     st.plotly_chart(px.bar(x=pairs.index, y=pairs.values, title=f"{selected_player} - Partnership Runs (non-striker)"), use_container_width=True)
# #                 else:
# #                     st.info("No 'non_striker' column — cannot compute partnerships.")

# # -------------------------
# # PDF Report tab
# # -------------------------

# # ============================================================
# # 🏏 IPL Analytics Dashboard – Advanced (with Comparison Mode)
# # ============================================================

# import streamlit as st
# import pandas as pd
# import plotly.express as px
# import os

# # ------------------------------------------------------------
# # Page Configuration
# # ------------------------------------------------------------
# st.set_page_config(page_title="IPL Analytics Dashboard", layout="wide")
# st.title("🏏 IPL Comprehensive Analytics Dashboard")

# # ------------------------------------------------------------
# # Data Upload
# # ------------------------------------------------------------
# st.sidebar.header("📂 Data Input")
# uploaded_file = st.sidebar.file_uploader("Upload IPL CSV file", type=["csv"])

# if uploaded_file is not None:
#     df = pd.read_csv(uploaded_file)
# else:
#     st.info("Upload `ipl_data.csv` to start analysis.")
#     st.stop()

# # ------------------------------------------------------------
# # Sidebar Filters
# # ------------------------------------------------------------
# teams = sorted(df['batting_team'].dropna().unique())
# players = sorted(df['batter'].dropna().unique())

# selected_team = st.sidebar.selectbox("Select Team", teams)
# selected_player = st.sidebar.selectbox("Select Player", players)

# # ------------------------------------------------------------
# # Tabs
# # ------------------------------------------------------------
# tabs = st.tabs([
#     "📊 Overview",
#     "🏏 Team Insights",
#     "👤 Player Insights",
#     "⚔️ Comparison Mode",
#     "📄 PDF Report"
# ])

# # ------------------------------------------------------------
# # 📊 Overview
# # ------------------------------------------------------------
# with tabs[0]:
#     st.subheader("General / Overview Insights")

#     total_matches = df['match_id'].nunique()
#     total_teams = df['batting_team'].nunique()
#     total_runs = df['total_runs'].sum()
#     total_wickets = df['is_wicket'].sum()
#     total_balls = len(df)
#     total_overs = total_balls / 6
#     run_rate = total_runs / total_overs

#     c1, c2, c3 = st.columns(3)
#     c1.metric("Total Matches", total_matches)
#     c2.metric("Total Teams", total_teams)
#     c3.metric("Total Runs", f"{total_runs:,}")

#     c4, c5, c6 = st.columns(3)
#     c4.metric("Total Wickets", f"{total_wickets:,}")
#     c5.metric("Total Overs", f"{total_overs:,.0f}")
#     c6.metric("Run Rate", f"{run_rate:.2f}")

#     st.divider()
#     st.write("### Runs Distribution by Team")
#     team_runs = df.groupby('batting_team')['total_runs'].sum().sort_values(ascending=False)
#     fig = px.bar(team_runs, x=team_runs.index, y=team_runs.values,
#                  title="Total Runs by Team", color=team_runs.values,
#                  color_continuous_scale="sunset")
#     st.plotly_chart(fig, use_container_width=True)

#     st.divider()
#     st.write("### Dismissal Type Distribution")
#     dismissal_counts = df['dismissal_kind'].dropna().value_counts()
#     fig = px.pie(values=dismissal_counts.values, names=dismissal_counts.index,
#                  title="Types of Dismissals", hole=0.4)
#     st.plotly_chart(fig, use_container_width=True)

# # ------------------------------------------------------------
# # 🏏 Team Insights
# # ------------------------------------------------------------


# with tabs[1]:
#     st.subheader(f"Team Analysis – {selected_team}")
#     team_df = df[df['batting_team'] == selected_team]

#     total_team_runs = team_df['total_runs'].sum()
#     total_team_wkts = team_df['is_wicket'].sum()
#     overs_team = len(team_df) / 6
#     rr_team = total_team_runs / overs_team

#     st.write(f"**Total Runs:** {total_team_runs:,} | **Wickets:** {total_team_wkts:,} | **Run Rate:** {rr_team:.2f}")

#     # Phase-wise performance
#     phase_df = team_df.copy()
#     phase_df['phase'] = pd.cut(phase_df['over'], bins=[0,6,15,20],
#                                labels=['Powerplay','Middle','Death'])
#     phase_summary = phase_df.groupby('phase')['total_runs'].mean()

#     fig = px.bar(phase_summary, x=phase_summary.index, y=phase_summary.values,
#                  title="Average Runs per Over by Phase", color=phase_summary.values)
#     st.plotly_chart(fig, use_container_width=True)

#     # Extras discipline
#     # Extras discipline (auto-detect column)
#     extras_col = None
#     for col in ['extras', 'extra_runs', 'Extra_Runs', 'Extras']:
#         if col in df.columns:
#             extras_col = col
#             break

#     if extras_col:
#         extras_df = team_df.groupby('bowling_team')[extras_col].sum().sort_values(ascending=True)
#         fig = px.bar(extras_df, x=extras_df.index, y=extras_df.values,
#                     title="Extras Conceded Against Each Team", color=extras_df.values)
#         st.plotly_chart(fig, use_container_width=True)
#     else:
#         st.warning("Extras column not found in dataset — skipping extras discipline chart.")


# # ------------------------------------------------------------
# # 👤 Player Insights
# # ------------------------------------------------------------
# with tabs[2]:
#     st.subheader(f"Player Analysis – {selected_player}")
#     player_df = df[df['batter'] == selected_player]

#     if len(player_df) > 0:
#         total_runs_player = player_df['batsman_runs'].sum()
#         balls_faced = len(player_df)
#         fours = len(player_df[player_df['batsman_runs'] == 4])
#         sixes = len(player_df[player_df['batsman_runs'] == 6])
#         dismissals = player_df['is_wicket'].sum()
#         avg = total_runs_player / dismissals if dismissals > 0 else total_runs_player
#         sr = (total_runs_player / balls_faced) * 100

#         st.write(f"**Runs:** {total_runs_player:,} | **Average:** {avg:.2f} | **Strike Rate:** {sr:.2f} | **4s:** {fours} | **6s:** {sixes}")

#         st.divider()
#         st.write("### Runs by Over")
#         over_summary = player_df.groupby('over')['batsman_runs'].sum()
#         fig = px.line(over_summary, x=over_summary.index, y=over_summary.values,
#                       markers=True, title=f"{selected_player} - Runs by Over")
#         st.plotly_chart(fig, use_container_width=True)

#         st.divider()
#         st.write("### Dismissal Type Distribution")
#         dismissal_counts = player_df['dismissal_kind'].dropna().value_counts()
#         fig = px.pie(values=dismissal_counts.values, names=dismissal_counts.index,
#                      title=f"{selected_player} - Dismissal Types", hole=0.4)
#         st.plotly_chart(fig, use_container_width=True)
#     else:
#         st.warning("No data available for this player in the dataset.")

# # ------------------------------------------------------------
# # ⚔️ Comparison Mode
# # ------------------------------------------------------------
# with tabs[3]:
#     st.subheader("⚔️ Comparison Mode")

#     compare_type = st.radio("Choose Comparison Type", ["Team vs Team", "Player vs Player"], horizontal=True)

#     if compare_type == "Team vs Team":
#         team1 = st.selectbox("Select Team 1", teams, key="t1")
#         team2 = st.selectbox("Select Team 2", teams, key="t2")

#         if team1 and team2:
#             c1, c2 = st.columns(2)

#             for col, team in zip([c1, c2], [team1, team2]):
#                 t_df = df[df['batting_team'] == team]
#                 runs = t_df['total_runs'].sum()
#                 wkts = t_df['is_wicket'].sum()
#                 overs = len(t_df) / 6
#                 rr = runs / overs

#                 col.write(f"### {team}")
#                 col.metric("Runs", f"{runs:,}")
#                 col.metric("Wickets", wkts)
#                 col.metric("Run Rate", f"{rr:.2f}")

#             st.divider()
#             st.write("### Phase-wise Run Rate Comparison")
#             phase_df = df.copy()
#             phase_df['phase'] = pd.cut(phase_df['over'], bins=[0,6,15,20],
#                                        labels=['Powerplay','Middle','Death'])
#             compare_phase = phase_df.groupby(['batting_team', 'phase'])['total_runs'].mean().reset_index()
#             compare_phase = compare_phase[compare_phase['batting_team'].isin([team1, team2])]
#             fig = px.bar(compare_phase, x="phase", y="total_runs",
#                          color="batting_team", barmode="group",
#                          title="Phase-wise Average Runs per Over")
#             st.plotly_chart(fig, use_container_width=True)

#     else:
#         player1 = st.selectbox("Select Player 1", players, key="p1")
#         player2 = st.selectbox("Select Player 2", players, key="p2")

#         if player1 and player2:
#             p1_df = df[df['batter'] == player1]
#             p2_df = df[df['batter'] == player2]

#             def player_stats(p_df):
#                 runs = p_df['batsman_runs'].sum()
#                 balls = len(p_df)
#                 sr = (runs / balls) * 100 if balls > 0 else 0
#                 dismissals = p_df['is_wicket'].sum()
#                 avg = runs / dismissals if dismissals > 0 else runs
#                 return runs, avg, sr

#             runs1, avg1, sr1 = player_stats(p1_df)
#             runs2, avg2, sr2 = player_stats(p2_df)

#             c1, c2 = st.columns(2)
#             c1.write(f"### {player1}")
#             c1.metric("Runs", f"{runs1:,}")
#             c1.metric("Average", f"{avg1:.2f}")
#             c1.metric("Strike Rate", f"{sr1:.2f}")

#             c2.write(f"### {player2}")
#             c2.metric("Runs", f"{runs2:,}")
#             c2.metric("Average", f"{avg2:.2f}")
#             c2.metric("Strike Rate", f"{sr2:.2f}")

#             st.divider()
#             st.write("### Runs by Over Comparison")
#             over1 = p1_df.groupby('over')['batsman_runs'].sum().reset_index()
#             over2 = p2_df.groupby('over')['batsman_runs'].sum().reset_index()
#             over1['Player'] = player1
#             over2['Player'] = player2
#             both = pd.concat([over1, over2])
#             fig = px.line(both, x="over", y="batsman_runs", color="Player",
#                           markers=True, title="Runs by Over Comparison")
#             st.plotly_chart(fig, use_container_width=True)
# with tabs[4]:
#     st.header("PDF Report")
#     pdf_path = "IPL_Comprehensive_Match_Insights.pdf"
#     if os.path.exists(pdf_path):
#         st.write("Download or preview the provided PDF report.")
#         with open(pdf_path, "rb") as f:
#             st.download_button("⬇️ Download PDF", data=f, file_name="IPL_Comprehensive_Match_Insights.pdf", mime="application/pdf")
#         try:
#             st.write("PDF preview below:")
#             st.pdf(pdf_path)
#         except Exception:
#             st.info("PDF preview not available in this environment — use download button.")
#     else:
#         st.info("No `IPL_Comprehensive_Match_Insights.pdf` found in the folder. You can place it beside this app to enable preview/download.")

# st.markdown("---")
# st.caption("Built By Henil — Advanced IPL Insights (General → Team → Player). Modify thresholds and filters inside the app file as needed.")
"""
ipl_dashboard_advanced.py
Streamlit app: IPL Analytics Dashboard (Advanced: General -> Team -> Player Insights + Comparison Mode)
Place this file in the same folder as:
 - ipl_data.csv
 - (optional) IPL_Comprehensive_Match_Insights.pdf

Run:
  python -m streamlit run "d:/Data Science Prep/Project_2/ipl_dashboard_advanced.py"
"""

import os
from io import BytesIO

import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

# -------------------------
# Page / Config
# -------------------------
st.set_page_config(page_title="IPL Analytics — Advanced", layout="wide")
st.title("🏏 IPL Analytics — Advanced (General • Team • Player • Comparison)")

# -------------------------
# Helper utilities
# -------------------------
@st.cache_data
def load_data(path="ipl_data.csv"):
    if not os.path.exists(path):
        st.error(f"Data file not found: {path}. Please upload or place it in the app folder.")
        return None

    df = pd.read_csv(path)
    # normalize column names (strip)
    df.columns = [c.strip() for c in df.columns]

    # attempt common renames/fallbacks
    if 'batsman' in df.columns and 'batter' not in df.columns:
        df.rename(columns={'batsman': 'batter'}, inplace=True)
    if 'batsman_runs' not in df.columns and 'batsman run' in df.columns:
        df.rename(columns={'batsman run': 'batsman_runs'}, inplace=True)

    # Provide default columns if missing (with warnings)
    for col in ['total_runs', 'batsman_runs', 'extra_runs', 'is_wicket', 'over', 'ball', 'match_id']:
        if col not in df.columns:
            # best-effort: if similar name exists, map; else create
            if col == 'total_runs' and 'runs' in df.columns:
                df.rename(columns={'runs': 'total_runs'}, inplace=True)
            elif col == 'is_wicket' and 'player_dismissed' in df.columns:
                # we'll infer is_wicket later; just continue
                pass
            else:
                # create safe default column so code doesn't crash
                st.warning(f"Column '{col}' not found in CSV — creating fallback column with zeros. Some metrics will be limited.")
                df[col] = 0

    # infer is_wicket from dismissal_kind if needed
    if 'is_wicket' not in df.columns or df['is_wicket'].isnull().all():
        if 'dismissal_kind' in df.columns:
            df['is_wicket'] = df['dismissal_kind'].notna().astype(int)
        else:
            df['is_wicket'] = df.get('is_wicket', 0)

    # parse date -> season if possible
    if 'season' not in df.columns:
        if 'date' in df.columns:
            try:
                df['date'] = pd.to_datetime(df['date'], errors='coerce')
                df['season'] = df['date'].dt.year
            except Exception:
                df['season'] = np.nan
        else:
            df['season'] = np.nan

    # fill team columns if missing
    df['batting_team'] = df.get('batting_team', pd.Series(['Unknown'] * len(df))).fillna('Unknown')
    df['bowling_team'] = df.get('bowling_team', pd.Series(['Unknown'] * len(df))).fillna('Unknown')

    # ensure numeric types for key columns
    for c in ['total_runs', 'batsman_runs', 'extra_runs', 'over', 'ball', 'match_id', 'is_wicket']:
        if c in df.columns:
            df[c] = pd.to_numeric(df[c], errors='coerce').fillna(0)

    return df


def phase_from_over(o):
    try:
        o = int(o)
    except Exception:
        return 'Other'
    if 1 <= o <= 6:
        return 'Powerplay'
    elif 7 <= o <= 15:
        return 'Middle'
    elif 16 <= o <= 20:
        return 'Death'
    else:
        return 'Other'


def detect_extras_column(df):
    for col in ['extra_runs', 'extras', 'Extra_Runs', 'Extras']:
        if col in df.columns:
            return col
    return None


# -------------------------
# Load dataset (main)
# -------------------------
st.sidebar.header("Data")
uploaded = st.sidebar.file_uploader("Upload CSV (optional) — will override default ipl_data.csv", type=['csv'])
if uploaded is not None:
    df = pd.read_csv(uploaded)
    st.sidebar.success("Uploaded CSV loaded.")
else:
    df = load_data("ipl_data.csv")

if df is None:
    st.stop()

# unify names if possible
if 'batsman' in df.columns and 'batter' not in df.columns:
    df.rename(columns={'batsman': 'batter'}, inplace=True)
if 'ball' not in df.columns and 'ball_in_over' in df.columns:
    df.rename(columns={'ball_in_over': 'ball'}, inplace=True)

# derived columns
if 'is_wicket' not in df.columns:
    if 'dismissal_kind' in df.columns:
        df['is_wicket'] = df['dismissal_kind'].notna().astype(int)
    else:
        df['is_wicket'] = 0

if 'season' not in df.columns:
    if 'date' in df.columns:
        try:
            df['date'] = pd.to_datetime(df['date'], errors='coerce')
            df['season'] = df['date'].dt.year
        except Exception:
            df['season'] = np.nan
    else:
        df['season'] = np.nan

# create phase column
df['phase'] = df['over'].apply(phase_from_over)

# -------------------------
# Sidebar selectors
# -------------------------
st.sidebar.subheader("Filters")
teams = sorted(df['batting_team'].dropna().unique())
players = sorted(df.get('batter', pd.Series([])).dropna().unique()) if 'batter' in df.columns else []
seasons = sorted([int(x) for x in df['season'].dropna().unique()]) if 'season' in df.columns and df['season'].notna().any() else []

selected_team = st.sidebar.selectbox("Team (for Team Insights)", options=['All'] + teams)
selected_player = st.sidebar.selectbox("Player (for Player Insights)", options=['Select player'] + players)
selected_season = None
if seasons:
    selected_season = st.sidebar.selectbox("Season (optional filter)", options=['All'] + seasons)

# -------------------------
# Main tabs
# -------------------------
tabs = st.tabs(["Overview", "Team Insights", "Player Insights", "⚔️ Comparison Mode", "PDF Report"])

# -------------------------
# Overview tab
# -------------------------
with tabs[0]:
    st.header("General / Overview Insights")
    total_matches = int(df['match_id'].nunique()) if 'match_id' in df.columns else int(df.shape[0])
    total_teams = int(df['batting_team'].nunique())
    total_runs = int(df['total_runs'].sum()) if 'total_runs' in df.columns else int(df['batsman_runs'].sum())
    total_wickets = int(df['is_wicket'].sum())
    total_balls = len(df)
    total_overs = total_balls / 6 if total_balls > 0 else 0
    overall_run_rate = total_runs / total_overs if total_overs > 0 else 0

    k1, k2, k3, k4 = st.columns(4)
    k1.metric("Total Matches", total_matches)
    k2.metric("Total Teams", total_teams)
    k3.metric("Total Runs", f"{total_runs:,}")
    k4.metric("Total Wickets", f"{total_wickets:,}")

    k5, k6, k7 = st.columns(3)
    k5.metric("Total Overs (approx.)", f"{total_overs:,.1f}")
    k6.metric("Total Balls", f"{total_balls:,}")
    k7.metric("Overall Run Rate (R/O)", f"{overall_run_rate:.2f}")

    st.markdown("---")

    # Dismissal distribution
    st.subheader("Dismissal Types Distribution")
    if 'dismissal_kind' in df.columns:
        dismiss_counts = df['dismissal_kind'].fillna('Not out').value_counts()
        fig = px.pie(names=dismiss_counts.index, values=dismiss_counts.values, title="Dismissal Types")
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("No 'dismissal_kind' column found — can't compute dismissal distribution.")

    st.markdown("---")

    # Top batters and bowlers overall
    st.subheader("Top Players (Overall)")
    col1, col2 = st.columns(2)
    if 'batter' in df.columns and 'batsman_runs' in df.columns:
        top_bat = df.groupby('batter')['batsman_runs'].sum().sort_values(ascending=False).head(15)
        col1.write("Top Batters (by runs)")
        col1.plotly_chart(px.bar(x=top_bat.index, y=top_bat.values, title="Top Batters by Runs"), use_container_width=True)
    else:
        col1.info("No 'batter' or 'batsman_runs' column.")

    if 'bowler' in df.columns:
        top_bowl = df[df['is_wicket'] == 1].groupby('bowler')['is_wicket'].sum().sort_values(ascending=False).head(15)
        col2.write("Top Wicket-Takers")
        col2.plotly_chart(px.bar(x=top_bowl.index, y=top_bowl.values, title="Top Wicket-Takers"), use_container_width=True)
    else:
        col2.info("No 'bowler' column to compute top wicket-takers.")

    st.markdown("---")

    # Match timeline by season (if season info available)
    st.subheader("Match / Runs Trend by Season")
    if 'season' in df.columns and df['season'].notna().any():
        season_runs = df.groupby('season')['total_runs'].sum().reset_index()
        fig = px.line(season_runs, x='season', y='total_runs', markers=True, title="Total Runs by Season")
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("No 'season' or 'date' information found to show timeline.")

# -------------------------
# Team Insights tab
# -------------------------
with tabs[1]:
    st.header("Team Insights")

    if selected_team == 'All':
        st.subheader("League-level Team Summaries")
        if 'total_runs' in df.columns:
            runs_by_team = df.groupby('batting_team')['total_runs'].sum().sort_values(ascending=False)
        else:
            runs_by_team = df.groupby('batting_team')['batsman_runs'].sum().sort_values(ascending=False)

        c1, c2 = st.columns([2, 1])
        c1.plotly_chart(px.bar(x=runs_by_team.index, y=runs_by_team.values, title="Total Runs by Team"), use_container_width=True)

        # extras per over (discipline) - auto detect extras column
        st.markdown("### Discipline & Extras")
        extras_col = detect_extras_column(df)
        if extras_col:
            team_extras = df.groupby('bowling_team')[extras_col].sum().reset_index()
            overs_bowled = df.groupby(['bowling_team', 'match_id'])['over'].nunique().groupby('bowling_team').sum().reset_index(name='overs_bowled')
            team_extras = team_extras.merge(overs_bowled, on='bowling_team', how='left').fillna(0)
            team_extras['extras_per_over'] = (team_extras[extras_col] / team_extras['overs_bowled']).replace([np.inf, -np.inf], 0).round(2)
            st.plotly_chart(px.bar(team_extras.sort_values('extras_per_over'), x='bowling_team', y='extras_per_over', title='Extras per Over (lower=better)'), use_container_width=True)
        else:
            st.info("No extras column (extra_runs/extras) found.")

        st.markdown("---")
        st.subheader("Phase-wise Run Rates (All Teams)")
        phase_runrate = df.groupby(['batting_team', 'phase']).agg(runs=('total_runs', 'sum'), balls=('ball', 'count')).reset_index()
        phase_runrate['overs'] = phase_runrate['balls'] / 6
        phase_runrate['run_rate'] = (phase_runrate['runs'] / phase_runrate['overs']).replace([np.inf, -np.inf], 0)
        pivot = phase_runrate.pivot(index='batting_team', columns='phase', values='run_rate').fillna(0).reset_index()
        sort_cols = [c for c in ['Powerplay', 'Middle', 'Death'] if c in pivot.columns]
        st.dataframe(pivot.sort_values(by=sort_cols, ascending=False).head(20))
    else:
        st.subheader(f"Team: {selected_team}")
        team_df = df[df['batting_team'] == selected_team]

        total_team_runs = int(team_df['total_runs'].sum()) if 'total_runs' in team_df.columns else int(team_df['batsman_runs'].sum())
        total_team_wickets = int(team_df['is_wicket'].sum())
        team_balls = len(team_df)
        team_overs = team_balls / 6 if team_balls > 0 else 0
        rr = total_team_runs / team_overs if team_overs > 0 else 0

        t1, t2, t3 = st.columns(3)
        t1.metric("Total Runs", f"{total_team_runs:,}")
        t2.metric("Total Wickets Conceded", f"{total_team_wickets:,}")
        t3.metric("Run Rate (R/O)", f"{rr:.2f}")

        st.markdown("---")
        st.subheader("Phase-wise Run Rate (Powerplay / Middle / Death)")
        phase_team = team_df.groupby('phase').agg(runs=('total_runs', 'sum'), balls=('ball', 'count')).reset_index()
        phase_team['overs'] = phase_team['balls'] / 6
        phase_team['run_rate'] = (phase_team['runs'] / phase_team['overs']).replace([np.inf, -np.inf], 0)
        fig = px.bar(phase_team, x='phase', y='run_rate', title=f"{selected_team} - Run Rate by Phase")
        st.plotly_chart(fig, use_container_width=True)

        st.markdown("---")
        st.subheader("Top Performers (Team)")
        if 'batter' in df.columns:
            top3_bats = team_df.groupby('batter')['batsman_runs'].sum().sort_values(ascending=False).head(10)
            st.write("Top batters for the team (by runs):")
            st.plotly_chart(px.bar(x=top3_bats.index, y=top3_bats.values, title="Top Batters (Team)"), use_container_width=True)
        else:
            st.info("No 'batter' column to show top batsmen.")

        if 'bowler' in df.columns:
            bowl_df = df[df['bowling_team'] == selected_team]
            top3_bowl = bowl_df[bowl_df['is_wicket'] == 1].groupby('bowler')['is_wicket'].sum().sort_values(ascending=False).head(10)
            st.write("Top wicket-takers for the team:")
            st.plotly_chart(px.bar(x=top3_bowl.index, y=top3_bowl.values, title="Top Bowlers (Team)"), use_container_width=True)
        else:
            st.info("No 'bowler' column to show top bowlers.")

        st.markdown("---")
        extras_col = detect_extras_column(df)
        if extras_col:
            team_ex = df[df['bowling_team'] == selected_team].groupby('match_id')[extras_col].sum().reset_index()
            st.write("Distribution of match extras conceded (by match):")
            st.plotly_chart(px.histogram(team_ex, x=extras_col, nbins=20, title="Extras per Match (bowling)"), use_container_width=True)
        else:
            st.info("No extras column found for extras distribution.")

        st.markdown("---")
        if 'season' in df.columns and df['season'].notna().any():
            st.write("Year / Season trend — Total runs by season for team")
            team_season = team_df.groupby('season')['total_runs'].sum().reset_index()
            fig = px.line(team_season, x='season', y='total_runs', markers=True, title=f"{selected_team} - Runs by Season")
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("No season/date column to show year-wise trend.")

# -------------------------
# Player Insights tab
# -------------------------
with tabs[2]:
    st.header("Player Insights")

    if selected_player == 'Select player':
        st.info("Choose a player from the sidebar to see detailed player insights.")
    else:
        if 'batter' not in df.columns:
            st.error("No 'batter' column found in dataset — player insights require batter column.")
        else:
            player_df = df[df['batter'] == selected_player].copy()
            if selected_season and selected_season != 'All':
                player_df = player_df[player_df['season'] == int(selected_season)]

            if player_df.empty:
                st.warning("No records found for this player with current filters.")
            else:
                total_runs_player = int(player_df['batsman_runs'].sum())
                balls_faced = int(player_df.shape[0])
                fours = int((player_df['batsman_runs'] == 4).sum())
                sixes = int((player_df['batsman_runs'] == 6).sum())
                dismissals = int(player_df['is_wicket'].sum())
                batting_avg = (total_runs_player / dismissals) if dismissals > 0 else total_runs_player
                strike_rate = (total_runs_player / balls_faced * 100) if balls_faced > 0 else 0

                c1, c2, c3, c4 = st.columns(4)
                c1.metric("Total Runs", f"{total_runs_player:,}")
                c2.metric("Balls Faced", f"{balls_faced:,}")
                c3.metric("Batting Average", f"{batting_avg:.2f}")
                c4.metric("Strike Rate", f"{strike_rate:.2f}")
                st.markdown(f"**Boundaries:** 4s = {fours} | 6s = {sixes}")

                st.markdown("---")
                st.subheader("Runs by Over (player)")
                over_summary = player_df.groupby('over')['batsman_runs'].sum().reset_index()
                fig = px.line(over_summary, x='over', y='batsman_runs', markers=True, title=f"{selected_player} - Runs by Over")
                st.plotly_chart(fig, use_container_width=True)

                st.markdown("---")
                if 'dismissal_kind' in player_df.columns:
                    st.subheader("Dismissal Types (player)")
                    dk = player_df['dismissal_kind'].fillna('Not out').value_counts()
                    st.plotly_chart(px.pie(names=dk.index, values=dk.values, title=f"{selected_player} - Dismissal Types"), use_container_width=True)
                else:
                    st.info("No 'dismissal_kind' column found for dismissal breakdown.")

                st.markdown("---")
                st.subheader("Favorite / Most Successful Bowlers vs Player")
                if 'bowler' in df.columns:
                    faced = player_df.groupby('bowler')['batsman_runs'].sum().sort_values(ascending=False).head(15)
                    st.write("Top bowlers conceded most runs to (i.e., bowlers the player scored most off):")
                    st.plotly_chart(px.bar(x=faced.index, y=faced.values, title=f"Most runs off bowlers vs {selected_player}"), use_container_width=True)

                    dismissals_by_bowler = player_df[player_df['is_wicket'] == 1].groupby('bowler')['is_wicket'].sum().sort_values(ascending=False).head(10)
                    st.write("Bowlers who dismissed this player most often:")
                    st.plotly_chart(px.bar(x=dismissals_by_bowler.index, y=dismissals_by_bowler.values, title=f"Bowlers dismissing {selected_player} most"), use_container_width=True)
                else:
                    st.info("No 'bowler' column present to analyze bowlers vs player.")

                st.markdown("---")
                if 'season' in df.columns and df['season'].notna().any():
                    st.subheader("Season-wise Performance")
                    season_summary = player_df.groupby('season')['batsman_runs'].sum().reset_index()
                    st.plotly_chart(px.bar(season_summary, x='season', y='batsman_runs', title=f"{selected_player} - Runs by Season"), use_container_width=True)
                else:
                    st.info("No 'season' info to show season-wise trend.")

                st.markdown("---")
                if 'non_striker' in df.columns:
                    st.subheader("Top Partnerships (player with non-strikers)")
                    pairs = player_df.groupby('non_striker')['batsman_runs'].sum().sort_values(ascending=False).head(15)
                    st.plotly_chart(px.bar(x=pairs.index, y=pairs.values, title=f"{selected_player} - Partnership Runs (non-striker)"), use_container_width=True)
                else:
                    st.info("No 'non_striker' column — cannot compute partnerships.")

# -------------------------
# Comparison Mode tab (new)
# -------------------------
with tabs[3]:
    st.header("⚔️ Comparison Mode")
    mode = st.radio("Compare", options=["Team vs Team", "Player vs Player"], horizontal=True)

    if mode == "Team vs Team":
        st.subheader("Compare Two Teams")
        comp_col1, comp_col2 = st.columns([1, 1])
        with comp_col1:
            team_a = st.selectbox("Team A", options=teams, key="comp_team_a")
        with comp_col2:
            team_b = st.selectbox("Team B", options=teams, key="comp_team_b")

        if team_a and team_b:
            left, right = st.columns(2)
            for col, team in zip([left, right], [team_a, team_b]):
                team_df = df[df['batting_team'] == team]
                runs = int(team_df['total_runs'].sum()) if 'total_runs' in team_df.columns else int(team_df['batsman_runs'].sum())
                wkts = int(team_df['is_wicket'].sum())
                balls = len(team_df)
                overs = balls / 6 if balls > 0 else 0
                rr = runs / overs if overs > 0 else 0
                col.write(f"### {team}")
                col.metric("Total Runs", f"{runs:,}")
                col.metric("Wickets", f"{wkts:,}")
                col.metric("Run Rate", f"{rr:.2f}")

            st.markdown("---")
            st.subheader("Phase-wise Run Rate Comparison")
            phase_df = df.copy()
            phase_df['phase'] = phase_df['over'].apply(phase_from_over)
            compare_phase = phase_df.groupby(['batting_team', 'phase']).agg(runs=('total_runs', 'sum'), balls=('ball', 'count')).reset_index()
            compare_phase['overs'] = compare_phase['balls'] / 6
            compare_phase['run_rate'] = (compare_phase['runs'] / compare_phase['overs']).replace([np.inf, -np.inf], 0)
            compare_phase = compare_phase[compare_phase['batting_team'].isin([team_a, team_b])]
            fig = px.bar(compare_phase, x='phase', y='run_rate', color='batting_team', barmode='group', title="Phase-wise Run Rate Comparison")
            st.plotly_chart(fig, use_container_width=True)

            st.markdown("---")
            st.subheader("Top Batters Comparison (Team)")
            top_a = df[df['batting_team'] == team_a].groupby('batter')['batsman_runs'].sum().sort_values(ascending=False).head(10)
            top_b = df[df['batting_team'] == team_b].groupby('batter')['batsman_runs'].sum().sort_values(ascending=False).head(10)
            fig = go.Figure()
            fig.add_trace(go.Bar(x=top_a.index, y=top_a.values, name=f"{team_a} Top Bats"))
            fig.add_trace(go.Bar(x=top_b.index, y=top_b.values, name=f"{team_b} Top Bats"))
            fig.update_layout(title="Top Batters (by runs) — side-by-side", barmode='group')
            st.plotly_chart(fig, use_container_width=True)

    else:
        st.subheader("Compare Two Players")
        p_col1, p_col2 = st.columns([1, 1])
        with p_col1:
            player_a = st.selectbox("Player A", options=players, key="comp_player_a")
        with p_col2:
            player_b = st.selectbox("Player B", options=players, key="comp_player_b")

        if player_a and player_b:
            p1 = df[df['batter'] == player_a]
            p2 = df[df['batter'] == player_b]

            def player_summary(p_df):
                runs = int(p_df['batsman_runs'].sum()) if 'batsman_runs' in p_df.columns else 0
                balls = int(len(p_df))
                sr = (runs / balls * 100) if balls > 0 else 0
                dismissals = int(p_df['is_wicket'].sum()) if 'is_wicket' in p_df.columns else 0
                avg = (runs / dismissals) if dismissals > 0 else 0
                fours = int((p_df['batsman_runs'] == 4).sum()) if 'batsman_runs' in p_df.columns else 0
                sixes = int((p_df['batsman_runs'] == 6).sum()) if 'batsman_runs' in p_df.columns else 0
                return {"runs": runs, "avg": avg, "sr": sr, "balls": balls, "fours": fours, "sixes": sixes, "dismissals": dismissals}

            s1 = player_summary(p1)
            s2 = player_summary(p2)

            left, right = st.columns(2)
            left.write(f"### {player_a}")
            left.metric("Runs", f"{s1['runs']:,}")
            left.metric("Average", f"{s1['avg']:.2f}")
            left.metric("Strike Rate", f"{s1['sr']:.2f}")
            left.write(f"4s = {s1['fours']} | 6s = {s1['sixes']} | Dismissals = {s1['dismissals']}")

            right.write(f"### {player_b}")
            right.metric("Runs", f"{s2['runs']:,}")
            right.metric("Average", f"{s2['avg']:.2f}")
            right.metric("Strike Rate", f"{s2['sr']:.2f}")
            right.write(f"4s = {s2['fours']} | 6s = {s2['sixes']} | Dismissals = {s2['dismissals']}")

            st.markdown("---")
            st.subheader("Runs by Over Comparison")
            over1 = p1.groupby('over')['batsman_runs'].sum().reset_index().assign(Player=player_a)
            over2 = p2.groupby('over')['batsman_runs'].sum().reset_index().assign(Player=player_b)
            both = pd.concat([over1, over2], ignore_index=True).fillna(0)
            fig = px.line(both, x='over', y='batsman_runs', color='Player', markers=True, title="Runs by Over Comparison")
            st.plotly_chart(fig, use_container_width=True)

            st.markdown("---")
            st.subheader("Dismissal Type Comparison")
            if 'dismissal_kind' in df.columns:
                d1 = p1['dismissal_kind'].fillna('Not out').value_counts().reset_index()
                d1.columns = ['dismissal', 'count']
                d1['player'] = player_a
                d2 = p2['dismissal_kind'].fillna('Not out').value_counts().reset_index()
                d2.columns = ['dismissal', 'count']
                d2['player'] = player_b
                dd = pd.concat([d1, d2], ignore_index=True)
                fig = px.bar(dd, x='dismissal', y='count', color='player', barmode='group', title="Dismissal Types by Player")
                st.plotly_chart(fig, use_container_width=True)
            else:
                st.info("No 'dismissal_kind' column present — can't compare dismissal types.")

# -------------------------
# PDF Report tab (user-provided filename)
# -------------------------
with tabs[4]:
    st.header("PDF Report")
    pdf_path = "IPL_Comprehensive_Match_Insights.pdf"
    if os.path.exists(pdf_path):
        st.write("Download or preview the provided PDF report.")
        with open(pdf_path, "rb") as f:
            st.download_button("⬇️ Download PDF", data=f, file_name=os.path.basename(pdf_path), mime="application/pdf")
        try:
            st.write("PDF preview below:")
            st.pdf(pdf_path)
        except Exception:
            st.info("PDF preview not available in this environment — use download button.")
    else:
        st.info(f"No `{os.path.basename(pdf_path)}` found in the folder. Place the PDF beside this app to enable preview/download.")

st.markdown("---")
st.caption("Built with Streamlit — Advanced IPL Insights (General → Team → Player → Comparison). Modify thresholds and filters inside the app file as needed.")
